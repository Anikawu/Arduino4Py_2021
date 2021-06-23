
def calc_bmi(h,w):
    if h<=0 or w<=0:
        return None
    def get_bmi():
        bmi = w/((h/100)**2)
        return bmi
    return  get_bmi

if __name__=='__main__':
    bmi1 = calc_bmi(170,60)
    bmi2 = calc_bmi(180,90)
    print("%.2f" % bmi1(),"%.2f" %bmi2())
