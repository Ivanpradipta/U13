def jumlahPrima(a):
    b=[]
    c=[]
    d=a*100
    for l in range(1,d):
        for q in range(2,l):
            if(l%q==0):
                break
        else:
            b.append(l)
    for i in range(1,hasil+1):
        c.append(b[i])
    f=sum(c)
    print(f)
    
hasil=5
jumlahPrima(hasil)
