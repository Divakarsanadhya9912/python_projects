o = input("Enter an operator:")

if o == '+':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1+n2)
elif o == '-':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1-n2)
elif o == '*':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1*n2)
elif o == '/':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1/n2)
elif o == '%':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1%n2)
elif o == '**':
    n1 = float(input("Enter 1st no.:"))
    n2 = float(input("Enter 2nd no.:"))
    print(n1**n2)
else :
    print("only + , - , * , / , % , ** will performed as an operator")