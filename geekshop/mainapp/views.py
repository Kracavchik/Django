import datetime
import json

from django.shortcuts import render


def read_json(name):
    path = "mainapp/json/" + name + '.json'
    with open(path, 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
        return data

def main(request):
    title = "главная"
    products = read_json('main').values()
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    links_menu = read_json('products').get('a')
    same_products = read_json('products').get('b')
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = read_json('contact').get('a')
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
