# Import python packages
import streamlit as st
import os

dashboard=st.Page('Dashboard.py',title='Executive Dashboard' , icon='📊')
City_Performance_Analysis=st.Page("City_Performance_Analysis.py", title="City Performance Analysis", icon="📊")
Booking_Trends=st.Page('Booking_Trends.py',title="Booking Trends", icon='📁')
Booking_Details_Explorer=st.Page('Booking_Details_Explorer.py',title='Booking Details Explorer' ,icon='🌎')
# Set up navigation
pg = st.navigation([dashboard,City_Performance_Analysis, Booking_Trends, Booking_Details_Explorer])
# Run the selected page
pg.run()


# try:

#   st.header("Executive Dashboard")
#   con=st.connection('snowflake')
#   session=con.session()
#   # total booking 
#   total_booking=session.sql('select count(*) from  hotel_db.public.GOLD_BOOKING_CLEAN ').to_pandas().iloc[0,0]
#   # total revenue 
#   total_revenue=session.sql('select sum(total_revenue) as total_revenue from hotel_db.public.GOLD_AGG_HOTEL_CITY_SALES  ').to_pandas().iloc[0,0]
#   # totral cities 
#   total_cities=session.sql('select COUNT(HOTEL_CITY)  from hotel_db.public.GOLD_AGG_HOTEL_CITY_SALES ').to_pandas().iloc[0,0]
#   # top performing 
#   top_performing = session.sql("""
# SELECT HOTEL_CITY, TOTAL_REVENUE
# FROM HOTEL_DB.PUBLIC.GOLD_AGG_HOTEL_CITY_SALES
# ORDER BY TOTAL_REVENUE DESC
# LIMIT 1
# """).to_pandas().iloc[0,0]

#   col1,col2,col3,col4=st.columns(4)
#   # st.write("dhjfjkshdjhfjsdhjfhjkdfkjhskfhkjsdkfh",st.columns(4))
#   col1.metric("Bookings", total_booking)
#   col2.metric("Revenue", total_revenue)
#   col3.metric("Cities", total_cities)
#   col4.metric("Avg Booking", top_performing)

#   #  charts display 
#   hotel_cities_wise_revenue=session.sql('select *  from hotel_db.public.GOLD_AGG_HOTEL_CITY_SALES ').to_pandas()
#   hotel_Daily_Booking_Trend=session.sql('select *  from hotel_db.public.GOLD_AGG_DAILY_BOOKING').to_pandas()
#   st.subheader('Daily Booking Trend:')
#   # st.write(hotel_Daily_Booking_Trend)
#   st.line_chart(hotel_Daily_Booking_Trend , x="DATE" ,y="TOTAL_BOOKING")

#   # avg_booking value

#   st.subheader('Revenue By Cities:')
#   # st.write(hotel_wise_revenue)
#   st.bar_chart(data=hotel_cities_wise_revenue, x="HOTEL_CITY" , y="TOTAL_REVENUE")

#   hotel_wise_revenue= session.sql('select HOTEL_ID , sum(TOTAL_AMOUNT) as Revenue  from hotel_db.public.GOLD_BOOKING_CLEAN group by HOTEL_ID  ').to_pandas()
#   # st.write(hotel_wise_revenue)
#   # remeber in snowflake alias act as upper case y=Reveneue is wrong 
#   st.subheader('Revenue By Hotel:')
#   st.line_chart(data=hotel_wise_revenue ,x='HOTEL_ID', y='REVENUE') 
  
#   # st.write(total_booking)
#   # st.write(total_revenue)
#   # st.write(hotel_wise_revenue)
  
  
  

# except Exception as error:
#     st.error("Unable to connect to Snowflake or read the table.")
#     st.exception(error)


