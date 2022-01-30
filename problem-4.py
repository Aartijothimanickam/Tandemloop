l=list(map(int,input("enter the list of numbers: ").split()))
d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in d:
     for j in l:
        if j%i == 0 :
            d[i]=d[i]+1
print(d)
