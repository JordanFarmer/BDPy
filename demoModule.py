def foo(a, b):
    return "[foo]:result=%d" % (a + b)


def bar(a, b):
    return "[bar]:result=%d" % (a * b)

if __name__ == '__main__':
    print("inside demoModule, foo result=%s" % foo(1, 2))

    print("inside demoModule, bar result=%s" % bar(3, 4))