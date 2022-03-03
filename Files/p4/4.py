import filecmp

if filecmp.cmp('txt1', 'txt1'):
    print("Two files are equal")
else:
    print("Two files are not equal")