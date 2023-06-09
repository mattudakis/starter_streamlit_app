import streamlit as st
import pandas as pd
import plotly.express as px


demo_df = pd.read_csv("demo_dataset.csv")
demo_df = demo_df.drop("Services",axis=1)

column_names = ["HDI index", "GDP per capita", "Life expectancy", "CO2 per capita"]


with st.sidebar:
    st.title("World Demographics")
    
    user_name = st.text_input("Welcome - please enter your name.")
    
    animate_widget = st.checkbox(label = "Animate")
   
    year_widget = st.slider(label = "Year to chart",
                            min_value = 1998,
                            max_value = 2018,
                            disabled = animate_widget)
    
    log_y_widget = st.checkbox(label = "Logarithmic Y-axis")

    log_x_widget = st.checkbox(label = "Logarithmic X-axis")
    
    x_data_widget = st.radio(label = "X-axis data",
                            options = column_names,
                            index = 0)
    
    y_data_widget = st.radio(label = "Y-axis data",
                            options = column_names, 
                            index = 3)
    

column1, column2 = st.columns([3, 1])


with column1:
    st.info("Welcome to the global demographic data explorer app.")
    
with column2:
    if user_name:
        st.info(f"Hi {user_name}!")
    

tab1, tab2 = st.tabs(["Data", "Visualisation"])


with tab1:
    st.dataframe(demo_df)


if animate_widget:
    chart = px.scatter(data_frame = demo_df,
                        x = x_data_widget,
                        y = y_data_widget,
                        log_y = log_y_widget,
                        color = "Continent",
                        size = "CO2 per capita",
                        hover_name = "Country",
                        animation_frame = "Year",
                        animation_group = "Country")
    
else:
    chart = px.scatter(data_frame = demo_df[demo_df["Year"] == year_widget],
                        x = x_data_widget,
                        y = y_data_widget,
                        log_y = log_y_widget,
                        color = "Continent",
                        size = "CO2 per capita",
                        hover_name = "Country")


with tab2:
    st.plotly_chart(chart)
