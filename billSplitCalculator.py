tip = 0
options = ["10%", "15%", "20%", "custom"]

current_bill = int(input("\nEnter total bill amount: "))
people = int(input("\nEnter number of people paying: "))

while True:
    print("\nPossible tip percenetages:")
    for index, item in enumerate(options, 1):
        print(f"{index}. {item}") 


    user_input = input("\nPlease select number for corresponding tip option: ")

    choice_num = int(user_input)
    if 1 <= choice_num <= len(options):
        selected_option = options[choice_num-1]
    else:
        print("\nPlease enter a menu number\n")
    
    if selected_option == "custom":
        selected_option = input("\nPlease type input percentage: ")
    break


percentage = int(selected_option.replace("%", ""))

tip = (current_bill*(percentage/100))

total_bill = current_bill + tip

amount = total_bill/people

print("\n-------------Your Final Receipt------------")
print(f"Original bill: {current_bill:,}")
print(f"Tip amount: {percentage}%")
print(f"Tip = Original bill x tip percentage: {tip:,.2f}")
print(f"Total bill (Original bill + tip): {total_bill:,.2f}")
print(f"Amount per person (Total bill/number of people): {amount:,.2f}\n")


