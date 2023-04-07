from services.math.fibonacci import fib
from services.math.root import square_root,cube_root
from services.sorting import insertionsort
from services.sorting.mergelist import merge_list
from services.sorting.mergesort import merge_sort,merge

def main():
    while True:
        print('\n choose an option: ')
        print('1. Fibonacci series')
        print('2. Square and Cube root')
        print('3. Binary insertion sort')
        print('4. Merge 2 Lists')
        print('5. Merge sort')
        print('5. Exit')
        choice = int(input('Enter yout choice: '))

        if choice == 1:
            n = int(input('Enter number: '))
            print("Fibonacci series till", n , fib(n))
        
        elif choice == 2:
            n = int(input('Enter number: '))
            print("Square root of ", n , square_root(n))
            print("Cube root of ", n ,cube_root(n))

        elif choice == 3:
            n = int(input('no. of items: '))
            lst = [int(input()) for i in range(n)]
            print(lst)
            print(insertionsort.binary_insertion_sort(lst))
        
        elif choice == 4:
            n = int(input('no. of items in list1: '))
            lst1 = [int(input()) for i in range(n)]
            m = int(input('no. of items in list2: '))
            lst2 = [int(input()) for j in range(m)]
            print(f"List1: {lst1}")
            print(f"list2: {lst2}")
            print('Merged list: ',merge_list(lst1,lst2))

        elif choice == 5:
            o = int(input('no. of items: '))
            lst = [int(input()) for k in range(o)]
            print(lst)
            print(merge_sort(lst))

        elif choice == 6:
            print('Exiting..')
            exit()

        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
 