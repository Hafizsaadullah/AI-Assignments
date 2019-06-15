# Taking Variables of Numbers
N1 = "First Number"
N2 = "Second Number"

# For Taking Input of Numbers
N1 = int(input("Please enter 1st number: "))
N2 = int(input("Please enter 2nd number: "))

# Take input about Operation
C = input("What do you want to do?  e.g(+,-,*,/): ")

# For Calculation
# Addition
if C=="+":
    print(N1,"+",N2,"=",N1+N2)
# Subtraction
elif C=="-":
    print(N1,"-",N2,"=",N1-N2)
# Multiplication
elif C=="*":
    print(N1,"*",N2,"=",N1*N2)
# Division
elif C=="/":
    print(N1,"/",N2,"=",N1/N2)
else:
    print("Please insert symbol from (+,-,*,/)")