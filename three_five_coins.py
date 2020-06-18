"""
    This program is a recursive solution to the problem of figuring without
    an amount of coins needed for any given quantity if the coins are only in
    3 and 5 denominations.
"""

def change(amount):
    assert(amount>= 8)
    if amount == 8:
        return [3,5]
    if amount == 9:
        return [3,3,3]
    if amount == 10:
        return [5,5]


    if amount == 3:
        return[3]
    if amount == 5:
        return [5]
    coins = change(amount -3)
    coins.append(3)
    return coins


print('Give amount of coins needed for 11 coins')
print(change(11))

print('give coins needed for amount of 3')
print(change(3))
