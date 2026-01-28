# gonna use `yield from ...` keyword 
def dummy_things():
    yield 'some thing 1'
    yield 'some thing 2'
    yield 'some thing 3'
    yield 'some thing 4'

def dummy_items():
    yield 'some item 1'
    yield 'some item 2'
    yield 'some item 3'
    yield 'some item 4'

def main(): # just yield from both funcs and use them however
    res1 = yield from dummy_items()
    res2 = yield from dummy_things()
    
    print(res1) # both of em returns none. why? 
    print(res2)

for item in main():
    print("CURRENT ITEM: ", item)
    