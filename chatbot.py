import random
from datetime import datetime

def welcome():
    print("=" * 50)
    print("          SMART BASIC CHATBOT")
    print("=" * 50)
    name = input("Enter your name: ")
    print(f"\nHello, {name}! Welcome to the chatbot.")
    print("\nYou can ask me:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- who created you")
    print("- python")
    print("- date")
    print("- time")
    print("- motivate me")
    print("- joke")
    print("- calculator")
    print("- bye")
    return name

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print("Result =", num1 + num2)
        elif op == "-":
            print("Result =", num1 - num2)
        elif op == "*":
            print("Result =", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operation.")
    except:
        print("Please enter valid numbers.")

def chatbot():
    name = welcome()

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did Python go to school? To improve its class!",
        "Why was the computer cold? It forgot to close Windows!"
    ]

    quotes = [
        "Success comes to those who never stop learning.",
        "Practice makes progress.",
        "Every expert was once a beginner."
    ]

    while True:
        user = input(f"\n{name}: ").lower()

        if user == "hello":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I am doing great. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: My name is Smart Python ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python as a CodeAlpha Internship project.")

        elif user == "python":
            print("Bot: Python is a simple and powerful programming language.")

        elif user == "date":
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "time":
            print("Bot:", datetime.now().strftime("%I:%M:%S %p"))

        elif user == "motivate me":
            print("Bot:", random.choice(quotes))

        elif user == "joke":
            print("Bot:", random.choice(jokes))

        elif user == "calculator":
            calculator()

        elif user == "bye":
            print(f"Bot: Goodbye {name}! Have a wonderful day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()