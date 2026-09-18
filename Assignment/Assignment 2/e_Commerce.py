catalog = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50,
    "monitor": 150 
    }

# while True:
#     print("1. Enter item")
#     print("2. Checkout")
#     print("3. Exit")

#     option = input("Choose your option: ")
#     grand_total = 0

#     if option =="1":
#         print(catalog)
#         print("Available items from catalogue")
#         item = input("Enter name of item from Catalogue: ")
#         if item in catalog:
#             price = catalog[item.]
#             grand_total +=price

#         else:
#             print("Item not available")
#     elif option =="2":
#         pass
#     elif option =="3":
#         print("Order Cancelled")
#         break
#     else:
#         print("Wrong input!!, Enter from 1-3")


grandTotal = 0
discountRate = 0
while True:

    userInput = input("Enter your item or checkout or Exit: ").capitalize().strip()

    if userInput == "Exit":
        print("Order CAncelld")
        break
    elif userInput == "Checkout":
        if grandTotal >= 500:
            discountRate = 0.10
        elif grandTotal >=200 and grandTotal <=499:
             discountRate = 0.05
        else:
            print("No discount")

            # Discount calculation
        totalDiscount = grandTotal * discountRate
        finalTotal = grandTotal - totalDiscount

        print("CHECKOUT RECEIPT")
        print("===========================")
        print(f"Subtotal: ${grandTotal:.1f}")
        print(f"Discount: ${totalDiscount:.1f}")
        print(f"Final Total: ${finalTotal:.1f}")
        print("===========================")
        print("Continue shopping!! or exit??\n")
    elif userInput in catalog:
        pass