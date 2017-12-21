'''The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?'''



d = 1
count = 0
while d < 1000:
    for n in range(1, 10):
        x = n ** d
        if len(str(x)) == d:
            print(x, n, len(str(n ** d)))
            count += 1
        elif len(str(x)) > d:
            break
    d += 1
#    if d % 100 == 0:
#        print(d)

print('COUNT', count)