n=int(input("Enter The Numbers Of Elements You Want To Add In A String:"))
l1=list()


for i in range(0,n):
    a=int(input(f"Enter The {i+1} Number:"))
    l1.append(a)
k=0.        #k
for i in l1:
    if(i==5):
        k+=1
print(k)
