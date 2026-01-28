def get_some_val_infinitely():
    counter = 0
    while True:
        yield counter 
        counter += 1

ref = get_some_val_infinitely()

n = 10 # control the infinite force to tame to your liking
for _ in range(n): # lets limit to just values from the infinite generator vals
    print(next(ref)) # calling the created generator func