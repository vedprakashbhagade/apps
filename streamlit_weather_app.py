import streamlit as st
import requests

# App title
st.title("🌤️ Weather Information App")

# Sidebar for user input
st.sidebar.header("Enter City Name")
city_name = st.sidebar.text_input("City", placeholder="Enter city name")

# OpenWeatherMap API setup
API_KEY = "e79c81366f89b737844b93a767675671"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Display weather information
if city_name:
    weather_data = get_weather(city_name)

    if weather_data:
        st.subheader(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
        st.write(f"**Temperature:** {weather_data['main']['temp']} °C")
        st.write(f"**Weather:** {weather_data['weather'][0]['description'].capitalize()}")
        st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
        st.write(f"**Wind Speed:** {weather_data['wind']['speed']} m/s")
    else:
        st.error("City not found! Please enter a valid city name.")
else:
    st.info("Enter a city name in the sidebar to get started.")
