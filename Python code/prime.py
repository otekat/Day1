def prime_num(n):
    for x in range(0,n):
        p=1
        for y in range(2,x):
            i=x%y
            if i==0:
                p=0
                break
        if p==1:
            print(x)
            
