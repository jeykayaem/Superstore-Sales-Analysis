# Superstore Sales Analysis

## 🔍 Project Overview
This project analyzes sales performance using the Superstore dataset.
The goal is to build a clean data model and interactive dashboard to
support business decision-making.
```
Superstore Sales Analysis
├── data/
│   ├── Superstore.csv
│   │
│   └── processed/
│       ├── Orders.csv
│       ├── Customers.csv
│       ├── cleaned_superstore dataset.csv
│       ├── Products.csv
│       └── DateTable.csv
│       └── cleaned_superstore dataset.csv
│
├── python/
│   └── preproceesing dataset.ipy
│
├── powerbi/
│   └── Sales_Dashboard.pbix
│
├── screenshots/
│   ├── data_model.png
│   ├── overview.png
│   ├── customer_segment_insights.png
│   ├── Product_performance.png
│   └── sales_by_geographics.png
│
├── README.md
├── INSTRUCTIONS.md
```

## Tools Used
- Python (Pandas)
- Power BI

## Objective
Analyze retail sales data to identify trends, regional performance, and profitability drivers.

## Key Insights
- Monthly sales trends
- Category-wise performance
- Regional sales analysis
- Profit margin tracking
- West region generated highest sales but lower profit margin
- Technology category was the most profitable
- Several products generated consistent losses

## Skills Demonstrated
- Data cleaning and preprocessing
- Business-focused dashboard creation

# Part 1: Pandas (Data Cleaning)

Use Python for everything Power BI shouldn’t handle.
Tasks
Rename columns
Handle missing values
Fix date formats
Remove duplicates
Export clean CSV

# Part 2: 🧱Power_BI_Dashboard
Designed a Product Performance dashboard page in Power BI highlighting sales vs profit, margin erosion, and loss-making products using advanced DAX.

👉 You will be able to build Dashboard like below <br><br>
👆 [Click Here View Interactive Power BI Dashboard](https://app.powerbi.com/reportEmbed?reportId=64926eaf-d4e9-4147-9950-9e5f1e2d2f5b&autoAuth=true&ctid=7fa5ed4e-af3e-433f-bb13-88714877fd75)

<br><br>
<img src="screenshots\overview.png" alt="Image Description" width="500"><br>
KPIs:
Over the past four years, Superstore generated $2.3 million in revenue but only had a gross profit of $286.41K. The company's average discount stood at 15.6%,with total order of 5K & Total Quantity 38k suggesting that the discounting strategy might have influenced the profit margin.

Sales by Region and state:
The West region boasted the highest revenue, with sales amounting to $715.2K, followed by the East region with sales of $585.01K.The Central region with sales of $560K, and the South with sales of $436K, represented two regions that might have had untapped potential worth exploring.

Sales vs. Profit by Category and Sub-Category:
The Technology category emerged as the leading performer in both sales and profit. Within this category, the Phones sub-category stood out with impressive sales and profit figures. On the other hand, the Furniture category showcased significant sales but had a notably lower profit margin. Within the Furniture category, the Tables displayed decent sales but operated at a loss. Additionally, both Bookcases and Supplies resulted in a negative profit for the company. These observations raise concerns, suggesting potential issues with the cost structure or pricing strategy, especially for the Tables, Bookcases, and Supplies subcategories.

Customer Segments and Preferences
Orders by Customer Segment: The Consumer segment was the largest customer base. Superstore should create tailored marketing campaigns targeting this segment to increase sales. The Corporate and Home Office segments with smaller customer bases, present growth opportunities with focused B2B strategies.
Orders by Shipping Preferences: Most customers preferred Standard Class shipping, indicating that they might prioritize cost savings over faster delivery.

<img src="screenshots\sales_by_geographics.png" width="500">

Top Three Cities by Sales Over Time:
Los Angeles and New York City have consistently led in sales, but while Los Angeles saw a slight decline in 2022, New York City surged. Seattle, on the other hand, experienced a significant rebound in 2022.

Top 10 Cities by Quantity:
New York City and Los Angeles dominate in product quantities across all categories.

Quantity by Sub-Category and State:
Binders, Paper, and Furnishings are consistently popular across California, New York, and Texas

<img src="screenshots\customer_segment_insights.png" alt="Image Description" width="500">

Segment by Sales and Profit Over Time:
Sales across all segments had increased year-over-year, with the Consumer segment leading the growth. The Home Office segment was smaller, yet it showed a significant increase in sales in 2022. Profit trends mirror the sales trends, but it's noteworthy that the Corporate segment's profit in 2022 didn't grow proportionally to its sales.

Ship Mode by Sales and Profit Over Time:
Standard Class remains the dominant shipping mode in terms of sales and profit, However, while sales for Standard Class increased in 2022, its profit decreased. First Class and Second Class have seen substantial growth in 2022.

Top 10 Cities by Orders:
New York City and Los Angeles had the most orders, highlighting their importance to Superstore's overall sales success.

<img src="screenshots\Product_performance.png" alt="Image Description" width="500">

“This page focuses on product performance, comparing sales, profit, and margin to identify products with strong revenue but weak profitability caused by discounting.”

Top Performing Sub-Categories:
Phones, Chairs, and Storage are the top three sub-categories in sales.
Labels, Paper, and Envelopes are the most profitable sub-categories, which indicates that the cost of goods sold was lucrative for those products.

Top Products by Sales & Profit:
"Canon imageCLASS 2200 Advanced Copier" had a good balance of high sales and profit, which indicated it was both popular and profitable.
“This visual highlights the top revenue-driving products, allowing stakeholders to see which products contribute most to sales.”
Profit Margin of 6 products is 50%.

Loss Making Products
Disposable bags,binding covers are making loss to company so need to work on this.