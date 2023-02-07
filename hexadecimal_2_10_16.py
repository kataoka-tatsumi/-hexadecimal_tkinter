import tkinter as tk
import tkinter.ttk as ttk
import sys
import numpy as np

#終了コマンド
def close():
    sys.exit()

#2進数変換
def Conv_hex_2():
    if(str.isdecimal(entry2.get())):
        try:
            #2_10進数変換
            sinsuu_2_to_10=int(entry2.get(),2)
            text1_1=tk.Label(text="10進数結果:")
            text1_1.grid(row=3,column=0)
            text1_2=tk.Label(text="                                                ")
            text1_2.grid(row=3,column=1)
            text1_2=tk.Label(text=str(sinsuu_2_to_10))
            text1_2.grid(row=3,column=1)

            #2進数表示
            text2_1=tk.Label(text="2進数結果:")
            text2_1.grid(row=4,column=0)
            text2_2=tk.Label(text="                                                ")
            text2_2.grid(row=4,column=1)
            text2_2=tk.Label(text=entry2.get())
            text2_2.grid(row=4,column=1)

            #2_16進数変換
            sinsuu_2_to_16=hex(sinsuu_2_to_10)
            text3_1=tk.Label(text="16進数結果:")
            text3_1.grid(row=5,column=0)
            text3_2=tk.Label(text="                                                ")
            text3_2.grid(row=5,column=1)
            text3_2=tk.Label(text=str(sinsuu_2_to_16)[2:])
            text3_2.grid(row=5,column=1)

        except:
            pass

#16進数変換
def Conv_hex_16():
    try:
        #16_10進数変換
        sinsuu_16_to_10=int(entry3.get(),16)
        text1_1=tk.Label(text="10進数結果:")
        text1_1.grid(row=3,column=0)
        text1_2=tk.Label(text="                                                ")
        text1_2.grid(row=3,column=1)
        text1_2=tk.Label(text=str(sinsuu_16_to_10))
        text1_2.grid(row=3,column=1)

        #16_2進数変換
        sinsuu_16_to_2=bin(sinsuu_16_to_10)
        text2_1=tk.Label(text="2進数結果:")
        text2_1.grid(row=4,column=0)
        text2_2=tk.Label(text="                                                ")
        text2_2.grid(row=4,column=1)
        text2_2=tk.Label(text=str(sinsuu_16_to_2)[2:])
        text2_2.grid(row=4,column=1)

        #16進数表示
        text3_1=tk.Label(text="16進数結果:")
        text3_1.grid(row=5,column=0)
        text3_2=tk.Label(text="                                                ")
        text3_2.grid(row=5,column=1)
        text3_2=tk.Label(text=entry3.get())
        text3_2.grid(row=5,column=1)

    except:
        pass


#10進数変換
def Conv_hex():
    if(str.isdecimal(entry1.get())):
        #10進数表示
        text1_1=tk.Label(text="10進数結果:")
        text1_1.grid(row=3,column=0)
        text1_2=tk.Label(text="                                                ")
        text1_2.grid(row=3,column=1)
        text1_2=tk.Label(text=entry1.get())
        text1_2.grid(row=3,column=1)

        #10_2進数変換
        text2_1=tk.Label(text="2進数結果:")
        text2_1.grid(row=4,column=0)
        sinsuu_10_to_2=(bin(int(entry1.get())))
        text2_2=tk.Label(text="                                                ")
        text2_2.grid(row=4,column=1)
        text2_2=tk.Label(text=str(sinsuu_10_to_2)[2:])
        text2_2.grid(row=4,column=1)
        
        #10_16進数変換
        text3_1=tk.Label(text="16進数結果:")
        text3_1.grid(row=5,column=0)
        sinsuu_10_to_16=(hex(int(entry1.get())))
        text3_2=tk.Label(text="                                                ")
        text3_2.grid(row=5,column=1)
        text3_2=tk.Label(text=str(sinsuu_10_to_16)[2:])
        text3_2.grid(row=5,column=1)
#メイン画面
root=tk.Tk()
root.title("test")
root.geometry("350x250")
text1=tk.Label(text="10進数:")
text1.grid(row=0,column=0)
entry1=tk.Entry()
entry1.grid(row=0,column=1)
text2=tk.Label(text="2進数:")
text2.grid(row=1,column=0)
entry2=tk.Entry()
entry2.grid(row=1,column=1)
text3=tk.Label(text="16進数:")
text3.grid(row=2,column=0)
entry3=tk.Entry()
entry3.grid(row=2,column=1)
button1_1=tk.Button(text="変換",command=Conv_hex)
button1_1.grid(row=0,column=2)
button1_2=tk.Button(text="変換",command=Conv_hex_2)
button1_2.grid(row=1,column=2)
button1_3=tk.Button(text="変換",command=Conv_hex_16)
button1_3.grid(row=2,column=2)
button1_4=tk.Button(text="閉じる",command=close)
button1_4.grid(row=6,column=1)

root.mainloop()