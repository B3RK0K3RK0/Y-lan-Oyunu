#Ekran, yılan ve yem için turtle; bekleme süreleri için time; yemin ekranda rastgele kordinatlarda çıkması için random küthüphanelerini ekledim.
import turtle
import time
import random
from turtle import Turtle

#Oyunun ekranının ebatlarını ve rengini ayarladım.
oyunEkranı = turtle.Screen()
oyunEkranı.tracer(0)
oyunEkranı.setup(600,600)
oyunEkranı.bgcolor("black")

#Oynıyacağımız yılanın şekli, rengi, hızı ve ilk konumunu ayarladım.
yılan: Turtle = turtle.Turtle()
yılan.shape("circle")
yılan.color("green")
yılan.speed(0)
yılan.penup()
yılan.goto(-200,0)
yılan.yön = "dur"

#Yemin şekli, rengi, hızı ilk ve konumunu ayarladım.
yem = turtle.Turtle()
yem.shape("square")
yem.color("yellow")
yem.speed(0)
yem.penup()
yem.goto(0,0)
yem.yön = "dur"

#Yılanı ekranda hareket ettirmek için fonksiyonlar tanımladım.
def yukarı():
    if yılan.yön != "aşağı":
        yılan.yön = "yukarı"
def aşağı():
    if yılan.yön != "yukarı":
        yılan.yön = "aşağı"
def sağa():
    if yılan.yön != "sol":
        yılan.yön = "sağ"
def sola():
    if yılan.yön != "sağ":
        yılan.yön = "sol"

#Oyunda yılanı kontrol edebilmek için w,a,s,d ve yön tuşlarına atadım.
oyunEkranı.listen()
oyunEkranı.onkeypress(yukarı, "w")
oyunEkranı.onkeypress(aşağı, "s")
oyunEkranı.onkeypress(sağa, "d")
oyunEkranı.onkeypress(sola, "a")

oyunEkranı.onkeypress(yukarı, "Up")
oyunEkranı.onkeypress(aşağı, "Down")
oyunEkranı.onkeypress(sağa, "Right")
oyunEkranı.onkeypress(sola, "Left")

#Tanımlı tuşlara basıldığında yılanın ekranda hareket ediceği yön ve ne kadar hareket ediceğini belirleyecek kordinatları atadığım bir fonksiyon tanımladım.
def hareket_et():
    if yılan.yön == "yukarı":
        y = yılan.ycor()
        yılan.sety(y + 20)
    if yılan.yön == "aşağı":
        y = yılan.ycor()
        yılan.sety(y - 20)
    if yılan.yön == "sağ":
        x = yılan.xcor()
        yılan.setx(x + 20)
    if yılan.yön == "sol":
        x = yılan.xcor()
        yılan.setx(x - 20)



bölümler = []
while True:
    oyunEkranı.update()

    

#Burada yılanın ekranın kenarlarına çarptığında ölmesini ve 1 saniye oyunu duraklamasını sağladım, aynı zamanda yılanın ilk kordinatlarına dönmesini ve atanan tuşlardan birine basılmadıkça hareket etmemesini ayarladım.
    if yılan.xcor() > 290 or yılan.xcor() < -290 or yılan.ycor() > 290 or yılan.ycor() < -290:
        time.sleep(1)
        yılan.goto(-200,0)
        yılan.yön = " dur"
#Yılan kenarlardan birine çarparsa ekranda göremiyeceğimiz (bu yüzden 2000,2000) bir yere taşımasını sağladım ve bölümler kısmını temizlettim.
        for i in bölümler:
            i.goto(2000,2000)

        bölümler.clear()

#Yılan ve yem arasında 20 pikselden az kaldığında yılanın yemi yemesini, yemin yenildikten sonra ekranda (ekrandan çıkmaması için -290,290 piksel arası aldım) rastgele bir kordinatta çıkmasını ayarladım.
    if yılan.distance(yem) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        yem.goto(x,y)

#Burada yılan her yem yediğinde yemin yılana eklenmesini, eklenen kısmın şekli, hızı ve rengini ayarladım. Ayrıca eklenen yemin yılanın arkasında çizgi bırakmasını engelledim(yeniBölüm.penup komutu ile). yeniBölümü bölümler kısmına ekledim
        yeniBölüm = turtle.Turtle()
        yeniBölüm.speed(0)
        yeniBölüm.shape("circle")
        yeniBölüm.penup()
        yeniBölüm.color("green")
        bölümler.append(yeniBölüm)

#Bölümleri saydırdım ve elementleri yerleştirdim.
    for i in range(len(bölümler)-1,0,-1):
        x = bölümler[i-1].xcor()
        y = bölümler[i-1].ycor()
        bölümler[i].goto(x,y)

#Son turtle'ı yılana ekler.
    if len(bölümler) >0:
        x = yılan.xcor()
        y = yılan.ycor()
        bölümler[0].goto(x,y)

    hareket_et()

#Yılanın kafası eğer kendi vücuduna 20 pikselden yakınsa ölür, 1 saniye bekler, başlangıç kordinatlarına gelir ve atanan bir tuşa basılmadığı sürece durur.
    for i in bölümler:
        if i.distance(yılan)<20:
           time.sleep(1)
           yılan.goto(-200,0)
           yılan.yön = "dur"

#Eğer yılan kendi vücuduna çarparak ölürse kafa hariç vücut ekranda göremeyeceğimiz (2000 , 2000) bir yere gider ve bölüm temizlenir (sadece kafa kalır).
           for i in bölümler:
                i.goto(2000 , 2000)


           bölümler.clear()

    time.sleep(0.1)