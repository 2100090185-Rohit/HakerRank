n,c,m = input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = list(map(int, input().strip().split(' ')))
flag=0
for i in range(n):
    if(p[i]>(m*c)):
        print("No")
        break
    elif(p[i]<= (m*c)):
        flag=flag+1
if(flag==n):
    print("Yes")