# ------------------------------------------------------------------------------------- #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# PCoonrad,6.6.2020,Added Product class constructor and attributes
# PCoonrad,6.7.2020,Added Product class properties and methods
# PCoonrad,6.7.2020,Added FileProcessor class save_data_to_file()
# PCoonrad,6.7.2020,Added IO class print_menu()
# PCoonrad,6.8.2020,Added IO class input_menu_choice() and print_current_list_items()
# PCoonrad,6.12..2020,Added FileProcessor class read_data_from_file()
# PCoonrad,6.13.2020,Added method input_new_product_and_price
# PCoonrad,6.13.2020,Added main body of script
# ------------------------------------------------------------------------------------- #
# Data -------------------------------------------------------------------------------- #
# Declare variables and constants
strFileName = 'products.txt'  # The name of the data file
lstOfProductObjects = []  # List of Product Objects

class Product:
    """Stores data about a product:

    constructor:
        __init__(): sets up the initial attribute values (name, price) of a new object
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PCoonrad,6.6.2020,Added constructor and attributes
        PCoonrad,6.7.2020,Added properties and method
    """
    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):  # the initializer sets the initial values for the object
        """ Set name and price of a new object"""
        # -- Attributes --
        try:  # section code that can raise exception
            self.__product_name = str(product_name)  # marking it private so it is hidden and not called directly
            self.__product_price = float(product_price)  # marking it private so it is hidden and not called directly
        except TypeError:  # argument has the wrong type
            print('Invalid type. Please enter a valid type.')  # custom message for the built-in exception
        except Exception as e:  # exception class at the bottom will catch any other non-specific type of error
            print('Something went wrong.')  # custom message for the built-in exception
            print("Python Built-In error message:", (e))  # custom message with Python messages for the built-in exception

    # -- Properties --
    # Product Name
    @property  # Don't use name for this directive
    def product_name(self):  # (getter or accessor) gets the value and does formatting logic
        return str(self.__product_name).title()  # Title case: if user enters lower case, it will set to uppercase

    @product_name.setter  # The name must match the property's name
    def product_name(self, value: str):  # (setter or mutator) sets the value and uses validation logic
        if str(value).isnumeric() == False:  # adding validation logic to check if value is not numeric
            self.__product_name = value  # if value is not numeric then set the value
        else:
            raise Exception("Names cannot be numbers.")  # otherwise raise an error message to say "Names cannot be numbers".

    # Product Price
    @property  # Don't use name for this directive
    def product_price(self):  # (getter or accessor) gets the value and does formatting logic
        return float(self.__product_price)

    @product_price.setter  # The name must match the property's name
    def product_price(self, value: float):  # (setter or mutator) sets the value and uses validation logic
        if float(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Price has to be a number.")

    # -- Methods --
    def __str__(self):  # string method that returns product data to string
        """Built in __str__ converts product price to string"""
        return self.product_name + "," + str(self.product_price)

# -- End of class --

# # Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        PCoonrad,6.7.2020,Added method save_data_to_file
        PCoonrad,6.12.2020,Added method read_data_from_file
    """
    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of products

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of products
        """
        try:
            print("Load data from 'products.txt' file:")
            file = open(strFileName, "r")
            for row in file:
                lstOfProductObjects.append(row.strip())
            print(lstOfProductObjects)
            file.close()
        except FileNotFoundError:
            print('Something went wrong.')  # custom message for the built-in exception
            print("File or file path does not exist.")  # custom message for the built-in exception

    @staticmethod
    def save_data_to_file(file_name,list_of_product_objects):
        """ Writes data from a list of products to a file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) of product data:
        :return: (list) of products
        """
        try:
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(str(row) + "\n")
            file.close()
            print("Data successfully saved to file!")
        except FileNotFoundError:
            print('Something went wrong.')  # custom message for the built-in exception
            print("File or file path does not exist.")  # custom message for the built-in exception

# -- End of class --

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """" Performs Input and Output tasks

    methods:
    print_menu():
    input_menu_choice():
    print_current_list_items(list_of_product_objects: list)
    input_new_product_and_price():

    changelog: (When,Who,What)
        PCoonrad,6.7.2020,Created Class
        PCoonrad,6.7.2020,Added method print_menu
        PCoonrad,6.8.2020,Added method input_menu_choice and print_current_list_items
        PCoonrad,6.13.2020,Added method input_new_product_and_price
    """
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options:
        1) Show current data
        2) Add new product
        3) Save data to file
        4) Exit Program
        ''')
        print()  # Add an extra line for presentation

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from the user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for presentation
        return choice

    @staticmethod
    def print_current_list_items(list_of_product_objects: list):
        """ Show the current list of products
        :param list_of_rows: (list) of rows you want to print to user

        :return: nothing
        """
        print("******* The current List of Products is: *******")
        for row in list_of_product_objects:
            print(row)
        print("************************************************")

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_name_and_price():
        """  Ask user to input new product and price

        :return: np
        """
        try:
            name = str(input("Enter a New Product Name: "))
            price = input("Enter a New Product Price: ")
            np = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return np

#Main Body of Script  ---------------------------------------------------- #
#Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

while (True):
    # Show user a menu of options
    IO.print_menu()

    # Gets user's menu option choice
    strChoice = IO.input_menu_choice()  # Get menu option

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':  # Show current data
        IO.print_current_list_items(lstOfProductObjects)
        continue  # to show the menu

    # Get product name and price from user and add to list
    elif strChoice.strip() == '2':  # Add a new product
         lstOfProductObjects.append(IO.input_new_name_and_price())
         continue  # to show the menu

    # Let user save current data to file
    elif strChoice.strip() == '3':  # Save data to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue

    # Let user Exit Program
    elif strChoice.strip() == '4':
        print("Goodbye!")
    break  # and Exit
