def add_number(x, y):
    return x+y

def subtract_number(x, y):
    return x-y

def multiply_number(x, y):
    return x*y

def divide_number(x, y):
    if y==0:
        print("error:division by zero")
    return x/y

print("select operations to perform:")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

choice=input("Enter choice to perform(1/2/3/4):")

num1=float(input('Enter first number:'))
num2=float(input('Enter Second number:'))

if choice=='1':
    print("Result:", add_number(num1,num2))
elif choice=='2':
    print("Result:", subtract_number(num1,num2))
elif choice=='3':
    print("Result:", multiply_number(num1,num2))
elif choice=='4':
    print("Result:", divide_number(num1,num2))
else:
    print("Invalid input")


