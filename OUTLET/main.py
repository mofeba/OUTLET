from outlet import outlet
def main():
    Outlet=outlet()
    while True:
        print("""
        ====== OUTLET =======
        1. Display available chargers
        2. Add chargers
        3. Book charger
        4. End charging
        5. Exit
        """)
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        if choice==1:
            Outlet.display_chargers()
        elif choice==2:
            charger_number=int(input("what charger number would you like to add?"))
            Outlet.add_chargers(charger_number)
        elif choice==3:
            charging_port=int(input("What charger would you like to use today?"))
            Outlet.book_charger(charging_port)
        elif choice==4:
            Outlet.end_charging()
        elif choice==5:
            break
        else:
            ("Error, input a number between 1-5")
            
if __name__=='__main__':
    main()

            
        