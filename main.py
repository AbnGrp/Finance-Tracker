import csv
import os
from datetime import datetime

CATEGORIES = ["Food", "Transport", "Cleaning", "Rent", "Entertainment", "Higine", "Health", "Training", "Other"]
CARDS = ["Banamex Credit", "Banamex Debit", "Hey Credit", "Hey Debit", "BBVA Credit", "BBVA Debit", "Nu Credit", "Nu Debit", "Cash"]

def get_float_input(amount):
    while True:
        try:
            return float(input(amount))
        except ValueError:
            print("Please enter a valid number. ")

def get_datetime_input():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    user_input = input(f'Date and time (press Enter for now: {now})')
    return user_input if user_input.strip() else now

def save_expense(date_time, amount, category, card, description, currency):
    file_exists = os.path.isfile("expenses.csv")
    with open("expenses.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date_time", "amount", "category", "card", "description", "currency"])
        writer.writerow([date_time, amount, category, card, description, currency])

def main():
    print("---Expense Tracker---")
    while True:
        date_time = get_datetime_input()
        amount = get_float_input("Amount: ")

        print("Categories: ", ", ".join(f"{i+1}) {c}" for i, c in enumerate(CATEGORIES)))
        category = CATEGORIES[int(input("Choose a category number: ")) - 1]

        print("Cards: ", ", ".join(f"{i+1}) {c}" for i, c in enumerate(CARDS)))
        card = CARDS[int(input("Choose a card: ")) - 1]

        description = input("Description (optional)")
        currency = input("Currency (e.g. USD, MXN): ") or "MXN"

        save_expense(date_time, amount, category, card, description, currency)
        print("Saved\n")

        again = input("Add another expense? (y/n): ").lower()
        if again != "y":
            break

if __name__=="__main__":
    main()
              