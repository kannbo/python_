import PySimpleGUI as sg,random

a=0
plus=1
up=0
while not up>0:
    up=random.randint(0,3)
    print(up)


window=sg.Window("クリッカー",[[sg.Push(),sg.T(0,key="text"),sg.Push()],[sg.B("クリック",key="btn"),sg.B(plus*up,key="btn2")]])

while True:
    e,h=window.read()
    if e==None:
        window.close()
        break
    if e=="btn":
        a+=plus
        window["text"].update(a)
    if e=="btn2":
        if a>=plus*up:
            a-=plus*up
            plus+=1
            up+=random.randint(1,3)
            window["btn2"].update(plus*up)
            window["text"].update(a)
    print("click!")
