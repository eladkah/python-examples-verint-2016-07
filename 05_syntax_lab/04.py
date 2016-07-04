
line = "dummy"
arr = []
index = 0
while (line != ""):
    line = raw_input()
    arr.insert(index, line)
    index+=1
for i in range(1,index + 1):
    print arr[index-i]