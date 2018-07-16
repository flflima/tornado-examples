def fibonacci(max):
    result = 0
    base = 1
    while result <= max:

        # This yield statement is where the execution leaves the function.
        print("resume %s" % (yield result))
        # This is where the execution comes back into the function. This is
        # just whitespace, but that it came back while preserving the state
        # of the function is pretty awesome.

        # Fibonacci code to increase the number according to
        #   https://en.wikipedia.org/wiki/Fibonacci_number
        n = result + base
        result = base
        base = n
        print("-----------------------------")

if __name__ == "__main__":
    for x in fibonacci(144):
        print(x)