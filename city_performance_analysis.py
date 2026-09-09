import streamlit  as st
# import plotly.express as px
# import altair as alt
# st.write("Altair Loaded Successfully")
st.title("City Performnace Analysis 📊")

try:

    # connection to the snowflake 
    con=st.connection('snowflake')
    session=con.session()
    # booking table information to dataframe 
    booking_df=session.sql('select * from hotel_db.public.GOLD_BOOKING_CLEAN;').to_pandas()
    city_df=session.sql('select distinct HOTEL_CITY from hotel_db.public.GOLD_BOOKING_CLEAN order by HOTEL_CITY ; ').to_pandas()
    city = st.selectbox(
    "Select a city",
     city_df['HOTEL_CITY'].tolist()
       )
    hotel_id_df=session.sql('select distinct HOTEL_ID, HOTEL_CITY from hotel_db.public.GOLD_BOOKING_CLEAN order by HOTEL_CITY; ').to_pandas()
    hotel=st.selectbox(
     'Select a hotel',
     hotel_id_df['HOTEL_ID'].tolist()
      )
     # filtering the data with hotel city and hotel id
    filtered_df = booking_df[(booking_df["HOTEL_CITY"] == city) & (booking_df["HOTEL_ID"] == hotel)]
    col1,col2,col3=st.columns(3)
    col1.metric('Booking', len(filtered_df))
    col2.metric('Revenue',round( filtered_df['TOTAL_AMOUNT'].sum(),2) )
    col3.metric("Avg Revenue",round(filtered_df["TOTAL_AMOUNT"].mean(),2)) # round to 2 places 
    st.header('Hotel Revenue ')
    hotel_revenue = filtered_df.groupby("HOTEL_ID")['TOTAL_AMOUNT'].sum().reset_index()
    st.bar_chart(hotel_revenue, x="HOTEL_ID",y='TOTAL_AMOUNT')


    top_5_hotel=session.sql('select * from  hotel_db.public.GOLD_BOOKING_CLEAN order by TOTAL_AMOUNT limit 5').to_pandas()
    st.write(top_5_hotel)
    st.bar_chart(top_5_hotel ,x="HOTEL_ID",y="TOTAL_AMOUNT")
    st.dataframe(top_5_hotel)
#     fig = px.pie(
#         top_5_hotel,
#         values="TOTAL_AMOUNT",
#         names="HOTEL_ID",
#         title="Top 5 Hotels Revenue Distribution"
# )

  
    # st.write('fiter data ', filtered_df)
     

    # st.write("Selected City:", hotel_id_df)
    
    
except Exception as error :
     st.error("Unable to connect to Snowflake or read the table.")
     st.exception(error)
    
    
