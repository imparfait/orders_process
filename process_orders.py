import pandas as pd

df = pd.read_csv('orders.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['TotalAmount'] = df['Quantity'] * df['Price']
print("=== Початковий DataFrame ===")
print(df)

total_income = df['TotalAmount'].sum()
print(f"\nСумарний дохід магазину: {round(total_income,2)}")

average_total_amount = df['TotalAmount'].mean()
print(f"Середнє значення TotalAmount: {average_total_amount:.2f}")

orders_per_customer = df['Customer'].value_counts()
print("\nКількість замовлень по кожному клієнту:")
print(orders_per_customer.to_string(index=True, header=False))

orders_above_500 = df[df['TotalAmount'] > 500]
print("\nЗамовлення з сумою покупки більше 500:")
print(orders_above_500)

sorted_by_date_desc = df.sort_values(by='OrderDate', ascending=False)
print("\nТаблиця відсортована за OrderDate у зворотньому порядку:")
print(sorted_by_date_desc)

orders_in_range = df[(df['OrderDate'] >= '2023-06-05') & (df['OrderDate'] <= '2023-06-10')]
orders_in_range=orders_in_range.sort_values(by='OrderDate', ascending=True)
print("\nЗамовлення з 5 по 10 червня включно:")
print(orders_in_range)

products_per_category = df.groupby('Category')['Product'].count()
print("\nКількість товарів за кожною категорією:")
print(products_per_category.to_string(index=True, header=False))

sales_per_category = df.groupby('Category')['TotalAmount'].sum()
print("\nСума продажів по кожній категорії:")
print(sales_per_category.to_string(index=True, header=False))

top_customers = df.groupby('Customer')['TotalAmount'].sum().sort_values(ascending=False).head(3)
print("\nТОП-3 клієнти за загальною сумою покупки:")
print(top_customers.to_string(index=True, header=False))

