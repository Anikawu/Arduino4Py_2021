#lambda lab :
#請利用lambda 做出能夠判斷odd 奇數 ,even 偶數的函式
#result(4) 得到"even"



result = lambda x: "even" if x % 2==0 else "odd"
printResult = lambda n:print(n)
n=3
printResult(result(n))