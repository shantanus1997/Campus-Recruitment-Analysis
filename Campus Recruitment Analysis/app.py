import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

st.title("Campus Recruitment Analysis")
st.sidebar.header("options")


@st.cache
def load_data():
    df = pd.read_csv('dataset/Placement_Data_Full_Class.csv')
    return df


genre = st.sidebar.radio("",('About Project', 'View Dataset', 'Graph Analysis'))


if genre == "About Project":
    st.info('''A college campus recruitment system that consists of a student login, company login and an admin login. The project is beneficial for college students, various companies visiting the campus for recruitment and even the college placement officer. The software system allows the students to create their profiles and upload all their details including their marks onto the system. The admin can check each student details and can remove faulty accounts. The system also consists of a company login where various companies visiting the college can view a list of students in that college and also their respective resumes. The software system allows students to view a list of companies who have posted for vacancy. The admin has overall rights over the system and can moderate and delete any details not pertaining to college placement rules. The system handles student as well as company data and efficiently displays all this data to respective sides. 
    pass''')



if  genre == "View Dataset":
    df = load_data()
    st.dataframe(df)
   

if genre == "Graph Analysis":
    df = load_data()

    choice = st.sidebar.selectbox("Select any one",("Gender Ratio","Placed and Unplaced","Degree_T and salary","degree_t and status"))

    if choice == "Gender Ratio":
        gender_ratio = df["gender"].value_counts()
        fig = px.pie(df,values=gender_ratio,names=df["gender"].unique(),title="Gender Ratio:Male vs Female")
        st.plotly_chart(fig)

    if choice == "Placed and Unplaced":
        fig,ax = plt.subplots(figsize=(12,6))
        fig = px.bar(df, x="gender",color="status")
        st.plotly_chart(fig)

    if choice == "Degree_T and salary":
        fig,ax = plt.subplots(figsize=(12,6))
        df.plot.scatter(x='degree_t',y='salary',title='Degrre_T and salary',c='salary',cmap='rainbow',ax=ax)
        st.pyplot(fig)

    if choice == "degree_t and status":
        df_copy = df.copy()
        fig = px.box(df, y="ssc_p",x="status",color = "status")
        st.plotly_chart(fig)
