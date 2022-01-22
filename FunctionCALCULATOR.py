print("*********** DIGITAL CALCULATOR **********")

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print()
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
     choice=input("enter your choice(1/2/3/4):")
     if choice in('1','2','3','4'):
        a=int(input("enter num1:"))
        b=int(input("enter num2:"))

        if choice=='1':
          print(a,"+",b,"=",add(a,b))
        elif choice=='2':
            print(a,"-",b,"=",sub(a,b))
        elif choice=='3':
            print(a,"*",b,"=",mul(a,b))
        elif choice=='4':
            print(a,"/",b,"=",div(a,b))
        next_calculation=input("do you want to contiue?(yes/no):")
        if next_calculation=="no":
          break
     else:
           print("invalid input")

        
