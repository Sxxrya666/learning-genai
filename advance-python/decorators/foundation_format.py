from functools import wraps

def deco_wrapper_to_use(fn):
    @wraps(fn)
    def inner_func():
        print('before the func call')
        fn()
        print('after the func call')
    return inner_func

########################## ###########################
@deco_wrapper_to_use 
def test_func():
    print('hi from test_func boss!!')
test_func() # one way to use decorator 
print('='* 20)

########################## ###########################

def test_func2():
    print('hi from test_func 2!!')

res = deco_wrapper_to_use(test_func2)
res() # another way to call decorator 
print('='* 20)

########################## ###########################

print(f'{test_func=}')
print(f'{test_func2=}')

# OUTPUT FOR THE above 2 print statements: 
#? test_func=<function deco_wrapper_to_use.<locals>.inner_func at 0x000001A73409CFE0>
#? test_func2=<function test_func2 at 0x000001A73409C360>
#* notice that the actual funciton name is not there for the test_func print. its showing the metadata of the decorator's wrapper function. WHICH WE DONT WANT. 

##############

#* > fix ?  use the functool's -> @wraps decorator. 
#* > where? in the inner func of the decorator.  

##############
# OUTPUT AFTER THE DECORATOR: 
#? test_func=<function test_func at 0x0000020BB4F7C360>
#? test_func2=<function test_func2 at 0x0000020BB4FCD4E0>