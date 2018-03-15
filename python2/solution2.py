import socket
import sys
import pickle
import datetime

pat0 = ['  ###  ', ' #   # ', '# #   #', '#  #  #', '#   # #', ' #   # ', '  ###  '] # ok
pat9 = [' ##### ', '#     #', '#     #', ' ######', '      #', '#     #', ' ##### '] # ok
pat4 = ['#      ', '#    # ', '#    # ', '#######', '     # ', '     # ', '     # '] # ok
pat5 = ['#######', '#      ', '#      ', ' ##### ', '      #', '#     #', ' ##### '] # ok
pat2 = [' ##### ', '#     #', '      #', ' ##### ', '#      ', '#      ', '#######'] # ok
pat1 = ['   #   ', '  ##   ', ' # #   ', '   #   ', '   #   ', '   #   ', ' ##### '] # ok
pat6 = [' ##### ', '#     #', '#      ', '###### ', '#     #', '#     #', ' ##### '] # ok
pat8 = [' ##### ', '#     #', '#     #', ' ##### ', '#     #', '#     #', ' ##### '] # ok
pat3 = [' ##### ', '#     #', '      #', ' ##### ', '      #', '#     #', ' ##### '] # ok
pat7 = ['#######', '#    # ', '    #  ', '   #   ', '  #    ', '  #    ', '  #    '] # ok

pat0e = ['  ###', ' #   #', '# #   #', '#  #  #', '#   # #', ' #   #', '  ###'] # ok
pat9e = [' #####', '#     #', '#     #', ' ######', '      #', '#     #', ' #####'] # ok
pat4e = ['#', '#    #', '#    #', '#######', '     #', '     #', '     #'] # ok
pat5e = ['#######', '#', '#', ' #####', '      #', '#     #', ' #####'] # ok
pat2e = [' #####', '#     #', '      #', ' #####', '#', '#', '#######'] # ok
pat1e = ['   #', '  ##', ' # #', '   #', '   #', '   #', ' #####'] # ok
pat6e = [' #####', '#     #', '#', '######', '#     #', '#     #', ' #####'] # ok
pat8e = [' #####', '#     #', '#     #', ' #####', '#     #', '#     #', ' #####'] # ok
pat3e = [' #####', '#     #', '      #', ' #####', '      #', '#     #', ' #####'] # ok
pat7e = ['#######', '#    #', '    #', '   #', '  #', '  #', '  #'] # ok

MY_SECRET = "f64eb4f2ef661f744f933e6a010ee0f9\n"
BUF_SIZE = 1024

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('localhost', 9999))

msg = skt.recv(BUF_SIZE)
print(msg)

skt.send("scalzo\n")

msg = skt.recv(BUF_SIZE)
print(msg)

skt.send(MY_SECRET)

msg = skt.recv(BUF_SIZE)
print(msg)

l = 0
h = 10**6
m = int((h-l)/2)
while h > l:
    print("Sending", m, "...")
    skt.send(str(m)+"\n")

    msg = skt.recv(BUF_SIZE)
    print(msg)
    if msg[20:23] == 'big':
        l = m
        m = int((h+l)/2)
    elif msg[20:23] == 'sma':
        h = m
        m = int((h+l)/2)
    else:
        break

msg = skt.recv(BUF_SIZE)
print(msg)

lines = msg.split("\n")
# for i in range(0,7):
#     print(lines[i])

num1 = []
num2 = []
num3 = []

for i in range(0,7):
    num1.append(lines[i][0:7])
    num2.append(lines[i][16:23])
    num3.append(lines[i][32:])

if cmp(num1, pat1) == 0 or cmp(num1, pat1e) == 0:
    n1 = int(1)
elif cmp(num1, pat2) == 0 or cmp(num1, pat2e) == 0:
    n1 = int(2)
elif cmp(num1, pat3) == 0 or cmp(num1, pat3e) == 0:
    n1 = int(3)
elif cmp(num1, pat4) == 0 or cmp(num1, pat4e) == 0:
    n1 = int(4)
elif cmp(num1, pat5) == 0 or cmp(num1, pat5e) == 0:
    n1 = int(5)
elif cmp(num1, pat6) == 0 or cmp(num1, pat6e) == 0:
    n1 = int(6)
elif cmp(num1, pat7) == 0 or cmp(num1, pat7e) == 0:
    n1 = int(7)
elif cmp(num1, pat8) == 0 or cmp(num1, pat8e) == 0:
    n1 = int(8)
elif cmp(num1, pat9) == 0 or cmp(num1, pat9e) == 0:
    n1 = int(9)
elif cmp(num1, pat0) == 0 or cmp(num1, pat0e) == 0:
    n1 = int(0)
else:
    pass

if cmp(num2, pat1) == 0 or cmp(num2, pat1e) == 0:
    n2 = int(1)
elif cmp(num2, pat2) == 0 or cmp(num2, pat2e) == 0:
    n2 = int(2)
elif cmp(num2, pat3) == 0 or cmp(num2, pat3e) == 0:
    n2 = int(3)
elif cmp(num2, pat4) == 0 or cmp(num2, pat4e) == 0:
    n2 = int(4)
elif cmp(num2, pat5) == 0 or cmp(num2, pat5e) == 0:
    n2 = int(5)
elif cmp(num2, pat6) == 0 or cmp(num2, pat6e) == 0:
    n2 = int(6)
elif cmp(num2, pat7) == 0 or cmp(num2, pat7e) == 0:
    n2 = int(7)
elif cmp(num2, pat8) == 0 or cmp(num2, pat8e) == 0:
    n2 = int(8)
elif cmp(num2, pat9) == 0 or cmp(num2, pat9e) == 0:
    n2 = int(9)
elif cmp(num2, pat0) == 0 or cmp(num2, pat0e) == 0:
    n2 = int(0)
else:
    pass

if cmp(num3, pat1) == 0 or cmp(num3, pat1e) == 0:
    n3 = int(1)
elif cmp(num3, pat2) == 0 or cmp(num3, pat2e) == 0:
    n3 = int(2)
elif cmp(num3, pat3) == 0 or cmp(num3, pat3e) == 0:
    n3 = int(3)
elif cmp(num3, pat4) == 0 or cmp(num3, pat4e) == 0:
    n3 = int(4)
elif cmp(num3, pat5) == 0 or cmp(num3, pat5e) == 0:
    n3 = int(5)
elif cmp(num3, pat6) == 0 or cmp(num3, pat6e) == 0:
    n3 = int(6)
elif cmp(num3, pat7) == 0 or cmp(num3, pat7e) == 0:
    n3 = int(7)
elif cmp(num3, pat8) == 0 or cmp(num3, pat8e) == 0:
    n3 = int(8)
elif cmp(num3, pat9) == 0 or cmp(num3, pat9e) == 0:
    n3 = int(9)
elif cmp(num3, pat0) == 0 or cmp(num3, pat0e) == 0:
    n3 = int(0)
else:
    pass

finalnum = n1*100 + n2*10 + n3
print("The numbers is", finalnum)

skt.send(str(finalnum)+"\n")
msg = skt.recv(BUF_SIZE)
print(msg)

msg = skt.recv(BUF_SIZE)
print(msg)

lines = msg.split("\n")

instr = ""
for l in lines[1:9]:
    instr = instr + "\n" + l

instr = instr[1:]
# print(instr)
timing = pickle.loads(instr)
print("Microseconds:", str(timing.microsecond))

skt.send(str(timing.microsecond)+"\n")
msg = skt.recv(BUF_SIZE)
print(msg)

msg = skt.recv(BUF_SIZE)
print(msg)

monthdic = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
weeklist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(msg[25:27])
month = msg[28:31]
year = int(msg[32:34])

specific = datetime.date(year, int(monthdic[month]), day).weekday()
print(weeklist[specific])

skt.send(str(weeklist[specific])+"\n")
msg = skt.recv(BUF_SIZE)
print(msg)
