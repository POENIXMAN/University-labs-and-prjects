import random as rn

def results(r_answ, mx_ques): 
    '(int,int) --> none'
    '''This function shows responds according to amount of right answers'''

    if r_answ == mx_ques:
        print('Fantastic! You got all the questions right!!!')
    elif r_answ < mx_ques and r_answ > 0:
        print(f'Well done ). You got {r_answ} right answers out of {mx_ques}')   
    elif r_answ == 0:
        print(f'Its ok. Study a little more and come back.')

def generate_num():
    '() --> int,int'
    num1 = rn.randint(0,9)
    num2 = rn.randint(0,9)
    
    return num1, num2

def answer_check(answer,r_answer,u_r_answers):
    '(int,int,int) --> int'
    '''Checks if the answer is right, if so, increments the right answers variable by 1'''
    
    if answer == r_answer:
        u_r_answers += 1
        print('That\'s right! Good job.')
    else:
        print('Oh shoot, you were so near... Next time you\'ll get it :)')
        print(f'The right answer is {r_answer}')
    return u_r_answers

def multiply():
    '() --> str'

    max_questions = int(input('How many questions do you want? '))
     
    answers = 1 #User's answers
    u_r_answers = 0 #User's right answers

    while answers <= max_questions:
        
        num1,num2 = generate_num()
        
        answer = int(input(f'What is the answer of {num1} * {num2} : '  )) # ask user for the answer

        r_answer = num1 * num2
        
        u_r_answers = answer_check(answer,r_answer,u_r_answers)
        
        answers += 1
    
    results(u_r_answers,max_questions)

def add():
    '() --> str'
    max_questions = int(input('How many questions do you want? '))
    answers = 1 #User's answers
    u_r_answers = 0 #User's right answers

    while answers <= max_questions:
        
        num1,num2 = generate_num()
        
        answer = int(input(f'What is the answer of {num1} + {num2} : '  )) # ask user for the answer

        r_answer = num1 + num2
        
        u_r_answers = answer_check(answer,r_answer,u_r_answers)
        
        answers += 1
    
    results(u_r_answers,max_questions)

def subtract():
    '() --> str'
    max_questions = int(input('How many questions do you want? '))   
    
    answers = 1 #User's answers
    u_r_answers = 0 #User's right answers

    while answers <= max_questions:
        
        num1,num2 = generate_num()
        
        if num1 < num2:
            num1,num2 = num2,num1
        
        answer = int(input(f'What is the answer of {num1} - {num2} : '  )) # ask user for the answer

        r_answer = num1 - num2
        
        u_r_answers = answer_check(answer,r_answer,u_r_answers)
        
        answers += 1
    
    results(u_r_answers,max_questions)

def math_practice():
    '() --> str'


    welcome_message = '''\n\tHello!!! This is a small program that will help
    you get used to (+ , - , and *) which you had in your math
                        classes :) '''

    print(welcome_message)

    type_of_operator = input('Enter what operator you want to practice with questions do you want (+,-,*) : ')


    if type_of_operator == '+':
        add()
    elif type_of_operator == '-':
        subtract()
    elif type_of_operator == "*":
        multiply()
    else:
        print('Please Enter one of these operators (*,-,+)')
        math_practice()

    
math_practice()

# Test run:


            #Hello!!! This is a small program that will help
    #you get used to (+ , - , and *) which you had in your math
                        #classes :)

    #Enter what operator you want to practice with questions do you want (+,-,*) : *

    #How many questions do you want? 3
    #What is the answer of 9 * 3 : 23
    #Oh shoot, you were so near... Next time you'll get it :)
    #The right answer is 27
    #What is the answer of 4 * 9 : 36
    #That's right! Good job.
    #What is the answer of 9 * 9 : 81
    #That's right! Good job.
    #Well done ). You got 2 right answers out of 3


    


