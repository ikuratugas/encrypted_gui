# import library you need
import tkinter
import customtkinter
from tkinter import messagebox
from PIL import Image  # bukan pip PIL tapi nanti downloa dengan pip pillow | customtkinter tidak punya imagewwidget

# key -> to know how it's work, watch channe <bro code> - simple enrypted decrepty in python
chars = " " + "abcdefghijklmnopqrstuvw.xyz1234567890~,!@#$%^&*()_+{}:?/>`<[]\n'\t" \
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
terje = "`" + "%z_y2QSTPDV?HIJEu)8t$s&B.WGCr!qo@n5m<l7kji^h,{g63fe0baXYN>:} \n'\t" \
              "LU/p9*Ad1c#MFx~w+4vOKRZ([]"
terje = list(terje)
kunci = terje.copy()

# event - event - event - event - event - event - event - event - event - event - event
def klik_enc(): # tombol enc
    textfile = "\n\n\n\n\n\n                                         I   N   P   U   T\n\n\n"
    if memo1.get("1.0", 'end') in textfile:
        tkinter.messagebox.showerror("Error", "silahkan input dulu, baru tekan tombol ini")
    else:
        memo2.configure(state='normal') #active kembali, karena awal program memo2 uneditable (biar bisa diedit)
        memo2.delete("1.0", 'end')

        #encrypted process
        sandi_pesan = ""
        isi_pesan = memo1.get("1.0", 'end')
        for letter in isi_pesan:
            index = chars.index(letter)
            sandi_pesan += kunci[index]

        memo2.insert("1.0", sandi_pesan)
        memo2.configure(state='disable')

def klik_dec(): # tombol dec
    textfile = "\n\n\n\n\n\n                                         I   N   P   U   T\n\n\n"
    if memo1.get("1.0", 'end') in textfile:
        tkinter.messagebox.showerror("Error", "silahkan input dulu, baru tekan tombol ini")
    else:
        memo2.configure(state='normal')
        memo2.delete("1.0", 'end')

        # decrypted process
        terjemahkan = ""
        tersandi = memo1.get("1.0", 'end')
        for letter in tersandi:
            index = kunci.index(letter)
            terjemahkan += chars[index]

        memo2.insert("1.0", terjemahkan)
        memo2.configure(state='disable')

def klik_clr(cp): # tombol copy (untuk menyalin text di output)
    textfile1 = "\n\n\n\n\n\n                                        O   U   T   P   U   T\n\n\n" # anying, sa bisa dapat dong solusinya, memang kampret otakku
    if  cp in textfile1:
        tkinter.messagebox.showerror("Error", "output masih kosong, silahkan input dulu")
    else:
        window.clipboard_clear()
        window.clipboard_append(cp)

def klik_inf(): # tombol info -> akan membuka window baru yang memunculkan info shortcut dan authornya
    #window2
    window2 = customtkinter.CTkToplevel()
    window2.geometry("220x250")
    window2.title("info app")
    window2.configure(fg_color='white')

    gambar2 = customtkinter.CTkImage(Image.open('profile.png'), size=(130, 90))
    #widget window2
    label_h1 = customtkinter.CTkLabel(master=window2, font=("Serif",14,'bold'), text="Shortcut",text_color='black')
    label1 = customtkinter.CTkLabel(master=window2, font=("Sans-serif", 12), text="   Ctrl + a       : Clear input  ", text_color='black')
    label2 = customtkinter.CTkLabel(master=window2, font=("Sans-serif", 12), text="   Ctrl + e       : Encrypted    ",text_color='black')
    label3 = customtkinter.CTkLabel(master=window2, font=("Sans-serif", 12), text="   Ctrl + d       : Decrypted    ",text_color='black')
    label4 = customtkinter.CTkLabel(master=window2, font=("Sans-serif", 12), text="   Ctrl + c       : Copy output  ",text_color='black')
    label_h2 = customtkinter.CTkLabel(master=window2, font=("Serif", 14, 'bold'), text="Made by",text_color='black')
    image2 = customtkinter.CTkLabel(master=window2, image=gambar2, text="")
    label5 = customtkinter.CTkLabel(master=window2, font=("Sans-serif", 12), text="  ikura apirianto  ",text_color='black', fg_color='yellow')

    #layout window2
    label_h1.place(relx=0.5, rely=0.05, anchor='center')
    label1.place(relx=0.1, rely=0.1)
    label2.place(relx=0.1, rely=0.18)
    label3.place(relx=0.1, rely=0.27)
    label4.place(relx=0.1, rely=0.36)
    label_h2.place(relx=0.5, rely=0.51, anchor='center')
    image2.place(relx=0.5,rely=0.75, anchor='center')
    label5.place(relx=0.5, rely=0.95, anchor='center')

def click_memo1(*args): # ketika klik / masuk di widget memo1
    memo1.delete("1.0",'end')
    memo1.configure(text_color='darkgreen')
    memo1.focus()

    memo2.configure(text_color='white', state='normal')
    memo2.delete("1.0", 'end')
    memo2.insert("5.5", "\n\n\n\n\n\n                                        O   U   T   P   U   T")
    memo2.configure(state='disable')
# /event - /event- /event- /event- /event- /event- /event- /event- /event- /event- /event- /event

# window
window = customtkinter.CTk()
window.title("Secret Message - i.4")
window.geometry("700x300")
window.resizable(False,False)
window.configure(fg_color="#000000")

# 0000000000 shortcut using keyboard 00000000000
# encrypt
def ctrl_e():
    klik_enc()
window.bind("<Control_L>e", lambda _ : ctrl_e())
window.bind("<Control_R>e", lambda _ : ctrl_e())

# decrypt
def ctrl_d():
    klik_dec()
window.bind("<Control_L>d", lambda _ : ctrl_d())
window.bind("<Control_R>d", lambda _ : ctrl_d())

# copy output
def ctrl_c():
    klik_clr(memo2.get("1.0",'end'))
window.bind("<Control_L>c", lambda _ : ctrl_c())
window.bind("<Control_R>c", lambda _ : ctrl_c())

# clear input
def ctrl_z():
    click_memo1()
window.bind("<Control_L>a", lambda _ : ctrl_z())
window.bind("<Control_R>a", lambda _ : ctrl_z())
# 0000000000000000000000000000000000000000000000

# widget - widget - widget - widget - widget - widget - widget - widget - widget - widget - widget - widget - widget
gambar1 = customtkinter.CTkImage(Image.open('iconpolos.png'), size=(50,50))
# membuat background pada window dengan label (memang agak ribet, soalnya gambar yang di downlaod jelek semua)
label_bg = customtkinter.CTkLabel(master=window,
                                  font=("arial", 13),
                                  text_color='#011003',
                                  text="01adfadfae0100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "0adfadfdfda100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "01adfadfae0100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "0adfadfdfda100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "01adfadfae0100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "0adfadfdfda100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "01adfadfae0100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "0adfadfdfda100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "01adfadfae0100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOfj87133040$*()0101010HV0adfae0100JFEHV\n"
                                       "0adfadfdfda100JFEHV01010()*&^$*()0101010Ikura*Apiriato897rjsnba9320jafnnoif4fauanab&^&*#JFIODO&^%$Rv048147#*&$\n"
                                       "9320jafnnoif4adfae0100JFEHV0adfae0100JFE$*()010101andlfj8713304and*#JFIOf4ANTO133040$*()0101010Hadfae0100JFEHV\n"
                                  )
image1 = customtkinter.CTkLabel(master=window, image=gambar1, text="")
memo1 = customtkinter.CTkTextbox(master=window, activate_scrollbars=True, text_color='green', fg_color="black", scrollbar_button_hover_color="darkgreen", font=("mono", 13))
button_enc = customtkinter.CTkButton(master=window, text="E N C", width=40, command=klik_enc, cursor='spider', fg_color='white',text_color='black', hover_color="#dddddd")
button_dec = customtkinter.CTkButton(master=window, text="D E C", width=40, cursor='spider', command=klik_dec, fg_color='white',text_color='black', hover_color="#dddddd")
button_clr = customtkinter.CTkButton(master=window, text="C O P Y", width=40, cursor='spraycan', fg_color='yellow',hover_color='#cccc00',text_color='black', command=lambda: klik_clr(memo2.get("1.0",'end')))
button_inf = customtkinter.CTkButton(master=window, text="i n f o", width=40, cursor='plus',fg_color='darkgreen',command=klik_inf, hover_color="#005500")
memo2 = customtkinter.CTkTextbox(master=window, activate_scrollbars=True, fg_color='darkblue',font=("mono", 13))

# layout window
label_bg.place(x=0, y=0)
memo1.place(relx=0.025,rely=0.05, relwidth=0.4, relheight=0.90)
button_enc.place(relx=0.45,rely=0.05, relwidth=0.1, relheight=0.2)
button_dec.place(relx=0.45,rely=0.27, relwidth=0.1, relheight=0.2)
image1.place(relx=0.5, rely=0.55, anchor='center')
button_clr.place(relx=0.45,rely=0.65, relwidth=0.1, relheight=0.2)
button_inf.place(relx=0.45,rely=0.87, relwidth=0.1, relheight=0.08)
memo2.place(relx=0.575, rely=0.05, relwidth=0.4, relheight=0.90)

# configure widget when start program
memo1.insert("1.0", "\n\n\n\n\n\n                                         I   N   P   U   T") # teks awal pada memo1
memo2.insert("1.0", "\n\n\n\n\n\n                                        O   U   T   P   U   T") # teks awal pada memo2
memo1.bind("<Button-1>", click_memo1) # ketika mengclick memo1 akan ke function click_memo1
memo2.configure(state='disable', text_color='gray') # disable biar pada memo2 uneditable
#  /widget /widget  /widget  /widget  /widget  /widget  /widget  /widget  /widget  /widget  /widget  /widget  /widget

# run
window.mainloop()