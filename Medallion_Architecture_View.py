import streamlit as st

st.header('Medallion Architecture view')

try:
    con=st.connection('snowflake')
    session=con.session()

    broze_table_count=session.sql('select count(*) from  hotel_db.public.BRONZE_HOTEL_BOOKING;').to_pandas().iloc[0,0]
    silver_table_count=session.sql('select count(*) from hotel_db.public.SILVER_HOTEL_BOOKINGS;').to_pandas().iloc[0,0]
    gold_table_count=session.sql('select count(*) from  hotel_db.public.GOLD_BOOKING_CLEAN;').to_pandas().iloc[0,0]

    col1,col2,col3=st.columns(3)
    col1.metric("total count of broznze table",broze_table_count)
    col2.metric("total count of silver table",silver_table_count)
    col3.metric("total count of gold table",gold_table_count)
     # col1.metric("total count of broznze table",broze_table_count)

        broze_table_df=session.sql('select count(*) from  hotel_db.public.BRONZE_HOTEL_BOOKING;').to_pandas()
    silver_table_df=session.sql('select count(*) from hotel_db.public.SILVER_HOTEL_BOOKINGS;').to_pandas()
    gold_table_df=session.sql('select count(*) from  hotel_db.public.GOLD_BOOKING_CLEAN;').to_pandas()

    

except Exception as error:
     st.error("Unable to connect to Snowflake or read the table.")
     st.exception(error)
    
