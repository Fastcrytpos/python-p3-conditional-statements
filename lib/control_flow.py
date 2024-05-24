#!/usr/bin/env python3

def admin_login(username, password):
    if (username=="admin" or username=="ADMIN" )and (password=="12345"):
        return "Access granted"
    else:
        return "Access denied"

    # your code here
    pass

def hows_the_weather(temperature):
    if temperature<=40:
        return "It's brisk out there!"
    elif temperature>40 and 65>temperature:
        return "It's a little chilly out there!"
    elif temperature>85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    # your code here
    pass

def fizzbuzz(num):
    if num%3==0 and num%5!=0:
        return "Fizz"
    elif num%5==0 and num%3!=0:
        return "Buzz"
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    else: return num
    # your code here
    pass

def calculator(operation, num1, num2):
    dict_map={
        "+":num1+num2,
        "-":num1-num2,
        "*":num1*num2,
        "/":num1/num2,
    }
    result=dict_map.get(operation,"Invalid operation!")
    if result=="Invalid operation!":
        print("Invalid operation!")
        return None
    else: 
        return result

    # your code here
    pass
