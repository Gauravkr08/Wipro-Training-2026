import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
print("Sales Data:")
print(df)

df["Total"] = df["Quantity"] * df["Price"]
print("\nData with Total Column:")
print(df)

total_sales = np.sum(df["Total"])
average_daily_sales = np.mean(df["Total"])
std_daily_sales = np.std(df["Total"])

print("\nSales Statistics:")
print(f"Total Sales: {total_sales}")
print(f"Average Daily Sales: {average_daily_sales:.2f}")
print(f"Standard Deviation of Daily Sales: {std_daily_sales:.2f}")

product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()
total_quantity_sold = product_sales.max()

print(f"\nBest-Selling Product: {best_selling_product} (Total Quantity Sold: {total_quantity_sold})")

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(df["Date"], df["Total"], color='skyblue')
plt.title("Daily Sales Total")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.subplot(1,2,2)
plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=140, colors=['orange','green','skyblue'])
plt.title("Total Quantity Sold by Product")

plt.tight_layout()
plt.show()
