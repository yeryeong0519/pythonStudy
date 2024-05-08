def div(func):
    def wrapper():
        return "<div>" + str(func()) + "</div>"
    return wrapper

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@div
@para
def outname():
    return "이름 : " + name + "님"

@div 
@para
def outage():
    return 29