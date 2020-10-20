import requests
import bs4
from tkinter import *


def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_data():
    url = 'https://www.worldometers.info/coronavirus/'
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    # print(bs)
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    # print(info_div)
    all_data = ""
    for item in info_div:
        text = item.find("h1", class_=None).get_text()
        # print(text)
        count = item.find("span", class_=None).get_text()
        # print(count)
        all_data = all_data + text + " " + count + "\n"
        # print(all_data)
    return all_data


def reload():
    new_data = get_covid_data()
    main_label['text'] = new_data


def get_country_data():
    country_name = input_field.get()
    url = f'https://www.worldometers.info/coronavirus/country/{country_name}/'

    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    # print(bs)
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    # print(info_div)
    all_data = ""
    for item in info_div:
        text = item.find("h1", class_=None).get_text()
        # print(text)
        count = item.find("span", class_=None).get_text()
        # print(count)
        all_data = all_data + text + " " + count + "\n"
        # print(all_data)
    main_label['text'] = all_data


# get_covid_data()

# now lets make a GUI

window = Tk()
window.geometry("900x700")
window.title("Covid 19 Tracker")
label0 = Label(window)
label0.pack()
banner = PhotoImage(file="coronavirus.png")
banner_label = Label(window, image=banner, width=250)
banner_label.pack()

label1 = Label(window)
label1.pack()

input_field = Entry(window, width=75)
input_field.pack()

main_label = Label(window, text=get_covid_data(), font="poppins 15 bold")
main_label.pack()

getdata_button = Button(window, text="Get Data", font="poppins 10 normal", command=get_country_data)
getdata_button.pack()

reload_button = Button(window, text="Reload", font="poppins 10 normal", command=reload)
reload_button.pack()

window.mainloop()
