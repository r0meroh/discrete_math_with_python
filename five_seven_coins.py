"""
    This program is a recursive solution to the problem of figuring without
    an amount of coins needed for any given quantity if the coins are only in
    5 and 7 denominations with user input.
"""

# function only to check amount as long as it is larger than 8
def change(amount):
    assert(amount>= 7)
    if amount == 28:
        return [7,7,7,7]
    if amount == 21:
        return [7,7,7]
    if amount == 19:
        return [7,7,5]
    if amount == 15:
        return [5,5,5]
    if amount == 14:
        return [7,7]
    if amount == 10:
        return [5,5]
    if amount == 7:
        return [7]

    coins = change(amount - 5)
    coins.append(5)
    return coins



for x in range(24,1000):
    print(change(x))


amount = int(input('enter amount\n'))
print(change(amount))
