original = "one two three"
e = original.split()

e[2:3]+e[1:2]+e
print(e[2:3]+e[1:2]+e)

# 리스트인지 스트링인지 구분

master = "you must have patience my young padawan"
e = master.split()


first = e[3:4]
second = e[:3]
third = e[4:]

yoda = first + second + third
yoda = " ".join(yoda)

# print(type(yoda))

print(yoda[:22].upper() + yoda[22:])