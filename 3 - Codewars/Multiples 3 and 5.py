def solution(number):
    sum = 0
    for i in range (0,number):
        if i % 5 == 0 or i % 3 == 0:
            sum += i

    return sum





solution(10)
