cases = int(input("How many cases do you want? ")

for i in range(cases):
    nks = []
    for i range(3):
        nks.append(int(input("N, K, S: ")))
    ktime = nks[1]-nks[0]
    ans1 = n+1
    ans2 = (k-s)+(n-s)
    
    if ans1 <= ans2:
        print(f"Case #{cases}: {ans1+ktime} ")
    else:
        print(f"Case #{cases}: {ans2+ktime}")
