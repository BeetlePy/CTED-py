import better_exceptions
better_exceptions.hook()
def error1(input):
    return input + 1

def error2(input):
    return input + 2

def str_erro(input):
    return str(input)

def real_error(input):
    return input + 1

input = 1
a = error1(input)
b = error2(a)
c = str_erro(b)
d = real_error(c)
print(d)
test = "hi"
print(test)