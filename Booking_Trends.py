import streamlit as st

st.title("📈 Booking Trends Analysis")

try:
    # Snowflake Connection
    con = st.connection("snowflake")
    session = con.session()

    # Fetch Data
    daily_df = session.sql("""
        SELECT *
        FROM HOTEL_DB.PUBLIC.GOLD_AGG_DAILY_BOOKING
    """).to_pandas()

    # =========================
    # KPI Section
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Bookings",
        int(daily_df["TOTAL_BOOKING"].sum())
    )

    col2.metric(
        "Average Daily Booking",
        round(daily_df["TOTAL_BOOKING"].mean(), 2)
    )

    col3.metric(
        "Peak Booking",
        int(daily_df["TOTAL_BOOKING"].max())
    )

    col4.metric(
        "Lowest Booking",
        int(daily_df["TOTAL_BOOKING"].min())
    )

    st.divider()

    # =========================
    # Highest & Lowest Booking Day
    # =========================

    highest_booking = daily_df.loc[
        daily_df["TOTAL_BOOKING"].idxmax()
    ]

    lowest_booking = daily_df.loc[
        daily_df["TOTAL_BOOKING"].idxmin()
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📈 Highest Booking Day",
            str(highest_booking["DATE"]),
            int(highest_booking["TOTAL_BOOKING"])
        )

    with col2:
        st.metric(
            "📉 Lowest Booking Day",
            str(lowest_booking["DATE"]),
            int(lowest_booking["TOTAL_BOOKING"])
        )

    st.divider()

    # =========================
    # Booking Trend
    # =========================

    st.subheader("📊 Daily Booking Trend")

    st.line_chart(
        daily_df,
        x="DATE",
        y="TOTAL_BOOKING"
    )

    st.divider()

    # =========================
    # Top 10 Busiest Days
    # =========================

    top_10_days = daily_df.sort_values(
        "TOTAL_BOOKING",
        ascending=False
    ).head(10)

    st.subheader("🔥 Top 10 Busiest Days")

    st.dataframe(
        top_10_days,
        use_container_width=True
    )

    st.bar_chart(
        top_10_days,
        x="DATE",
        y="TOTAL_BOOKING"
    )

except Exception as error:
    st.error("Unable to connect to Snowflake or read the table.")
    st.exception(error)
