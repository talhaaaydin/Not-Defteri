import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.font as tkFont
import time
class notepad():
    fontfamily = 'Consolas'
    fontsize = 11
    allSelected = False
    aboutText = """Bu program Kodlardan Bir Blog yazarı Talha Abd. Aydın tarafından
yazılmıştır.
Yeni Dosya: Ctrl + n
Dosya Aç: Ctrl + o
Dosya Kaydet : Ctrl + s
Kapat: Ctrl + q
    """
    
    def __init__(self, master):
        self.master = master
        master.title('Not Defteri')
        self.fileOpened = False
        self.fileDir = None
        menubar = Menu(master)
        master.config(menu=menubar)
        self.setupFileMenubar(menubar)
        menubar.add_command(label='Hakkında', command=self.about)
        self.setupFontMenubar(menubar)
        self.font = tkFont.Font(family = self.fontfamily, size = self.fontsize)
        self.textBox = Text(pncr, undo=True, font=self.font)
        self.textBox.pack(fill=BOTH)
        self.textBox.focus_set()
        self.bindShortcuts()


    def bindShortcuts(self):
        self.master.bind('<Control-s>', self.dosyakaydet)
        self.master.bind('<Control-o>', self.dosyaaç)
        self.master.bind('<Control-n>', self.yenidosya)
        self.master.bind('<Control-q>', self.kapat)
    
    def changeFamily(self, family):
        self.fontfamily = family
        self.updateFont()

    def changeSize(self, size):
        self.fontsize = size
        self.updateFont()

    def updateFont(self):
        self.font.configure(family=self.fontfamily, size=self.fontsize)
        self.master.update()
        
    def setupFileMenubar(self,menu):
        acilirMenu = Menu(menu)
        acilirMenu.add_command(label='Yeni', command=self.yenidosya)
        acilirMenu.add_command(label='Aç', command=self.dosyaaç)
        acilirMenu.add_command(label='Kaydet', command = self.dosyakaydet)
        acilirMenu.add_separator()
        acilirMenu.add_command(label='Kapat', command = self.kapat)
        menu.add_cascade(label='Dosya', menu=acilirMenu)
        
    def setupFontMenubar(self,menu):
        bicim = Menu(menu)
        yaziTipi = Menu(bicim)
        yaziTipi.add_command(label='Arial', command = lambda:self.changeFamily('Arial'))
        yaziTipi.add_command(label='Consolas', command = lambda:self.changeFamily('Consolas'))
        yaziTipi.add_command(label='Georgia', command = lambda:self.changeFamily('Georgia'))
        bicim.add_cascade(label='Yazı Tipi', menu=yaziTipi)
        
        yaziBoyut = Menu(bicim)
        yaziBoyut.add_command(label='10', command = lambda:self.changeSize(10))
        yaziBoyut.add_command(label='11', command = lambda:self.changeSize(11))
        yaziBoyut.add_command(label='12', command = lambda:self.changeSize(12))
        bicim.add_cascade(label='Yazı Boyutu', menu=yaziBoyut)

        menu.add_cascade(label='Biçim', menu=bicim)
        
    def yenidosya(self, event=None):
        self.textBox.delete('1.0', END)
        self.fileOpened = False

    def dosyaaç(self, event=None):
        try:
            f = filedialog.askopenfilename(title='Dosya Aç', filetypes = (('Yazı Dosyaları', '*.txt'), ('Tüm Dosyalar', '*.*')))
            self.fileOpened = True
            self.fileDir = f
            f1 = open(self.fileDir, mode='r')
            self.textBox.delete('1.0', END)
            self.textBox.insert(END,f1.read())
            print('dosya açıldı')
        except:
            self.fileOpened = False
            self.fileDir = None
            print('dosya seçilmedi')

    def acilmisDosyayiKaydet(self):
        try:
            f1 = open(self.fileDir, mode='w')
            f1.write(self.textBox.get('1.0', END))
            self.fileOpened = True
            print('dosya kaydedildi')
        except:
            print('dosya kaydedilmedi')


    def acilmamisDosyayıKaydet(self):
        try:
            f = filedialog.asksaveasfilename(title='Dosya Kaydet', defaultextension = '.txt',filetypes = (('Yazı Dosyaları', '*.txt'), ('Tüm Dosyalar', '*.*')))
            self.fileOpened = True
            self.fileDir = f
            f1 = open(self.fileDir, mode='w')
            f1.write(self.textBox.get('1.0', END))
            print('dosya kaydedildi')
        except:
            self.fileOpened = False
            self.fileDir = None
            print('dosya kaydedilmedi')


    def dosyakaydet(self, event = None):
        if(self.fileOpened):
            self.acilmisDosyayiKaydet()
        else:
            self.acilmamisDosyayıKaydet()

    def about(self):
        messagebox.showinfo('Hakkında', self.aboutText)        

    def kapat(self,event = None):
        pncr = self.master
        print('program kapatılıyor', end=''),
        time.sleep(0.2)
        print('.', end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.4)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.6)
        print('\nHOŞCAKAL')
        time.sleep(0.1)
        pncr.destroy()

    def showBool(self):
        print('FileOpened: ' + str(self.fileOpened))
    

pncr = Tk()
app = notepad(pncr)
pncr.mainloop()
