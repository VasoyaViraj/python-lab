input_str = str(input()).lower()

arr = input_str.split(' ')
sett = set(arr)
newArr = list(sett)

newArr.sort(key=lambda x:x[0])
strr = ''
for i in newArr:
    strr = newArr + i + " "

print(strr)