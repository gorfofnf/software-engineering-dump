
num1= float(input("Qual o primeiro número?"))
num2= float(input("O segundo?"))
num3= float(input("E o terceiro?"))
nums=[num1,num2,num3]
if num1> num2 and num1>num3:
    print("O valor",num1,"é o maior.")
    if num2>num3:
        print("E o valor",num3,"é o menor")
    else:
        print("E o valor",num2,"é o menor")
elif num2> num1 and num2>num3:
    print("O valor",num2,"é o maior.")
    if num1>num3:
        print("E o valor",num3,"é o menor")
    else:
        print("E o valor",num1,"é o menor")
elif num3> num1 and num3>num2:
    print("O valor",num3,"é o maior.")
    if num1>num2:
        print("E o valor",num2,"é o menor")
    else:
        print("E o valor",num1,"é o menor")
org= sorted(nums,reverse=True)
print("A ordem decrescente entre eles é",org)