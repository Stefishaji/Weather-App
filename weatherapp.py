import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# ============ CONFIG ============
API_KEY = '91959f885d923b4f43d285fc68a15be2'  # <-- Replace this with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

# ============ UI TITLE ============
st.set_page_config(page_title="Real-Time Weather App", page_icon="🌦")
st.title("🌦 Real-Time Weather App")

# ============ USER INPUT ============
city = st.text_input("Enter City Name (e.g., Kozhikode,IN)", "Kozhikode,IN")

unit = st.radio("Choose Temperature Unit", ("Celsius", "Fahrenheit"))
unit_param = 'metric' if unit == 'Celsius' else 'imperial'
unit_symbol = '°C' if unit == 'Celsius' else '°F'

# ============ CURRENT WEATHER FUNCTION ============
def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units={unit_param}"
    response = requests.get(url)
    return response.json()

# ============ FORECAST FUNCTION ============
def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units={unit_param}"
    response = requests.get(url)
    return response.json()

# ============ FETCH CURRENT WEATHER ============
if city:
    data = get_current_weather(city)

    if data.get("cod") != 200:
        st.error(f"City not found or error: {city}")
    else:
        st.subheader(f"Current Weather in {data['name']}, {data['sys']['country']}")
        st.write(f"**Temperature**: {data['main']['temp']} {unit_symbol}")
        st.write(f"**Humidity**: {data['main']['humidity']}%")

        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

        st.write(f"**Sunrise**: {sunrise}")
        st.write(f"**Sunset**: {sunset}")

        # Weather icon
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        st.image(icon_url, caption=data['weather'][0]['description'].title())

    # ============ FETCH AND PLOT FORECAST ============
    forecast_data = get_forecast(city)

    if forecast_data.get("cod") == "200" and "list" in forecast_data:
        st.subheader("5-Day Forecast (12 PM readings)")

        dates = []
        temps = []

        used_days = set()
        for item in forecast_data["list"]:
            dt = datetime.fromtimestamp(item["dt"])
            local_hour = dt.hour + 5.5  # Adjust for India time (approx)
            day_str = dt.strftime('%Y-%m-%d')

            # Pick one reading closest to midday per day
            if 11 <= local_hour <= 14 and day_str not in used_days:
                dates.append(dt.strftime('%a %d %b'))
                temps.append(item["main"]["temp"])
                used_days.add(day_str)

        if dates and temps:
            fig, ax = plt.subplots()
            ax.plot(dates, temps, marker='o', linestyle='-', color='orange')
            ax.set_xlabel("Date")
            ax.set_ylabel(f"Temperature ({unit_symbol})")
            ax.set_title("5-Day Forecast")
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.info("Forecast data retrieved, but couldn't find 12 PM readings. Try a larger city.")
    else:
        st.warning("Forecast data not available.")
