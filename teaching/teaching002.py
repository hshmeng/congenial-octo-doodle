import random

def guess_number_game():
    # 生成一个 1 到 100 之间的随机数
    number_to_guess = random.randint(1, 100)

    # 初始化尝试次数
    attempts = 0

    while True:
        # 让用户猜测数字
        user_guess = int(input("猜一个 1 到 100 之间的数字: "))
        attempts += 1

        # 检查用户的猜测是否正确
        if user_guess == number_to_guess:
            print(f"恭喜！你在 {attempts} 次尝试后找到了数字。")
            break
        elif user_guess < number_to_guess:
            print("太低了！再试一次。")
        else:
            print("太高了！再试一次。")

# 开始游戏
guess_number_game()
