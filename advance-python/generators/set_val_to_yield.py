def order_list():
    # incorrecto cuz. put yield in `()` like this: `{(yield)}`
    # some_item = f'you ordered a/an: {yield}'    
    # 

    # yield f'you ordered a/an: {(yield)}' # WRONG

    item1 = yield # correct: catch the val 
    yield f"you ordered a/an: {item1}" 

    item2 = yield  # catch the val
    yield f"you again ordered a/an : {item2}"
    

ref = order_list()

########################## DOESNT WORK ###########################

next(ref)
print(ref.send('milk'))
print(ref.send('icecream'))


########################## WORKS CORRECTLY ###########################

# next(ref)
# print(ref.send('milk'))
# next(ref)
# print(ref.send('icecream'))
