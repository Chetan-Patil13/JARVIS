# What is the value of g(728) for the function below?
def h(n):
    s = True
    for i in range(1,n+1):
        if i*i == n:
            s = False
    return(s)
print(h(81))