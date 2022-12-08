import cv2
from tkinter import *
from PIL import Image, ImageDraw,  ImageTk

def press_btn():
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()
    # Делаем снимок
    ret, frame = cap.read()
    # Записываем в файл
    cv2.imwrite('cam.jpg', frame)
    # Отключаем камеру
    cap.release()

    image = cv2.imread('cam.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    k = 0
    #xml1 = cv2.CascadeClassifier('haarcascade_eye.xml')
    xml2 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #detecting1 = xml1.detectMultiScale(image_gray, minSize = (30, 30))
    detecting2 = xml2.detectMultiScale(image_gray, minSize = (30, 30))

    #for(a, b, width, height) in detecting1:
            #cv2.rectangle(image,(a, b),
                         #(a + height, b + width),
                         #(0, 275, 0), 4)
    for(a, b, width, height) in detecting2:
            cv2.rectangle(image, (a, b),
                         (a + height, b + width),
                         (76, 187, 23), 4)
            k += 1

    t = str(k)
    text.delete('1.0', END)
    text.insert(END, 'Количесво студентов = ' + t)
    cv2.imwrite('image.jpg', image)
    open_image()
def open_image():

    img = Image.open(r'C:\Users\student.SSGA\Desktop\Lyahova\Object detection\image.jpg')
    img = ImageTk.PhotoImage(img)
    label = Label(frame, image = img)
    label.image = img
    label.pack(side = LEFT )

root = Tk()
root['bg'] = '#FAF0E6' #Цвет фона
root.title('Подсчет количества студентов')
root.wm_attributes('-alpha', 1)
root.geometry('600x600')
root.resizable(width = False,height = False) #Запрет на изменение размера

canvas = Canvas(root, height = 600, width = 600)
canvas.pack()

frame = Frame(root, bg='#FAF0E6')
frame.place(relx = 0, rely =0.1, relwidth=1, relheight=0.9)

frame1 = Frame(root, bg='#FAF0E6')
frame1.place(relx = 0, rely = 0, relwidth=0.5, relheight=0.1)
frame2 = Frame(root, bg='#FAF0E6')
frame2.place(relx = 0.5, rely =0, relwidth=0.5, relheight=0.1)

text = Text(frame2,height=19.28,width=40, font='Arial 19',wrap=WORD)
text.pack()
btn_p = Button(frame1, text = 'Посчитать', bg = '#EDD19C', command = press_btn, height = 20,
          width = 20, font = 'Arial 19')

btn_p.pack()
root.mainloop()