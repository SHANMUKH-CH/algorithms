def algo(i,j):
    if len(str(i))==1 or len(str(j))==1:    return i*j
    else:
        m=(max(len(str(i)),len(str(j))))//2
        a,b=i//pow(10,m),i%pow(10,m)
        c,d=j//pow(10,m),j%pow(10,m)
        ac,bd=algo(a,c),algo(b,d)
        step3=algo((a+c),(b+d))
        return (((ac)*pow(10,2*m))+((step3-bd-ac)*pow(10,m))+(bd))
if __name__=='__main__':
    print(algo(1234,5678))