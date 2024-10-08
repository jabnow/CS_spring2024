#question 3 part a
def sum_square(n):
    tup = (range(0, n, 1))
    count = 0
    for thing in tup:
        thing **= 2
        count += thing
    return count

#question 3 part b
def sum_square2(n):
    #uses list comprehension
    return sum(i**2 for i in range(0, n))

#question 3 part c
def sum_square_odd(n):
    i = 1
    total = 0
    while i < n:
        if i % 2 == 1:
            total += i**2
            i += 2
    return total

#question 3 part d
def sum_square_odd2(n):
    return sum(i**2 for i in range(1, n, 2) if i % 2 == 1)