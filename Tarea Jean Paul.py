i=0
i2=0
arreglo1=[0,0,0,0,0,] 
arreglo2=[0,0,0,0,0,] 
result=[0,0,0,0,0,0,0,0,0,0]
while i!=5:
  arreglo1[i]=int(input("DIGITE EL numero del primer arreglo"))
  
  i=i+1
i=0
while i!=5:
  arreglo2[i]=int(input("DIGITE EL  numero del segundo arreglo"))
  i=i+1
i=0
while i!=10:
  if i<=4:
     result[i]=arreglo1[i]
  elif i>=5:
     result[i]=arreglo2[i2]
     i2=i2+1
  i=i+1
i=0
for i in range(10-1):       
       for j in range(10-1): 
           if result[j] > result[j+1]:
               result[j], result[j+1] = result[j+1], result[j]
print("El arreglo es ",result)
