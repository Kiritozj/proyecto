#Reino del Dragon....
import random
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk,Tk, PhotoImage, Label
from PIL import Image, ImageTk as itk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

app = tk.Tk()
app.geometry("500x500")
app.configure(background="black")
tk.Wm.wm_title(app, "Funciones al ataque")
app.iconbitmap('C:\\Users\\DAGO\\Desktop\\proyecto\\imagenes\\ICONO.ico')
image = tk.PhotoImage(file = "dragon.png")
fondo = Label (app, image=image).place(x=0,y=0)

app.mainloop()



def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("Ha que cueva quieres entrar? 1 o 2?")
        cueva = input()     
    return cueva
def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)  
    FriendlyCueva = random.randint (1, 2)
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
    else:
        print ("El dragon te come de un bocado....")
# EmpezarNuevo = ("si")
# while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
#         introduccion()
   
#         NumCaverna = CambiarCueva()
   
#         cheqcueva(NumCaverna)
   
#         print ("Quieres jugar de nuevo? (si o no)")
#         EmpezarNuevo = input()
if __name__=="__main__":