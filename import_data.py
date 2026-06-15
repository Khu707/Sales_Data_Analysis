
from matplotlib import lines
from matplotlib import lines
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# print("Libraries imported successfully")


df = pd.read_csv('Sample-Superstore.csv')
df.head()


# print("Total Rows:", df.shape[0])
# df.info()
# df.isnull().sum()




# # Cell 5: Analysis - 
# region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
# print("Sales by Region:")
# print(region_sales)

# top_products=df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(5)
# print(top_products)

# Q4: Which Category has highest loss? – FILTER + GROUP BY
# loss_category = df[df['Profit'] < 0].groupby('Category')['Profit'].sum().sort_values()
# print(loss_category)

# # Q5: Average discount by Segment – AGG
# avg_discount = df.groupby('Segment')['Discount'].mean()
# print(avg_discount)


# # Cell 6:1- Bar Chart
# region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
# plt.figure(figsize=(8,5))
# region_sales.plot(kind='bar', color='blue')
# plt.title('Total Sales by Region - Analysis')
# plt.ylabel('Sales')
# plt.tight_layout()
# plt.show()


# 2 nd bar chart
top_products=df.groupby("Segment")["Profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(7,5))
top_products.plot(kind='bar', color='green')
plt.title('Top Products - Analysis')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()


#2 Line Chart
# State_quantity = df.groupby('State')['Quantity'].sum().sort_values(ascending=False)
# plt.figure(figsize=(10,5))
# State_quantity.plot(kind='line', marker='o', color='green')
# plt.title('State-wise Quantity Distribution - Analysis')
# plt.ylabel('Quantity')
# plt.grid(True)
# plt.show()



# Chart 3: Pie Chart – Sales by Category    
# category_sales = df.groupby('Category')['Sales'].sum()
# plt.figure(figsize=(6,6))
# category_sales.plot(kind='pie', autopct='%1.1f%%')
# plt.title('Sales Distribution by Category')
# plt.ylabel('')
# plt.show()




# # Cell 10: Save cleaned data + summary
# region_sales.to_csv('Region_Wise_Sales.csv')
# top_products.to_excel('Top5_Profitable_Products.xlsx')

# print("Project Complete. Files saved.")
