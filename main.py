from datetime import datetime as dt
import requests
import turtle as trtl
import time


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7830c51a2f03f19bbecd951b282df16"




'''
UI.goto(-200, 0)
UI.write("Pick A City: ", font =  ("times","24", "bold italic"))
UI.goto(-70,0)

wn.listen()

def enter_press():
    UI.clear()
    UI.goto(0,0)

def a_press():
    UI.write("a", font =  ("times","24", "bold italic"))
    UI.forward(12)


def A_press() :
    UI.write("A", font =  ("times","24", "bold italic"))
    UI.forward(15)

def b_press():
    UI.write("b", font =  ("times","24", "bold italic"))
    UI.forward(12)


def B_press() :
    UI.write("B", font =  ("times","24", "bold italic"))
    UI.forward(15)

def c_press():
    UI.write("c", font =  ("times","24", "bold italic"))
    UI.forward(11)


def C_press() :
    UI.write("C", font =  ("times","24", "bold italic"))
    UI.forward(15)

def d_press():
    UI.write("d", font =  ("times","24", "bold italic"))
    UI.forward(12)

def D_press() :
    UI.write("D", font =  ("times","24", "bold italic"))
    UI.forward(15)

def e_press():
    UI.write("e", font =  ("times","24", "bold italic"))
    UI.forward(12)

def E_press() :
    UI.write("E", font =  ("times","24", "bold italic"))
    UI.forward(15)

def f_press():
    UI.write("f", font =  ("times","24", "bold italic"))
    UI.forward(8)


def F_press() :
    UI.write("F", font =  ("times","24", "bold italic"))
    UI.forward(16)

def g_press():
    UI.write("g", font =  ("times","24", "bold italic"))
    UI.forward(12)


def G_press() :
    UI.write("G", font =  ("times","24", "bold italic"))
    UI.forward(15)

def h_press():
    UI.write("h", font =  ("times","24", "bold italic"))
    UI.forward(13)


def H_press() :
    UI.write("H", font =  ("times","24", "bold italic"))
    UI.forward(16)

def i_press():
    UI.write("i", font =  ("times","24", "bold italic"))
    UI.forward(10)


def I_press() :
    UI.write("I", font =  ("times","24", "bold italic"))
    UI.forward(13)

def j_press():
    UI.write("j", font =  ("times","24", "bold italic"))
    UI.forward(11)


def J_press() :
    UI.write("J", font =  ("times","24", "bold italic"))
    UI.forward(15)

def k_press():
    UI.write("k", font =  ("times","24", "bold italic"))
    UI.forward(12)


def K_press() :
    UI.write("K", font =  ("times","24", "bold italic"))
    UI.forward(15)

def l_press():
    UI.write("l", font =  ("times","24", "bold italic"))
    UI.forward(10)


def L_press() :
    UI.write("L", font =  ("times","24", "bold italic"))
    UI.forward(15)

def m_press():
    UI.write("m", font =  ("times","24", "bold italic"))
    UI.forward(14)


def M_press() :
    UI.write("M", font =  ("times","24", "bold italic"))
    UI.forward(17)

def n_press():
    UI.write("n", font =  ("times","24", "bold italic"))
    UI.forward(12)


def N_press() :
    UI.write("N", font =  ("times","24", "bold italic"))
    UI.forward(15)

def o_press():
    UI.write("o", font =  ("times","24", "bold italic"))
    UI.forward(12)


def O_press() :
    UI.write("O", font =  ("times","24", "bold italic"))
    UI.forward(15)

def p_press():
    UI.write("p", font =  ("times","24", "bold italic"))
    UI.forward(12)

def P_press():
    UI.write("P", font =  ("times","24", "bold italic"))
    UI.forward(15)

def q_press() :
    UI.write("q", font =  ("times","24", "bold italic"))
    UI.forward(12)
    
def Q_press():
    UI.write("Q", font =  ("times","24", "bold italic"))
    UI.forward(15)


def r_press() :
    UI.write("r", font =  ("times","24", "bold italic"))
    UI.forward(11)

def R_press():
    UI.write("R", font =  ("times","24", "bold italic"))
    UI.forward(16)


def s_press() :
    UI.write("s", font =  ("times","24", "bold italic"))
    UI.forward(10)

def S_press():
    UI.write("S", font =  ("times","24", "bold italic"))
    UI.forward(15)


def t_press() :
    UI.write("t", font =  ("times","24", "bold italic"))
    UI.forward(10)

def T_press():
    UI.write("T", font =  ("times","24", "bold italic"))
    UI.forward(15)


def u_press() :
    UI.write("u", font =  ("times","24", "bold italic"))
    UI.forward(13)

def U_press():
    UI.write("U", font =  ("times","24", "bold italic"))
    UI.forward(15)


def v_press() :
    UI.write("v", font =  ("times","24", "bold italic"))
    UI.forward(11)

def V_press():
    UI.write("V", font =  ("times","24", "bold italic"))
    UI.forward(15)


def w_press() :
    UI.write("w", font =  ("times","24", "bold italic"))
    UI.forward(14)

def W_press():
    UI.write("W", font =  ("times","24", "bold italic"))
    UI.forward(17)


def x_press() :
    UI.write("x", font =  ("times","24", "bold italic"))
    UI.forward(12)

def X_press():
    UI.write("X", font =  ("times","24", "bold italic"))
    UI.forward(15)


def y_press() :
    UI.write("y", font =  ("times","24", "bold italic"))
    UI.forward(12)

def Y_press():
    UI.write("Y", font =  ("times","24", "bold italic"))
    UI.forward(14)


def z_press() :
    UI.write("z", font =  ("times","24", "bold italic"))
    UI.forward(12)

def Z_press():
    UI.write("Z", font =  ("times","24", "bold italic"))
    UI.forward(14)

def space_press():
    UI.write(" ", font =  ("times","24", "bold italic"))
    UI.forward(12)

CITY = ""



wn.listen()
wn.onkey(a_press, "a")
wn.onkey(A_press, "A")
wn.onkey(b_press, "b")
wn.onkey(B_press, "B")
wn.onkey(c_press, "c")
wn.onkey(C_press, "C")
wn.onkey(d_press, "d")
wn.onkey(D_press, "D")
wn.onkey(e_press, "e")
wn.onkey(E_press, "E")
wn.onkey(f_press, "f")
wn.onkey(F_press, "F")
wn.onkey(g_press, "g")
wn.onkey(G_press, "G")
wn.onkey(h_press, "h")
wn.onkey(H_press, "H")
wn.onkey(i_press, "i")
wn.onkey(I_press, "I")
wn.onkey(j_press, "j")
wn.onkey(J_press, "J")
wn.onkey(k_press, "k")
wn.onkey(K_press, "K")
wn.onkey(l_press, "l")
wn.onkey(L_press, "L")
wn.onkey(m_press, "m")
wn.onkey(M_press, "M")
wn.onkey(n_press, "n")
wn.onkey(N_press, "N")
wn.onkey(o_press, "o")
wn.onkey(O_press, "O")
wn.onkey(p_press, "p")
wn.onkey(P_press, "P")
wn.onkey(q_press, "q")
wn.onkey(Q_press, "Q")
wn.onkey(r_press, "r")
wn.onkey(R_press, "R")
wn.onkey(s_press, "s")
wn.onkey(S_press, "S")
wn.onkey(t_press, "t")
wn.onkey(T_press, "T")
wn.onkey(u_press, "u")
wn.onkey(U_press, "U")
wn.onkey(v_press, "v")
wn.onkey(V_press, "V")
wn.onkey(w_press, "w")
wn.onkey(W_press, "W")
wn.onkey(x_press, "x")
wn.onkey(X_press, "X")
wn.onkey(y_press, "y")
wn.onkey(Y_press, "Y")
wn.onkey(z_press, "z")
wn.onkey(Z_press, "Z")

wn.onkey(space_press, "space")
wn.onkey(enter_press, "Return")




'''






def kel_cel_fer(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit


CITY = input("Pick a city: ")

UI = trtl.Turtle()
UI.penup()

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
x = (response['cod'])


while x != 200: 
    response['message']
    print("city not valid")
    CITY = input("Pick a city: ")
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    x = (response['cod'])
        

else:



    temp_kelvin = response['main']['temp']
    temp_cel, temp_fer = kel_cel_fer(temp_kelvin)

#work on time later(it isnt working)

    time_difference = response['timezone']

    time = time.time()
    time = time + 25200
    time = time + time_difference
    time = round(time)



    time = dt.fromtimestamp(time)


   



    temp_fer = round(int(temp_fer))
    



    wn = trtl.Screen()
    UI.penup()
    UI.goto(-730, 370)
    UI.write(CITY, font = ("Herculanum", "75", "bold italic"))
    UI.right(90)
    UI.forward(80)
    UI.left(90)
    deg_sym = "°F"
    UI.write( temp_fer, "°", font = ("Herculanum", "60", "bold italic"))
    UI.write(deg_sym, font = ("Herculanum", "60", "bold italic"))

    UI.goto(-730,370)
    UI.right(90)
    UI.forward(120)
    UI.left(90)
    UI.write(time, font = ("Herculanum", "24", "bold italic"))


    wn.mainloop()
