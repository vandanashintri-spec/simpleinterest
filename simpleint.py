def simint(principal,interest,time):
    return (principal*interest*time)/100

if__name__=="__main__":
    p=int(input("Enter principal amount"))
    i=int(input("Enter interest"))
    t=int(input("Enter time"))

print("Simple interest:",simint(p,i,t))