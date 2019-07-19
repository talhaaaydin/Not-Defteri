from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

pncr = tk.Tk()
pncr.title('Adsız Dosya - Not Defteri')

fileOpened = False
fileDir = None

def çıkış():
    global pncr
    pncr.quit()

def get_textarea_value():
    global textarea
    return textarea.get("1.0", END)

def kaydetAçılmışDosya():
    global fileDir, fileOpened
    f = open(fileDir, 'w')
    f.write(get_textarea_value())
    fileOpened = True
    başlığıGüncelle(f)
    f.close()


def kaydetYeniDosya():
    global pncr, fileOpened, fileDir
    data = get_textarea_value()
    f = filedialog.asksaveasfile (mode='w',defaultextension=".txt",filetypes=(("Yazı dosyası", "*.txt"),("Tüm Dosyalar", "*.*")),title='Kaydet',initialdir=pncr.winfo_pathname)
    if f != None:
        fileOpened = True
        başlığıGüncelle(f)
        f.write(data)
        f.close()

def kaydet():
    global fileOpened
    if fileOpened:
        print('Açılmış Dosya Güncelleniyor...')
        kaydetAçılmışDosya()
        print('Dosya Güncellendi.')
    else:
        kaydetYeniDosya()
        print('Yeni Dosya Oluşturuldu ve Kaydedildi.')
    
def başlığıGüncelle(f):
        global fileOpened, fileDir, pncr
        if fileOpened:
                fileDir = f.name
                title = f.name.rsplit('/')[-1]
                title = title.split('.')[0]            
                pncr.title(title + ' - Not Defteri')
                pncr.update()

def aç():
    global textarea, pncr
    global fileOpened, fileDir
    f = filedialog.askopenfile(mode='r', defaultextension=".txt",filetypes=(('Yazı Dosyası', '*.txt'), ('Tüm Dosyalar', '*.*')), title='Aç', initialdir=pncr.winfo_pathname)
    if f == None:
        fileOpened = False
        fileDir = None
        print('Dosya Açılmadı!')
        return
    text = f.read()
    fileOpened = True
    başlığıGüncelle(f)
    print('Dosya Açılıyor.')
    f.close()
    if text != None:
        textarea.delete(1.0, END)
        textarea.insert(END, text)
        print('Dosya Açıldı.')

def yeni():
    global textarea, pncr
    global fileOpened, fileDir
    fileOpened = False
    fileDir = None
    pncr.title('Adsız Dosya - Not Defteri')
    pncr.update()
    textarea.delete(1.0, END)
    print('Yeni Yazı Dosyası Açıldı')

def hakkında():
    messagebox.showinfo('Hakkında', 'Bu program yazı yazmak, okumak, yazıyı düzenlemek için Kodlardan Bir Blog yazarı Talha Aydın tarafından yazılmıştır')

menubar = Menu(pncr)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label='Yeni', command=yeni)
filemenu.add_command(label='Aç', command=aç)
filemenu.add_command(label='Kaydet', command=kaydet)
filemenu.add_separator()
filemenu.add_command(label='Çıkış', command=çıkış)
menubar.add_cascade(label='Dosya', menu=filemenu)
menubar.add_command(label='Hakkında', command=hakkında)

textarea = Text(pncr, width=100,height=20)
textarea.pack() 

pncr.configure(background='white')
pncr.config(menu=menubar)
pncr.mainloop()