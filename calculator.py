num1 = int(input('Enter the Value 1 :'))
num2 = int(input('Enter the Value 2 :'))
opr = input('Enter (+ - * /)')

if opr=='+':
    print(num1+num2)
elif opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
else :
    print('invalid opr....')            