import streamlit as st
import pandas as pd 
import plotly.express as px
import gzip, pickle
import matplotlib.pyplot as plt



pickle_in = open('model.p', 'rb') 
model_load = pickle.load(pickle_in)





Real_data = pd.read_excel("Delhi.xlsx",index_col=[0],parse_dates=[0],skiprows=2)
Eda_data = pd.read_csv("Delhi_EDA.csv",index_col=[0],)


html_temp = """
<h1 style="color:green;text-align:center;">Airqulity(PM2.5) Prediction </h>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)



nav = st.sidebar.selectbox("Pages",["Before EDA","After EDA","Prediction"])



if nav == "None":
    st.write("Delhi airquality Prediction")

if nav == "Before EDA":
    
    if st.sidebar.checkbox("Show Data"):
        st.dataframe(Real_data, width = 600 , height = 200 )
    
    graph = st.sidebar.radio("Graph",["Histogram","Line Plot"])

    if graph == "Histogram":
       fig = px.histogram(Real_data, title = 'PM2.5 histogram', width = 600)
       st.plotly_chart(fig)
    if graph == "Line Plot":
       
        
        fig = px.line(Real_data, title = 'PM2.5 Value On Monthly With Slider', width = 600)

        fig.update_xaxes(
            rangeslider_visible = True)
        st.plotly_chart(fig)
       
    
       
if nav == "After EDA":
    
    if st.sidebar.checkbox("Show Data"):
        st.dataframe(Eda_data, width = 600 , height = 200 )
    
    graph = st.sidebar.selectbox("",["Histogram","Line Plot"])

    if graph == "Histogram":
       fig = px.histogram(Eda_data, title = 'PM2.5 histogram', width = 600)
       st.plotly_chart(fig)
    
    if graph == "Line Plot":
       
        
        fig = px.line(Eda_data , y = 'pm25', title = 'PM2.5 Value On Monthly basis', width = 600)

        fig.update_xaxes(
            rangeslider_visible = True)
            
        st.plotly_chart(fig)

if nav == "Prediction":
    st.header("Forcasting Value")
    val = st.number_input('Enter the Number', min_value = 1, max_value = 60)
    
    prediction = model_load.forecast(val)
    st.write(val,"Hours Of Prediction")
    if st.button("Predict"):
    	
    	st.dataframe((prediction[0]), width = 600 , height = 500 )
        
        
        
        
        
        
        
