# import urllib.request

# def download_file(url, filename):
#     txt = urllib.request.urlopen(url).read().decode('utf-8')
#     open(filename, 'w').write(txt)

# download_file('http://jonghyup.com/tmp/input.txt', 'input.txt')


out = open('output.txt', 'w')

for line in open('input.txt'):
    if line == '202531340':
        print(line[-1])
        _ = out.write(line) # out.write(line[-1])만 사용하면 추가된 내용의 줄 수가 나옴

with open ('output.txt', 'w') as f:
    for line in open('input.txt'):
        if line == '202531340':
            print(line[-1])
            _ = f.write(line)

out.close()
