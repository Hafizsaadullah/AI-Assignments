# Subject Alphabet Code
E = "English"
M = "Math"
U = "Urdu"
I = "Islamiat"
C = "Computer"

# Input and Output Marks
E = int(input("Enter English Marks: "))
if E < 0 or E > 100 :  
    print ("Please Enter Correct Marks (For Example 0-100)")    

M = int(input("Enter Math Marks: "))
if M < 0 or M > 100 :  
    print ("Please Enter Correct Marks (For Example 0-100)")    
    
U = int(input("Enter Urdu Marks: "))
if U < 0 or U > 100 :  
    print ("Please Enter Correct Marks (For Example 0-100)")    

I = int(input("Enter Islamiat Marks: "))
if I < 0 or I > 100 :  
    print ("Please Enter Correct Marks (For Example 0-100)")    

C = int(input("Enter Computer Marks: "))
if C < 0 or C > 100 :  
    print ("Please Enter Correct Marks (For Example 0-100)")    

# For Marks 
Total_Marks =   int(500)
obtain_Marks = int(E)    +   int(M)  +   int(U)  +   int(I)  +   int(C)

# For Percentage

Percentage = obtain_Marks / Total_Marks * 100

print("Your Percentage is", float(Percentage))

# For Grade

if Percentage <= 32:
    print("Your Grade is F")
elif Percentage <= 49:
    print("Your Grade is D")
elif Percentage <= 59:
    print("Your Grade is C")
elif Percentage <= 69:
    print("Your Grade is B")
elif Percentage <= 79:
    print("Your Grade is A")
elif Percentage <= 100:
    print("Your Grade is A+")
else: 
    print("Please Check your Marks again and enter correctly")