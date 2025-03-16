from tkinter import*
from PIL import Image, ImageTk
import speech_to_text_p6
import action_pr6

root = Tk()
root.title("AI ASSISTANT")
root.geometry("550x675")  # Geometry of window
root.resizable(False, False)  # Does not allow window to resize
root.config(bg="#6F8FAF")

#ask function
def ask():
    user_val=speech_to_text_p6.speech_to_text()
    bot_val=action_pr6.action(user_val)
    text.insert(END,'user--->'+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")

def send():
    send=entry.get()
    bot=action_pr6.action(send)
    text.insert(END,'user--->'+send+"\n")
    if bot!=None:
        text.insert(END,"BOT<---"+str(bot)+"\n")

def delete():
    text.delete('1.0',"end")

# FRAME
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label
text_label = Label(frame, text="AI ASSISTANT", font=("Comic Sans MS", 14, "bold"), bd=3, fg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = Image.open("IMAGE.png")  # Open the image using PIL
image = image.resize((200, 200))  # Resize the image (optional, adjust as needed)
image_tk = ImageTk.PhotoImage(image)  # Convert to Tkinter format

# Make sure the image reference is kept
image_label = Label(frame, image=image_tk)
image_label.grid(row=1, column=0, pady=20)

# Keep a reference to the image
image_label.image = image_tk

#adding text widget
text=Text(root,font=('couries 10 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=75,y=375,width=375,height=100)

#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=85,y=500,width=350,height=30)

#buttons
button1=Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=40,y=550)
button2=Button(root,text="DELETE",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
button2.place(x=190,y=550)
button3=Button(root,text="SEND",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button3.place(x=365 ,y=550)

root.mainloop()
