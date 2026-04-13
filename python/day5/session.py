def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(f"Addition : {result}")

add(8, 5)
add(10, 15, 25)

def subtract(*numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    print(f"Subtraction : {result}")

subtract(8, 5)
# how many types of argumnts?
