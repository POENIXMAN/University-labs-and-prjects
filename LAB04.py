import math
import random

#---------------------------------------------------Problem 1----------------------------------------------

def  _distance(X1,X2,Y1,Y2):
    '''(num)--> num
    Calculates and prints the distance between 2 points
    '''
    formula = math.sqrt(pow((X2-X1),2)+pow((Y2-Y1),2))
    print(f'\nThe distance is {formula}')

def _angle():
    '''()--> num

    Enter 3 points(X,Y), separated by comma : 1,1,6.5,1,6.5,2.5

    >>>The three angles are  15.26 90.0 74.74
    '''
    X1,Y1,X2,Y2,X3,Y3 = eval(input('\n>>> Enter 3 points(X,Y), separated by comma : '))

    a = math.sqrt((X2 - X3) * (X2 - X3) + (Y2 - Y3) * (Y2 - Y3))
    b = math.sqrt((X1 - X3) * (X1 - X3) + (Y1 - Y3) * (Y1 - Y3))
    c = math.sqrt((X1 - X2) * (X1 - X2) + (Y1 - Y2) * (Y1 - Y2))

    A = math.degrees(math.acos((a*a - b*b - c*c)/(-2*b*c)))
    B = math.degrees(math.acos((b*b - a*a - c*c)/(-2*a*c)))
    C = math.degrees(math.acos((c*c - b*b - a*a)/(-2*a*b)))

    print('\nThe three angles are : ', round(A*100)/100.0,' ; ', round(B*100)/100.0,' ; ', round(C*100)/100.0 )

_distance(4,6,0,6)
_angle()

#---------------------------------------------------Problem 2----------------------------------------------

def guess_alphabet():
    '''(string)---> string

     Guess the alphabet function
    '''
    print('\n>>> Try to guess the random character :)')

    userChr = input('Enter an uppercase alphabetic character : \n')
    alpha = chr(random.randrange(65,91))

    if userChr.isalpha() and userChr.isupper():
        if alpha == userChr:
            print('**Good Guess**')
            print(f'The random character is {alpha}')
        else:
            print('Wrong Guess :/')
            print(f'The random character is {alpha}')
    else:
        print('Please, enter an uppercase alphabetic')

guess_alphabet()

#---------------------------------------------------Problem 3----------------------------------------------
def typeOfTriangle(side1,side2,side3):
    '''(num)--> string

    Gives the type of triangle by given sides

    >>>typeOfTriangle(3,2,3)
    The triangle is Isosceles
    >>>typeOfTriangle(2,5,1)
    Invalid Triangle
    '''
    case1 = side1 + side2 > side3
    case2 = side1 + side3 > side2
    case3 = side2 + side3 > side1

    if (case1 and case2 and case3): #Checks that sum of 2 sides is bigger than 3rd side
        if side1 == side2 == side3:      
            return print('\nThe triangle is Equilateral')
        elif side1 == side2 or side2 == side3 or side1 == side3:
            return print('The triangle is Isosceles')
        else:
            return print('The triangle is Scalene')
    else:
        return print('Invalid Triangle')

typeOfTriangle(3,3,3)
typeOfTriangle(3,2,3)
typeOfTriangle(4,5,3)
typeOfTriangle(3,0,5)

#---------------------------------------------------Problem 4----------------------------------------------
def Grades():
    '''() --> num, string

    Computes the  average 
    from best 2 tests and the final
    Also it gives the letter grade
    '''
    print('\n>>> Grade Computing Applictation' + '\nBy Ahmad Nasser')

    T1 = float(input('\nEnter Grade of Test1 : \n'))
    T2 = float(input('Enter Grade of Test2 : \n'))
    T3 = float(input('Enter Grade of Test3 : \n'))
    F = float(input('Enter Grade of Final : \n'))
    
    BTest1 = T1
    BTest2 = T2

    if T3 > T1:
        BTest1 = T3
    elif T3 > T2:
        BTest2 = T3

    average = (0.3*BTest1) + (0.3*BTest2) + (0.4*F)
    print(f"\nYour Computed average is : {average}")

    if (average >= 90):
        LG = 'A'
    elif (average >= 80):
        LG = 'B'
    elif (average >= 70):
        LG = 'C'
    elif (average >= 60):
        LG = 'D'
    else:
        LG = 'F'
    
    print(f"YourComputed letter grade is : {LG}")
    print('\nThank you')

Grades()
    





    