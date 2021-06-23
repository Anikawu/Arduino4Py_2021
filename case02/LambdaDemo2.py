#取的x,y的最大值  並將最大值 *2
def max(x,y):
    if x> y:
        return x
    else:
        return y

if __name__=='__main__':
    a=10
    b=15
    maxValue =max(a,b)
    result=maxValue *2
    print(result)
    #-------lambda寫法------
    maxValue = lambda x,y :x if x>y else y
    result = maxValue(a,b) *2
    print(result)
    # -------lambda寫法2------
    maxValue = lambda x, y: x if x > y else y
    multi2 = lambda x:x * 2
    print(maxValue(a,b))
    print(multi2(7))
    print(multi2(maxValue(a,b))) #multi2(15)
    print(multi2(15))