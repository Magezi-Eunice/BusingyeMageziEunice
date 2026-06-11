def ecommerce_login():
    print("Welcome to the Login System")

    userRole = {
        "Admin": "adminpassword", 
        "Customer": "custompassword", 
        "Cashier": "cashpassword"
    }

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:
        userName = input("Enter username here: ")
        password = input("Enter password here: ")

        if userName in userRole:
            if userRole[userName] == password:
                print(f"Sucessful Login {userName}!")
                if userName == "Admin":
                    print("You have full access.")
                elif userName == "Customer":
                    print("You can view and buy products.")
                elif userName == "Cashier":
                    print("You can recieve payments.")
                return True
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")

        attempts += 1
        remaining = maxAttempts - attempts
        print(f"{remaining} attempts left")

    print("Maximum login attempts reached.")
    return False


def taxCollector():
    location = input("Enter location (Africa, Europe, America, Australia, Asia): ").title()

    match location:
        case "Africa":
            tax = 0.18 * subTotal
        case "Europe" | "Australia":
            tax = 0.20 * subTotal
        case "America" | "Asia":
            tax = 0.19 * subTotal
        case _:
            print("Invalid location")
    
    return tax


def discountCalculate():
    couponList = {
        "COUP001": 0.05,
        "COUP002": 0.10,
        "COUP003": 0.20,
        "COUP004": 0.50
    }

    if subTotal < 0:
        discount = 0
        print("You are not eligible for a discount")
    elif 20000 <= subTotal >= 50000:
        discount = 0.05 * subTotal
        print(f"You are eligible for a 5% discount") 
    elif 50000 < subTotal >= 100000:
        discount = 0.1 * subTotal
        print(f"You are not eligible for a 10% discount")
    else:
        discount = 0.15 * subTotal
        print(f"You are not eligible for a 15% discount")
    
    coupon = input("Enter coupon code: ")

    if coupon in couponList:
        amount = couponList[coupon] * subTotal
        totalDiscount = discount + amount
        print(f"Congradulations! You get an additional {couponList[coupon]:.1%} off on your order")
    else:
        print(f"This is an invalid coupon code")

    return discount

def totalBill():
    tax= taxCollector()
    discount = discountCalculate()

    finalPrice = (subTotal + tax) - discount

    reciept = f"""

            -------Your Reciept-------
                Sub Total: {subTotal}
                Tax: + {tax}
                Total discount: - {discount}
                Final Price: {finalPrice}

            """
    
    print(reciept)

ecommerce_login()
subTotal = int(input("Please enter total expenditure: "))
totalBill()