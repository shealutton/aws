zsh
# Ha! IT WORKS!
aws ec2 describe-instances
aws ec2 describe-instances --output text
aws ec2 describe-instances --instance-id i-0ef59f3a27ac6e69c --output text
aws ec2 describe-instances --instance-id i-0ef59f3a27ac6e69c --query 'Reservations[0].Instances[0].PublicIpAddress' --output text
name=‘shealutt’
echo $name
now=$(date)
echo $now
cd ~
instanceid=$(aws ec2 run-instances --instance-type i2.8xlarge --key ebsdemokeypair --image-id ami-60b6c60a --block-device-mappings file://mapping.json --query 'Instances[0].InstanceId' --output text)
echo $instanceid
ip=$(aws ec2 describe-instances --instance-id $instanceid --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
echo $ip
key=$(aws ec2 describe-instances --instance-id $instanceid --query 'Reservations[0].Instances[0].KeyName' --output text)
echo $key
cd ~/Downloads
chmod 400 $key.pem
ssh -i $key.pem ec2-user@$ip
yes
lsblk
exit
az=$(aws ec2 describe-instances --instance-id $instanceid --query 'Reservations[0].Instances[0].Placement.AvailabilityZone' --output text)
echo $az
ebs1=$(aws ec2 create-volume --availability-zone $az --size 150 --volume-type gp2 --query 'VolumeId' --output text)
ebs2=$(aws ec2 create-volume --availability-zone $az --size 150 --volume-type gp2 --query 'VolumeId' --output text)
ebs3=$(aws ec2 create-volume --availability-zone $az --size 150 --volume-type gp2 --query 'VolumeId' --output text)
echo $ebs1 $ebs2 $ebs3
aws ec2 attach-volume --volume-id $ebs1 --instance-id $instanceid --device /dev/sdj
aws ec2 attach-volume --volume-id $ebs2 --instance-id $instanceid --device /dev/sdk
aws ec2 attach-volume --volume-id $ebs3 --instance-id $instanceid --device /dev/sdl
ssh -i $key.pem ec2-user@$ip
lsblk
sudo -s
yum install fio -y
fio \
--name fio_test_file \
--direct=1 \
--rw=randread \
--bs=4k \
--size=1G \
--numjobs=16 --time_based --runtime=10 --group_reporting --norandommap \
--filename=/dev/xvdj
mdadm --create /dev/md0 --level=0 --raid-devices=3 /dev/xvd[jkl]
lsblk
mdadm --detail /dev/md0
fio \
--name fio_test_file --direct=1 --rw=randread --bs=4k --size=1G \
--numjobs=16 --time_based --runtime=10 --group_reporting --norandommap \
--filename=/dev/md0
exit
exit
ebs4=$(aws ec2 create-volume --availability-zone $az --size 450 --volume-type io1 --iops 9000 --query 'VolumeId' --output text)
echo $ebs4
aws ec2 attach-volume --volume-id $ebs4 --instance-id $instanceid --device /dev/sdm
ssh -i $key.pem ec2-user@$ip
lsblk
sudo -s
fio \
--name fio_test_file --direct=1 --rw=randread --bs=4k --size=1G \
--numjobs=16 --time_based --runtime=10 --group_reporting --norandommap \
--filename=/dev/sdm
lsblk
fio \
--name fio_test_file --direct=1 --rw=randread --bs=4k --size=1G \
--numjobs=16 --time_based --runtime=10 --group_reporting --norandommap \
--filename=/dev/xvdb
mdadm --create /dev/md1 --level=0 --raid-devices=8 /dev/xvd[b-i]
mdadm --detail /dev/md1
fio \
--name fio_test_file --direct=1 --rw=randread --bs=4k --size=1G \
--numjobs=256 --time_based --runtime=10 --group_reporting --norandommap \
--filename=/dev/md1
exit
exit
aws ec2 detach-volume --volume-id $ebs1 --instance-id $instanceid --force
aws ec2 detach-volume --volume-id $ebs2 --instance-id $instanceid --force
aws ec2 detach-volume --volume-id $ebs3 --instance-id $instanceid --force
aws ec2 detach-volume --volume-id $ebs4 --instance-id $instanceid --force
aws ec2 delete-volume --volume-id $ebs1
aws ec2 delete-volume --volume-id $ebs2
aws ec2 delete-volume --volume-id $ebs3
aws ec2 delete-volume --volume-id $ebs4
aws ec2 terminate-instances --instance-ids $instanceid
#end
