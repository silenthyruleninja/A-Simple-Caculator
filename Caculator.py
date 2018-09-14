Name = input('Name:')
print('Welcome '+Name+' to my first attempt at building a program!!!')

while True:
    print('Options:')
    print('Enter \'add\' to add two numbers')
    print('Enter \'subtract\' to subtract two numbers')
    print('Enter \'divide\' to divide two numbers')
    print('Enter \'quit\' to end the program')
    user_input = input(':')

    if user_input == 'quit':
        break
#add
    elif user_input == 'add':
        num1 = float(input('Enter a number:'))
        num2 = float(input('Enter another number:'))
        result = str(num1+num2)
        print('The answer is '+result)
#subtract
    elif user_input == 'subtract':
        num1 = float(input('Enter a number:'))
        num2 = float(input('Enter another number:'))
        result = str(num1 - num2)
        print('The answer is '+result)
 #multiply       
    elif user_input == 'multiply':
        num1 = float(input('Enter a number:'))
        num2 = float(input('Enter another number:'))
        result = str(num1 * num2)
        print('The answer is '+result)
 #divide       
    elif user_input == 'divide':
        try:
            num1 = float(input('Enter a number:'))
            num2 = float(input('Enter a number:'))
            result = str(num1 / num2)
            print('The answer is '+result)
        except ZeroDivisionError:
            print('Can you like calm down and not divide by zero')
            
    else:
        print('Try again')
