import math
#=========Problem 2===========

value = eval(input('Enter five digit numeber : '))    #Get a five digit number from the user

f_d = value%10
value = value//10

s_d = value%10
value= value//10

t_d = value%10
value = value//10

four_d= value%10
value= value//10

five_d = value%10
value = value//10




print(f_d,s_d,t_d,four_d,five_d,  sep="  ")


#----------------------------------------------------------------------------------------------------
#=========Problem 3===========

#Prompt the user for input
seconds = eval(input('\nEnter an integer for seconds : '))

#Get hours, minutes and remaining seconds

hours  = seconds//3600  # Get the hours 
minutes = (seconds%3600)//60 # Get the minutes from the remaining seconds after getting the hours
remainingSeconds = (seconds%3600)%60 #Get the remaining seconds after getting hours, then minutes
print(f'{seconds} seconds is : {hours}  hours {minutes} minutes {remainingSeconds} seconds')



#----------------------------------------------------------------------------------------------------
#=========Problem 4===========

statement = input("Enter two words separated by space : ")

st= statement.split()
print(st[0]*2,st[1]*2, sep=" ")
print(st[0]*2+st[1]*2)

#----------------------------------------------------------------------------------------------------
#=========Problem 5===========

#Get name and age of the user
name, age = input('Please enter your name then age(separated by space : ').split(" ")

N_age = 90-int(age)

print(f'Hi, my name is {name} and I am {age} years old.\nIn {N_age} years, i will be 90.') 

#----------------------------------------------------------------------------------------------------
#=========Problem 6===========

pointOneX, pointOneY = eval(input("Enter x and y for  point1 separated by comma : "))
pointTwoX, pointTwoY = eval(input("Enter x and y for  point2 separated by comma : "))

distance = math.sqrt(pow((pointTwoX-pointOneX),2)+pow((pointTwoY-pointOneY),2))
print(distance)
    
   