import tkinter
from datetime import datetime

hshmeng = tkinter.Tk()#创建一个窗口
hshmeng.title("HSHMENG")#设置标题
hshmeng.geometry("500x300")#设置大小
hshmeng.config(bg="pink")#设置背景颜色

def hastime():
    now = datetime.now()#获取当前时间
    now_text = now.strftime("%Y-%m-%d %H:%M:%S")#格式化当前时间
    shuru_huoqu = shuru.get()#获取输入框内容
    liebiao.insert(0,now_text+"--"+shuru_huoqu)
    shuru.delete(0,tkinter.END)

shuru = tkinter.Entry(hshmeng,width=40)#创建输入布局控件
shuru.grid(row=0,column=0)#布局输入框控件
anniu = tkinter.Button(hshmeng,text="记录",command=hastime)
anniu.grid(row=0,column=1)
liebiao = tkinter.Listbox(hshmeng,width=50)
liebiao.grid(row=2,column=0,columnspan=2,padx=20,pady=10)

hshmeng.mainloop()#消息循环，保持界面显示