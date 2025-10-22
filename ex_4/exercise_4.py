# import urllib.request

# def download_file(url, filename):
#     txt = urllib.request.urlopen(url).read().decode('utf-8')
#     open(filename, 'w').write(txt)

# download_file('http://jonghyup.com/tmp/input.txt', 'input.txt')


with open('input.txt', 'r') as f:
    data = f.readlines()

for i in data:
    if i[:9] == '202531340':
        print(i[0:-2])


