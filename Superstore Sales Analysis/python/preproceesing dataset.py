import pandas as pd

df = pd.read_csv("C:\\Workspace\\Superstore_2\\Data\\Superstore Dataset.csv")

# Check top 5 rows
print(df.head())

# Check dataset info
print(df.info())

# Check summary stats
print(df.describe())

df.columns = df.columns.str.lower().str.replace(" ", "_")
df.drop_duplicates(inplace=True)

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
df.to_csv("C:\\Workspace\\Superstore_2\Data\\processed\\cleaned_superstore dataset.csv", index=False)
print(df.info())

orders = df[[
    'order_id',
    'order_date',
    'customer_id',
    'product_id',
    'sales',
    'quantity',
    'profit'
]]
customers = df[[
    'customer_id',
    'customer_name',
    'segment',
    'region'
]].drop_duplicates()

print(df.columns.tolist())

products = df[[
    'product_id',
    'product_name',
    'category',
    'sub-category'
]].drop_duplicates()


date_table = pd.DataFrame({
    'date': orders['order_date'].unique()
})

date_table['year'] = pd.to_datetime(date_table['date']).dt.year
date_table['month'] = pd.to_datetime(date_table['date']).dt.month
date_table['month_name'] = pd.to_datetime(date_table['date']).dt.month_name()
date_table['quarter'] = pd.to_datetime(date_table['date']).dt.to_period('Q').astype(str)
orders.to_csv("C:\\Workspace\\Superstore_2\\Data\\processed\\Orders.csv", index=False)
customers.to_csv("C:\\Workspace\\Superstore_2\\Data\\processed\\Customers.csv", index=False)
products.to_csv("C:\\Workspace\\Superstore_2\\Data\\processed\\Products.csv", index=False)
date_table.to_csv("C:\\Workspace\\Superstore_2\\Data\\processed\\DateTable.csv", index=False)
