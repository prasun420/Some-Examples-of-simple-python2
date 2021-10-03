## uploaded in YouTube , Asked in Accenture
def turnoff(n,k):
    if (k<=0):
        return n
    return (n&~(1<<(k-1)))
n=13
k=3
print(turnoff(n,k))