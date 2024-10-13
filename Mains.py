'''def sum (a,b):
    sum = a+b
    return sum


# First sum


a= int(input("Enter your first number: "))
b= int(input("Enter your second number: "))
result = sum(a,b)
print ("The sum of ",a,"and ", b, "is : ", result)

# Second Sum


a= int(input("Enter your first number: "))
b= int(input("Enter your second number: "))
result = sum(a,b)
print ("The sum of ",a,"and ", b, "is : ", result)'''


def fibonacci():
    first = 0
    second = 1
    third = 0
    print ( first , end= "," )
    i = 1
   # while (i<=20):
    for i in range (100):
        third = second + first
        print ( second  , end= ",")
        first = second 
        second = third
        i+=1

fibonacci()