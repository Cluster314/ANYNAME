import requests
from tkinter import *
url = "https://quranapi.pages.dev/"
def get_quran_info(surahnum: int):
    global url
    surahnum = str(surahnum)
    url = f"{url}/api/{surahnum}.json"
    return requests.get(url).json()
NO = int(input("Surah Number: "))
print("hint: a new window has opened in your taskbar, it has a python icon on it.")
window = Tk()
vr = 1
lb = Listbox(window,font=("Arial", 15),width=500,height=10)
lb.pack()
lb.insert(1, "In the name of Allah, The Most Compassionate, The Most Merciful.")
for i in get_quran_info(NO)["english"]:
    vr+=1
    lb.insert(vr,f"{vr-1}. {i}")
horizontal_scrollbar = Scrollbar(window, orient="horizontal", command=lb.xview)
horizontal_scrollbar.pack(side="bottom", fill="x")
lb.config(xscrollcommand=horizontal_scrollbar.set)
window.mainloop()              