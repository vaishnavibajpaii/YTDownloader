from pytube import YouTube

from os import rename
from os.path import isfile
from time import localtime , sleep

from tkinter import Tk, Entry, Grid, Place, Label, Button, GROOVE,RAISED, Text, Frame, Pack, END,LEFT, RIGHT, BOTTOM, BOTH
from tkinter import messagebox as Ms
from tkinter import filedialog as Fd

import socket
#==============================================================================================================================
Window = Tk()
Window.geometry('600x350')
Window.title("YT-Downloader..")
Window.configure(background='#d90429')
Window.resizable(0,0)
#==============================================================================================================================
# 2b2d42 , ef233c , d90429 , edf2f4
#ec4040
folder_path = ""
#==============================================================================================================================
def check_con():
    try:
        socket.create_connection(("Google.com",80))
        return True
    except OSError:
        return False
#==============================================================================================================================
def set_loc():
    global folder_path, location_text
    folder_path = Fd.askdirectory()
    if folder_path: location_text.config(text=folder_path)
    else: Ms.showerror('Folder Not selected',"Please Select a folder to download the vedio")
#============================================================================================================================== https://www.youtube.com/watch?v=igW_YJ7r1Zc
def download():
    global folder_path, url_entry, status_lable
    con = check_con()
    if con:
        url = url_entry.get()
        url_entry.delete(0,END)
        if len(url)==0: Ms.showerror('Enter URL',"Enter the URL of the vedio to download")
        if len(url)!=0:
            do = False
            if not folder_path: Ms.showerror('Folder Not selected',"Please Select a folder to download the vedio")
            else:
                status_lable.config(text=" Status :: Getting vedio... ")
                try:
                    print()
                    yt = YouTube(url)
                    do = True
                except Exception:
                    status_lable.config(text=" Status :: Download Failed! ")
                    Ms.showerror('Wrong Url',"Enter the Correct URL to download the vedio")
                if do:
                    t = localtime()
                    fomat = "mp4"
                    status_lable.config(text=" Status :: DOWNLOADING... ")
                    new_nm = f"{folder_path}/YTDownloader_vedio-{t.tm_year}-{t.tm_mon}-{t.tm_mday}-{t.tm_hour}-{t.tm_min}.{fomat}"
                    print()
                    sleep(1)
                    vedio = yt.streams.filter(progressive=True,file_extension=fomat).last()
                    vedio.download(folder_path)
                    status_lable.config(text=" Status :: VEDIO-DOWNLOADED ")
                    nm = f"{folder_path}/{vedio.title}.{fomat}"
                    nm = nm.replace("|","")
                    nm = nm.replace("#","")
                    rename(nm,new_nm)
                    fomat = "mp4"

    else: Ms.showerror('Check Network',"Please Check the Network Connection of your Device. \nAnd Make the Connection Stable")
#==============================================================================================================================
Search_lable = Label(Window,text=" URL of the Vedio :- ",font='centaur 20',bg='#d90429')
Search_lable.place(x=40,y=20)

Url_Entry_frame = Frame(Window, width=600, height=25,borderwidth=1,bg="#2b2d42")
Url_Entry_frame.place(x=50,y=50)
url_entry = Entry(Url_Entry_frame,font="Arial 15",width=30,fg="#2b2d42")
url_entry.pack()

location_frame = Frame(Window, width=600, height=2,bg='#d90429')
location_frame.place(x=40,y=100)
location_lable = Label(location_frame,text=" Location to save Vedio :-    ",font='centaur 20',bg='#d90429')
location_lable.grid(row=0,column=0)
location_button = Button(location_frame,text='Choose Loaction',font='Century 12 ',width=15,height=1,command=set_loc)
location_button.grid(row=0,column=1)
location_text = Label(location_frame,text="     Path not selected      ",fg="#edf2f4",font='centaur 15',bg='#d90429')
location_text.grid(row=1,columnspan=2)

status_lable = Label(Window,text=" Status :: NONE ",font='Century 16',bg='#d90429',fg="#edf2f4")
status_lable.place(x=40,y=275)

Search_button = Button(Window,bg='#8d99ae',text='Download',font='Century 12 ',width=8,command=download)
Search_button.place(x=475,y=275)
#==============================================================================================================================,fg="#2b2d42"

if __name__ == "__main__":
    
    Window.mainloop()