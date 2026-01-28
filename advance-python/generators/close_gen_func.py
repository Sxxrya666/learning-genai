def test_func(): 
    # try: 
    while True: # infinite generator
        some_val = yield "my work is being done..."
    # except: 
    #     print('some error while working')
    
    
my_work = test_func()
print(next(my_work))
my_work.close() # closes gracefully. or just use a context manager to do that atuomatically