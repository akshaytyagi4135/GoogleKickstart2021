def kickstart():
    def fac(n):  
        if n == 1:  
            return n  
        else:  
            return n*fac(n-1)
    def suffle(li):
        for j in range(len(li)-1):
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp
    def order():
        k=0
        for i in range(l):
            if(temp1[i]==lis[i]):
                k=k+1
        return k
    def combine(lis):
        w=''
        for i in lis:
             w=w+i
        print(w)
    testcase=int(input(""))
    for i in range(testcase):
        s=str(input(""))
        l=len(s) #for length
        f=fac(l) #factorial value
        lis=list(s) #listing string
        temp1=list(s)
        j=0
        for i in range(f):
            suffle(lis)
            k=order()
            if(k==0):
                combine(lis)
                break
            else:
                j=j+1
            if(j==f):
                print("IMPOSSIBLE")
kickstart()

