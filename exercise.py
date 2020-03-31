import random

response = input('Do you want to guess a number? ')

if response == 'yes':
    Status = True
    #newcomment in if block
    while Status == True:

        x = random.randint(0, 100)

        y = input('Input a number from 0 to 100: ')
        z = int(y)

        print(f'The randomly generated number is {x}')
        print(f'The inputted number is {z}')

        difference = abs(x - z)

        if z < 0 or z > 100:
            print('Number is out of range')
            Status = False
            while Status == False:
                response1 = input('Do you want to re-enter a new number? ')
                if response1 == 'yes':
                    Status = True
                elif response1 == 'no':
                    print('Program ended')
                    break
                else:
                    print('Not understood')
        else:
            if difference == 0:
                print(f'The numbers are the same')

            elif difference in range(0, 10):
                print(f'The two numbers are close to each other')
            elif difference in range(10, 30):
                print(f'The numbers are a bit far apart')
            elif difference in range(30, 99):
                print(f'The numbers are so far apart')
            #else:
                #print(f'Numbers are different')

            newreply = input('Do you want to guess a new number? ')
            if newreply == 'yes':
                Status = True
            elif newreply == 'no':
                Status = False
                while Status == False:
                    print('Program closed. Thank you')
                    break

            else:
                print('Not understood')

else:

    print('Program ended')


#if response == 'no':
    #Status = False
