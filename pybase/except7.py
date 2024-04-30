class NickNameError(Exception):
    def __str__(self) -> str:
        return "허용되지 않는 별명입니다. "

def nickName(name):
    if name == "바보":
        raise nickNameError()
    print("my nickname is %s.", name)
    
try:
    nickName("먹보")
    nickName("바보")
except NickNameError as e:
    print(e)