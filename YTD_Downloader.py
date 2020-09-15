from tkinter import *
from tkinter import ttk
from pytube import YouTube                #pip install pytube3
import tkinter.font as font
from tkfilebrowser import askopendirname  #pip install tkfilebrowser
from PIL import ImageTk,Image             #pip install Pillow

root = Tk()
root.resizable(width=False, height=False)
root.title("Youtube Video Downloader")
root.geometry("455x510")
root.iconbitmap("YT.ico")
folder_img = ImageTk.PhotoImage(Image.open("folder (2).png"))

root.configure(background="white")

def verify():
      try:
            yt = YouTube(link.get())
            Label(root,text=' '+yt.title+"\nVERIFIED ✔",fg="green").grid(row=2,column=1)
      except:
            if len(link.get())<1:
                  er=Label(root,text="    Please Enter URL    ",fg="blue").grid(row=2,column=1)
                  er.grid_forget()
            else:
                  
                  er2=Label(root,text="Invalid URL Entered ✗",fg="red").grid(row=2,column=1)
                  er2dqw.grid_forget()

def opendir():
      global dir_path
      dir_path = askopendirname(title = "Select path",initialdir="C:/")
      print(dir_path)
      if len(dir_path)>0:
            dir_path = str(dir_path+'\\')
      path.insert(0,str(dir_path))  
      
def download():
      
      if len(link.get())<1:
            er=Label(root,text="    Please Enter URL    ",fg="blue").grid(row=2,column=1)
      else:
                 
            er2=Label(root,text="Invalid URL Entered ✗",fg="red").grid(row=2,column=1)

      yt = YouTube(link.get())
      choice = quality.get()
      
      if choice == choices[0]:
            video = yt.streams.get_by_itag(5)
      elif choice == choices[1]:
            video = yt.streams.get_by_itag(18)
      else:
            audio = yt.streams.get_audio_only()
            audio.download(dir_path)
      video.download(dir_path)
      Label(root,text="✔ Downloaded Successfully! ✔").grid(row=9,column=1)
                  
 
title=Label(root,text="Youtube Video Downloader",fg="red",bg="white",font="catull 20 bold")
title.grid(row=0,column=0,columnspan=3,pady=10)   
      
#Link
Label(root,text="Enter Link",pady=25,bg="white",font="catull 10 bold").grid(row=1,column=0)
link = Entry(root,width=50,bd=2)
link.grid(row=1,column=1,padx=10,ipady=3)
Button(root,text="Verify",font="8",command=verify,padx=1).grid(row=1,column=2)

#Quality
Label(root,text="Quality",pady=25,bg="white",font="catull 10 bold").grid(row=3,column=0)

choices = ["720p","360p","Audio (mp3)"]

quality = ttk.Combobox(root,values=choices,state="readonly")
quality.current(1)                                            # Putting Default value as 360p
quality.grid(row=3,column=1,ipadx=50,ipady=3)

#Path
Label(root,text = "Save to",bg="white",font="catull 10 bold").grid(row=5,column=0,pady=20)
path = Entry(root,width = 50,bd=1)
path.grid(row=5,column=1,ipady=3)
folder_button = Button(root,image = folder_img,command = opendir).grid(row=5,column=2)

#Download
download = Button(root,text="DOWNLOAD",padx=30,fg="white",bg="red",font="catull 15",command=download)
download.grid(row=7,column=1,pady=25)

#Exit
Button(root,text="EXIT",padx=30,pady=5,font="bold 10",command=root.destroy).grid(row=10,column=1)

#Developer
Label(root,text="Developer: Prithviraj Lohar",fg="#19CF21",font="Helvetica 12 bold").grid(row=14,column=1,pady=30)
root.mainloop()