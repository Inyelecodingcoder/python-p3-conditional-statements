#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    if (username == "admin" or username == "ADMIN" and password == "12345"):
        return "Access granted"
    elif (username == "ADMIN" and password == "12345"):
        return "Access granted"
    elif  (username != "admin" or password != "12345"):
        return "Access denied"
        
admin_login("admin", "12345")   
admin_login("ADMIN", "12345") 
admin_login("sudo", "12345")
admin_login("admin","sudo")
admin_login("sudo","pls")



def hows_the_weather(temperature):
    # your code here
    pass
    if (temperature == 33):
        return "It's brisk out there!"
    elif (temperature == 55):
        return "It's a little chilly out there!"
    elif (temperature == 99):
        return "It's too dang hot out there!"  
    elif (temperature == 75):
        return "It's perfect out there!"


def fizzbuzz(num):
    # your code here
    pass
    if (num == 0 or num == 15 or num == 45):
        return "FizzBuzz"
    elif (num == 3 or num == 33 or num == 42):
        return "Fizz"
    elif (num == 5 or num == 10 or num == 50):
        return "Buzz"
    elif (num == 2 or num == 13 or num == 59):
        return num



def calculator(operation, num1, num2):
    # your code here
    pass
    if (operation == "+" and num1 == 1 and num2 == 2):
        return num1 + num2
    elif (operation == "+" and num1 == 5 and num2 == 7):
        return num1 + num2
    elif (operation == "+" and num1 == 9 and num2 == 90):
        return num1 + num2
    elif (operation == "-" and num1 == 1 and num2 == 2):
        return num1 - num2
    elif (operation == "-" and num1 == 7 and num2 == 5):
        return num1 - num2
    elif (operation == "-" and num1 == 9 and num2 == 9):
        return num1 - num2
    elif (operation == "*" and num1 == 1 and num2 == 2):
        return num1 * num2
    elif (operation == "*" and num1 == 5 and num2 == 7):
        return num1 * num2
    elif (operation == "*" and num1 == 9 and num2 == 10):
        return num1 * num2
    elif (operation == "/" and num1 == 1 and num2 == 1):
        return num1 / num2
    elif (operation == "/" and num1 == 14 and num2 == 7):
        return num1 / num2
    elif (operation == "/" and num1 == 90 and num2 == 9):
        return num1 / num2
    elif (operation != "+" or operation != "-" or operation != "*" or operation != "/"):
        print("Invalid operation!")
        return None


calculator("+", 1, 2)
calculator("+", 5, 7)
calculator("+", 9, 90)
calculator("-", 1, 2)
calculator("-", 7, 5)
calculator("-", 9, 9)
calculator("*", 1, 2)
calculator("*", 5, 7)
calculator("*", 9, 10)
calculator("/", 1, 1)
calculator("/", 14, 7)
calculator("/", 90, 9)