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
# we must go backwards so that we don't change how cities that we will reach in the future will react to conditions in the
# current city, sink or not.
for i in range(2*N - 1, N - 1, -1):
    if valid_city[i % N]:
        # you can travel from this city to next if a[i] > b[i]
        diff = a[i] - b[i]
        # if not ie a[i] < b[i] meaning it costs more to travel than we have
        if diff < 0:
            valid_city[i % N] = False
            # min value this can take is N - 1 by design
            k = i - 1
            # travel backwards, marking invalid cities till diff becomes valid ie >= 0
            while diff < 0 and k >= 0:
                diff += a[k] - b[k]
                if diff < 0:
                    valid_city[k % N] = False
                k -= 1

sum_valid_cities = 0
for i in range(N):
    if valid_city[i]:
        sum_valid_cities += 1
print(sum_valid_cities)        

# runtime = O(n) since we keep track of valid and invalid cities by valid_city and the outer and inner loop only make at
# at max 2N iterations (summed)