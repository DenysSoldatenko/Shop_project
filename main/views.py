from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Main Page',
        'content': "Furniture Store HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About Us',
        'content': "About Us",
        'text_on_page': "Text about why this store is awesome and how great our products are.",
    }

    return render(request, 'main/about.html', context)
