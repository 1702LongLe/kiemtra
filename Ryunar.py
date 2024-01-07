from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.font as tkFont

root = Tk()
root.title('Du lịch Du thuyền Hạ Long ')
root.geometry('1440x1080')

note1 = 'Du thuyền thăm vịnh'
note2 = 'Du thuyền bao nguyên ngày'
note3 = 'Du thuyền 3 sao'
note4 = 'Du thuyền 4 sao'
note5 = 'Du thuyền 5 sao'
note6 = 'Du thuyền 5 sao trọn gói'
note7 = 'Du thuyền 3 ngày 2 đêm'


# font = tkFont.Font (family)
def search():
    search = text_root1.get(1.0,'end-1c')

    if  search == note1 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền thăm Vịnh với giá là: 150.000 VNĐ/1 người')
    elif  search == note2 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền bao nguyên ngày với giá là:  3.000.000 VNĐ/1 người')
    elif  search == note3 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền 3 sao với giá là:  1.500.000 VNĐ/1 người')
    elif  search == note4 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền 4 sao với giá là:  2.000.000 VNĐ/1 người')
    elif  search == note5 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền 5 sao với giá là:  3.000.000 VNĐ/1 người')
    elif  search == note6 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền 5 sao trọn gói với giá là: 7.000.000 VNĐ/1 người')
    elif  search == note7 :
        print('Lần nhập thành công')
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã chọn vé: \nDu thuyền 3 ngày 2 đêm hãy liên hệ : 2132.546.546')      
    else: 
        print('Xin lỗi lần nhập thất bại')
        messagebox.showinfo('Thông báo','Xin lỗi quý khách nhập không thành công!')

def phone():
    messagebox.showinfo('Thông báo','Hãy liên hệ: 2132.546.546')

logo = PhotoImage(file = "C:/Users/OSC/Documents/code/Logo Ryunar/hi.png")
root.iconphoto(True,logo)

img = Image.open("C:/Users/OSC/Documents/code/Logo Ryunar/ryunar.png")
img = img.resize((250,100))
image = ImageTk.PhotoImage(img)
l = Label(root,image=image).place(x=10,y=0)

img1 = Image.open("C:/Users/OSC/Documents/code/Logo Ryunar/duthuyen.png")
img1 = img1.resize((562,300))
image1 = ImageTk.PhotoImage(img1)
l1 = Label(root,image=image1).place(x=450,y=100)

main=Label(root,text ='Bạn lựa chọn du thuyền Hạ Long nào?', fg='black', font= tkFont.Font(family="Roboto",size=25,weight="bold"))
main.place(x=420,y=460)

main0=Label(root,text ='Hơn 100 tour du thuyền hạng sang giá tốt đang chờ bạn', fg = 'gray', font= tkFont.Font(family="Roboto",size=12,weight="bold"))
main0.place(x=480,y=500)

main1=Label(root,text = note1,fg='gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main1.place(x=600,y=580)

main2=Label(root,text =note2,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main2.place(x=600,y=600)

main3=Label(root,text =note3,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main3.place(x=600,y=620)

main4=Label(root,text =note4,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main4.place(x=600,y=640)

main5=Label(root,text =note5,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main5.place(x=600,y=660)

main6=Label(root,text =note6,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main6.place(x=600,y=680)

main7=Label(root,text =note7,fg = 'gray',font = tkFont.Font(family="Roboto",size=12,weight="bold"))
main7.place(x=600,y=700)

text_root1=Text(root,width=60,height=2)
text_root1.place(x=350,y=540)

my_button= Button (root,text='Tìm kiếm',bg= 'blue',width= 15,height=1,font= tkFont.Font(family="Roboto",size=15,weight="bold"),command=search)
my_button.place(x=850,y=540)

my_button1= Button (root,text='Liên hệ Ryunar',bg= 'blue',width=15,height=1,font= tkFont.Font(family="Roboto",size=15,weight="bold"),command=phone)
my_button1.place(x=1200,y=10)


root.mainloop()