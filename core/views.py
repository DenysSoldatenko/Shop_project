from django.shortcuts import render

def homepage(request):
    context = {
        'title': 'Home',
        'content': "Welcome to Luxe Living!",
    }

    return render(request, 'core/homepage.html', context)

def about_us(request):
    context = {
        'title': 'About Us',
        'content': "About Us - Luxe Living Furniture",
        'text_on_page': """
            At Luxe Living, we believe that your home is more than just a place — it's a sanctuary where unforgettable moments are created.

            Our mission is simple: L.U.X.E. — Living Unmatched eXperiences Everywhere. 

            Whether you're hosting friends, enjoying a family movie night, or simply relaxing with a book, we offer high-quality, stylish, and affordable furniture to make your space truly your own.

            Passionate about design and functionality, Luxe Living is your go-to destination for bringing comfort, sophistication, and innovation into your home. Browse our curated collections and see why our customers trust us to make their homes a reflection of their style and personality!
        """,
    }

    return render(request, 'core/about_us.html', context)
