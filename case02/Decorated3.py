# 裝飾器3 + 帶參數

def login(password):
    def decorated(func): #func=要被裝飾的方法  ex:report()
        def check():
            if (password ==1234):
                print("登入成功")
                func()
            else:
                print("登入失敗")
                None
        return check
    return decorated


@login(password=1234)
def report():
    print("密件:解封日 7.12")

report()