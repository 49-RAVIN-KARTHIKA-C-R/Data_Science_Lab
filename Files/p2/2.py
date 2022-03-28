with open('text1.txt') as f1:
    with open('text2.txt','a') as f2:
        f2.write(f1.read())
with open('text2.txt') as f:
    print(f.read())