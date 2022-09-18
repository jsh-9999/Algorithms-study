# n = 1260 basic example of greedy method
#
# count =0
#
# coin_types= [500, 100 ,50, 10]
#
# for coin in coin_types:
#     count+=n
#     n%=coin
# print(count)


# n,m = map(int, input().split()) #using min() of python
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_val = min(data)
#
#     result = max(min_val, result)
# print(result)


n,m = map(int, input().split())

result =0

for i in range(m):
    data = list(map(int, input().split()))

    min_value = 10001

    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)

