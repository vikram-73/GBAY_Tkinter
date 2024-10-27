from tkinter import *
from tkinter import ttk,messagebox
import customtkinter
import tkinter.font as font
import webbrowser
import speech_recognition
from pygame import mixer
import time
import customtkinter as tk

mixer.init()



customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("blue")


#search

def search():
    if qn.get()!="":
        if(temp.get()=='google' or temp.get()=='brave' or temp.get()=='amazon' or temp.get()=='youtube'):
            pass
        else:
       
            brav=['ibomma','i bomma','bomma','movie','movierulz','rulz','tamilrockers','soap2day','ads','noads','adds','advertisements']
            yut=['youtube','vlogs','logs','vlog','vlogging','blogs','vloging','vlogger','blogger','trailer','teaser','glimpse','tube','video','videos','channel','gaming','subscribe','reviews','review','unbox','unboxing','yt','class','classes','tutorial','tutorials']
            amaz=['price','under','buy','purchase','laptops','laptop','accesories','emi','phone','phones']

            y=(qn.get()).lower()
            x=y.split()
                
                #print(x)
            for i in x:
                if i in brav:
                    temp.set("brave")
                    break
                elif i in yut:
                    temp.set("youtube")
                    break
                elif i in amaz:
                    temp.set("amazon")
                    break
                else:
                    temp.set('google')
        if(temp.get()=='google'):
            webbrowser.open(f'https://www.google.com/search?q={qn.get()}')
            
        if(temp.get()=='brave'):
            webbrowser.open(f'https://search.brave.com/search?q={qn.get()}')

        if(temp.get()=='amazon'):
            webbrowser.open(f'https://www.amazon.in/s?k={qn.get()}&ref=nb_sb_noss')

        if(temp.get()=='youtube'):
            webbrowser.open(f'https://www.youtube.com/results?search_query={qn.get()}')

    else:
        mixer.music.load('mixkit-click-error-1110.wav')
        mixer.music.play()
        messagebox.showerror("Warning!",'Forgot To Fill.........?')

#voice defini

def voice():
    mixer.music.load('mixkit-western-guitar-drum-single-2333.wav')
    mixer.music.play()
    spr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            spr.adjust_for_ambient_noise(m,duration=0.2)
            audio=spr.listen(m)
            mess=spr.recognize_google(audio)
            #mixer.music.load('mixkit-arcade-mechanical-bling-210.wav')
            #mixer.music.play()
            qn.delete(0,END)
            qn.insert(0,mess)
            #time.sleep(5)
            temp.set('')
            search()


            

        except:
            pass


#refresh
def refresh():
    mixer.music.load('P5VA5VG-gun-reloading.mp3')
    mixer.music.play()
    qn.delete(0,END)
    temp.set(None)

#our frame 
app=customtkinter.CTk()
app.geometry("750x350")
app.resizable(0,0)




temp=StringVar()
style=ttk.Style()
style.theme_use('xpnative')


style.configure("Custom.TRadiobutton", font=("Arial", 15), foreground="red", background="dark",borderwidth=2,relief="solid")
#style.map("TRadiobutton", cursor=[("active", "hand2")])
#style.layout("Custom.TRadiobutton",[('Radiobutton.padding',{'sticky': 'nswe','children': [('Radiobutton.focus',{'sticky': 'nswe','children': [('Radiobutton.indicator',{'side': 'left','sticky': ''}),('Radiobutton.label',{'sticky': 'nswe'})],'border': 4})],'border': 2})])


app.title("GBAY")
mixer.music.load('mixkit-shot-light-energy-flowing-2589.wav')
mixer.music.play()
app.iconbitmap('Screenshot (52).ico')

b1Image=PhotoImage(file="Screenshot 2023-07-09 210944(2).png")
b1label=Label(app,image=b1Image,bd=0)
b1label.place(x=0,y=0)

bImage=PhotoImage(file="Screenshot 2023-07-09 210944.png")
blabel=Label(app,image=bImage,bd=0)
blabel.place(x=150,y=0)


'''gImage=PhotoImage(file="google-logo-png-icon-free-download-SUF63j.png")
glabel=Label(app,image=gImage)
glabel.place(x=133,y=248)'''


#textg=customtkinter.CTkLabel(app,text="G",font=('arial',30,'bold'),fg_color="blue",text_color="white",corner_radius=50)


#textg.place(x=50,y=20)



text1=customtkinter.CTkLabel(app,text="Enter your Query",font=('arial',14,'bold'),fg_color="blue",text_color="white",corner_radius=10)
text1.place(x=250,y=120)
qn=customtkinter.CTkEntry(app,border_color="#bd8c08",height=35,width=500)
qn.place(x=50,y=150)      

micImage=PhotoImage(file="png-transparent-mic-microphone-record-icon-iconnice-vector-icon-icon-thumbnail.png")
micButton=Button(app,image=micImage,bg='red',bd=3,cursor='hand2',activebackground='#11d181',command=voice)
micButton.place(x=700,y=187)

seImage=PhotoImage(file="download.png")
seButton=Button(app,image=seImage,bg='red',bd=3,cursor='hand2',activebackground='#11d181',command=search)
seButton.place(x=750,y=187)

g1Image=PhotoImage(file="colourful-google-logo-in-dark-background-free-vector.png")
g1label=Label(app,image=g1Image,bd=0)
g1label.place(x=105,y=250)

goog=ttk.Radiobutton(app,text='',value='google',variable=temp,style="Custom.TRadiobutton")
goog.place(x=105,y=250)

br1Image=PhotoImage(file="HD-wallpaper-brave-browser-black-brave-browser-lion.png")
br1label=Label(app,image=br1Image,bd=0)
br1label.place(x=305,y=250)

braveb=ttk.Radiobutton(app,text='',value='brave',variable=temp,style="Custom.TRadiobutton")
braveb.place(x=305,y=250)
 
a1Image=PhotoImage(file="download1.png")
a1label=Label(app,image=a1Image,bd=0)
a1label.place(x=505,y=250)

amaz=ttk.Radiobutton(app,text='',value='amazon',variable=temp,style="Custom.TRadiobutton")
amaz.place(x=505,y=250)
 
y1Image=PhotoImage(file="images.png")
y1label=Label(app,image=y1Image,bd=0)
y1label.place(x=705,y=250)

yt=ttk.Radiobutton(app,text='',value='youtube',variable=temp,style="Custom.TRadiobutton")
yt.place(x=705,y=250)

refre=Button(app,text='Reset',fg='white',font=('arial',14,'bold'),bg='red',bd=3,cursor='hand2',activebackground='#11d181',command=refresh)
refre.place(x=400,y=350)




def enter_fun(value):
    seButton.invoke()

app.bind('<Return>',enter_fun)


def button_mic(value):
    micButton.invoke()
app.bind("<Control-KeyPress-?>", button_mic)

def button_reset(value):
    refre.invoke()
app.bind("<Control-KeyPress-r>", button_reset)



app.mainloop() 
