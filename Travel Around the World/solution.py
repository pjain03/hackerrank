N, C = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# first shot at storing previous info for dyn. prog. Don't see how this would reduce computation.
diff = [a[x] - b[x] for x in range(N)]
num = N
# start at a city
for i in range(N):
    gas = min(C, a[i])
    k = i
    # travel to other cities
    for j in range(N):
        # unless no gas left for travel
        gas -= b[k]    
        if gas < 0:
            num -= 1
            break
        k = (k + 1) % N
        # fill as much as possible
        gas = min(C, gas + a[k])
        
print(num)        