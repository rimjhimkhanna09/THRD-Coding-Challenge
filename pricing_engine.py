import pandas as pd
import numpy as np

def load_data():
    """Load and prepare the input data."""
    products_df = pd.read_csv('products.csv')
    sales_df = pd.read_csv('sales.csv')
    
    # Merge sales data with products
    merged_df = products_df.merge(
        sales_df[['sku', 'quantity_sold']], 
        on='sku', 
        how='left'
    )
    
    # Fill NaN values in quantity_sold with 0
    merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)
    return merged_df

def apply_pricing_rules(row):
    """Apply pricing rules to a single product."""
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    
    # Rule 1: Low Stock, High Demand
    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    
    # Rule 2: Dead Stock
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.70
    
    # Rule 3: Overstocked Inventory
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.90
    
    # If no rules apply, keep current price
    else:
        new_price = current_price
    
    # Rule 4: Minimum Profit Constraint (Always Applied)
    min_price = cost_price * 1.2
    new_price = max(new_price, min_price)
    
    # Round to 2 decimal places
    return round(new_price, 2)

def main():
    # Load and process data
    df = load_data()
    
    # Store old prices
    df['old_price'] = df['current_price'].apply(lambda x: f"${x:.2f}")
    
    # Apply pricing rules
    df['new_price'] = df.apply(apply_pricing_rules, axis=1)
    df['new_price'] = df['new_price'].apply(lambda x: f"${x:.2f}")
    
    # Create output dataframe
    output_df = df[['sku', 'old_price', 'new_price']]
    
    # Save to CSV
    output_df.to_csv('updated_prices.csv', index=False)
    print("Updated prices have been saved to 'updated_prices.csv'")

if __name__ == "__main__":
    main()
