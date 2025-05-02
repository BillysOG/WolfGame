def happy(func):
    def wrapper():
        print("She's happy!")
        func()
    return wrapper

def smiling(func):
    def wrapper():
        print("She's smiling!")
        func()
    return wrapper

@happy
@smiling
def cute():
    print("She's... cute.....")
    
cute()