x= int(input("Enter the number:"))
s=1
if x%2==0 :
    x=x-1
for i in range(0,x):
    print(s,end="\t")
    s=s+2
