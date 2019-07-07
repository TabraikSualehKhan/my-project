def add () :
    x= int (input("Enter 1st number : "))
    y= int(input("Enter 2nd number : "))
    return x+y  

def sub  () :
    x= int (input("Enter 1st number : " ))
    y= int(input("Enter 2nd number : "))
    return x-y

def mul  () :
    x= int (input("Enter 1st number : "))
    y= int(input("Enter 2nd number : "))
    return x*y 

def div () :
    x= int (input("Enter 1st number : "))
    y= int(input("Enter 2nd number : "))
    return x/y 
 
operator =  (input ("Enter any input    "))

if operator == '+' :
    print (add())

elif operator == '-' :
    print (sub())

elif operator == '*' :
    print (mul())

elif operator == '/' :
    print (div())

else :
    print ("wrong input")




# print ("Welcome to Calculator")

# operator = (input("Enter any operator (+ , - , * , /) : "))
# if operator == "+" or "-":
#         print ("valid")
# else :    
#     print ("enter again")
# number1= int (input("Enter 1st number : "))
# number2= int(input("Enter 2nd number : "))

# if operator == '+' :
#     c=number1+number2
#     print("The addition of two number : ", c )
    
# elif operator == '-' :
#     c=number1-number2
#     print("The subtraction of two number : ", c )

# elif operator == '*' :
#     c=number1*number2
#     print("The multiplication of two number : ", c )
    
# elif operator == '/' :
#     c=number1 / number2
#     print("The division of two number : ", c )   
# else: 
#     print ("You have enter wrong operator")
    
