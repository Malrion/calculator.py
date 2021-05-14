# Variables for the result
c = 0
history = []
# Main code
while True:
    # Entering a number 
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    # Operation selection
    print()
    watch = input("Enter operation (+,-,*,/,%,**,//,history,exit): ")
    print()
    # Result
    if watch == "+":
        c = a + b
        print("Your result: " + str(c))
        print()
        d = a,'+',b,'=',c
        history.append(d)
    elif watch == "-":
        c = a - b
        print("Your result: " + str(c))
        print()
        d = a,'-',b,'=',c
        history.append(d)
    elif watch == "*":
        c = a * b
        print("Your result: " + str(c))
        print()
        d = a,'*',b,'=',c
        history.append(d)
    elif watch == '/':
        if b == 0.0:
            print('You cannot divide by zero!')
            print()
        else:
            c = a / b
            print("Your result: " + str(c))
            print()
            d = a,'/',b,'=',c
            history.append(d)
    elif watch == "%":
        c = a % b
        print("Your result: " + str(c))
        print()
        d = a,'%',b,'=',c
        history.append(d)
    elif watch == "**":
        c = a ** b
        print("Your result: " + str(c))
        print()
        d = a,'**',b,'=',c
        history.append(d)
    elif watch == '//':
        if b == 0.0:
            print('You cannot divide by zero!')
            print()
        else:
            c = a // b
            print("Your result: " + str(c))
            print()
            d = a,'//',b,'=',c
            history.append(d)
    elif watch == "exit":
        break
    elif watch == 'history':
        for histor in history:
            print(histor)
    else:
        print("Such an operation is impossible!")
        print()
