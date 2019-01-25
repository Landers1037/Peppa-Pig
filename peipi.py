'''猪头佩琪的画法'''
import time
import turtle as t

class peipi():
    def __init__(self):
        #画笔的初始化
        print('peipi pig')

    def nose(self,x,y): #鼻子
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.setheading(-30)
        t.begin_fill()
        a=0.4
        for i in range(120):
            if 0<=i<30 or 60<=i<90:
                a=a+0.08
                t.left(3)
                t.forward(a)
            else:
                a=a-0.08
                t.left(3)
                t.forward(a)
        t.end_fill()

        t.penup()
        t.setheading(90)
        t.forward(25)
        t.setheading(0)
        t.pendown()
        t.pencolor(255,155,192)
        t.setheading(10)
        t.begin_fill()
        t.circle(5)
        t.color(160,82,45)
        t.end_fill()

        t.penup()
        t.setheading(0)
        t.forward(20)
        t.pendown()
        t.pencolor(255,155,192)
        t.setheading(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()




    def eyes(self,x,y): #眼睛
        t.color((255, 155, 192), "white")
        t.penup()
        t.goto(x, y)
        t.setheading(90)
        t.forward(-20)
        t.setheading(0)
        t.forward(-95)
        t.pendown()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.penup()
        t.setheading(90)
        t.forward(12)
        t.setheading(0)
        t.forward(-3)
        t.pendown()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

        t.color((255, 155, 192), "white")
        t.penup()
        t.seth(90)
        t.forward(-25)
        t.seth(0)
        t.forward(40)
        t.pendown()
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        t.color("black")
        t.penup()
        t.setheading(90)
        t.forward(12)
        t.setheading(0)
        t.forward(-3)
        t.pendown()
        t.begin_fill()
        t.circle(3)
        t.end_fill()

    def head(self,x,y):
        t.color((255, 155, 192), "pink")
        t.penup()
        t.goto(x, y)
        t.setheading(0)
        t.pendown()
        t.begin_fill()
        t.setheading(180)
        t.circle(300, -30)
        t.circle(100, -60)
        t.circle(80, -100)
        t.circle(150, -20)
        t.circle(60, -95)
        t.setheading(161)
        t.circle(-300, 15)
        t.penup()
        t.goto(-100, 100)
        t.pendown()
        t.setheading(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()

    def ears(self,x,y): #耳朵
       t.color((255, 155, 192), "pink")
       t.penup()
       t.goto(x, y)
       t.pendown()
       t.begin_fill()
       t.setheading(100)
       t.circle(-50, 50)
       t.circle(-10, 120)
       t.circle(-50, 54)
       t.end_fill()
       t.penup()
       t.setheading(90)
       t.forward(-12)
       t.setheading(0)
       t.forward(30)
       t.pendown()
       t.begin_fill()
       t.setheading(100)
       t.circle(-50, 50)
       t.circle(-10, 120)
       t.circle(-50, 56)
       t.end_fill()

    def face(self,x,y): #脸
        t.color((255, 155, 192))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)
        t.begin_fill()
        t.circle(30)
        t.end_fill()

    def mouth(self,x,y): #嘴巴
        t.color(239, 69, 19)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(-80)
        t.circle(30, 40)
        t.circle(40, 80)

    def body(self,x,y): #身体
        t.color("red", (255, 99, 71))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.setheading(-130)
        t.circle(100, 10)
        t.circle(300, 30)
        t.setheading(0)
        t.forward(230)
        t.setheading(90)
        t.circle(300, 30)
        t.circle(100, 3)
        t.color((255, 155, 192), (255, 100, 100))
        t.setheading(-135)
        t.circle(-80, 63)
        t.circle(-150, 24)
        t.end_fill()

    def hands(self,x,y): #手
        t.color((255, 155, 192))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(-160)
        t.circle(300, 15)
        t.penup()
        t.setheading(90)
        t.forward(15)
        t.setheading(0)
        t.forward(0)
        t.pendown()
        t.setheading(-10)
        t.circle(-20, 90)

        t.penup()
        t.setheading(90)
        t.forward(30)
        t.setheading(0)
        t.forward(237)
        t.pendown()
        t.setheading(-20)
        t.circle(-300, 15)
        t.penup()
        t.setheading(90)
        t.forward(20)
        t.setheading(0)
        t.forward(0)
        t.pendown()
        t.setheading(-170)
        t.circle(20, 90)

    def feet(self,x,y): #脚
        t.pensize(10)
        t.color((240, 128, 128))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(-90)
        t.forward(40)
        t.setheading(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

        t.pensize(10)
        t.color((240, 128, 128))
        t.penup()
        t.setheading(90)
        t.forward(40)
        t.setheading(0)
        t.forward(90)
        t.pendown()
        t.setheading(-90)
        t.forward(40)
        t.setheading(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)

    def tail(self,x,y): #尾巴
        t.pensize(4)
        t.color((255, 155, 192))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.seth(0)
        t.circle(70, 20)
        t.circle(10, 330)
        t.circle(70, 30)

    def setting(self): #画笔的设置
        t.pensize(4)
        t.hideturtle()  # 使乌龟无形（隐藏）
        t.colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
        t.color((255, 155, 192), "pink")
        t.setup(840, 500)
        t.speed(20)

    def write(self,x,y):
        t.pencolor('red')
        t.penup()
        t.goto(x,y)
        t.write('新年快乐',font=('宋体',40,'normal'))


    def main(self):
        self.setting()  # 画布、画笔设置
        self.nose(-100, 100)  # 鼻子
        self.head(-69, 167)  # 头
        self.ears(0, 160)  # 耳朵
        self.eyes(60, 140)  # 眼睛
        self.face(80, 10)  # 腮
        self.mouth(-20, 30)  # 嘴
        self.body(-32, -8)  # 身体
        self.hands(-56, -45)  # 手
        self.feet(2, -177)  # 脚
        self.write(-350,-20)
        self.tail(148, -155)  # 尾巴
        t.mainloop()

if __name__=='__main__':
    pig=peipi()
    pig.main()
