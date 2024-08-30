print('select an operation to perform')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
num=int(input('choose an opertion from 1 2 3 4 ='))
if num==1:
    num1=int(input('Enter the first number ='))
    num2=int(input('Enter the second number='))
    print('sum is', num1+num2)
elif num==2:
     num1=int(input('Enter the first number='))
     num2=int(input('Enter the second number='))
     print('difference is', num1-num2)
elif num==3:
     num1=int(input('Enter the first number='))
     num2=int(input('Enter the second number='))
     print('Multiplication is', num1*num2) 
elif num==4:
     num1=int(input('Enter the first number='))
     num2=int(input('Enter the second number='))
     print('division is', num1//num2)
else :
     print('invalid operation')  
     
       

    
