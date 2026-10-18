def my_function():
    print("Hello from my_function!")

def good_function():
    print("This is a good function!")

def hello_from_downing():
    from datetime import date
    print(f"Hello from Downing! -- {date.today()}")

def daily_greeting():
    from datetime import datetime
    hour = datetime.now().hour
    if hour < 12:
        print("Good morning!")
    elif hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")