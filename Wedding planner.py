##############################   Project Pseudocode   #################################
#  Name: Vladislava Sicicorez
#
#  Purpose: Wedding ceremony and reception planner
#
#  Algorithm:
#
#   Start
#	Bride Last name input
# 	Groom Last name input
# 	Format name of the event: Bride Last Name – Groom Last name Wedding
# 	Number of guests input
# 	Date input
# 	Sunset time input
#
# 	if Sunset time after 6
# 		Ceremony time – 4PM and Picture time 5PM-6PM
#     	else
#         		Ceremony time 3
#         		Picture time 4:00PM - 5:00PM
#
#	Cocktail hour time = Ceremony_time+1
# 	Grand Entry time = Cocktail_hour+1
#	Dinner_Begin_Time = Grand_Entry
#	dinner_end_time = Dinner_Begin_Time+2
#	Grand_Exit = Dinner_Begin_Time+5
#
# 	Create dictionary appetizer menu
# 	Dictionary cocktail hour menu - create
#	Total number of appetizers = 0
# 	Display appetizer menu
# 	Get input for appetizer selection
#
#         while Appetizer_selection true
#         		prompt for number of appetizers
#         		get number of pieces – multiply number of orders by 50
#        		print appetizer selections and number of selection
#		prompt for appetizer selection
#
#         for i in Cocktail_hour_menu:
#         		print(i," - ", Cocktail_hour_menu[i],"pieces")
#
#    print total number of appetizers and per person
#    ask user to change the appetizer selections
#    while user wants to change the selection:
#		    take user back to appetizer selection
#		    ask user to change the appetizer selection
#		    if user doesn’t want to change appetizer selection:
#			    Continue the program
#		    else
#		        Go back to appetizer selection
#
#    Get selection for the first dance time
#    Get selection for cake cutting time
#    Create dictionary for buffet menu
#    Create dictionary for Plated menu
#    Get menu selection
#    Calculate Dinner time
#    Calculate First Dance Time
#    Calculate Cake time
#    Calculate Grand Exit time
#    Format and output Ceremony time, Picture time, Cocktail hour time and menu, Grand Entrance     #        Time, Dinner Time and menu, Cake cutting time and Grand Exit time
#    End
#########################################################################


#intitial information input from user
Bride = input("Enter Bride's Last Name: ")
Groom = input("Enter Groom's Last Name: ")
Name_of_the_event = ("{}-{} Wedding".format(Bride, Groom))
print()
Num_adl_guests = int(input("Enter number of guests (12 and up): "))
Num_kids = int(input("Enter number of guests (Age 3-11): "))
Num_infant = int(input("Enter number of guests (Under 3) for highchair count: "))
print()
Date = input("Enter date in MM/DD/YYYY: ")
print()

Sunset_time = input("Enter sunset time in HH:MM format: ")
Sunset = Sunset_time.split(":")
Sunset.append("PM")


print()
#set ceremony time based on sunset time
for i in Sunset:
    hour = int(Sunset[0])
    if hour>6:
        Ceremony_time = (4)
        Picture_time = ("5:00PM - 6:00PM")
    else:
        Ceremony_time = (3)
        Picture_time = ("4:00PM - 5:00PM")

Cocktail_hour = Ceremony_time+1
Grand_Entry = Cocktail_hour+1
Dinner_Begin_Time = Grand_Entry
dinner_end_time = Dinner_Begin_Time+2
Grand_Exit = Dinner_Begin_Time+5

Appetizer_menu = {1:"Shrimp DeJonghe",
                  2:"Cream Cheese filled Artichoke Hearts",
                  3:"Lobster Empanadas",
                  4:"Crab Beignets",
                  5:"Vegetable Spring Rolls",
                  6:"Raspberry Brie en Croute"}
Cocktail_hour_menu = {}


global total_apps
#function for appetizer choises
def appetizers():
    global Num_adl_guests
    print()

    print ("Please select appetizers from the provided menu")

    print ("*"*25)


    for i in Appetizer_menu:
        print (i, Appetizer_menu[i])

    print ("*"*25)

    Appetizer_selection = int(input("Enter selection number (Ex.: Enter 1 for Shrimp DeJoghe) or enter 0 to exit: "))

    global Cocktail_hour_menu

    Cocktail_hour_menu = {}

    while Appetizer_selection != 0:
        Num_appetizer = int(input("Enter number of orders (1 order = 50 pieces)): "))
        apps_num = Num_appetizer*50
        Cocktail_hour_menu[Appetizer_menu[Appetizer_selection]] = Num_appetizer*50
        print()
        print ("****NOTE: selecting same appetizer twice will delete your previous entry****")
        Appetizer_selection = int(input("Enter selection number (Ex.: Enter 1 for Shrimp DeJoghe) or enter 0 to exit: "))

    print ("-"* 25)
    print()
    apps = []
    total_apps = 0

    print ("Cocktail Hour menu: ")

    for i in Cocktail_hour_menu:
        print(i," - ", Cocktail_hour_menu[i],"pieces")
        apps.append(Cocktail_hour_menu[i])

    total_apps = sum(apps)

    apps_per_adl = total_apps/Num_adl_guests

    print ()

    print ("Total number of appetizers: {} or {:.1f} pieces per adult (recommended not less than 2 pieces)".format (total_apps, apps_per_adl))

    print()

appetizers()

#allow user to change appetizer choise
enter_loop = int(1)

while enter_loop == 1:
    print ("Would you like to change your appetizer choices?")
    print ('Enter "Y" for yes or "N" for no:')
    appetizer_change = str(input())

    while appetizer_change == 'Y' or appetizer_change == 'y':
        appetizers()
        print ("Would you like to change your appetizer choices?")
        print ('Enter "Y" for yes or "N" for no:')
        appetizer_change = str(input())

        if appetizer_change == 'N' or appetizer_change == 'n':
            print()

        else:
            print ("Wrong entry, try again")
            appetizers()

    if appetizer_change == 'N' or appetizer_change == 'n':
        enter_loop = "exit"

    else:
        print ("Wrong entry, try again")
        appetizers()
        enter_loop = 1

#determine time for first dance
print ('Would you like to have your first dance at the "Grand Entry" or after dinner?')

def first_dance_decision():

    global dance_time

    print ('Enter "G" to dance at the "Grand Entry"')

    print ('Enter "A" for after dinner')

    dance_time = input()

    return dance_time

first_dance_decision()

if dance_time == "G" or dance_time == "g":
        first_dance_time = Grand_Entry
        dinner_time = Grand_Entry+0.5

elif dance_time == "A" or dance_time == "a":
        first_dance_time =  dinner_end_time
        dinner_time = Grand_Entry+0.25

else:
    print ("Wrong entry")
    first_dance_decision()

print()
#determine time for cake cutting
print ("Would you like to cut the cake right after dinner or at the ending of the reception?")

def cake_time_decision():
    global cake_time

    print('Enter "A" for after dinner')

    print('Enter "R" for at the end of the reception')

    cake_time = input()

cake_time_decision()
print()
if cake_time == "A" or cake_time == "a":
    cake_cutting_time =  dinner_time+2

elif cake_time == "R" or cake_time == "r":
    cake_cutting_time = Grand_Exit-1

else:
    print ("Wrong entry")
    cake_time_decision()


#output dinner menu and allow user to make a selection
def dinner():
    global plated_dinner
    global dinner_buffet

    print ("Select option to view Dinner Menu:")

    print('For Plated option enter "P"')

    print('For Buffet enter "B"')

    print('Or enter "ALL" to see Plated and Buffet options: ')

    plated_dinner = {1: 'TRUFFLED CHICKEN - Truffle Scented Breast of Chicken with Parmesan Herb Polenta and Local Vegetables',
                 2:'GRILLED ATLANTAC SALMON With Sweet Corn, Tomato and Avocado Relish',
                 3: 'JUMBO SHRIMP SCAMPI Sautéed with Butter, Herbs, Garlic And White Wine',
                }

    dinner_buffet = {4 :"THE OLEANDER : Chicken and Pineapple Skewers with a Honey Mustard Dipping Sauce; Bite Size Vegetable Quiche; Spanakopita; Miniature Egg Rolls; Crab Balls with Tarter and Cocktail Sauce; Farfalle Pasta Tossed with Bay Shrimp, Kalamata Olives, Grape Tomatoes,Capers, and Basil Pesto; Chocolate Dipped Strawberries; Mints and Nuts;",
                 5 :"THE JASMINE : Green Garden Salad with Choice of Dressings; Cold Boiled Shrimp with Red and Remoulade Sauce; Mushrooms Stuffed with Spinach and Ham; Blackened Chicken Alfredo with Pasta; Parmesan Encrusted Eggplant with Marinara Sauce and Mozzarella Cheese; Crab Cakes with Spicy Tomato Coulis; Chef’s Choice of Vegetable; Warm Breads and Butter; Chocolate Dipped Strawberries;Mints and Nuts;",
                     }

    global dinner_menu

    dinner_menu = {1: 'TRUFFLED CHICKEN - Truffle Scented Breast of Chicken with Parmesan Herb Polenta and Local Vegetables',
                   2:'GRILLED ATLANTAC SALMON With Sweet Corn, Tomato and Avocado Relish',
                   3: 'JUMBO SHRIMP SCAMPI Sautéed with Butter, Herbs, Garlic And White Wine',
                   4 :"THE OLEANDER : Chicken and Pineapple Skewers with a Honey Mustard Dipping Sauce; Bite Size Vegetable Quiche; Spanakopita; Miniature Egg Rolls; Crab Balls with Tarter and Cocktail Sauce; Farfalle Pasta Tossed with Bay Shrimp, Kalamata Olives, Grape Tomatoes,Capers, and Basil Pesto; Chocolate Dipped Strawberries; Mints and Nuts;",
                   5 :"THE JASMINE : Green Garden Salad with Choice of Dressings; Cold Boiled Shrimp with Red and Remoulade Sauce; Mushrooms Stuffed with Spinach and Ham; Blackened Chicken Alfredo with Pasta; Parmesan Encrusted Eggplant with Marinara Sauce and Mozzarella Cheese; Crab Cakes with Spicy Tomato Coulis; Chef’s Choice of Vegetable; Warm Breads and Butter; Chocolate Dipped Strawberries;Mints and Nuts;",
                   }

    dinner_decision = input()

    if (dinner_decision == "P") or (dinner_decision == "p"):

            for i in plated_dinner:
                print (i,"-", plated_dinner[i])

            print ("Would you like to see Buffet Menu? Y/N")
            dec = input()

            if (dec == "Y") or (dec == "y"):
                    for i in dinner_buffet:
                        print (i,"-", dinner_buffet[i])

            elif (dec == "N") or (dec == "n"):
                print()

            else:
                    print("Wrong entry")
                    dinner()

    elif (dinner_decision == "B") or (dinner_decision == "b"):

            for i in dinner_buffet:
                print (i,"-", dinner_buffet[i])

            print ("Would you like to see Plated Dinner Menu? Y/N")
            dec = ()
            dec = input()

            if (dec == "Y") or (dec == "y"):
                for i in plated_dinner:
                    print (i,"-", plated_dinner[i])

            elif (dec == "N") or (dec == "n"):
                print()

            else:
                print("Wrong entry")
                dinner()

    elif (dinner_decision == "ALL") or (dinner_decision == "all"):
                for i in dinner_menu:
                    print (i, "-", dinner_menu[i])
    else:
            print("Wrong entry, try again")
            dinner()
dinner()

def choose_dinner():

     print ("Enter your dinner choise (number 1, 2, 3 (plated options); 4 or 5 (buffet options)): ")

     d_choise = int(input())

     if d_choise == 1:
         dinner_menu_ch = dinner_menu[1]

     elif d_choise == 2:
         dinner_menu_ch = dinner_menu[2]

     elif d_choise == 3:
         dinner_menu_ch = dinner_menu[3]

     elif d_choise == 4:
        dinner_menu_ch = dinner_menu[4]

     elif d_choise == 5:
         dinner_menu_ch = dinner_menu[5]

     else:
         print("Wrong entry, try again")
         choose_dinner()

     return (d_choise)

dinner_menu_choise = choose_dinner()
print()
print()
print()
#output data based on user inputs
print (Name_of_the_event) #Bride's Last name - Groom's Last name wedding

print ("Date: {}".format(Date)) #wedding date

print ("Number of guests: {}".format(Num_kids+Num_adl_guests+Num_infant))  #number of adults, kids and infants

print("-"*51)

format_table = '{:<20}{:5}{name_of_function:<51}' #table format

print(format_table.format("Time","|",name_of_function = "Name of Function")) #table header

print("*"*51)

print(format_table.format("{}:00PM - {}:00PM".format(Ceremony_time,Ceremony_time+1),' ',name_of_function = "Ceremony time")) #ceremony time output (time and name of the event)

print(format_table.format(Picture_time,'  ',name_of_function = "Picture time")) #picture time output (time and name of the event)

print(format_table.format("{}:00PM - {}:00PM".format(Cocktail_hour,Cocktail_hour+1),'  ',name_of_function = "Cocktail hour"))#cocktial hour output (time and name of the event)

print(format_table.format("{}:00PM" .format(Grand_Entry),'  ',name_of_function = "Grand Entry"))#grand entry output (time and name of the event)

#format dinner time from float to time format (time and name of the event)
form_dinner_time_hour = int(dinner_time//1)
form_dinner_time_minute = int((dinner_time - form_dinner_time_hour)*60)

#first dance output (time and name of the event)
if first_dance_time<dinner_time:
    print (format_table.format("{}:00PM".format(first_dance_time),' ',name_of_function = "First Dance"))
    print(format_table.format("{}:{}PM - {}:{}PM".format(form_dinner_time_hour,form_dinner_time_minute, form_dinner_time_hour+2, form_dinner_time_minute),'  ', name_of_function="Dinner"))

else:
    print(format_table.format("{}:{}PM - {}:{}PM".format(form_dinner_time_hour,form_dinner_time_minute, form_dinner_time_hour+2, form_dinner_time_minute),'  ', name_of_function="Dinner"))
    print (format_table.format("{}:00PM".format(first_dance_time),' ',name_of_function = "First Dance"))

#wedding program and dancing output (time and name of the event)
print (format_table.format("{}:{}PM - {}:00PM".format(form_dinner_time_hour+2,form_dinner_time_minute,Grand_Exit),' ', name_of_function = "Wedding Program and Dancing"))

#cake cutting time output (time and name of the event)
if cake_cutting_time == (form_dinner_time_hour+2):
    print (format_table.format("{}:15PM".format(form_dinner_time_hour+2),' ',name_of_function = "Cake cutting"))

else:
    print (format_table.format("{}:00PM".format(form_dinner_time_hour+4),' ',name_of_function = "Cake cutting"))

#grand exit output(time and name of the event)
print (format_table.format("{}:00PM".format(Grand_Exit),' ',name_of_function = "Grand Exit"))

print ("*"*51)

#output cocktial hour menu
print()
print ("Cocktail hour menu:")
print()
for i in Cocktail_hour_menu:
    print(i," - ", Cocktail_hour_menu[i],"pieces")

print ("Tropical Fruit punch")
print()
print ("*"*51)
print()
#output dinner menu

print ("Dinner Menu:")
print()
if (dinner_menu_choise == 1) or (dinner_menu_choise == 2) or (dinner_menu_choise == 3):
    print ("{} plates of {}".format(Num_adl_guests,dinner_menu[dinner_menu_choise]))

else:
    buffet_list = dinner_menu[dinner_menu_choise].split(':')
    buffet_name = buffet_list[0]
    buffet_descrip = buffet_list[1].split(';')
    print ("{} guests for {}".format(Num_adl_guests,buffet_name))

    for i in buffet_descrip:
        print (i)

print ("{} Chicken Tenders with french fries for kids".format(Num_kids))

print ("Iced Tea, Tropical Fruit Punch")

print ("Freshly baked bread and butter")

print()
number_number_of_h_chairs = Num_infant
print ("Number of high chairs needed: {}".format(number_number_of_h_chairs))
print()

print ("Congratulations!")
print ("♥"*51)










