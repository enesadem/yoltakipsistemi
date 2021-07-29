import cv2
import numpy as np
from tkinter import *
import pafy
from PIL import ImageTk,Image

#r = sr.Recognizer()
#with sr.Microphone() as source:
#    audio = r.listen(source)
#    voice = r.recognize_google(audio , language='tr-TR')
#    print(voice)

gostergekalinligi = 1
window = Tk()
window.title("Yol Takip Sistemi")
window.geometry('240x500')
ytk_logo = ImageTk.PhotoImage(Image.open("logo.png"))
ytk_label = Label(image=ytk_logo)
ytk_label.grid(column=0, row=5)
lbl2 = Label(window, text="\n\nyoltakipsistemi.tk")
lbl2.grid(column=0, row=90)
lbl = Label(window, text="Programı başlatmak için\nlinkinizi aşağıdaki\nalana yapıştırınız.")
lbl.grid(column=0, row=10)
lbl.grid(column=0, row=10)
#arayazi = Label(window, text="\n------\n")
#arayazi.grid(column=0, row=2)
var = IntVar()
rad1 = Radiobutton(window, text='Demo Sensör', value=1, variable=var)
rad2 = Radiobutton(window, text='Düz Sensör', value=2, variable=var)
rad3 = Radiobutton(window, text='Kare Sensör', value=3, variable=var)
rad1.grid(column=0, row=30)
rad2.grid(column=0, row=40)
rad3.grid(column=0, row=50)
txt = Entry(window,width=40)
txt.grid(column=0, row=20
         )
arayazi2 = Label(window, text="------")
arayazi2.grid(column=0, row=65)
yazi1 = Label(window, text="Gösterge kalınlığını değiştirmek \n için aşağıdaki \n butonları kullanınız.")
yazi1.grid(column=0, row=70)

def clicked():
    url = txt.get()
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    best.resolution, best.extension
    ('1280x720', 'mp4')
    Oynatici = cv2.VideoCapture(best.url)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = np.ones((4, 4), np.uint8)
    kernel2 = np.ones((6, 6), np.uint8)

    class Koordinat:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.y = y

    class Sensor:
        def __init__(self, Koordinat1, Koordinat2, KGenislik, KUzunluk):
            self.Koordinat1 = Koordinat1
            self.Koordinat2 = Koordinat2
            self.KUzunluk = KUzunluk
            self.KGenislik = KGenislik
            self.MaskeAlani = abs(self.Koordinat2.x - Koordinat1.x) * abs(self.Koordinat2.y - self.Koordinat1.y)
            self.Maske = np.zeros((KUzunluk, KGenislik, 1), np.uint8)
            cv2.rectangle(self.Maske, (self.Koordinat1.x, self.Koordinat1.y), (self.Koordinat2.x, self.Koordinat2.y),
                          (255), cv2.FILLED)
            self.Durum = False
            self.AlgilananArac = 0

    if (var.get()==1):
        Sensor1OranDegiskeni = 0.70
        s1k11 = 570
        s1k12 = 570
        s1k21 = 710
        s1k22 = 640
        s2k11 = 0
        s2k12 = 490
        s2k21 = 155
        s2k22 = 560
        s3k11 = 810
        s3k12 = 570
        s3k21 = 1100
        s3k22 = 640
        s4k11 = 250
        s4k12 = 570
        s4k21 = 450
        s4k22 = 640
    elif (var.get()==2):
        Sensor1OranDegiskeni = 0.05
        s1k11 = 0
        s1k12 = 570
        s1k21 = 1280
        s1k22 = 590
        s2k11 = 0
        s2k12 = 0
        s2k21 = 0
        s2k22 = 0
        s3k11 = 0
        s3k12 = 0
        s3k21 = 0
        s3k22 = 0
        s4k11 = 0
        s4k12 = 0
        s4k21 = 0
        s4k22 = 0
    elif (var.get()==3):
        Sensor1OranDegiskeni = 0.10
        s1k11 = 0
        s1k12 = 690
        s1k21 = 1280
        s1k22 = 691
        s2k11 = 0
        s2k12 = 30
        s2k21 = 1280
        s2k22 = 31
        s3k11 = 30
        s3k12 = 0
        s3k21 = 31
        s3k22 = 720
        s4k11 = 1250
        s4k12 = 0
        s4k21 = 1251
        s4k22 = 720
    else:
        Sensor1OranDegiskeni = 1.00
        s1k11 = 0
        s1k12 = 0
        s1k21 = 0
        s1k22 = 0
        s2k11 = 0
        s2k12 = 0
        s2k21 = 0
        s2k22 = 0
        s3k11 = 0
        s3k12 = 0
        s3k21 = 0
        s3k22 = 0
        s4k11 = 0
        s4k12 = 0
        s4k21 = 0
        s4k22 = 0

    Sensor1 = Sensor(Koordinat(s1k11, s1k12), Koordinat(s1k21, s1k22), 1280, 720)
    Sensor2 = Sensor(Koordinat(s2k11, s2k12), Koordinat(s2k21, s2k22), 1280, 720)
    Sensor3 = Sensor(Koordinat(s3k11, s3k12), Koordinat(s3k21, s3k22), 1280, 720)
    Sensor4 = Sensor(Koordinat(s4k11, s4k12), Koordinat(s4k21, s4k22), 1280, 720)

    # cv2.imshow("Maske",Sensor1.Maske)
    font = cv2.FONT_HERSHEY_DUPLEX

    while (1):
        ret, Kare = Oynatici.read()
        BolunmusO = Kare[0:720, 0:1280]

        WBOynatici = fgbg.apply(BolunmusO)
        WBOynatici = cv2.morphologyEx(WBOynatici, cv2.MORPH_OPEN, kernel)
        # WBOynatici = cv2.morphologyEx(WBOynatici, cv2.MORPH_CLOSE, kernel2)
        WBOynatici = cv2.dilate(WBOynatici, kernel2, iterations=1)
        (cnts, _) = cv2.findContours(WBOynatici, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        DoluKare = np.zeros((BolunmusO.shape[0], BolunmusO.shape[1], 1))

        Sonuc = BolunmusO.copy()
        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if (w > 60 and h > 60):
                cv2.rectangle(Sonuc, (x, y), (x + w, y + h), (0, 255, 0), thickness=gostergekalinligi)
                cv2.rectangle(DoluKare, (x, y), (x + w, y + h), (255), thickness=cv2.FILLED)

        cv2.rectangle(Sonuc, (Sensor1.Koordinat1.x, Sensor1.Koordinat1.y), (Sensor1.Koordinat2.x, Sensor1.Koordinat2.y),
                      (0, 0, 255), thickness=cv2.FILLED)
        cv2.rectangle(Sonuc, (Sensor2.Koordinat1.x, Sensor2.Koordinat1.y), (Sensor2.Koordinat2.x, Sensor2.Koordinat2.y),
                      (0, 0, 255), thickness=cv2.FILLED)
        cv2.rectangle(Sonuc, (Sensor3.Koordinat1.x, Sensor3.Koordinat1.y), (Sensor3.Koordinat2.x, Sensor3.Koordinat2.y),
                      (0, 0, 255), thickness=cv2.FILLED)
        cv2.rectangle(Sonuc, (Sensor4.Koordinat1.x, Sensor4.Koordinat1.y), (Sensor4.Koordinat2.x, Sensor4.Koordinat2.y),
                      (0, 0, 255), thickness=cv2.FILLED)

        Sensor1_Maske_Sonuc = cv2.bitwise_and(DoluKare, DoluKare, mask=Sensor1.Maske)
        Sensor1PSayisi = np.sum(Sensor1_Maske_Sonuc == 255)
        Sensor1Oran = Sensor1PSayisi / Sensor1.MaskeAlani

        Sensor2_Maske_Sonuc = cv2.bitwise_and(DoluKare, DoluKare, mask=Sensor2.Maske)
        Sensor2PSayisi = np.sum(Sensor2_Maske_Sonuc == 255)
        Sensor2Oran = Sensor2PSayisi / Sensor2.MaskeAlani

        Sensor3_Maske_Sonuc = cv2.bitwise_and(DoluKare, DoluKare, mask=Sensor3.Maske)
        Sensor3PSayisi = np.sum(Sensor3_Maske_Sonuc == 255)
        Sensor3Oran = Sensor3PSayisi / Sensor3.MaskeAlani

        Sensor4_Maske_Sonuc = cv2.bitwise_and(DoluKare, DoluKare, mask=Sensor4.Maske)
        Sensor4PSayisi = np.sum(Sensor4_Maske_Sonuc == 255)
        Sensor4Oran = Sensor4PSayisi / Sensor4.MaskeAlani

        if (Sensor1Oran >= Sensor1OranDegiskeni and Sensor1.Durum == False):
            cv2.rectangle(Sonuc, (Sensor1.Koordinat1.x, Sensor1.Koordinat1.y),
                          (Sensor1.Koordinat2.x, Sensor1.Koordinat2.y),
                          (0, 255, 0), thickness=cv2.FILLED)
            Sensor1.Durum = True
        elif (Sensor1Oran < Sensor1OranDegiskeni and Sensor1.Durum == True):
            cv2.rectangle(Sonuc, (Sensor1.Koordinat1.x, Sensor1.Koordinat1.y),
                          (Sensor1.Koordinat2.x, Sensor1.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)
            Sensor1.Durum = False
            Sensor1.AlgilananArac += 1
        else:
            cv2.rectangle(Sonuc, (Sensor1.Koordinat1.x, Sensor1.Koordinat1.y),
                          (Sensor1.Koordinat2.x, Sensor1.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)

        if (Sensor2Oran >= 0.50 and Sensor2.Durum == False):
            cv2.rectangle(Sonuc, (Sensor2.Koordinat1.x, Sensor2.Koordinat1.y),
                          (Sensor2.Koordinat2.x, Sensor2.Koordinat2.y),
                          (0, 255, 0), thickness=cv2.FILLED)
            Sensor2.Durum = True
        elif (Sensor2Oran < 0.50 and Sensor2.Durum == True):
            cv2.rectangle(Sonuc, (Sensor2.Koordinat1.x, Sensor2.Koordinat1.y),
                          (Sensor2.Koordinat2.x, Sensor2.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)
            Sensor2.Durum = False
            Sensor2.AlgilananArac += 1
        else:
            cv2.rectangle(Sonuc, (Sensor2.Koordinat1.x, Sensor2.Koordinat1.y),
                          (Sensor2.Koordinat2.x, Sensor2.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)

        if (Sensor3Oran >= 0.30 and Sensor3.Durum == False):
            cv2.rectangle(Sonuc, (Sensor3.Koordinat1.x, Sensor3.Koordinat1.y),
                          (Sensor3.Koordinat2.x, Sensor3.Koordinat2.y),
                          (0, 255, 0), thickness=cv2.FILLED)
            Sensor3.Durum = True
        elif (Sensor3Oran < 0.30 and Sensor3.Durum == True):
            cv2.rectangle(Sonuc, (Sensor3.Koordinat1.x, Sensor3.Koordinat1.y),
                          (Sensor3.Koordinat2.x, Sensor3.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)
            Sensor3.Durum = False
            Sensor3.AlgilananArac += 1
        else:
            cv2.rectangle(Sonuc, (Sensor3.Koordinat1.x, Sensor3.Koordinat1.y),
                          (Sensor3.Koordinat2.x, Sensor3.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)

        if (Sensor4Oran >= 0.30 and Sensor4.Durum == False):
            cv2.rectangle(Sonuc, (Sensor4.Koordinat1.x, Sensor4.Koordinat1.y),
                          (Sensor4.Koordinat2.x, Sensor4.Koordinat2.y),
                          (0, 255, 0), thickness=cv2.FILLED)
            Sensor4.Durum = True
        elif (Sensor4Oran < 0.30 and Sensor4.Durum == True):
            cv2.rectangle(Sonuc, (Sensor4.Koordinat1.x, Sensor4.Koordinat1.y),
                          (Sensor4.Koordinat2.x, Sensor4.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)
            Sensor4.Durum = False
            Sensor4.AlgilananArac += 1
        else:
            cv2.rectangle(Sonuc, (Sensor4.Koordinat1.x, Sensor4.Koordinat1.y),
                          (Sensor4.Koordinat2.x, Sensor4.Koordinat2.y),
                          (0, 0, 255), thickness=cv2.FILLED)

        cv2.putText(Sonuc, str(Sensor1.AlgilananArac), (Sensor1.Koordinat1.x + 20, Sensor1.Koordinat1.y + 65), font, 3,
                    (255, 255, 255))
        cv2.putText(Sonuc, str(Sensor2.AlgilananArac), (Sensor2.Koordinat1.x + 20, Sensor2.Koordinat1.y + 65), font, 3,
                    (255, 255, 255))
        cv2.putText(Sonuc, str(Sensor3.AlgilananArac), (Sensor3.Koordinat1.x + 20, Sensor3.Koordinat1.y + 65), font, 3,
                    (255, 255, 255))
        cv2.putText(Sonuc, str(Sensor4.AlgilananArac), (Sensor4.Koordinat1.x + 20, Sensor4.Koordinat1.y + 65), font, 3,
                    (255, 255, 255))

        #cv2.imshow("Without Background Oynatici", WBOynatici)
        cv2.imshow("Sonuc", Sonuc)
        #cv2.imshow("SMSonuc", Sensor1_Maske_Sonuc)
        #cv2.imshow("DoluKare", DoluKare)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    Oynatici.release()
    cv2.destroyAllWindows()

def clickedarttir():
    global gostergekalinligi
    gostergekalinligi += 1
    yazi1.configure(text=("Gösterge kalınlığı\n", gostergekalinligi, "\nolarak değiştirilmiştir."))

def clickeddusur():
    global gostergekalinligi
    gostergekalinligi -= 1
    yazi1.configure(text=("Gösterge kalınlığı\n", gostergekalinligi, "\nolarak değiştirilmiştir."))


btnarttir = Button(window, text="Arttır", command=clickedarttir)
btnarttir.grid(column=0, row=80)
btndusur = Button(window, text="Düşür", command=clickeddusur)
btndusur.grid(column=0, row=81)
btn = Button(window, text="BAŞLAT", command=clicked)
btn.grid(column=0, row=60)

window.mainloop()