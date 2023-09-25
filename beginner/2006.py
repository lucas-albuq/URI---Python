t = int(input())
a, b, c, d, e = map(int, input().split())
count = 0
if a == t:
    count+=1
if b == t:
    count+=1
if c == t:
    count+=1
if d == t:
    count+=1
if e == t:
    count+=1
print(count)