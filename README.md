# Midterm Project - Dosa Restaurant Orders Processing

## Project Overview
This project processes order data from a dosa restaurant to generate:
1. `customers.json`: A mapping of phone numbers to customer names.
2. `items.json`: A summary of items ordered with price and order count.
This helps the restaurant owner analyze customer data and track the popularity of different dosas.

## Installation
Requires Python 3.

## How It Works
1. Reads orders from example_orders.json.
2. Extracts unique customers and their phone numbers.
3. Aggregates item data, tracking price and order count.
4. Saves results to customers.json and items.json.

## Usage
Run the script with:
```bash
python process_orders.py example_orders.json

