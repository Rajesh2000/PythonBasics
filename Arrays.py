import array as ar
a = ar.array('i',[1,2,3,4,5]) #i is integer typecode of array
while True:
    print('-------------WELCOME-------------')
    print('1. Print Array')
    print('2. Add Elements')
    print('3. Delete Elements')
    print('4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('The array elements are: ')
        for numbers in a:
            print(numbers)

    elif choice == 2:
        val = int(input('Enter the integer number: '))
        if isinstance(val, int):  #check val is int or not
            a.append(val)

    elif choice == 3:
        value = a.pop()
        print('The value deleted was: ',value)
    elif choice == 4:
        break
    else:
        print('Enter a valid choice...')
