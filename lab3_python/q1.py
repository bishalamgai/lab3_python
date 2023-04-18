# initialize the shopping cart dictionary
shoppingCart = {}

# main menu loop
while True:
    print("\nWELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        count = int(input("Enter the number of items to be added in the stationary shop: "))

        # check if cart is full
        if len(shoppingCart) + count > 5:
            print("Cart is full.")
        else:
            # add products to cart
            for i in range(count):
                product = input("Enter an item: ")
                brand = input("Enter the brand name: ")
                shoppingCart[product] = brand

            # display cart contents
            print("You added following items to the cart:")
            for product, brand in shoppingCart.items():
                print(f"{product}: {brand}")

    elif choice == '2':
        searchProduct = input("Enter the item to be searched: ")

        # search for product in cart
        if searchProduct in shoppingCart:
            print(f"{searchProduct}: {shoppingCart[searchProduct]}")
        else:
            print("No product exists with this name.")

    elif choice == '3':
        if not shoppingCart:
            print("Cart is empty, no item is found.")
        else:
            delProduct = input("Enter the item to be deleted: ")

            # delete product from cart
            if delProduct in shoppingCart:
                del shoppingCart[delProduct]
                print(f"{delProduct} is removed from the cart.")
            else:
                print("No product exists with this name.")

    elif choice == '4':
        break

    else:
        print("Wrong option entered.")
