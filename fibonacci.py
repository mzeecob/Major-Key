y = int(input('enter your number '))
count = 0
first_number = 0
second_number = 1
def fib():
    global first_number
    global second_number
    global count
    while count < y:
        b = first_number + second_number
        first_number = second_number
        second_number = b
        count += 1
        print(b)
