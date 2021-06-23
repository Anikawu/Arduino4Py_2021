#嵌套函式1
def mssage(text):
    text=text + "by 巨匠電腦"
    def print_message():
        print(text)

    return print_message

def mssage2(text):
    text=text + "by 巨匠電腦"
    def print_message():
        print(text)

    return print_message



if __name__ =='__main__':
    m1= mssage("Hello")
    m1()   #有()表示立即執行
    mssage2("Hello")