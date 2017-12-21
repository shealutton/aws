'''Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525)
 are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers
 is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.'''


def bouncy(number):
    number_list = str(number)
    length = len(number_list)
    up = False
    down = False
    position = 0
    while position < length - 1:
        if number_list[position] < number_list[position + 1]:
            down = True
        if number_list[position] > number_list[position + 1]:
            up = True
        if up and down:
            return True
        position += 1
    return False


#target_percentage = .50
#target_percentage = .90
target_percentage = .99  # Winner 1587000
bouncy_list = []
n = 1
while True:
    if bouncy(n):
        bouncy_list.append(n)
        if len(bouncy_list) / target_percentage == n:
            print('Winner', n)
            break
    n += 1
