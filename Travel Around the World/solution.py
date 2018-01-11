N, C = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
valid_city = [True for x in range(N)]

for i in range(N):
    if b[i] > C or b[i] - a[i] > C:
        print(0)
        exit()   
    a[i] = min(a[i], C)    

# so that starting at any point in this (in first N), we take N steps and reach the start again
a = a + a
b = b + b
for i in range(N):
    if valid_city:
        # you can travel from this city to next if a[i] > b[i]
        diff = a[i] - b[i]
        # if not ie a[i] < b[i] meaning it costs more to travel than we have
        if diff < 0:
            valid_city[i] = False
            # max value this can take is 2N by design, so we only need to be cautious of staying in bounds of valid_city
            k = i + 1
            change = 0
            while diff < 0 and change < N:
                diff += a[k] - b[k]
                if diff < 0:
                    valid_city[k % N] = False
                change += 1
                k += 1

sum_valid_cities = 0
for i in range(N):
    if valid_city[i]:
        print(i)
        sum_valid_cities += 1
print(sum_valid_cities)        