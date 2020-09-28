

#included all the required modules for this project 



from tkinter import Tk,Button,Text,Label,Frame,Scrollbar,StringVar,LabelFrame,Entry
import wikipedia,time,threading
import tkinter.messagebox
from tkinter.ttk import Combobox
from playsound import playsound
from gtts import gTTS
import os,threading,time



#initialized the class with parameters

class Wiki:
    def __init__(self,root):
        self.root=root
        self.root.title("wikipedia")
        self.root.geometry("800x500")
        self.root.resizable(0,0)
        #self.root.iconbitmap("sym.ico")


         #decleard the textvariables for given entries required for tkinter Entry
        wiki_search=StringVar()  #inputes to be passed
        lang=StringVar()            #language to be passed

 

        
        #this are the however effects only included for styling the buttons while hover on it.it will give the user  a clear idea on which button he is in.
        
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
             But_speak['background']="black"
             But_speak['foreground']="cyan"  
        def on_leave3(e):
             But_speak['background']="SystemButtonFace"
             But_speak['foreground']="SystemButtonText"






           
        #function to clear input entries as well as the text 
        def clear():
            TXT.delete("1.0","end")
            wiki_search.set("")
            TXT.config(bg="white")



            
         #function to be to search the given input on wikipedia and also provide the all certain information in textbox
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


            

        



        """
        added speak translator if in case user might not understand the inputs on text this function will help user to speak the give output provided on textbox
        for more specify I also included an language selector to select and translate the give input in specific language to clerify to user
        this will never speak directly to the user./ but I have provided a file that will help to this to speak ..
        when you search the given name.It will first save in TEMP folder in c drive as temps.mp3 .when ever you click this speak button this will try to find this
        file and the read all the data in given file and then starts to speaks the data
        """
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

                


        
        
      
    #===================frame==========================================
        Main_Frame=Frame(self.root,width=800,height=500,relief="ridge",bd=3,bg="gray75")   #Mainframe
        Main_Frame.place(x=0,y=0)
        

        Frame_top=Frame(Main_Frame,width=795,height=100,bg="green",relief="ridge",bd=4)  #topframe
        Frame_top.place(x=0,y=0)
        

        Frame_bottom=Frame(Main_Frame,width=795,height=395,bg="blue",relief="ridge",bd=4) #bottomframe
        Frame_bottom.place(x=0,y=100)




        

    #===============================LabelFrame============================
        
        Lab_top=LabelFrame(Frame_top,text="Search in wikipedia",width=785,height=90,bg="#7282cf",fg="#f9eefb") #LabelFrame
        Lab_top.place(x=0,y=0)
        
          
        #this entry will provide user to search 
        Ent_search=Entry(Lab_top,width=50,font=('times new roman',12,'italic'),relief="ridge",bd=4,bg="snow",textvariable=wiki_search)  
        Ent_search.place(x=21,y=7)
        
        
        #select the langueages
        lab=Label(Lab_top,text="SELECT LANGUAGE",font=('times new roman',8,'italic'),bg="#7282cf",fg="white")
        lab.place(x=21,y=40)
        
        #list of languages are English,hindi,marathi
        lan_list=["en","hi","mr"]
        lan_combo=Combobox(Lab_top,values=lan_list,font=('arial',10),width=14,state="readonly",textvariable=lang)
        lan_combo.set("en")
        lan_combo.place(x=139,y=40)
        
        #buton to search
        But_search=Button(Lab_top,text="Search",width=20,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=search_on)
        But_search.place(x=450,y=7)
        But_search.bind("<Enter>",on_enter1)
        But_search.bind("<Leave>",on_leave1)
        
        #but clear the data
        But_clear=Button(Lab_top,text="Clear",width=15,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=clear)
        But_clear.place(x=630,y=7)
        But_clear.bind("<Enter>",on_enter2)
        But_clear.bind("<Leave>",on_leave2)
        
        #button to speak
        But_speak=Button(Lab_top,text="Speak",width=15,font=('times new roman',10,'bold'),relief="ridge",bd=4,cursor="hand2",command=speak)
        But_speak.place(x=630,y=40)
        But_speak.bind("<Enter>",on_enter3)
        But_speak.bind("<Leave>",on_leave3)
        


    #=============================Frame_bottom+++++++++++++++++++++++++++++++++=
        #scrollbar on y axis
        scroll=Scrollbar(Frame_bottom)
        scroll.pack(side="right",fill="y")
        TXT=Text(Frame_bottom, width=109,height=24,font=('arial',10,'bold'),bd=1,bg="gray95",relief="ridge",state="normal",yscrollcommand=scroll.set)
        TXT.pack(side="left")
        scroll.config(command=TXT.yview)
        



if __name__ == "__main__":
    root=Tk()
    app=Wiki(root)    
    root.mainloop()
    
    

