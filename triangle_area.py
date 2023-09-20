import math


def triangle_area(a, b, c):
    if a * b * c == 0:
        answer = "side can't be 0"

    elif a > b + c or b > a + c or c > a + b:
        answer = "Incorrect triangle"

    else:
        answer = round((math.sqrt((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) * 0.25), 3)
    print(answer)
    return answer
