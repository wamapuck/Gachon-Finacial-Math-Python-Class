import urllib.request
txt = urllib.request.urlopen("http://jonghyup.com/tmp/alice.txt").read().decode('utf-8')

txt = txt.split()

# print(txt)

dict = {}

# def wc():
#     for i in txt:

#         if i == "that's":
#             dict["that's"] = dict.get("that's", 0) + 1
#             continue

#         if i == "that,":
#             dict["that"] = dict.get("that", 0) + 1
#             continue

#         if i == "that;":
#             dict["that;"] = dict.get("that;", 0) + 1
#             continue

#         if i == "the":
#             dict["the"] = dict.get("the", 0) + 1
#             continue
        
#         if i == "their":
#             dict["their"] = dict.get("their", 0) + 1
#             continue

#         if i == "them":
#             dict["them"] = dict.get("them", 0) + 1
#             continue

#     return dict

def wc(word):
    for i in txt:
        if i == word:
            dict[word] = dict.get(word, 0) + 1
            
    return dict

for i in txt:
    dict[i] = dict.get(i, 0) + 1

def wcc(word):
    return dict.get(word, 0)


    # for i in txt:
    #    dict[i] = dict.get(i, 0) + 1

    # print("%s :%d" % (word, dict[word]))


print(wcc("the"))
# print(wc(input("__")))