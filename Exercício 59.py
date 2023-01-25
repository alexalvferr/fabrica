num1=int(input('Digite o Primeiro Número: '))
num2=int(input('Digite o Segundo Número: '))

if num2<num1:
  for i in range(num2+1,num1,1):
    print(i)

else:
  for i in range(num1+1,num2,1):
    print(i)
    