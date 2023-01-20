from bs4.element import Comment, NavigableString, Tag
import requests
import sys
import bs4
from bs4 import BeautifulSoup
from tkinter import *

# url=input("Enter the website (main url) which you wanna parse:")

# r = requests.get(url)
# con = r.content

# soup = BeautifulSoup(con,'html.parser')

# t=soup.title.string
# print("Title of this page is-",t)
# link=soup.find_all('a')
# for l in link :
#     print(url+str(l.get('href')))

# con=soup.find('div').get_text()
# print(con)


# print("\n Classes in div :",soup.find('div')['class'])
# # print("ID's  in div :",soup.find('div')['id']) --> cannt be written

# val=soup.find('div',class_='container')
# for c in val.contents:
#     print(c)

win = Tk()
# win.configure("see")
win.title("WEB SCRAPPER")

win.geometry("400x400")
win.minsize(200, 200)
win.maxsize(800, 800)


def scrappin():
    u = requests.get(URL.get())
    a = URL.get()  # to be used to get url value
    soup = BeautifulSoup(u.text, 'html.parser')

    save = open("WEB_TEXT.txt", 'w', encoding="utf-8")  # append mode
    content = soup.find("body").get_text()
    for i in content:
        save.write(i)
    save.close()

    save1 = open("WEB_CODE.txt", 'w', encoding="utf-8")
    for i in soup.select('body'):
        save1.write(soup.prettify())
    save1.close()

    save2 = open("WEB_LINKS.txt", 'w', encoding="utf-8")  # append mode
    links = soup.find_all('a')
    for j in links:
        save2.write(a+str(j.get('href')))
        save2.write("\n")
    save2.close()


f = Frame(win, bg='#baaff9', borderwidth=5, relief=RIDGE)
f.pack(side=TOP, fill=X)

label = Label(f, text="Scrapping tool >> by Faiz ", bg="white", font=(
    "Helvetica", 12), borderwidth=3, relief=RIDGE, pady=15)
label.pack(pady=3)


f2 = Frame(win, bg='#baaff9', borderwidth=5, relief=RIDGE)
f2.pack(side=LEFT, fill=X, pady=20)

var = "About: \n \n This Application is useful in \n scrapping data through any \n websites' API's.  \n You can Enter the URL to \n execute this event.."

label1 = Label(f2, text=var, borderwidth=3, relief=SUNKEN,
               bg="#f3ff8f", font=("Helvetica", 11), pady=150, bd=6)

label1.pack(pady=50)

# f3=Frame(win,bg='#baaff9',borderwidth=5,relief=RIDGE)
# f3.pack(side=LEFT,fill=X,pady=20,padx=20)

URL = StringVar()

Enter = Entry(win, bd=8, font=("Helvetica", 12), textvariable=URL)
Enter.pack(pady=100, padx=20)


button = Button(win, text=" Click to Scrap", bd=5, command=scrappin)
button.pack()


win.mainloop()
