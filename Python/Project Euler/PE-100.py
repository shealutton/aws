'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain.
'''


def prob(x, y):
    a = x - 1
    percent = (x / (x + y)) * (a / (a + y))
    if percent <= 0.50000000000001 and percent >= 0.49999999999999:
        print(percent, (x / (x + y)), (a / (a + y)))
        return True



for blue in range(1, 10000):
    for red in range(1, 10000):
        if prob(blue, red):
            print(blue, red)




(15 / x ) * ((15-1) / (x - 1)) = .5

15   *   15-1    = .5
x         x-1

15    *   15-1
         (x^2-1x) = .5x

15 * 15-1
     x^2-1x = .5x


15-1
x-1  = .7

14
x-1 = .7
14 = .7 * (x-1)
14=.7x-.7
14.7=.7x
x=21




