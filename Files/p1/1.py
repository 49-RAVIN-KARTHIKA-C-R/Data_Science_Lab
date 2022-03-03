with open('text1.txt') as f1:
    with open('text2.txt','w') as f2:
        f2.write(f1.read())
with open('text2.txt','r') as f:
    print(f.read())
