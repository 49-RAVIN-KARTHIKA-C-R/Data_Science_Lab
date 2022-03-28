with open("text") as f:
    data = f.read()
    pos = int(input('Enter the position :'))
    temp = data[pos:].index('.')
    endPos = pos + temp + 1

with open('text', "w") as f:
    f.write(data[:pos] + data[endPos:])

with open("text") as f:
    print(f.read())
