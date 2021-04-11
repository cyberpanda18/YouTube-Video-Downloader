from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    link_label = Label(root, 
                       text="YouTube link  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)
   
    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1, 
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan = 2)
   
    destination_label = Label(root, 
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)
   
    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2, 
                              column=1,
                              pady=5,
                              padx=5)
   
    browse_B = Button(root, 
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)
   
    Download_B = Button(root,
                        text="Download", 
                        command=download, 
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)
  
# Defining Browse() to select a 
# destination folder to save the video
  
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir 
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
   
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
  
def download():

    #Showing all details for videos and downloading them one by one
    link = video_Link.get()
    yt = YouTube(link)
    download_folder=download_Path.get()
    print("\nDetails for Video","\n")
    print("Title of video:   ",yt.title)
    print("Number of views:  ",yt.views)
    print("Length of video:  ",yt.length,"seconds")

    '''Progressive streams are limited to 720p and it contains both audio and video codec files
    while Dash streams have higher quality but only have video codecs.'''

    #filter out progressive streams first
    stream = str(yt.streams.filter(progressive=True))
    #print(stream)
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    #print("\nAll available options for downloads:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        #print(i+1,") ",st[1]," and ",st[3],sep='')
    print(stream)
    #tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.filter(progressive=True, resolution='720p')
    print (ys)
    if ys :
        #print("\nDownloading...")
        ys.download(download_folder)
    else:
        ys = yt.streams.get_by_resolution('360p')
        #print("\nDownloading...")
        ys.download(download_folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY", 
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_folder)
  
    #print()

# Creating object of tk class
root = tk.Tk()
   
# Setting the title, background color 
# and size of the tkinter window and 
# disabling the resizing property
root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")
   
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
   
# Calling the Widgets() function
Widgets()
   
# Defining infinite loop to run
# application
root.mainloop()

