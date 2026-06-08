from datetime import datetime

width = 70

print("=" * width)
print("CHATBOT".center(width))
print("=" * width)

name = input("Enter your name: ")

print("\nBot: Hi " + name + "! 👋")
print("Bot: Type 'bye' anytime to end the chat.\n")

while True:

    msg = input(f"{name}: ".rjust(width))

    user_msg = msg.lower()

    if user_msg in ["hi", "hello"]:
        print("\nBot: Hello! Nice to meet you.\n")

    elif user_msg == "how are you?":
        print("\nBot: I'm doing well. Thanks for asking!\n")

    elif user_msg == "your name?":
        print("\nBot: I'm a simple chatbot created using Python.\n")

    elif user_msg == "who made you?":
        print("\nBot: Indhu created me for her AI internship project. \n")

    elif user_msg == "what's the time now?":
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"\nBot: Current time is {current_time}\n")

    elif user_msg == "date?":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"\nBot: Today's date is {current_date}\n")

    elif user_msg == "favorite color?":
        print("\nBot: I like blue. \n")

    elif user_msg == "may i know your favorite food?":
        print("\nBot: I don't eat, but biryani sounds amazing. \n")

    elif user_msg == "hobbies?":
        print("\nBot: Chatting with people is my favorite hobby.\n")

    elif user_msg == "thank you":
        print("\nBot: You're welcome! \n")

    elif user_msg == "bye":
        print(f"\nBot: Goodbye {name}! Have a wonderful day. 👋\n")
        break

    else:
        print("\nBot: Sorry, I didn't understand that.\n")