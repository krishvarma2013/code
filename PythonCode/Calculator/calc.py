def addition():
    count = 0
    a = int(input("First Number "))
    b = int(input("Second Number "))
    count = a+b
    print (count)

def subtraction():
    count = 0 
    c = int(input("First Number "))
    d = int(input("Second Number "))
    count = c-d
    print (count)

def multiplication():
    count = 0 
    e = int(input("First Number "))
    f = int(input("Second Number "))
    count = e * f
    print (count)

def division():
    count = 0
    g = int(input("First Number "))
    h = int(input("Second Number "))
    count = g / h
    print (count)

def modular():
    count = 0
    i = int(input("First Number"))
    j = int(input("Second Number"))
    count = i % j
    print (count)

sign = input("What sign do you want to do- addition, subtraction, division, modular, or multiplication ")
if sign == "multiplication":
    multiplication()
if sign == "division":
    division()
if sign == "subtraction":
    subtraction()
if sign == "addition":
    addition()
if sign == "modular":
    modular()
else:
    print("choose out of addition, subtraction, division, and multiplication")
    exit()