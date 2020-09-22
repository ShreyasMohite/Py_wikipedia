from tkinter import Tk,Button,Text,Label,Frame,Scrollbar,StringVar,LabelFrame,Entry
import wikipedia,time,threading
import tkinter.messagebox
from tkinter.ttk import Combobox
from playsound import playsound
from gtts import gTTS
import os,threading,time

class WIKI:
    def __init__(self,root):
        self.root=root
        self.root.title("wikipedia")
        self.root.geometry("800x500")
        self.root.resizable(0,0)
        #self.root.iconbitmap("sym.ico")

        wiki_search=StringVar()
        lang=StringVar()

        def on_enter1(e):
            But_search['background']="black"
            But_search['foreground']="cyan"
  
        def on_leave1(e):
            But_search['background']="SystemButtonFace"
            But_search['foreground']="SystemButtonText"

        def on_enter2(e):
            But_clear['background']="black"
            But_clear['foreground']="cyan"
  
        def on_leave2(e):
            But_clear['background']="SystemButtonFace"
            But_clear['foreground']="SystemButtonText"



        def on_enter3(e):
             But_Speak['background']="black"
             But_Speak['foreground']="cyan"
  
        def on_leave3(e):
             But_Speak['background']="SystemButtonFace"
             But_Speak['foreground']="SystemButtonText"






           

        def Clear():
            TXT.delete("1.0","end")
            wiki_search.set("")
            TXT.config(bg="white")

        def search_on():
            try:
                TXT.delete("1.0","end")
                search_text=wiki_search.get()
                langs=lang.get()
                wikipedia.set_lang(langs)
                
                get_details=wikipedia.summary(search_text)
                TXT.insert(END,get_details)
            except:
               # tkinter.messagebox.showerror("Network Error","your internet is may not working")
               pass

        




        def speak():
            try:
                time.sleep(1)
                
                texts=TXT.get("1.0","end")
                tts = gTTS(text=texts, lang=lang.get())
                filename = 'C:\\TEMP\\temps.mp3'
                tts.save(filename)
                playsound('C:\\TEMP\\temps.mp3')
                os.remove(filename)
                #remove temperory file
            except:
                tkinter.messagebox.askretrycancel("Internet Error","INTERNET CONNECTION MAY GONE OR LANGUAGE ERROR",icon="info")


        
        
      
    #===================frame
        Main_Frame=Frame(self.root,width=800,height=500,relief="ridge",bd=3,bg="gray75")
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(Main_Frame,width=795,height=100,bg="green",relief="ridge",bd=4)
        Frame_top.place(x=0,y=0)

        Frame_bottom=Frame(Main_Frame,width=795,height=395,bg="blue",relief="ridge",bd=4)
        Frame_bottom.place(x=0,y=100)




        

    #===============================LabelFrame============================
        Lab_top=LabelFrame(Frame_top,text="Search in wikipedia",width=785,height=90,bg="#7282cf",fg="#f9eefb")
        Lab_top.place(x=0,y=0)

        Ent_search=Entry(Lab_top,width=50,font=('times new roman',12,'italic'),relief="ridge",bd=4,bg="snow",textvariable=wiki_search)
        Ent_search.place(x=21,y=7)

        lab=Label(Lab_top,text="SELECT LANGUAGE",font=('times new roman',8,'italic'),bg="#7282cf",fg="white")
        lab.place(x=21,y=40)

        lan_list=["en","hi","mr"]
        lan_combo=Combobox(Lab_top,values=lan_list,font=('arial',10),width=14,state="readonly",textvariable=lang)
        lan_combo.set("en")
        lan_combo.place(x=139,y=40)

        But_search=Button(Lab_top,text="Search",width=20,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=search_on)
        But_search.place(x=450,y=7)
        But_search.bind("<Enter>",on_enter1)
        But_search.bind("<Leave>",on_leave1)

        But_clear=Button(Lab_top,text="Clear",width=15,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=Clear)
        But_clear.place(x=630,y=7)
        But_clear.bind("<Enter>",on_enter2)
        But_clear.bind("<Leave>",on_leave2)

        But_Speak=Button(Lab_top,text="Speak",width=15,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=speak)
        But_Speak.place(x=630,y=40)
        But_Speak.bind("<Enter>",on_enter3)
        But_Speak.bind("<Leave>",on_leave3)


    #=============================Frame_bottom+++++++++++++++++++++++++++++++++=
        scroll=Scrollbar(Frame_bottom)
        scroll.pack(side="right",fill="y")
        TXT=Text(Frame_bottom, width=109,height=24,font=('arial',10,'bold'),bd=1,bg="gray95",relief="ridge",state="normal",yscrollcommand=scroll.set)
        TXT.pack(side="left")
        scroll.config(command=TXT.yview)



if __name__ == "__main__":
    root=Tk()
    app=WIKI(root)
    
    root.mainloop()
    
    
