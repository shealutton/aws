#!/usr/bin/perl -w
# Shea Lutton

use strict;
my $total = 0;
my $count = 0;
my $len = 0;
my $maxcount = 0;
my $max = "X";
my $min = "X";
my $mean = 0.0;
my $median = 0.0;
my $stddev = 0.0;
my $stderr = 0.0;
my (@array, @sorted, @buckets, %bucketvals);
my ($subvalue, $sigmaSubvalue, $range, $bucket, $multiplier, $bin_width);

while (<>) {
  chomp;
  next unless m/^[-+]?[0-9]*\.?([0-9]+)/; # only positive ints, negative ints, positive real, neg real
  push @array, $_;
  $len = length($1) if length($1) > $len;
  $min = $_ if $min eq "X"; # init $min
  $max = $_ if $max eq "X"; # init $max
  $count ++;
  $total += $_;
  $max = $_ if $_ > $max;
  $min = $_ if $_ < $min;
}
if ( $count == 0 ) { die "I need a column of numbers\n" }
$mean = $total / $count;
$range = $max - $min;

# Create histogram buckets
$bin_width = $range/20;
$multiplier = 1;
$bucket = $min;
while ($bucket < $max) {
   push (@buckets, $bucket);
   $bucket = $min + ($bin_width * $multiplier);
   $multiplier++;
}
foreach $bucket (@buckets) {
   $bucketvals{$bucket} = 0; # needed to init the histogram buckets
}
foreach (@array) { # iterate through the main array to prep stddev and stder and populate histogram
   $subvalue = (($_ - $mean)**2); # stddev prep
   $sigmaSubvalue += $subvalue; # stddev prep
   $maxcount = $maxcount+1 if $_ eq $max; # tally up the total samples = $max
   foreach $bucket (@buckets) {
      if (( $_ >= $bucket ) && ( $_ < $bucket+$bin_width )) { # this method excludes the $max sample from histogram (see $maxcount)
         $bucketvals{$bucket} ++ ;
      }
   }
}
$bucketvals{$min + ($bin_width * 19)} = $bucketvals{$min + ($bin_width * 19)}+$maxcount; # add $maxcount to the largest bucket for an accurate histogram

@sorted = sort{ $a <=> $b } @array; # Find the median
if ($total % 2) { # if an even number
$median = $sorted[$count/2];
} else { # if an odd number
$median = ($sorted[$count/2] + $sorted[$count/2 - 1]) / 2;
}
$stddev = (sqrt $sigmaSubvalue) / (sqrt ($count - 1));
$stderr = ($stddev / (sqrt $count));

print  "samples:     $count\nmin:         $min\nmax:         $max\n";
printf ("range:       %.${len}f\n", $range);
printf ("sum:         %.${len}f\n", $total);
printf ("mean:        %.${len}f\n", $mean);
printf ("median:      %.${len}f\n", $median);
printf ("std_dev:     %.${len}f\n", $stddev);
printf ("std_error:   %.${len}f\n", $stderr);
printf ("bin width:   %.${len}f\n", $bin_width);
print  "\n       Histogram\n        Bin Frequency   (\%)\n";
foreach $bucket (@buckets) {
   printf("%10.${len}f %-10d (%0.1f%%)\n",$bucket, $bucketvals{$bucket}, $bucketvals{$bucket}/$count*100);
}


