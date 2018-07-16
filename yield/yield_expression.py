def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value) # yield returns None if called by next()
                                      # otherwise returns the val passed in send(val)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

print("\nCreates generator:\n")

generator = echo(1)

print(generator)

print("\nFirst 'next()' call\n")

print(next(generator))

print("\nSecond 'next()' call\n")

print(next(generator))

print("\nFirst 'send()' call\n")

print(generator.send(2))

print("\nThird 'next()' call\n")

print(next(generator))

print("\nFirst 'throw()' call\n")

generator.throw(TypeError, "spam")

print("\nFourth 'next()' call\n")

print(next(generator))

generator.close()