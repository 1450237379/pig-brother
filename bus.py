money = int(input("输入你有多少钱"))
seat = int(input("输入有多少座位"))

if money >= 2:
    print("可以上车")

    if seat >= 1:
        print("有座位")
    else:
        print("没有座位")

else:
    print("没钱上车")
