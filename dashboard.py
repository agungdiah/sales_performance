import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Header
st.markdown(
    "<h1 style='text-align: center; color: #1f77b4; font-size: 3rem; font-weight: bold;'>Olist Performance Dashboard</h1>", 
    unsafe_allow_html=True
)

# Tagline
st.markdown(
    "<p style='text-align: center; color: #87CEEB; font-size: 1rem; font-style: italic;'>Reach More Buyers! Start Selling on Olist and Achieve Your Business Success</p>", 
    unsafe_allow_html=True
)

# CSS styling for border around metrics and smaller font size for labels
metric_style = """
    <style>
    .metric-box {
        border: 2px solid #1f77b4;
        padding: 20px;
        border-radius: 8px;
        background-color: #ffffff;
        text-align: center;
        font-size: 1.5rem;
        color: #1f77b4;  /* Set the text color to blue (same as header) */
    }
    .metric-label {
        font-size: 0.63rem;  /* Make the label font size smaller */
        text-align: center;
        color: #1f77b4;
    }
    </style>
"""

st.markdown(metric_style, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(f'<div class="metric-box"><div><b>3.095</b></div><div class="metric-label">No. of Sellers</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-box"><div><b>73</b></div><div class="metric-label">Item Types</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-box"><div><b>27</b></div><div class="metric-label">No. Country State</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="metric-box"><div><b>4.119</b></div><div class="metric-label">No. Country City</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown(f'<div class="metric-box"><div><b>4,09</b></div><div class="metric-label">Average Rating</div></div>', unsafe_allow_html=True)

# "Visualization of Total Transactions and Total Revenue"
file_path_total_revenue = "https://raw.githubusercontent.com/agungdiah/sales_performance/master/Dataset/total_revenue_per_year.csv"
revenue_data = pd.read_csv(file_path_total_revenue)

file_path_total_transaction = "https://raw.githubusercontent.com/agungdiah/sales_performance/master/Dataset/total_transactions_per_year.csv"
transaction_data = pd.read_csv(file_path_total_transaction)

col1, col2 = st.columns(2)
with col1:
    #total transactions per year
    fig1 = px.line(transaction_data, 
                   x='purchase_year', 
                   y='order_id', 
                   title='Total Transactions Per Year', 
                   labels={'purchase_year': 'Year', 'order_id': 'Total Transactions'},
                   markers=True)
    fig1.update_layout(
    plot_bgcolor="#0e1117", 
    paper_bgcolor="#0e1117",
    font=dict(size=14, color="white"),
    title_font=dict(size=20),
    margin=dict(b=50),
    xaxis=dict(
            tickmode='array',  
            tickvals=transaction_data['purchase_year'] 
    )
    #xaxis=dict(showgrid=False),
    #yaxis=dict(showgrid=False),
    )
    st.plotly_chart(fig1, use_container_width=True) #biar ada di kolom daerahnya

with col2:
    # total revenue per year
    fig2 = px.line(revenue_data, 
                   x='delivery_year', 
                   y='payment_value', 
                   title='Total Revenue Per Year', 
                   labels={'delivery_year': 'Year', 'payment_value': 'Total Payment Value'},
                   markers=True)
    fig2.update_layout(
    plot_bgcolor="#0e1117", 
    paper_bgcolor="#0e1117",
    font=dict(size=14, color="white"),
    title_font=dict(size=20),
    margin=dict(b=50),
    xaxis=dict(
            tickmode='array',  
            tickvals=revenue_data['delivery_year'] 
    )
    #xaxis=dict(showgrid=False),
    #yaxis=dict(showgrid=False),
    )
    st.plotly_chart(fig2, use_container_width=True) 

# "Product Category Distribution Across States and Cities Visualization"
file_path_product_sales_by_region = "https://raw.githubusercontent.com/agungdiah/sales_performance/master/Dataset/product_sales_by_region.csv"
product_sales_by_region = pd.read_csv(file_path_product_sales_by_region)

# Filter setup
st.sidebar.markdown(
    "<h2 style='text-align: left; color: #1f77b4;'>🔍 Filter Options</h2>",
    unsafe_allow_html=True,
)

filtered_categories = product_sales_by_region['product_category_name_english'].unique()
filtered_categories = [category for category in filtered_categories if category != 'Unknown']

def format_category_name(category):
    formatted = category.replace('_', ' ').title()  
    return formatted.replace(" And ", " and ")
category_mapping = {category: format_category_name(category) for category in filtered_categories}
reverse_category_mapping = {v: k for k, v in category_mapping.items()}
sorted_categories_cleaned = sorted(category_mapping.values())
product_filter_cleaned = st.sidebar.selectbox(
    'Select a Product Category',
    options=sorted_categories_cleaned,
)
product_filter = reverse_category_mapping[product_filter_cleaned]

# Filter data
filtered_data = product_sales_by_region[
    product_sales_by_region['product_category_name_english'] == product_filter
]
product_filter_title = product_filter_cleaned  


state_count = filtered_data['customer_state'].nunique()
city_count = filtered_data['customer_city'].nunique()
state_list = filtered_data['customer_state'].unique()
city_list = filtered_data['customer_city'].unique()
state_city_data = filtered_data[['customer_state', 'customer_city']].drop_duplicates()
state_city_data.columns = ['State', 'City']
state_city_data = state_city_data.sort_values(by=['State', 'City']).reset_index(drop=True)

geolokasfig = px.scatter_geo(
    filtered_data,
    lat='geolocation_lat',
    lon='geolocation_lng',
    color='customer_state',
    hover_name='customer_city',
    title=f"Customer Distribution for {product_filter_title} Product",  # Judul tanpa underscore dan dengan huruf kapital
    labels={'customer_state': 'State', 'customer_city': 'City'},
    template="plotly_dark"
)
geolokasfig.update_geos(showland=True, landcolor='lightgray', visible=True)
geolokasfig.update_layout(
    title_font=dict(size=20),  
    title_x=0,  
    title_y=0.95,  
    margin=dict(t=40, b=20) 
)
st.plotly_chart(geolokasfig, use_container_width=True)

# Menampilkan informasi tambahan
st.markdown("<h5 style='text-align: left; font-size: 17px; margin-top: -50px;'>Additional Information</h5>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 15px; color: rgba(128, 128, 128, 1); margin-top: -35px;'>- <strong>{product_filter_title} has been purchased by customers in <span style='font-weight: bold;'>{state_count}</span> states</strong></p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 15px; color: rgba(128, 128, 128, 1); margin-top: -20px;'>- <strong>{product_filter_title} has been purchased by customers in <span style='font-weight: bold;'>{city_count}</span> cities</strong></p>", unsafe_allow_html=True)
if st.button("Show Detailed Information"):
    st.write("### State and City Table")
    st.dataframe(state_city_data)


col5, col6 = st.columns(2)
# Top 5 Best Performing Products by Transaction
file_path_top_5_products = "https://raw.githubusercontent.com/agungdiah/sales_performance/master/Dataset/top_5_products.csv"
top_5_products = pd.read_csv(file_path_top_5_products)
top_5_products['product_category_name_english'] = top_5_products['product_category_name_english'].str.replace('_', ' ')

# Performance of Deliveries: On-Time vs Late
file_path_performa_logistik = "https://raw.githubusercontent.com/agungdiah/sales_performance/master/Dataset/performa_logistik1.csv"
performa_logistik = pd.read_csv(file_path_performa_logistik)
performa_logistik['status'] = performa_logistik['status'].replace({
    'Tepat Waktu': 'On Time',
    'Terlambat': 'Late'
})

with col5:
    fig_top = px.bar(
        top_5_products, 
        x="total order",  
        y="product_category_name_english",  
        title="Top 5 Products by Transactions",  
        labels={"product_category_name_english": "Product Category", "total order": "Total Transactions"},
        color="product_category_name_english",  
        orientation="h",  
        template="plotly_dark"  
    )
    fig_top.update_layout(
        plot_bgcolor="#0e1117",  
        paper_bgcolor="#0e1117", 
        font=dict(size=12, color="white"),  
        title_font=dict(size=20), 
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False), 
        showlegend=False,  
    )
    st.plotly_chart(fig_top, use_container_width=True)

with col6:
    fig_pie = px.pie(
    performa_logistik,
    names='status',
    values='jumlah',
    title="Performance of Deliveries",
    color='status',
    color_discrete_map={'On Time': 'green', 'Late': 'red'}
    )
    fig_pie.update_traces(
    textinfo='percent+label',  
    pull=[0.1, 0] 
    )
    fig_pie.update_layout(
    title_font=dict(size=20),
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
    #margin=dict(t=40, b=20),
    height = 400
    )
    st.plotly_chart(fig_pie, use_container_width=True)
