'''Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below
one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.
How many numbers below a googol (10^100) are not bouncy?'''


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
            return False
        position += 1
    return True


def b2(number):
    L = []
    number_string = str(number)
    for item in number_string:
        L.append(item)
    forward = L.sort()
    reverse = L.reverse()
    if L == forward:
        return True
    if L == reverse:
        return True
    return False


bouncy_list = []
x = set()
for n in range(1, 1000000):
    #if bouncy(n):
    if b2(n):
        bouncy_list.append(n)

print(bouncy_list)
