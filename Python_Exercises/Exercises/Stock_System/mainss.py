from StockSystem import StockSystem
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"
if __name__ == "__main__":
    # create stock system object
    ss = StockSystem()
    while True:
        print("**** WELCOME TO STOCKSYSTEM! **** ")
        print("********************************* ")
        print(f"To display all products press {BLUE}'1'{RESET}")
        print(f"To enter new product press {BLUE}'2'{RESET}")
        print(f"To exit the main menu press {BLUE}'0'{RESET}")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            ss.display_all_products()
        elif user_choice == "2":
            ss.add_new_product()
        elif user_choice =="0":
            exit() #can use the word break
            
