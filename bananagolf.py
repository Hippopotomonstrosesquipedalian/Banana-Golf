inp=input("Which Banana Golf programme do you want to run?\n")
f=open(inp,"r")
l=f.readlines()
var=[]
def a(num1,num2,op,save):
    if op==1:
        num=num1+num2
    elif op==2:
        num=num1-num2
    elif op==3:
        num=num1*num2
    elif op==4:
        num=num1/num2
    else:
        raise SyntaxError("Only arguments allowed for operator are 1, 2, 3 and 4.")
    if save==2:
        var=var+num
    elif save==1:
        print(num)
    else:
        raise SyntaxError("Only arguments allowed for savemode are 1 and 2.")
for x in range(0,len(l)):
    y=l[x]
    if y=="H"or y=="H\n":
        print("Hello, World!")
    elif y=="Q"or y=="Q\n":
        g=open(__file__)
        print(g.read())
        g.close()
    elif y[0]=="E":
        c=""
        for a in range(1,len(y)):
            c=c+y[a]
        raise Exception(c)
    elif y[0]=="X":
        d=""
        for b in range(1,len(y)):
            d=d+y[b]
        exec(d)
    elif y=="S"or y=="S\n":
        break
    elif y[0]=="P":
        e=""
        for f in range(1,len(y)):
            e=e+y[f]
        print(e)
    elif y=="B"or y=="B\n":
        print("Banana! Num num num num num!")
    elif y[0]=="V":
        g=""
        for h in range(1,len(y)):
            g=g+y[h]
        var=var+[g]
    elif y[0]=="W":
        i=""
        for j in range(1,len(y)):
            i=i+y[j]
        print(var[int(i)])
    elif y[0]=="I":
        k=""
        for m in range(1,len(y)):
            k=k+y[m]
        var=var+[input(k)]
    elif y[0]=="A":
        n=""
        for o in range(1,len(y)):
            n=n+y[o]
        exec("a("+n+")")
    elif y[0]=="#" or y=="\n":
        continue
    elif y=="R" or y=="R\n":
        print(open(inp).read())
        open(inp).close()
    else:
        raise SyntaxError("Unrecognised command. Is each command on a new line?")
exec(open(__file__).read())
