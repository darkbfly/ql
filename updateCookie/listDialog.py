import tkinter as tk

返回值 = -99
win = tk.Tk()

def myfunction(data):
    global 返回值
    返回值 = data
    win.quit()

def runDialog(jsonData):
    n = len(jsonData)
    win.title("列表界面")
    win.attributes('-topmost', True)  # 将顶层窗口置于最前
    win.geometry('{width}x{high}'.format(width=300, high=n * 50))

    for x in jsonData:
        button = tk.Button(win, text=x, padx=10, pady=10, command=lambda j=x: myfunction(jsonData[j]))
        button.pack()
    tk.mainloop()
    return 返回值


if __name__ == '__main__':
    print(runDialog({'按钮1': 1, '按钮2': 3}))