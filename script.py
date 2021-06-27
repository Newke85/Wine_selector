from node import *
from linkedlist import LinkedList
from data import *


def insert_wine_types():
    wine_type_list = LinkedList()
    for wine_type in types:
        wine_type_list.insert_beginning(wine_type)
    return wine_type_list

def insert_wine_list():
    wine_list = LinkedList()
    for wine_type in types:
        wine_sublist = LinkedList()
        for wine in types:
            if wine[0] == wine_type:
                wine_sublist.insert_beginning(wine)
        wine_list.insert_beginning(wine_sublist)
    return wine_list

types_of_wine = insert_wine_types()
wine_details = insert_wine_list()

def user_choice():
    print("Welcome to Wine Selector, please see our availible varieties of wine: ")
    print(* types, sep=", ")
    user_selection = input("Please type in the variety that you would like to buy ")
    matching_wine = []
    get_list_head = types_of_wine.get_head_node()
    while get_list_head is not None:
        if  str(get_list_head.get_value()).startswith(user_selection):
            matching_wine.append(get_list_head.get_value())
        get_list_head = get_list_head.get_next_node()

    print(matching_wine[0])
    wine_list_head = wine_details.get_head_node()
    while wine_list_head is not None:
        sublist_head = wine_list_head.get_value().get_head_node()
        if sublist_head.get_value()[0] == "merlot":
            while sublist_head.get_next_node() is not None:
                print("_____Summary_____")
                print(f"Winery:  {sublist_head.get_value()[1]}")
                print(f"Region:  {sublist_head.get_value()[2]}")
                print(f"Vintage:  {sublist_head.get_value()[3]}")
                print("_________________\n")
                sublist_head = sublist_head.get_next_node()
        wine_list_head = wine_list_head.get_next_node()


def start_wine_selector():
    insert_wine_types()
    insert_wine_list()
    user_choice()

    

start_wine_selector()