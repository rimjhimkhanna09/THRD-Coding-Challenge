# THRD Coding Challenge - Pricing Engine

This Python script implements an automated pricing engine that adjusts product prices based on inventory levels and sales performance.

## Requirements
- Python 3.x
- pandas

## Input Files
- `products.csv`: Contains product catalog with pricing, cost, and stock information
- `sales.csv`: Contains recent sales data

## Output
- `updated_prices.csv`: Contains SKU, old price, and new price with currency units

## Running the Script
1. Install requirements: `pip install pandas`
2. Place input CSV files in the same directory as the script
3. Run: `python pricing_engine.py`

## Pricing Rules
1. Low Stock, High Demand: +15% if stock < 20 and quantity_sold > 30
2. Dead Stock: -30% if stock > 200 and quantity_sold = 0
3. Overstocked Inventory: -10% if stock > 100 and quantity_sold < 20
4. Minimum Profit: Ensures price is at least 20% above cost
