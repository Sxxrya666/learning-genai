from pydantic import BaseModel 

# its very simple . its just a class that will be using itself.
# so in order to tell a class in python that "hey i am going to be using myself",
# i cant just directly assign a type hint saying `some_property: int[<class_name>] 
# or items: list[Item]`; it will throw a NameError. so, my guy pydantic allows to reference it by just passing the name of the class as a string. THATS IT.


class Folder(BaseModel):
    name: str
    subfolders: list['Folder'] = [] # mucha perfecto
    # subfolders: list[Folder] = [] # INCORRECTO CUZ
obj = {
    # already passed name, so need to pass again.
    'subfolders': [{
        "name": 'someshit'
    }]
}

f = Folder(name='someFolder', **obj)
# OUTPUT: name='someFolder' subfolders=[Folder(name='someshit', subfolders=[])]

print(f)