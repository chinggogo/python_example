# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
import random

print("終極密碼(範圍1~100)(包含1、100)")
min = 1
max = 100
count=1
goal = random.randint(1,100)
while True:
    num=int(input("請輸入數字({0}~{1}):".format(min,max)))
    if num < min or num > max :
        print("超出範圍，重新輸入")
        continue
    if num == goal:
        print("用了{0}次恭喜中獎".format(count))
        break
    if num > goal:
        if num == max:
            max -= 1
        else:
            max = num
        print("小一點")
    else:
        if num == min:
            min+=1
        else:
            min = num
        print("大一點")
    count+=1

    






