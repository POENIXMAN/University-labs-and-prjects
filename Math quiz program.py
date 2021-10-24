import random 
import time

correct_answers_count = 0
numbers_count = 0
Number_of_Questions = 5 

startTime = time.time()

while numbers_count < Number_of_Questions:

    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    
    
    if number1 < number2:
        number1,number2 = number2,number1
    
    answer = eval(input(f'That is {number1} - {number2}? '))

    if number1 - number2 == answer:
        print('You are correct')
        correct_answers_count += 1
    else:
        print(f'Your answer is wrong.',f'\n{number1} - {number2} = {number1-number2}')

    numbers_count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print(f'You got {correct_answers_count} right answers out of {Number_of_Questions}',
 f'\nIt took you {testTime} seconds to finish')
    

