from datetime import datetime as dt
import requests
import turtle as trtl
import time


wn = trtl.Screen()
UI = trtl.Turtle()
UI.penup()



def a_press():
    UI.write("a")
    UI.forward(10)

def enter_press():
    UI.clear()


def A_press() :
    UI.write("A")
    UI.forward(10)



wn.listen()
wn.onkey(a_press, "a")
wn.onkey(A_press, "A")
wn.onkey(enter_press, "Return")






wn.mainloop()