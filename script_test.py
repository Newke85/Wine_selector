
from linkedlist import LinkedList
from data import *

def welcome():
    print("Welcome to the wine selector")

def insert_wine_types():
    wine_type_list = LinkedList()
    for wine_type in types:
        wine_type_list.insert_beginning(wine_type)
    return wine_type_list

def insert_wine_list():
    wine_list = LinkedList()
    for wine_type in types:
        wine_sublist = LinkedList()
        for wine in wines:
            if wine[0] == wine_type:
                wine_sublist.insert_beginning(wine)
        wine_list.insert_beginning(wine_sublist)
    return wine_list

types_of_wine = insert_wine_types()
wine_details = insert_wine_list()

def user_choice():
    print("We have the following varieties of wine to choose from: ")
    print(* types, sep=", ")
    user_selection = input("Please type in the variety that you would like to buy\n ")
    matching_wine = []
    get_list_head = types_of_wine.get_head_node()
    while get_list_head is not None:
        if  str(get_list_head.get_value()).startswith(user_selection):
            matching_wine.append(get_list_head.get_value())
        get_list_head = get_list_head.get_next_node()
    selected_wine = matching_wine[0]
    print(f"We have the following {selected_wine} availible:")
    wine_list_head = wine_details.get_head_node()
    while wine_list_head.get_next_node() is not None:
        sublist_head = wine_list_head.get_value().get_head_node()
        if sublist_head.get_value()[0] == selected_wine:
            while sublist_head.get_next_node() is not None:
                print("________Summary________")
                print(f"Winery:  {sublist_head.get_value()[1]}")
                print(f"Region:  {sublist_head.get_value()[2]}")
                print(f"Vintage: {sublist_head.get_value()[3]}")
                print("_______________________\n")
                sublist_head = sublist_head.get_next_node()
        wine_list_head = wine_list_head.get_next_node()

    start_again = ""
    while start_again != 'y' or 'n': 
        start_again = input("Would you like to search for other wine? Press y for yes and n for no: ")
        if start_again == 'y':
            user_choice()
        elif start_again == 'n':
            print("Goodbye")
            break



def start_wine_selector():
    welcome()
    insert_wine_types()
    insert_wine_list()
    user_choice()

    

start_wine_selector()