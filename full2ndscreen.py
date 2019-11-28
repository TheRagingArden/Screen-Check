from Tkinter import *
import time
rot = Tk()

wth,hgh = rot.winfo_screenwidth(),rot.winfo_screenheight()
#take desktop width and hight (pixel)
_w,_h = 800,600 #root width and hight
a,b = (wth-_w)/2,(hgh-_h)/2 #Put root to center of display(Margin_left,Margin_top)

def spann():
    def _exit():
        da.destroy()
    da = Toplevel()
    da.geometry('%dx%d+%d+%d' % (wth, hgh,1920, 0))
    da.configure(bg="red")
    Button(da,text="Exit",command=_exit).pack()
    da.overrideredirect(1)
    da.focus_set()#Restricted access main menu

def spann2():
    def _exit():
        da.destroy()
    da = Toplevel()
    da.geometry('%dx%d+%d+%d' % (wth, hgh,0, 0))
    da.configure(bg="green")
    Button(da,text="Exit",command=_exit).pack()
    da.overrideredirect(1)
    da.focus_set()#Restricted access main menu


Button(rot,text="Exit",command=lambda rot=rot : rot.destroy()).pack()

but2 = Button(rot,text="Show on Primary Monitor",command=spann2)
but2.pack()
but = Button(rot,text="Show on Secondary Monitor",command=spann)
but.pack()

a = 1920
b= 0
#print'step1'
#time.sleep(20)

rot.title("Monitor")
rot.geometry('%sx%s+%s+%s'%(_w,_h,a,b))
rot.mainloop()
""" Geometry pattern 'WxH+a+b'
        W = Width
        H = Height
        a = Margin_left+Margin_Top"""