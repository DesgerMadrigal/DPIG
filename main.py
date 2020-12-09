from tkinter import *
import instaloader
from tkinter import messagebox as mg

parser = instaloader.Instaloader()

def insta():
    mg.showinfo("anuncio","descarga iniciada")
    parser.download_profile(n1.get(), profile_pic=True)
    mg.showwarning("anuncio","descarga finalizada")

root = Tk()
root.config(bd=10)
root.title("Instaloder")# titulo de la pestaña
root.iconbitmap("icon.ico")# icono de la app

n1 = StringVar()# variable de, nombre dde usuario

Label(root, text="INSTALOADER").pack()
Label(root, text="Descargar las publicaciones,").pack()
Label(root, text="de un perfil de instagram").pack()
Label(root, text=" ").pack()
Label(root, text="Digite la cuenta de usuario").pack()
Entry(root, justify="center", textvariable=n1).pack()# usuario
Label(root, text=" ").pack()
Button(root, text="Insertar", command=insta).pack()



root.mainloop()
