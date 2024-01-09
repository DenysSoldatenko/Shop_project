from django.shortcuts import render

def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": [
            {
                "image": "deps/images/goods/set_of_tea_table_and_three_chairs.jpg",
                "name": "Tea Table and Three Chairs",
                "description": "A set of three chairs and a designer table for the living room.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set_of_tea_table_and_two_chairs.jpg",
                "name": "Tea Table and Two Chairs",
                "description": "A set of a table and two chairs in minimalist style.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double_bed.jpg",
                "name": "Double Bed",
                "description": "A double bed with a headboard and very orthopedic.",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen_table.jpg",
                "name": "Kitchen Table with Sink",
                "description": "A kitchen dining table with a built-in sink and chairs.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen_table_2.jpg",
                "name": "Kitchen Table with Stove",
                "description": "A kitchen table with a built-in stove and sink. Many shelves and overall beautiful.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner_sofa.jpg",
                "name": "Corner Sofa for Living Room",
                "description": "A corner sofa that folds into a double bed, perfect for the living room and guest receptions!",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside_table.jpg",
                "name": "Bedside Table",
                "description": "A bedside table with two drawers (flower not included).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Ordinary Sofa",
                "description": "A sofa, also called an ordinary couch, nothing special to say about it.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office_chair.jpg",
                "name": "Office Chair",
                "description": "A product description about how great this chair is, but it's just a chair, what else to say...",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Plant",
                "description": "A decorative plant to add freshness and serenity to your interior.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Stylized Flower",
                "description": "A designer flower (possibly artificial) for decorating your interior.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange_table.jpg",
                "name": "Strange Bedside Table",
                "description": "A rather unusual looking table, but perfect for placing next to the bed.",
                "price": 25.00,
            },
        ],
    }
    return render(request, "inventory/catalog.html", context)


def product(request):
    return render(request, "inventory/product.html")
