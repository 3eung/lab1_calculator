#Lab 1-3
def add(x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide(x,y):
    return x/y
def power (x,y):
    return x**y
def cal_OR(x,y):
    return x//y, x%y

while True:
    print("="*20)
    print("Select operation")
    print("0.Exit")
    print("1.Add")
    print("2.Subtract")
    print("3.multiply")
    print("4.divide")
    print("5.power")
    print("6.cal_OR")

    choice=input("Enter choice (0/1/2/3/4/5/6)")


    if choice=="0":
        break

    if (choice<'0') or (choice>'6'):
        print("Unvalid input")
        continue

    num1=float(input("첫번째 숫자를 입력하시오"))
    num2=float(input("두번째 숫자를 입력하시오"))


    if choice=="1":
        print(num1,"+",num2,"=", add(num1,num2))
        
    elif choice=="2":
        print(num1,"-",num2,"=", subtract(num1,num2))
        
    elif choice=="3":
        print(num1,"*",num2,"=", multiply(num1,num2))
        
    elif choice=="4":
        print(num1,"/",num2,"=", divide(num1,num2))
        
    elif choice=="5":
        print(num1,"^",num2,"=", power(num1,num2))

    elif choice=="6":
        s,t=cal_OR(num1,num2)
        print(num1,"을 ",num2,"로 나누었을 때 몫은", s,"\n",num1,"을 ",num2,"로 나누었을 때 나머지는", t)