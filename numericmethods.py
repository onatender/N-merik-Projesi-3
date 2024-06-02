def fx(x,y):
    return  1 + y/x

def fx2(x,y):
    return y-x**2+1

def fx3(x,y):
    return -1*x*y**2


def heun(start,start_val,end,iter,fx):
    diff = (end-start)/iter

    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+diff,start_val+k1*diff)
        start_val = start_val + diff*(k1/2 + k2/2)    
        start+=diff
    return start_val


def midpoint(start,start_val,end,iter,fx):
    diff = (end-start)/iter
    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+diff/2,start_val+(k1/2)*diff)
        start_val = start_val + k2*diff
        start+=diff
    return start_val

def ralston(start,start_val,end,iter,fx):
    diff = (end-start)/iter

    while start<end:
        k1 = fx(start,start_val)
        k2 = fx(start+(3/4)*diff,start_val+(3/4)*k1*diff)
        start_val = start_val + diff*((1/3)*k1+(2/3)*k2)
        start+=diff
    return start_val

# print(heun(start=1,start_val=0.5,end=1.2,iter=2,fx=fx))
# print(midpoint(start=0,start_val=0.5,end=0.4,iter=2,fx=fx2))
# print(ralston(start=2,start_val=1,end=2.2,iter=2,fx=fx3))

iteations = [5,10,20,50,100]

for iteration in iteations:
    print(f"Heun's method for {iteration} iterations: {heun(start=1,start_val=0.5,end=1.2,iter=iteration,fx=fx)}")
    print(f"Midpoint method for {iteration} iterations: {midpoint(start=1,start_val=0.5,end=1.2,iter=iteration,fx=fx)}")
    print(f"Ralston's method for {iteration} iterations: {ralston(start=1,start_val=0.5,end=1.2,iter=iteration,fx=fx)}")