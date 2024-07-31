import turtle

def draw_star():
    # 创建一个新的 turtle 对象
    star = turtle.Turtle()

    # 画一个五角星
    for i in range(5):
        star.forward(100) # 前进 100 步
        star.right(144)   # 右转 144 度

    # 隐藏 turtle
    star.hideturtle()

# 运行画星星的函数
draw_star()

# 保持窗口打开
turtle.done()
