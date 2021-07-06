from linkedlist import LinkedList
from data import *

def welcome():
    print("Welcome to the wine selector")

# Code to insert wine types into a LinkedList. The data is in data.py
def insert_wine_types():
    wine_type_list = LinkedList()
    for wine_type in types:
        wine_type_list.insert_beginning(wine_type)
    return wine_type_list

# Code to insert wine region into a LinkedList. The data is in data.py
def insert_wine_region():
    region_list = LinkedList()
    for region in regions:
        region_list.insert_beginning(region)
    return region_list

# Code to insert wine data into a LinkedList of Linkedlist. The data is in data.py
def insert_wine_list():
    wine_list = LinkedList()
    for wine_type in types:
        wine_sublist = LinkedList()
        for wine in wines:
            if wine[0] == wine_type:
                wine_sublist.insert_beginning(wine)
        wine_list.insert_beginning(wine_sublist)
    return wine_list

# Code to insert wine data into a LinkedList of Linkedlist. The data is in data.py
def insert_region_list():
    area_list = LinkedList()
    for region in regions:
        region_sublist = LinkedList()
        for wine in wines:
            if wine[2] == region:
                region_sublist.insert_beginning(wine)
        area_list.insert_beginning(region_sublist)     
    return area_list

variety_of_wine = insert_wine_types()
wine_details = insert_wine_list()
wine_regions = insert_wine_region()
region_details = insert_region_list()

# Code to ask user how they would like to search for their wine
def user_choice():
    how_user_search = input("How would you like to search for your wine? Please type 'v' for variey or 'r' for region: \n").lower()
    if how_user_search == 'v':
        choose_variety()
    elif how_user_search == 'r':
        choose_region()
    else:
        print("I did not understand your input, please try again")
        return user_choice()

# Code if user want to search by variety
def choose_variety():
    print("We have the following varieties of wine to choose from: ")
    print(* types, sep=", ")
    user_selection = input("Please type in the variety that you would like to buy\n").title()
    
    # Search for user input in data structure
    matching_wine = []
    get_list_head = variety_of_wine.get_head_node()
    while get_list_head is not None:
        if  str(get_list_head.get_value()).startswith(user_selection):
            matching_wine.append(get_list_head.get_value())
        get_list_head = get_list_head.get_next_node()

        if len(matching_wine) == 1:
            selected_wine = matching_wine[0]

            # Print a list of wine that matches user input
            print(f"We have the following {selected_wine} availible:")
            wine_list_head = wine_details.get_head_node()
            while wine_list_head.get_next_node() is not None:
                sublist_head = wine_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_wine:
                    while sublist_head.get_next_node() is not None:
                        print("________Summary________")
                        print(f"Winery:   {sublist_head.get_value()[1]}")
                        print(f"Region:   {sublist_head.get_value()[2]}")
                        print(f"Vintage:  {sublist_head.get_value()[3]}")
                        print("_______________________\n")
                        sublist_head = sublist_head.get_next_node()
                wine_list_head = wine_list_head.get_next_node()
            start_again()

    if len(matching_wine) == 0:
        print('Unfortunately we don\'t have your selected variety availible')
        start_again()
        


# Code if user want to search by region
def choose_region():
    print("We have wine from the following regions: ")
    print(* regions, sep=", ")
    user_selection = input("Please type in the region that you would like to explore\n").title()

    # Search for user input in data structure
    selected_wine_region = []
    get_list_head = wine_regions.get_head_node()
    while get_list_head is not None:
        if  str(get_list_head.get_value()).startswith(user_selection):
            selected_wine_region.append(get_list_head.get_value())
        get_list_head = get_list_head.get_next_node()

        if len(selected_wine_region) == 1:
            selected_area = selected_wine_region[0]

            # Print a list of wine that matches user input
            print(f"We have wine from the following wineries in {selected_area}:")
            wine_list_head = region_details.get_head_node()
            while wine_list_head.get_next_node() is not None:
                sublist_head = wine_list_head.get_value().get_head_node()
                if sublist_head.get_value()[2] == selected_area:
                    while sublist_head.get_next_node() is not None:
                        print("________Summary________")
                        print(f"Winery:   {sublist_head.get_value()[1]}")
                        print(f"Variety:  {sublist_head.get_value()[0]}")
                        print(f"Vintage:  {sublist_head.get_value()[3]}")
                        print("_______________________\n")
                        sublist_head = sublist_head.get_next_node()
                wine_list_head = wine_list_head.get_next_node()
            start_again()
    if len(selected_wine_region) == 0:
        print('Unfortunately we don\'t have wine from the selected region')
        start_again()            
 


# Code to aske the user if they would like to search again
def start_again():
    start_again = ""
    while start_again != 'y' or 'n': 
        start_again = input("Would you like to search for other wine? Press y for yes and n for no: ").lower()
        if start_again == 'y':
            user_choice()
        elif start_again == 'n':
            print("Goodbye")
            break
    

def start_wine_selector():
    welcome()
    user_choice()


start_wine_selector()