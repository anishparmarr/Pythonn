print("Enter 10 values")
a=[]
c=True
while c:
   b=int(input("Enter value : "))
   if b==0:
       break
   elif b%2==0:
       a.append(b)
print("The list is : ",a)
