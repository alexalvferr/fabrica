n = 1 
P = 0 
I = 0 

while n <= 10: 
  a = int(input('Digite Um Número Inteiro: ')) 
  n = n + 1 
  if a % 2 == 0: 
    P = P + 1 
  else: 
    I = I + 1 
    
     
print("A qtd de números pares é: ", P) 
print("A qtd de números ímpares é: ", I) 