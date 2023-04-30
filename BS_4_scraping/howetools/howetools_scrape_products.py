from bs4 import BeautifulSoup
import requests



link = "https://www.howetools.co.uk/power-tools/makita?p=2"

for i in range(1,67):
    if link[-2].isdigit():
        digit = int(link[-2:])
    else:
        digit = int(link[-1])

    if link[-2:].isdigit():
        link = link[:-2]
    else:
        link = link[:-1]
    digit += 1
    link += str(digit)


    response = requests.get(link)

    soup = BeautifulSoup(response.content, "html.parser")
    model = soup.find_all("a", class_="product-item-link")
    price = soup.find_all("span", class_="price")
    name = soup.find_all("div", class_="short-description")

    for t, p, n in zip(model, price, name):
        print(f"{n.text},{t.text},{p.text}")

