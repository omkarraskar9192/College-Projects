A = float(input("Enter Your First No. : "))
C =  input("Enter Your Opreation in (+,-,*,/) : ")
B = float (input("Enter Your Second No. : "))

if  (C == '+'):
    print(A+B)
elif (C =='-'):
    print(A-B)
elif (C =='*') :
    print(A*B)
elif (C =='/'):
    if(B==0):
        print("Your Value is infinity")
    else:
        print(A/B)
else:
    print("No result Please Enter Right Opreter ")

print("Thank You")