def cart(item):
    shopping_cart = [
        'notebooks',
        'candy',
        'toys',
    ]

    if item in shopping_cart:
        print(f"{item} is already in the cart.")
    else:
        shopping_cart.append(item)
        print(f"{item} has been added to the cart.")

    return shopping_cart
