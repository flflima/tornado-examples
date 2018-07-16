mylist = [1, 2, 3]
for i in mylist:
    print(i)

print("...")

mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)

print("...")

mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)

print("...")

# do not print anything
for i in mygenerator:
    print(i)
else:
    print("Nothing to print")

print("...")

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i
        print("ahoy %d" % i)

mygenerator = createGenerator()

print(mygenerator)
print("")

# for i in mygenerator:
#     print(i)
print(mygenerator.__next__())

print("Wait for it...")
print("")

print(mygenerator.__next__())

print("Wait a little more...")
print("")

print(next(mygenerator))

print("...")