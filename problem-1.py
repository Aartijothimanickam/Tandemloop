class operation:
    a=0
    b=0
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def op(self,s):
        if s == "Add":
            return self.a+self.b
        elif s == "Sub":
            return self.a - self.b
        elif s == "Multiply":
            return self.a * self.b
        elif s == "Divide":
            return self.a / self.b
        else:
            return 0

x=int(input())
y=int(input())
o=operation (x,y)
p=input("calculation to be done(Add,Sub,Multiply,Divide):")
print(o.op(p))
