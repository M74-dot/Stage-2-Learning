from calculator.addition import add
from calculator.subtraction import sub
from calculator.multiplication import mul
from calculator.division import divide

def main():
    while True:
        print('\n choose an option: ')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1 :
            number1 = float(input('Enter number 1: '))
            number2 = float(input('Enter number 2: '))
            result = add(number1, number2)
            print(f"{number1} + {number2} = {result}")
        
        elif choice == 2 :
            number1 = float(input('Enter number 1: '))
            number2 = float(input('Enter number 2: '))
            result = sub(number1, number2)
            print(f"{number1} - {number2} = {result}")

        elif choice == 3 :
            number1 = float(input('Enter number 1: '))
            number2 = float(input('Enter number 2: '))
            result = mul(number1, number2)
            print(f"{number1} * {number2} = {result}")

        elif choice == 4 :
            number1 = float(input('Enter number 1: '))
            number2 = float(input('Enter number 2: '))
            result = divide(number1, number2)
            print(f"{number1} / {number2} = {result}")

        elif choice == 5 :
            print('Exiting..')
            exit()
        
        else:
            print('Invalid Option. Please choose again.')

if __name__ == '__main__':
    main()