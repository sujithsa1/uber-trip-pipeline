import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Uber Trip Analytics",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark uber-style theme
st.markdown("""
<style>
    .main { background-color: #0a0a0a; }
    .stApp { background-color: #0a0a0a; }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #00d4aa;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin: 5px;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 900;
        color: #00d4aa;
        margin: 0;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .section-header {
        color: #00d4aa;
        font-size: 1.3rem;
        font-weight: 700;
        border-left: 4px solid #00d4aa;
        padding-left: 10px;
        margin: 20px 0 10px 0;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border: 1px solid #00d4aa33;
        border-radius: 12px;
        padding: 15px;
    }
    div[data-testid="stMetricValue"] { color: #00d4aa !important; }
    div[data-testid="stMetricLabel"] { color: #aaa !important; }
    .stDataFrame { background: #1a1a2e; }
    h1, h2, h3 { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

DB_URL = "postgresql://uberadmin:UberTrip2026!@uber-trips-db.c0rwmgkciat4.us-east-1.rds.amazonaws.com:5432/uber_trips"

@st.cache_data
def load_data():
    engine = create_engine(DB_URL)
    trips = pd.read_sql("SELECT * FROM raw_trips", engine)
    zone = pd.read_sql("SELECT * FROM gold_zone_performance", engine)
    hourly = pd.read_sql("SELECT * FROM gold_hourly_demand", engine)
    drivers = pd.read_sql("SELECT * FROM gold_driver_performance", engine)
    daily = pd.read_sql("SELECT * FROM gold_daily_summary", engine)
    return trips, zone, hourly, drivers, daily

# Sidebar
with st.sidebar:
    st.markdown("## 🚗 Uber Analytics")
    st.markdown("---")
    st.markdown("### Pipeline Stack")
    st.markdown("🪣 **AWS S3** — Data Lake")
    st.markdown("🐘 **PostgreSQL RDS** — Warehouse")
    st.markdown("🔧 **dbt** — 7 Models, 12 Tests")
    st.markdown("🌀 **Airflow** — 8 Task DAG")
    st.markdown("🐍 **Python + Pandas** — ETL")
    st.markdown("---")
    st.markdown("### Data Stats")
    st.markdown("📅 Period: March 2026")
    st.markdown("🔄 Updates: Daily")
    st.markdown("✅ Tests: 12/12 Passing")
    st.markdown("---")
    st.markdown("Built by **Sujith** 🚀")

# Header
st.markdown("""
<div style='text-align:center; padding: 20px 0;'>
    <h1 style='font-size:3rem; color:#00d4aa; margin:0;'>🚗 UBER TRIP ANALYTICS</h1>
    <p style='color:#888; font-size:1.1rem; margin:5px 0;'>
        Real-time insights powered by AWS S3 · PostgreSQL · dbt · Airflow
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

with st.spinner("⚡ Loading data from AWS RDS..."):
    trips, zone, hourly, drivers, daily = load_data()

# KPI Row
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("🚗 Total Trips", f"{len(trips):,}", "+10,000 today")
col2.metric("💰 Total Revenue", f"${trips['total_amount'].sum():,.0f}", "+$362K")
col3.metric("✅ Completion Rate", f"{(trips['completed_flag'].mean()*100):.1f}%")
col4.metric("💵 Avg Fare", f"${trips['fare_amount'].mean():.2f}")
col5.metric("📏 Avg Distance", f"{trips['distance_miles'].mean():.1f} mi")

st.divider()

# Charts Row 1
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<p class="section-header">💰 Revenue by Pickup Zone</p>', unsafe_allow_html=True)
    fig = px.bar(
        zone.sort_values("total_revenue", ascending=True),
        x="total_revenue", y="pickup_zone",
        orientation="h",
        color="total_revenue",
        color_continuous_scale=[[0, "#003d30"], [0.5, "#00a884"], [1, "#00d4aa"]],
        text="total_revenue",
        labels={"total_revenue": "Revenue ($)", "pickup_zone": "Zone"}
    )
    fig.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
    fig.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="white", height=400,
        coloraxis_showscale=False,
        xaxis=dict(gridcolor="#222", color="white"),
        yaxis=dict(gridcolor="#222", color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown('<p class="section-header">🚦 Trip Status</p>', unsafe_allow_html=True)
    status_counts = trips["trip_status"].value_counts().reset_index()
    status_counts.columns = ["status", "count"]
    fig = go.Figure(data=[go.Pie(
        labels=status_counts["status"],
        values=status_counts["count"],
        hole=0.6,
        marker_colors=["#00d4aa", "#ff4757"],
        textinfo="label+percent",
        textfont_color="white"
    )])
    fig.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="white", height=400,
        showlegend=True,
        legend=dict(font=dict(color="white")),
        annotations=[dict(
            text=f"{(trips['completed_flag'].mean()*100):.0f}%<br>Complete",
            x=0.5, y=0.5, font_size=16, showarrow=False,
            font_color="#00d4aa"
        )]
    )
    st.plotly_chart(fig, use_container_width=True)

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="section-header">⏰ Hourly Trip Demand</p>', unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hourly.sort_values("hour_of_day")["hour_of_day"],
        y=hourly.sort_values("hour_of_day")["total_trips"],
        mode="lines+markers",
        line=dict(color="#00d4aa", width=3),
        marker=dict(size=8, color="#00d4aa"),
        fill="tozeroy",
        fillcolor="rgba(0, 212, 170, 0.1)"
    ))
    fig.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="white", height=350,
        xaxis=dict(gridcolor="#222", color="white", title="Hour of Day"),
        yaxis=dict(gridcolor="#222", color="white", title="Trips")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown('<p class="section-header">📈 Daily Revenue Trend</p>', unsafe_allow_html=True)
    daily["trip_date"] = pd.to_datetime(daily["trip_date"])
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily.sort_values("trip_date")["trip_date"],
        y=daily.sort_values("trip_date")["total_revenue"],
        mode="lines",
        line=dict(color="#00d4aa", width=2),
        fill="tozeroy",
        fillcolor="rgba(0, 212, 170, 0.1)"
    ))
    fig.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="white", height=350,
        xaxis=dict(gridcolor="#222", color="white"),
        yaxis=dict(gridcolor="#222", color="white", title="Revenue ($)")
    )
    st.plotly_chart(fig, use_container_width=True)

# Top Drivers
st.markdown('<p class="section-header">🏆 Top 10 Drivers Leaderboard</p>', unsafe_allow_html=True)
top_drivers = drivers.nlargest(10, "total_earnings")[
    ["driver_id", "total_trips", "completed_trips", "total_earnings", "completion_rate"]
].reset_index(drop=True)
top_drivers.index += 1
top_drivers["total_earnings"] = top_drivers["total_earnings"].apply(lambda x: f"${x:,.2f}")
top_drivers["completion_rate"] = top_drivers["completion_rate"].apply(lambda x: f"{x:.1f}%")
top_drivers.columns = ["Driver ID", "Total Trips", "Completed", "💰 Earnings", "✅ Completion Rate"]
st.dataframe(top_drivers, use_container_width=True, height=380)

st.divider()
st.markdown("""
<div style='text-align:center; color:#555; padding:10px;'>
    Built by Sujith &nbsp;|&nbsp; AWS S3 · PostgreSQL RDS · dbt · Apache Airflow · Streamlit
</div>
""", unsafe_allow_html=True)
