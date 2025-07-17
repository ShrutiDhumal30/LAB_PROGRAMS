#Online restaurant system

print("Welcome to Our restaurant")
print("Give your order by selecting the choice")

total_bill = 0
#ordered_item = 0
ordered_item = []

while True:

    print("------------------------")
    print("1.Breakfast:")
    print("2.Lunch")
    print("3.Drinks")
    print("4.Dessert")
    print("5.Exit and generate bill")

    Choice = int(input("Select your choice:"))

    if(Choice==1):
        print("Select dish for your breakfast:")
        print("1.Idli - Rs.40")
        print("2.Sandwich - Rs.50")
        print("3.Pohe - Rs.30")
        print("4.Dosa - Rs.80")

        dish_choice = int(input("Select your dish(1-4):"))

        if(dish_choice==1):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 40 * quantity
            ordered_item.append(f"Idli :{quantity}")
        elif(dish_choice==2):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill +50 * quantity
            ordered_item.append(f"Sandwich :{quantity}")
        elif(dish_choice==3):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill +30 * quantity
            ordered_item.append(f"Pohe :{quantity}")
        elif(dish_choice==4):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill+80 * quantity
            ordered_item.append(f"Dosa :{quantity}")
        else:
            print("Invalid dish choice")


    elif(Choice==2):
        print("Select dish for your Lunch:")
        print("1.Pav Bhaji - Rs.100")
        print("2.Parathas - Rs.85")
        print("3.Kadai Paneer - Rs.120")
        print("4.Chole Bhature - Rs.130")

        dish_choice = int(input("Select your dish(1-4):"))

        if(dish_choice==1):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 100 * quantity
            ordered_item.append(f"Pav Bhaji :{quantity}")
        elif(dish_choice==2):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill +85 * quantity
            ordered_item.append(f"Parathas :{quantity}")
        elif(dish_choice==3):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill +120 * quantity
            ordered_item.append(f"Kadai Paneer :{quantity}")
        elif(dish_choice==4):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill+130 * quantity
            ordered_item.append(f"Chole Bhature :{quantity}")
        else:
            print("Invalid dish choice")


    elif(Choice==3):
        print("Select your drink:")
        print("1.Tea - Rs.15")
        print("2.Coffee - Rs.20")
        print("3.Cold Coffee - Rs.45")
        print("4.Milkshake - Rs.55")

        dish_choice = int(input("Select your dish(1-4):"))

        if(dish_choice==1):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 15 * quantity
            ordered_item.append(f"Tea :{quantity}")
        elif(dish_choice==2):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 20 * quantity
            ordered_item.append(f"Coffee :{quantity}")
        elif(dish_choice==3):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 45 * quantity
            ordered_item.append(f"Cold Coffee :{quantity}")
        elif(dish_choice==4):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill+ 55 * quantity
            ordered_item.append(f"Milkshake :{quantity}")
        else:
            print("Invalid dish choice")


    elif(Choice==4):
        print("Select your Dessert:")
        print("1.Gulabjamun - Rs.60")
        print("2.Brownies - Rs.80")
        print("3.Custard - Rs.65")
        print("4. Ice Cream - Rs.75")

        dish_choice = int(input("Select your dish(1-4):"))

        if(dish_choice==1):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 60 * quantity
            ordered_item.append(f"Gulabjamun :{quantity}")
        elif(dish_choice==2):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 80 * quantity
            ordered_item.append(f"Brownies :{quantity}")
        elif(dish_choice==3):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill + 65 * quantity
            ordered_item.append(f"Custard :{quantity}")
        elif(dish_choice==4):
            quantity = int(input("Enter quantity:"))
            total_bill=total_bill+ 75 * quantity
            ordered_item.append(f"Ice Cream :{quantity}")
        else:
            print("Invalid dish choice")

    else:
        print("\nGenerating your bill....")
        if ordered_item:
            print("Orderd Dishes:")
            for item in ordered_item:
                print(f"- {item}")
       
        print(f"Total amount : Rs.{total_bill}")
        print("Thank you for visiting!")
        break

   


    


