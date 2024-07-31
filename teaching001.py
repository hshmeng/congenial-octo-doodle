import random

def gacha_game():
    # 定义一个原神角色的列表
    characters = ["安柏", "芭芭拉", "北斗", "班尼特", "重云", "迪卢克", "迪奥娜", "优菈", "菲谢尔", "甘雨", "胡桃", "琴", "凯亚", "刻晴", "可莉", "丽莎", "莫娜", "凝光", "诺艾尔", "七七", "雷泽", "罗莎莉亚", "砂糖", "达达利亚", "旅行者", "温迪", "香菱", "魈", "行秋", "辛焱", "烟绯", "钟离"]

    # 随机选择一个角色
    selected_character = random.choice(characters)

    # 打印结果
    print(f"恭喜！你抽到了 {selected_character}！")

# 运行抽奖游戏
gacha_game()
