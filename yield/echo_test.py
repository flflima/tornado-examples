def echo():
    x = 0
    while True:
        print("call yield")
        n = (yield x)
        print("value = %s" % n)
        x += 1

echo_gen = echo()

print(echo_gen)

print(next(echo_gen))

print(echo_gen.send(20))

print(next(echo_gen))