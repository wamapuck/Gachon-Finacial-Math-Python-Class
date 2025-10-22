import urllib.request
txt = urllib.request.urlopen("http://jonghyup.com/tmp/score.csv").read().decode('utf-8')

txt = txt.split("\n")
print(txt)

List = []
nameList = []

for i in txt[1:-1]:
    i = i.split(",")
    # print(i)
    # print("=============================")

    if int(i[1]) + int(i[2]) + int(i[3]) >= 250:
        nameList.append(i[0])

print(len(nameList))
for i in nameList:
    print(i)
