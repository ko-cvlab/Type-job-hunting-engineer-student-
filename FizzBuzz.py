for num in range(1, 101):
    string = ''

    # ここから記述
    # 15の倍数のとき，stringを"FizzBuzz"とする．
    if num%15 == 0:
        string = "FizzBuzz"
    # 5の倍数のとき，stringを"Buzz"とする．
    elif num%5 == 0:
        string = "Buzz"
    # 3の倍数のとき，stringを"Fizz"とする．
    elif num%3 == 0:
        string = "Fizz"
    # それ以外のとき，stringを変数"num"とする．
    else:
        string = str(num)
    # ここまで記述

    print(string)