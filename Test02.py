

# n, k = map(int, input().split())
#
# cnt =0
#
#
# while n!=1:
#
#     if n%k==0:
#         n/=k
#         cnt+=1
#
#     elif n%k==1:
#         n-=1
#         cnt+=1
#
# print(cnt)
#


# n = int(input())
#
# x, y = 1, 1
# plans = input().split()
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx=x+dx[i]
#             ny=y+dy[i]
#
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
# print(x, y)



h = int(input())

count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)