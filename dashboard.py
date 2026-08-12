import streamlit as st
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Retail Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# 2. MYSQL DATABASE CONNECTION
# ==========================================

DB_USER = "root"
DB_PASSWORD = "3306"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "sales_analysis"

engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# ==========================================
# 3. LOAD DATA
# ==========================================

query = """
SELECT *
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)


# ==========================================
# 4. DATA PREPARATION
# ==========================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Year"] = df["Order_Date"].dt.year

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)


# ==========================================
# 5. TITLE
# ==========================================

st.title("📊 Retail Sales Intelligence Dashboard")

st.write(
    "Interactive analysis of sales, profit, customers, products and regional performance."
)


# ==========================================
# 6. SIDEBAR FILTERS
# ==========================================

st.sidebar.header("Filters")

years = sorted(df["Year"].dropna().unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

categories = sorted(df["Category"].dropna().unique())

selected_category = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)


# ==========================================
# 7. APPLY FILTERS
# ==========================================

filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Category"].isin(selected_category))
]


# ==========================================
# 8. KPI CALCULATIONS
# ==========================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_quantity = filtered_df["Quantity"].sum()

average_sales = filtered_df["Sales"].mean()


# ==========================================
# 9. DISPLAY KPIs
# ==========================================

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col5.metric(
    "Quantity Sold",
    f"{total_quantity:,}"
)

col6.metric(
    "Average Sales",
    f"${average_sales:,.2f}"
)


st.divider()


# ==========================================
# 10. SALES BY CATEGORY
# ==========================================

st.subheader("Sales by Category")

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots()

category_sales.plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel("Category")
ax1.set_ylabel("Sales")
ax1.set_title("Sales by Category")

plt.xticks(rotation=0)

st.pyplot(fig1)


# ==========================================
# 11. SALES BY REGION
# ==========================================

st.subheader("Sales by Region")

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots()

region_sales.plot(
    kind="bar",
    ax=ax2
)

ax2.set_xlabel("Region")
ax2.set_ylabel("Sales")
ax2.set_title("Sales by Region")

plt.xticks(rotation=45)

st.pyplot(fig2)


# ==========================================
# 12. PROFIT BY CATEGORY
# ==========================================

st.subheader("Profit by Category")

category_profit = (
    filtered_df
    .groupby("Category")["Profit"]
    .sum()
)

fig3, ax3 = plt.subplots()

category_profit.plot(
    kind="bar",
    ax=ax3
)

ax3.set_xlabel("Category")
ax3.set_ylabel("Profit")
ax3.set_title("Profit by Category")

plt.xticks(rotation=0)

st.pyplot(fig3)


# ==========================================
# 13. MONTHLY SALES TREND
# ==========================================

st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby("Month")["Sales"]
    .sum()
)

fig4, ax4 = plt.subplots()

monthly_sales.plot(
    kind="line",
    marker="o",
    ax=ax4
)

ax4.set_xlabel("Month")
ax4.set_ylabel("Sales")
ax4.set_title("Monthly Sales Trend")

plt.xticks(rotation=45)

st.pyplot(fig4)


# ==========================================
# 14. SALES BY SEGMENT
# ==========================================

st.subheader("Sales by Customer Segment")

segment_sales = (
    filtered_df
    .groupby("Segment")["Sales"]
    .sum()
)

fig5, ax5 = plt.subplots()

segment_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax5
)

ax5.set_ylabel("")

st.pyplot(fig5)


# ==========================================
# 15. TOP 10 CUSTOMERS
# ==========================================

st.subheader("Top 10 Customers by Sales")

top_customers = (
    filtered_df
    .groupby("Customer_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    top_customers.reset_index(),
    use_container_width=True
)


# ==========================================
# 16. TOP 10 PRODUCTS
# ==========================================

st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df
    .groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    top_products.reset_index(),
    use_container_width=True
)


# ==========================================
# 17. DATA SUMMARY
# ==========================================

st.divider()

st.subheader("Filtered Dataset")

st.write(
    f"Showing {len(filtered_df):,} records after applying the selected filters."
)

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)