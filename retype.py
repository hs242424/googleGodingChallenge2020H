cases = int(input())

for i in range(cases):
    n, k, s = map(int, input().split())
    print(n, k, s)
    
    ktime = k-1
    ans1 = n+1
    ans2 = (k-s)+(n-s+1)
    
    if ans1 <= ans2:
        print(f"Case #{cases+1}: {ans1+ktime} ")
    else:
        print(f"Case #{cases+1}: {ans2+ktime}")
