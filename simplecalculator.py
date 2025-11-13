#simple calculator

##using if-else
# def calc(a,b,opp):
#     if(opp=="+"):
#         return a+b
#     elif(opp=="-"):
#         return a-b
#     elif(opp=="*"):
#         return a*b
#     elif(opp=="/"):
#         if(b==0):
#             return "error"
#         return a//b
#     elif(opp=="%"):
#         return a%b
#     else:
#         return "invalid operation"

##using match
# def calc(a, b, opp):
#     match opp:
#         case "+":
#             return a + b
#         case "-":
#             return a - b
#         case "*":
#             return a * b
#         case "/":
#             return a // b if b != 0 else "Error: divide by zero"
#         case "%":
#             return a % b
#         case _:
#             return "Invalid operator"


# a = int(input("enter num1 :")) 
# b = int(input("enter num2 :"))  
# opp = input("select operation:")
# print(calc(a,b,opp))

#for more than 2 numbers
def clc(nums, opp):
    sum = 0
    product = 1

    match opp:
        case "+":
            for n in nums:
                sum += n
            return sum
        case "*":
            for n in nums:
                product *= n
            return product
        case _:
            return "invalid"

numbers = list(map(int, input("enter numbers separated by spaces:").split()))
operation = input("enter operation(+ or *)")
print(clc(numbers, operation))

