from sys import stdin
from sys import argv

def my_key_fun(line):
    for word in line.replace("\n", " ").split(" "):
        if word.isdigit():
            return int(word)

mylist = []
N = int(argv[1])

for line in stdin:
    mylist.append(line)

sortedlist = sorted(mylist, key=my_key_fun, reverse=True)

p = 0
previous = -1
for i in sortedlist:
    print(i.rstrip())
    if p == N+1 and p != previous:
        break
    elif p == N+1 and p == previous:
        p -= 1
        continue
    else:
        p += 1
