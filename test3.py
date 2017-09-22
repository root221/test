def anonymous(x):
	return x**2 + 1

def integrate(fun,start,end):
	step = 0.1
	intercept = step
	area = 0
	while intercept < end:
		intercept += step
		area += anonymous(intercept) * step	
	return area

print(integrate(anonymous,0,10))
#integrate(anonymous,0,10)