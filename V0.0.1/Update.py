from customtkinter import *
import socket
import time
import os

HOST = '192.168.8.100'
port = 5555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = CTk()

app.title("Easy script")
app.overrideredirect(True) # removes title bar
width, height = 400, 400
app.geometry(str(width) + "x" + str(height))
app.geometry("+" + str(int(app.winfo_screenwidth()/2 - width/2)) + "+" + str(int(app.winfo_screenheight()/2 - height/2)))

progressbar = CTkProgressBar(master=app, orientation=HORIZONTAL)
progressbar.set(0)
progressbar.place(x=100, y=200)

title = CTkLabel(master=app, text='Python Easy script')
title.place(x=42, y=100)
title.configure(font=("Courier", 30))

version_text = CTkLabel(master=app, text='Version: ')
version_text.place(x=10, y=370)

info_text = CTkLabel(master=app, text='Connecting to server...', text_color='#595959')
info_text.place(x=130, y=210)


def task():
    progressbar.set(0.3)
    app.update()
    try:
        socket.connect((HOST, port))
        socket.send("version".encode('utf-8'))
        answer = socket.recv(1024).decode('utf-8')
        version_text.configure(text=f'Version: {answer}')
        socket.close()
    except ConnectionRefusedError:
        progressbar.set(0)
        info_text.place(x=100, y=210)
        info_text.configure(text='Server not reachable! closing app')
        app.update()
        time.sleep(1.5)
        app.destroy()
        return 0
    progressbar.set(0.9)
    info_text.place(x=100, y=210)
    info_text.configure(text='Connected to server! starting app')
    app.update()
    time.sleep(1)
    progressbar.set(1)
    app.destroy()
    os.system("App.py")


app.after(1000, task)
app.mainloop()

