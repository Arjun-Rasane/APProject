from datetime import datetime as dt
import requests
import turtle as trtl
import time


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7830c51a2f03f19bbecd951b282df16"

wn = trtl.Screen()
UI = trtl.Turtle()
UI.penup()

UI.goto(-200, 0)
UI.write("Pick A City: ", font =  ("times","24", "bold italic"))
UI.goto(-70,0)

wn.listen()

def enter_press():
    UI.clear()

def a_press():
    UI.write("a")
    UI.forward(10)


def A_press() :
    UI.write("A")
    UI.forward(10)

def b_press():
    UI.write("b")
    UI.forward(10)


def B_press() :
    UI.write("B")
    UI.forward(10)

def c_press():
    UI.write("c")
    UI.forward(10)


def C_press() :
    UI.write("C")
    UI.forward(10)

def d_press():
    UI.write("d")
    UI.forward(10)


def D_press() :
    UI.write("D")
    UI.forward(10)

def e_press():
    UI.write("e")
    UI.forward(10)


def E_press() :
    UI.write("E")
    UI.forward(10)

def f_press():
    UI.write("f")
    UI.forward(10)


def F_press() :
    UI.write("F")
    UI.forward(10)

def g_press():
    UI.write("g")
    UI.forward(10)


def G_press() :
    UI.write("G")
    UI.forward(10)

def h_press():
    UI.write("h")
    UI.forward(10)


def H_press() :
    UI.write("H")
    UI.forward(10)

def i_press():
    UI.write("i")
    UI.forward(10)


def I_press() :
    UI.write("I")
    UI.forward(10)

def j_press():
    UI.write("j")
    UI.forward(10)


def J_press() :
    UI.write("J")
    UI.forward(10)

def k_press():
    UI.write("k")
    UI.forward(10)


def K_press() :
    UI.write("K")
    UI.forward(10)

def l_press():
    UI.write("l")
    UI.forward(10)


def L_press() :
    UI.write("L")
    UI.forward(10)

def m_press():
    UI.write("m")
    UI.forward(10)


def M_press() :
    UI.write("M")
    UI.forward(10)

def n_press():
    UI.write("n")
    UI.forward(10)


def N_press() :
    UI.write("N")
    UI.forward(10)

def o_press():
    UI.write("o")
    UI.forward(10)


def O_press() :
    UI.write("O")
    UI.forward(10)

def p_press():
    UI.write("p")
    UI.forward(10)

def P_press():
    UI.write("P")
    UI.forward(10)

def q_press() :
    UI.write("q")
    UI.forward(10)
    
def Q_press():
    UI.write("Q")
    UI.forward(10)


def r_press() :
    UI.write("r")
    UI.forward(10)

def R_press():
    UI.write("R")
    UI.forward(10)


def s_press() :
    UI.write("s")
    UI.forward(10)

def S_press():
    UI.write("S")
    UI.forward(10)


def t_press() :
    UI.write("t")
    UI.forward(10)

def T_press():
    UI.write("T")
    UI.forward(10)


def u_press() :
    UI.write("u")
    UI.forward(10)

def U_press():
    UI.write("U")
    UI.forward(10)


def v_press() :
    UI.write("v")
    UI.forward(10)

def V_press():
    UI.write("V")
    UI.forward(10)


def w_press() :
    UI.write("w")
    UI.forward(10)

def W_press():
    UI.write("W")
    UI.forward(10)


def x_press() :
    UI.write("x")
    UI.forward(10)

def X_press():
    UI.write("X")
    UI.forward(10)


def y_press() :
    UI.write("y")
    UI.forward(10)

def Y_press():
    UI.write("Y")
    UI.forward(10)


def z_press() :
    UI.write("z")
    UI.forward(10)

def Z_press():
    UI.write("Z")
    UI.forward(10)

def space_press():
    UI.write(" ")
    UI.forward(10)





wn.listen()
wn.onkey(a_press, "a")
wn.onkey(A_press, "A")
wn.onkey(a_press, "b")
wn.onkey(A_press, "B")
wn.onkey(a_press, "c")
wn.onkey(A_press, "C")
wn.onkey(a_press, "d")
wn.onkey(A_press, "D")
wn.onkey(a_press, "e")
wn.onkey(A_press, "E")
wn.onkey(a_press, "f")
wn.onkey(A_press, "F")
wn.onkey(a_press, "g")
wn.onkey(A_press, "G")
wn.onkey(a_press, "h")
wn.onkey(A_press, "H")
wn.onkey(a_press, "i")
wn.onkey(A_press, "I")
wn.onkey(a_press, "j")
wn.onkey(A_press, "J")
wn.onkey(a_press, "k")
wn.onkey(A_press, "K")
wn.onkey(a_press, "l")
wn.onkey(A_press, "L")
wn.onkey(a_press, "m")
wn.onkey(A_press, "M")
wn.onkey(a_press, "n")
wn.onkey(A_press, "N")
wn.onkey(a_press, "o")
wn.onkey(A_press, "O")
wn.onkey(a_press, "p")
wn.onkey(A_press, "P")
wn.onkey(a_press, "q")
wn.onkey(A_press, "Q")
wn.onkey(a_press, "r")
wn.onkey(A_press, "R")
wn.onkey(a_press, "s")
wn.onkey(A_press, "S")
wn.onkey(a_press, "t")
wn.onkey(A_press, "T")
wn.onkey(a_press, "u")
wn.onkey(A_press, "U")
wn.onkey(a_press, "v")
wn.onkey(A_press, "V")
wn.onkey(a_press, "w")
wn.onkey(A_press, "W")
wn.onkey(a_press, "x")
wn.onkey(A_press, "X")
wn.onkey(a_press, "y")
wn.onkey(A_press, "Y")
wn.onkey(a_press, "z")
wn.onkey(A_press, "z")

wn.onkey(space_press, "Space")
wn.onkey(enter_press, "Return")





CITY = input("Pick a city: ")




def kel_cel_fer(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

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


    print(time)



    temp_fer = round(int(temp_fer))
    print(temp_fer)




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
