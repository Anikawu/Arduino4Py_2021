# 利用 lambda 設計一個 bmi 函數式宣告
# 並 "印出" 170, 60 的 "bmi 值"
# bmi <= 18 "過輕", bmi > 23 "過重", 其他 "正常"
# Ex: checkBMI(170, 60) 輸出 24.76 (正常)

def getBMIResult(bmi):   #if 直接寫下面lambda def可不用寫
    if bmi <=18:
        return "過輕"
    elif bmi >23:
        return"過重"
    else:
        return "正常"


w=60
h=170
bmiValue = lambda h,w:w/(h/100)**2
#checkBMI = lambda bmi:"過輕" if bmi<=18 else"過重" if bmi>23 else "正常"
checkBMI =lambda bmi:getBMIResult(bmi)
bmi=bmiValue(170,60)
print("%.2f"%bmi,checkBMI(bmi))

