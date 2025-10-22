import urllib.request

# txt = urllib.request.urlopen("http://jonghyup.com/tmp/score.csv").read().decode('utf-8')
# open ('score.csv', 'w').write(txt)

nameList = []

with open('score.csv', 'r') as f:
    data = f.readlines()
    for i in data[1:]:
        i = i.split(",")
        print(i)
        print(type(i[2]))
        if int(i[1])+int(i[2])+int(i[3]) >= 250:
            nameList.append(i[0])

print(len(nameList))
for i in nameList:
    print(i)

