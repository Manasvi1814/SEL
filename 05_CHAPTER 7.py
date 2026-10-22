# using with no need to write f.close()

with open("file.txt", "r" )as f:
    data = f.read()
    print(data)