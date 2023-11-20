#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()    

def greet(name):
    print(f"Hello, {name}!")

greet("John Doe")  # Hello, John Doe!


def greet_with_default(name="programmer"):
    print(f"hello,{name}!")
    print("Hello, programmer!")

greet_with_default("Jane")

def add(num1, num2):
    return num1+num2

print(add(2,3))


def halve(number):
    return number/2
print (halve(10))

