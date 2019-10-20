from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
w=Tk()
w.title('Speed converter')
w.config(bg='#00ff00')

def convert(getparam):
    global str1
    str1=str1+str(getparam)
    f1.set(str1)


    #print(type(str1))


def afconvert():

    try:
        global str1
        ans = str(eval(str1))
        res1=combo1.get()
        res2=combo2.get()
        c2=f2.get()


        #f2.set(str1)
        if(res1==res1=='Select unit :'):
            messagebox.showinfo('Info','Select the Speed type')
        elif(res1==res2):
            f2.set(ans)

        elif(res1=='LIGHTSPEED c'and res2=='MACH Ma'):
            ans = float(str1)
            f2.set(ans*880965.201)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'MACH Ma'):
            ans = float(str1)
            f2.set(ans * 1.13511862e-6)
        elif(res1=='LIGHTSPEED c' and res2=='METER PER SECOND m/s'):
            ans = float(str1)
            f2.set(ans * 299792458)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'METER PER SECOND m/s'):
            ans = float(str1)
            f2.set(ans * 3.33564098e-9)
        elif (res1 == 'MACH Ma' and res2 == 'METER PER SECOND m/s'):
            ans = float(str1)
            f2.set(ans * 340.3)
        elif (res2== 'MACH Ma' and res1== 'METER PER SECOND m/s'):
            ans = float(str1)
            f2.set(ans * 0.0029385836)
        elif(res1=='LIGHTSPEED c' and res2=='KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 1.07925285e9)
        elif (res2== 'LIGHTSPEED c' and res1 == 'KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 9.26566931e-10)
        elif (res1 == 'MACH Ma' and res2 == 'KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 1225.08)
        elif (res2== 'MACH Ma' and res1 == 'KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 0.000816273223)
        elif (res1 == 'METER PER SECOND m/s' and res2 == 'KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 3.6)
        elif (res2== 'METER PER SECOND m/s' and res1 == 'KILOMETER PER HOUR km/h'):
            ans = float(str1)
            f2.set(ans * 0.277777778)

        elif(res1=='KILOMETER PER SECOND km/s' and res2=='LIGHTSPEED c'):
            ans=float(str1)
            f2.set(ans*3.33564095e-6)
        elif (res2 == 'KILOMETER PER SECOND km/s' and res1 == 'LIGHTSPEED c'):
            ans = float(str1)
            f2.set(ans * 299792.458)
        elif (res2 == 'KILOMETER PER SECOND km/s' and res1 == 'MACH Ma'):
            ans = float(str1)
            f2.set(ans * 0.3403)
        elif (res1 == 'KILOMETER PER SECOND km/s' and res2 == 'MACH Ma'):
            ans = float(str1)
            f2.set(ans * 2.9385836)
        elif(res1=='METER PER SECOND m/s' and res2=='KILOMETER PER SECOND km/s'):
            ans = float(str1)
            f2.set(ans*0.0010)
        elif (res2== 'METER PER SECOND m/s' and res1 == 'KILOMETER PER SECOND km/s'):
            ans = float(str1)
            f2.set(ans * 1000)
        elif (res1 == 'KILOMETER PER HOUR km/h' and res2 == 'KILOMETER PER SECOND km/s'):
            ans = float(str1)
            f2.set(ans * 0.000277777778)
        elif (res2 == 'KILOMETER PER HOUR km/h' and res1 == 'KILOMETER PER SECOND km/s'):
            ans = float(str1)
            f2.set(ans * 3600)
        elif(res1=='LIGHTSPEED c' and res2=='KNOT kn'):

            ans=float(str1)
            f2.set(ans*582749918)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 1.71600196e-9)

        elif (res1 == 'MACH Ma' and res2 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 661.490281)
        elif (res2== 'MACH Ma' and res1 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 0.00151173801)
        elif (res1 == 'METER PER SECOND m/s' and res2 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 1.9438449)
        elif (res2== 'METER PER SECOND m/s' and res1== 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 0.514444444)
        elif (res1 == 'KILOMETER PER HOUR km/h' and res2 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 0.539956803)
        elif (res2 == 'KILOMETER PER HOUR km/h' and res1== 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 1.852)
        elif (res1 == 'KILOMETER PER SECOND km/s' and res2 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 1943.84449)
        elif (res2== 'KILOMETER PER SECOND km/s' and res1 == 'KNOT kn'):
            ans = float(str1)
            f2.set(ans * 0.000514444444)
        elif(res1=='LIGHTSPEED c' and res2=='MILE PER HOUR mph'):
            ans=float(str1)
            f2.set(ans*670616629)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'MILE PER HOUR mph'):
            ans = float(str1)
            f2.set(ans * 1.49116493e-9)
        elif(res1=='MACH Ma'and res2=='MILE PER HOUR mph'):
            ans=float(ans)
            f2.set(ans*761.22942)
        elif (res2== 'MACH Ma' and res1 == 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans * 0.00131366441)
        elif(res1=='METER PER SECOND m/s' and res2=='MILE PER HOUR mph'):
            ans=float(ans)
            f2.set(ans*2.23693629)
        elif (res2== 'METER PER SECOND m/s' and res1 == 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans * 0.44704)
        elif (res1 == 'KILOMETER PER HOUR km/h' and res2 == 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans *0.621971192 )
        elif (res2== 'KILOMETER PER HOUR km/h' and res1== 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans *1.609344 )
        elif (res1 == 'KILOMETER PER SECOND km/s' and res2 == 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans *2236.93629 )
        elif (res2 == 'KILOMETER PER SECOND km/s' and res1== 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans *0.00044704 )
        elif(res1=='KNOT kn' and res2=='MILE PER HOUR mph'):
            ans=float(ans)
            f2.set(ans*1.15077945)
        elif (res2 == 'KNOT kn' and res1 == 'MILE PER HOUR mph'):
            ans = float(ans)
            f2.set(ans * 0.868976242)
        elif(res1=='LIGHTSPEED c' and res2=='FOOT PER SECOND fps'):
            ans=float(ans)
            f2.set(ans*983571056)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans * 1.01670336e-9)
        elif (res1 == 'MACH Ma' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans * 1116.46982)
        elif (res2== 'MACH Ma' and res1 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans * 0.000895680282)
        elif (res1 == 'METER PER SECOND m/s' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans * 3.2808399)
        elif (res2 == 'METER PER SECOND m/s' and res1== 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *0.3408)
        elif (res1 == 'KILOMETER PER HOUR km/h' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans * 0.911344415)
        elif (res2 == 'KILOMETER PER HOUR km/h' and res1 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *1.09728)
        elif (res1 == 'KILOMETER PER SECOND km/s' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *3280.8399 )
        elif (res2== 'KILOMETER PER SECOND km/s' and res1== 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *0.0003048 )
        elif (res1 == 'KNOT kn' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *1.6878096 )
        elif (res2== 'KNOT kn' and res1 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *0.592483801 )
        elif (res1 == 'MILE PER HOUR mph' and res2 == 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *1.46666667 )
        elif (res2 == 'MILE PER HOUR mph' and res1== 'FOOT PER SECOND fps'):
            ans = float(ans)
            f2.set(ans *0.6818182)
        #INCH PER SECOND ips
        elif (res1 == 'LIGHTSPEED c' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *11.18028527e10)
        elif (res2 == 'LIGHTSPEED c' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *8.47252802e-11)
        elif (res1 == 'MACH Ma' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *13397.6378)
        elif (res2 == 'MACH Ma' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *7.46400235e-5)
        elif (res1 == 'METER PER SECOND m/s' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *39.3700787)
        elif (res2 == 'METER PER SECOND m/s' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *0.0254)
        elif (res1 == 'KILOMETER PER HOUR km/h' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *10.936133)
        elif (res2 == 'KILOMETER PER HOUR km/h' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *0.09144)
        elif (res1 == 'KILOMETER PER SECOND km/s' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *39370.0787)
        elif (res2 == 'KILOMETER PER SECOND km/s' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *2.54e-5)
        elif (res1 == 'KNOT kn' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *20.2537183)
        elif (res2 == 'KNOT kn' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *0.0493736501)
        elif (res1 == 'MILE PER HOUR mph' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *17.6)
        elif (res2 == 'MILE PER HOUR mph' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *0.0568181818)
        elif (res1 == 'FOOT PER SECOND fps' and res2 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *12)
        elif (res2 == 'FOOT PER SECOND fps' and res1 == 'INCH PER SECOND ips'):
            ans = float(ans)
            f2.set(ans *0.0833333333)


        else:
            messagebox.showerror('Error', 'Wrong conversion')
    except:
       messagebox.showerror('Error','Wrong conversion')

def delete():
    global str1
    str1=e1.get()[:-1]
    v=e1.delete(0,END)
    e1.insert(0,str1)
    '''self.txt=self.e.get()[:-1] 
            self.e.delete(0,END) 
            self.e.insert(0,self.txt) '''




    #e1.insert(str1)
    if(str1==1):
        e1.insert(0,'0.0')
def clear():
    global str1
    str1=''
    f1.set(str1)
str1=''
temp1=['LIGHTSPEED c','MACH Ma','METER PER SECOND m/s','KILOMETER PER HOUR km/h','KILOMETER PER SECOND km/s','KNOT kn','MILE PER HOUR mph','FOOT PER SECOND fps','INCH PER SECOND ips','INCH PER SECOND ips']
temp2=['LIGHTSPEED c','MACH Ma','METER PER SECOND m/s','KILOMETER PER HOUR km/h','KILOMETER PER SECOND km/s','KNOT kn','MILE PER HOUR mph','FOOT PER SECOND fps','INCH PER SECOND ips','INCH PER SECOND ips']
uframe=LabelFrame(w)
combo1=Combobox(uframe,values=temp1,width=25)
combo1.set('Select unit :')
combo1.grid(row=0,column=0)
uframe.config(bg='#00ff00')
f1=DoubleVar()
e1=Entry(uframe,textvariable=f1)

e1.grid(row=0,column=1)
l1=Label(uframe,text='Convert to',bg='#00ff00').grid(row=1,column=0)
combo2=Combobox(uframe,values=temp2,width=25)
combo2.set('Select unit :')
combo2.grid(row=2,column=0)
l1=Button(uframe,text='Convert',activeforeground='#ff4b00',activebackground='white',fg='white',bg='#ff4b00',command=afconvert).grid(row=3,column=1,ipadx=30)
f2=DoubleVar()
e2=Entry(uframe,textvariable=f2).grid(row=2,column=1)

lframe=LabelFrame(w)
lframe.config(bg='#00ff00')
b1=Button(lframe,text='1',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('1')).grid(row=0,column=0,ipadx=30,ipady=3)
b2=Button(lframe,text='2',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('2')).grid(row=0,column=1,ipadx=30,ipady=3)
b3=Button(lframe,text='3',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('3')).grid(row=0,column=2,ipadx=32,ipady=3)

b4=Button(lframe,text='4',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('4')).grid(row=1,column=0,ipadx=30,ipady=3)
b5=Button(lframe,text='5',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('5')).grid(row=1,column=1,ipadx=30,ipady=3)
b6=Button(lframe,text='6',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('6')).grid(row=1,column=2,ipadx=32,ipady=3)

b7=Button(lframe,text='7',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('7')).grid(row=2,column=0,ipadx=30,ipady=3)
b8=Button(lframe,text='8',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('8')).grid(row=2,column=1,ipadx=30,ipady=3)
b9=Button(lframe,text='9',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('9')).grid(row=2,column=2,ipadx=32,ipady=3)

dot=Button(lframe,text='.',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('.')).grid(row=3,column=0,ipadx=32,ipady=3)
zero=Button(lframe,text='0',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=lambda:convert('0')).grid(row=3,column=1,ipadx=30,ipady=3)
_delete_=Button(lframe,text='del',activeforeground='blue',activebackground='white',fg='white',bg='blue',command=delete).grid(row=3,column=2,ipadx=26,ipady=3)

clear=Button(lframe,text='Clear',activeforeground='white',activebackground='red',fg='white',bg='blue',command=clear).grid(row=4,columnspan=7,ipadx=115)
lframe.config(bg='#00ff00')
uframe.grid(row=0,column=0)
lframe.grid(row=1,column=0)
w.resizable(0,0)
w.geometry('387x285+150+150')
w.mainloop()
