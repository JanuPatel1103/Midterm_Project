import json
import argparse
import re
from collections import defaultdict

def format_phone_number(phone):
    """Ensure phone numbers are formatted as xxx-xxx-xxxx"""
    pattern = r"\d{3}-\d{3}-\d{4}"
    return phone if re.match(pattern, phone) else None

def process_orders(input_file):
    customers = {}
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

            # ❌ Intentional Mistake: Using incorrect dictionary key (causes KeyError)
            if item_name not in items:
                items[item_name]["cost"] = price  # Wrong key "cost" instead of "price"
            items[item_name]["order_count"] += 1  # Wrong key "order_count" instead of "orders"

    # ❌ Intentional Mistake: Wrong file mode ("r" instead of "w")
    with open("customers.json", "r") as cfile:
        json.dump(customers, cfile, indent=4)  # This will cause an error

    # ❌ Intentional Mistake: Forgetting to open the file before writing
    json.dump(items, ifile, indent=4)  # "ifile" is not defined, causes NameError

    print("Processing complete. Files 'customers.json' and 'items.json' have been created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Dosa restaurant orders.")
    parser.add_argument("input_file", help="Path to the JSON orders file")
    args = parser.parse_args()

    process_orders(args.input_file)
