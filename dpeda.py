import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Extensive analysis of our available products")

# Function to load data and create visualizations
def load_and_visualize_data_appliances():
    # Load data
    data = pd.read_csv('appliances.csv')

    # Scatter plot
    st.write("## Brand vs Price")
    fig_scatter = px.scatter(data, x='appliances_type', y='price', title='Scatter Plot')
    st.plotly_chart(fig_scatter)

    # Bar chart
    st.write("## Typical review rating for different appliances type")
    fig_bar = px.bar(data, x='appliances_brand', y='customer_review_rating', title='Bar Chart')
    st.plotly_chart(fig_bar)

    # Pie chart
    st.write("## Overall Review of Brands")
    fig_pie = px.histogram(data, x='appliances_brand', y='customer_review_rating', title='Pie Chart')
    st.plotly_chart(fig_pie)
    
    
    

# Title of the web app
def load_and_visualize_data_car():
    # Load data
    data = pd.read_csv('car.csv')

    # Scatter plot
    st.write("## Car Companies and Price")
    fig_scatter = px.scatter(data, x='car_company', y='price', title='Scatter Plot')
    st.plotly_chart(fig_scatter)

    # Bar chart
    st.write("## Mileages according to car companies\n")
    fig_bar = px.bar(data, x='car_company', y='mileage', title='Bar Chart')
    st.plotly_chart(fig_bar)

    # Pie chart
    st.write("## Usage")
    fig_pie = px.pie(data, names='km_covered', values='years_used', title='Pie Chart')
    st.plotly_chart(fig_pie)
    
    
def load_and_visualize_data_cloth():
    # Load data
    data = pd.read_csv('cloth.csv')

    # Scatter plot
    st.write("## Scatter Plot")
    fig_scatter = px.scatter(data, x='cloth_material', y='price', title='Scatter Plot')
    st.plotly_chart(fig_scatter)

    # Bar chart
    st.write("## Bar Chart")
    fig_bar = px.bar(data, x='cloth_type', y='price', title='Bar Chart')
    st.plotly_chart(fig_bar)

    # Pie chart
    st.write("## Pie Chart")
    fig_pie = px.pie(data, names='cloth_material', values='price', title='Pie Chart')
    st.plotly_chart(fig_pie)
    
def load_and_visualize_data_shoe_and_bag():
    # Load data
    data = pd.read_csv('shoe_and_bag.csv')

    # Scatter plot
    st.write("## Scatter Plot")
    fig_scatter = px.scatter(data, x='sb_type', y='price', title='Scatter Plot')
    st.plotly_chart(fig_scatter)

    # Bar chart
    st.write("## Bar Chart")
    fig_bar = px.bar(data, x='sb_brand', y='price', title='Bar Chart')
    st.plotly_chart(fig_bar)

    # Pie chart
    st.write("## Pie Chart")
    fig_pie = px.pie(data, names='sb_brand', values='customer_review_rating', title='Pie Chart')
    st.plotly_chart(fig_pie)
    
def load_and_visualize_data_vehicle():
    # Load data
    data = pd.read_csv('vehicle.csv')

    # Scatter plot
    st.write("## Scatter Plot")
    fig_scatter = px.scatter(data, x='vehicle_model', y='price', title='Scatter Plot')
    st.plotly_chart(fig_scatter)
    
    st.write("## Scatter Plot")
    fig2_scatter = px.scatter(data, x='mileage', y='price', title='Scatter Plot')
    st.plotly_chart(fig2_scatter)

    # Bar chart
    st.write("## Bar Chart")
    fig_bar = px.bar(data, x='vehicle_company', y='price', title='Bar Chart')
    st.plotly_chart(fig_bar)

    # Pie chart
    st.write("## Pie Chart")
    fig_pie = px.pie(data, names='vehicle_name', values='mileage', title='Pie Chart')
    st.plotly_chart(fig_pie)
    
    st.write("## Bar Chart")
    fig1_bar = px.bar(data, x='vehicle_name', y='price', title='Bar Chart')
    st.plotly_chart(fig1_bar)






# Sidebar selection box for choosing category
selected_category = st.sidebar.selectbox('Select a category', ['appliances', 'clothes', 'shoes and bags', 'cars', 'Vehicles'], key='category_selector')

# Display different visualizations based on selected category
if selected_category == 'appliances':
    load_and_visualize_data_appliances()
elif selected_category == 'cars':
    load_and_visualize_data_car()
elif selected_category == 'clothes':
    load_and_visualize_data_cloth()
elif selected_category == 'shoes and bags':
    load_and_visualize_data_shoe_and_bag()
elif selected_category == 'Vehicles':
    load_and_visualize_data_vehicle()

