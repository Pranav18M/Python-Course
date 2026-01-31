for i in range(1,11):
  if(i&2==0):
    print(i)


# qus num 2

count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)        


# qus num 3

a=[]
for i in range(5):
    b=int(input())
    a.append(b)
print(a)    

sum=0
for i in a:
    sum=sum+i
    sum=sum/5
print(sum)    

