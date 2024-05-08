from functools import wraps

def para(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    return wrapper

@para
def outnmae(name):
    return "이름 :" + name + "님"

@div
@para
def outname():
    return "이름 : " + name + "님"

@div 
@para
def outage():
    return 29