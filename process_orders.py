import json
import argparse
import re
from collections import defaultdict

def format_phone_number(phone):
    """Ensure phone numbers are formatted as xxx-xxx-xxxx"""
    pattern = r"\d{3}-\d{3}-\d{4}"
    return phone if re.match(pattern, phone) else None

def process_orders(input_file):

    # Dictionary to store customers {phone_number: customer_name}
    customers = {}

    # Dictionary to store item details {item_name: {"price": price, "orders": count}}
    items = defaultdict(lambda: {"price": 0, "orders": 0})

    with open(input_file, "r") as file:
        orders = json.load(file)

    for order in orders:
        phone = format_phone_number(order["phone"])
        name = order["name"]

        if phone:
            customers[phone] = name  # Store phone and name

        for item in order["items"]:
            item_name = item["name"]
            price = item["price"]

            if item_name not in items:
                items[item_name]["price"] = price
            items[item_name]["orders"] += 1

    # Save customers.json
    with open("customers.json", "w") as cfile:
        json.dump(customers, cfile, indent=4)

    # Save items.json
    with open("items.json", "w") as ifile:
        json.dump(items, ifile, indent=4)

    print("Processing complete. Files 'customers.json' and 'items.json' have been created.")

if __name__ == "__main__":
    # Set up argument parser to accept input JSON file as a command-line argument
    parser = argparse.ArgumentParser(description="Process Dosa restaurant orders.")
    parser.add_argument("input_file", help="Path to the JSON orders file")
    args = parser.parse_args()

    process_orders(args.input_file)
