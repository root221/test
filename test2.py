computed = {}
def combination(n,r):
    if (n,r) in computed:
        return computed[(n,r)]
    elif r == 1:
        computed[(n,r)] = n
        return n
    elif r==n:
        computed[(n,r)] = 1
        return 1
    else: 
        computed[(n,r)] = combination(n-1,r) + combination(n-1,r-1) 
        return computed[(n,r)]
    
    
#print(combination(5,2))
print(combination(990,33))
