from collections import Counter

with open('freequency.txt') as f:
    print(Counter(f.read().split()))

# dict=dict()
# with open('freequency.txt') as f:
#     data=f.read()
#     data=data.strip()
#     words=data.split(" ")
#     for words in data:
#         if dict[words] in words:
#             dict[words]+=1
#         else:
#             dict[words]=1
# for keys in list(dict.keys()):
#     print(keys+" : "+dict[keys])

