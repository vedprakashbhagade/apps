import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV Data Visualizer 📈")

# Sidebar for file upload
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Display the uploaded data
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    # Visualization options
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Histogram"]
    )
    columns = df.select_dtypes(include=['float64', 'int64']).columns

    if len(columns) > 0:
        x_col = st.sidebar.selectbox("Select X-axis Column", columns)
        y_col = st.sidebar.selectbox("Select Y-axis Column", columns)

        # Generate visualizations
        if chart_type == "Line Chart":
            st.subheader("Line Chart")
            st.line_chart(df[[x_col, y_col]].set_index(x_col))
        elif chart_type == "Bar Chart":
            st.subheader("Bar Chart")
            st.bar_chart(df[[x_col, y_col]].set_index(x_col))
        elif chart_type == "Histogram":
            st.subheader("Histogram")
            bins = st.sidebar.slider("Number of bins", 5, 50, 10)
            fig, ax = plt.subplots()
            sns.histplot(df[x_col], bins=bins, kde=True, ax=ax)
            st.pyplot(fig)
    else:
        st.warning("No numeric columns found for visualization.")
else:
    st.info("Upload a CSV file to start.")

