# Olist Performance Dashboard

## Introduction
Welcome to the **Olist Performance Dashboard**! This dashboard provides an insightful visualization of the overall performance of the Olist platform. It is designed to help potential sellers evaluate the potential of selling on Olist by showcasing key metrics, sales trends, and product distribution across regions. By using this dashboard, sellers can make informed decisions about joining the Olist platform, assess the growth opportunities, and understand how their products might perform across different regions.

Explore the dashboard here:  https://dashboard-salesperformance.streamlit.app/

---
## Features

### 1. **Key Metrics Overview**
At the top of the dashboard, you’ll find key metrics that provide a quick snapshot of Olist's ecosystem:

- **3,095 Sellers**: The number of active sellers on Olist.
- **73 Item Types**: The variety of products available for sale on the platform.
- **27 Countries**: Olist operates across 27 different countries.
- **4,119 Cities**: The platform reaches customers in over 4,000 cities.
- **4.09 Average Rating**: The platform's average customer satisfaction rating.

---

### 2. **Visualizing Total Transactions & Revenue**
The dashboard includes two key visualizations:

- **Total Transactions per Year**: Displays the number of transactions made on Olist per year.
- **Total Revenue per Year**: Shows the revenue generated by Olist sales over the years.

Both graphs are presented using **line charts** to highlight trends and growth patterns.

---

### 3. **Product Distribution Across Regions**
This section visualizes how products are distributed across different states and cities where customers are purchasing from. It includes the following:

- **State & City Counts**: Displays the number of states and cities where the selected product category is sold.
- **Geographic Distribution**: Uses a map to show the geographic distribution of customers for the selected product category.

You can filter data by **product category** to analyze the performance of specific product types.

---

### 4. **Top 5 Best Performing Products by Transaction**
This visualization provides insights into the **Top 5 Products** by the total number of transactions. It allows you to see which product categories are performing the best in terms of sales volume.

---

### 5. **Delivery Performance: On-Time vs Late**
A pie chart presents the **On-Time vs Late Delivery Performance** for products, showing the percentage of deliveries made on time versus those delayed. This metric is important for understanding the logistical efficiency of the platform and ensuring customer satisfaction.

---

### 6. **Filter Options**
On the sidebar, you can use a **filter** to choose a **Product Category**. Upon selecting a category, you will see:

- The number of states and cities that have purchased products in that category.
- A **map** that visualizes customer distribution based on geolocation.
- **Detailed data tables** that show states and cities where the products are sold.

---

## Technologies Used
This dashboard is built using the following technologies:
- **Streamlit**: For creating the interactive web application.
- **Pandas**: For data manipulation and processing.
- **Plotly**: For creating interactive visualizations like line charts, scatter plots, and pie charts.
- **Matplotlib and Seaborn**: For additional visualizations and styling.

## Conclusion
The **Olist Performance Dashboard** is a valuable tool for anyone considering selling on the Olist platform. It provides insights into the platform’s performance, allowing potential sellers to assess Olist's growth potential, product demand in various regions, and the logistical efficiency of the platform. By exploring the data, sellers can make more informed decisions and better strategize their approach to succeed on Olist

## How to Use
1. **Install Dependencies**  
   If you want to run this application locally, you will need to install the dependencies first. You can use pip to install them:

   ```bash
   pip install -r requirements.txt

2. **Run the Application**  
  After all dependencies are installed, run the application using the following command:

   ```bash
   streamlit run dahsboard.py
