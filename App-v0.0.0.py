from customtkinter import *
import socket


HOST = '192.168.8.100'
port = 5555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = CTk()

app.title("Easy script")
width, height = 800, 800
app.geometry(str(width) + "x" + str(height))
app.geometry("+" + str(int(app.winfo_screenwidth()/2 - width/2)) + "+" + str(int(app.winfo_screenheight()/2 - height/2)))

app.mainloop()
