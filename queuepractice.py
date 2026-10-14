from collections import deque

line = deque()
p = 0

while p < 10:
    line.append(p)
    p += 1
    print(line)

print()
print()
while line:
    id = line.popleft()
    print(id)
