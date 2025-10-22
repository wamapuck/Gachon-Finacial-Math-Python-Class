# csv파일 split으로 나누어서 사용

total = 0

for line in open('data.csv'):
    t = line.split(',')
    total = total + print(float(t[1]))