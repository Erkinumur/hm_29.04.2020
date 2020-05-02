def myDecorator(func):
    func_name = str(func).split()[1] 
    def wraper(*args, **kwargs):
        print(f'Calling {func_name}({args}, {kwargs})')
        result = func(*args, **kwargs)
        print(f'Finished {func_name}({result})')
    return wraper



@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)

    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)