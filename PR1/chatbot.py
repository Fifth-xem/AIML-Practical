def chatbot():
    print("=== Welcome to AI Chatbot ===")

    while True:
        print("\nMain Menu")
        print("1. Greetings")
        print("2. Student Information")
        print("3. College Information")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Main Menu
        if choice == "1":
            while True:
                print("\n--- Greetings Menu ---")
                print("1. Hello")
                print("2. How are you?")
                print("3. Your Name")
                print("4. Back to Main Menu")

                sub = input("Choose: ")

                if sub == "1":
                    print("Bot: Hello! Nice to meet you.")

                elif sub == "2":
                    print("Bot: I am doing great!")

                elif sub == "3":
                    print("Bot: I am an AI Chatbot.")

                elif sub == "4":
                    break

                else:
                    print("Invalid Choice!")

        elif choice == "2":
            while True:
                print("\n--- Student Menu ---")
                print("1. Attendance")
                print("2. Marks")
                print("3. Fees")
                print("4. Back")

                sub = input("Choose: ")

                if sub == "1":
                    print("Bot: Your attendance is 92%.")

                elif sub == "2":
                    print("Bot: Your marks are 85%.")

                elif sub == "3":
                    print("Bot: Your fees are paid.")

                elif sub == "4":
                    break

                else:
                    print("Invalid Choice!")

        elif choice == "3":
            while True:
                print("\n--- College Menu ---")
                print("1. Courses")
                print("2. Faculty")
                print("3. Library")
                print("4. Back")

                sub = input("Choose: ")

                if sub == "1":
                    print("Bot: We offer B.Tech, BCA, MBA, MCA.")

                elif sub == "2":
                    print("Bot: We have experienced faculty.")

                elif sub == "3":
                    print("Bot: Library is open from 9 AM to 6 PM.")

                elif sub == "4":
                    break

                else:
                    print("Invalid Choice!")

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid Main Menu Choice!")

chatbot()
