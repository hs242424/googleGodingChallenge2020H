cases = int(input("How many cases do you want? "))

for i in range(cases):
    nks = []
    for i in range(3):
        nks.append(int(input("N, K, S: ")))
    n = nks[0] 
    k = nks[1]
    s = nks[2]
    ktime = k
    ans1 = n+1
    ans2 = (k-s)+(n-s)
    
    if ans1 <= ans2:
        print(f"Case #{cases}: {ans1+ktime} ")
    else:
        print(f"Case #{cases}: {ans2+ktime}")
