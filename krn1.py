def uskor(func):
    def wr(u,u0,t):
        print('a = (u − u0) / t ; a= ', (u-u0) / t)
        return func(u,u0,t)
    return wr
@uskor
def hz(u,u0,t):
    print('s=0,5*(u0+u)*t')
    s=0,5*(u0+u)*t
    return s
res=hz(100,1,12)
print(res)