#python 沒有 switch case
#lambda + dict 合作

id ="A123456789"
sex =id[1]
print(sex)

sex_info ={
    1:lambda: print("男"),
    2:lambda: print("女")
}
sex_error = lambda : print("性別錯誤")
sex_info.get(int(sex),sex_error)()