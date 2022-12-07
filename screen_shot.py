#モジュールのインポート
import tkinter
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
#日付
import datetime
#スクリーンショット
import pyautogui 


#撮影
def shot(event):
    #時刻取得
    dt_now = datetime.datetime.now()
    #print(dt_now.strftime('%Y-%m-%d-%H:%M:%S'))

    f_x0=focus.winfo_x()
    f_y0=focus.winfo_y()
    f_width=focus.winfo_width()
    f_height=focus.winfo_height()
    screen_shot = pyautogui.screenshot(region=(f_x0, f_y0, f_width, f_height+20)) 
    screen_shot.save('./スクリーンショット '+dt_now.strftime('%Y-%m-%d %H:%M:%S')+'.png')



#コンソール側ウインドウ作成
main = tkinter.Tk()
main.title("スクリーンショット")
main.geometry('400x200')


#撮影ボタン
shot_button = tkinter.Button(main,text='撮影', width=30)
shot_button.grid(column=0,row=1,padx=50,pady=20)
shot_button.bind('<Button-1>', shot)

#コンソール側を画面右下へ
# アプリ画面(Window)の幅
main_width = 400
# アプリ画面(Window)の高さ
main_height = 200
# パソコン画面の幅を取得
pcW = main.winfo_screenwidth()
# パソコン画面の高さを取得
pcH = main.winfo_screenheight()
main_x = pcW - main_width
main_y = pcH - main_height
main.geometry(str(main_width)+"x"+str(main_height)+"+"+str(main_x)+"+"+str(main_y))


#フォーカス側ウインドウ作成
focus = tkinter.Tk()
focus.title("撮影範囲")
focus.geometry('600x600')
focus.config(bg="white")
focus.attributes("-alpha",0.5)


# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
main.mainloop()