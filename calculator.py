import math

def calc (oper,*nums):
    total = nums[0] #assigns the first number in the list total
    result = 0
    if oper == "a" :
        result = sum(nums)
    elif oper == "b" :
        for i in range(1,len(nums)):     #loops until it reaches the last element
            total = total - nums[i] 
            result = total       
    elif oper == "c" :
        for i in range(1,len(nums)):
            total = total * nums[i] 
            result = total   
    elif oper == "d" :
        for i in range(1,len(nums)):     
            total = total / nums[i] 
            result = total   
    elif oper == "e" :
        result = math.cos(*nums)
    elif oper == "f" :
        result = math.sin(*nums)
    elif oper == "g" :
        result = math.log(*nums)
    elif oper == "h" :
        result = math.sqrt(*nums)
    elif oper == "i" :
        result = math.cbrt(*nums)
    elif oper == "z" :
        exit()
    else:
        print("Invalid operation")
    print(result)
   
while True: # this is an infite loop until it is stopped 
    print("Welcome to my calculator")
    oper = input("We have the following operation:\n a. Addition \n b. Subtraction\n c. Multiplication\n d. Division\n e. Cosine\n f. Sin\n g. Log\n h. Squareroot\n i. Cuberoot\n z. Exit \n")
    if oper == "z" :
            exit()
            
    nums = list(map(float, input("Enter the numbers (space-separated): ").split()))

    calc(oper,*nums)

    choice = input ("Do you want another operation: ")
    if choice.lower() != "y":
        break