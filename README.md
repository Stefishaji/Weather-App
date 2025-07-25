
#Real-Time Weather App – Project Report

#1. Project Title

Real-Time Weather App using Streamlit and OpenWeatherMap API

#2. Objective

The objective of this project is to develop an interactive, user-friendly web application that provides **real-time weather data** and a **5-day temperature forecast** for any city. The app enables users to check weather conditions such as temperature, humidity, sunrise and sunset time, and forecast trends using a clean interface powered by **Streamlit**.


# 3. Tools & Technologies Used

| Technology/Tool        | Purpose                            |
| ---------------------- | ---------------------------------- |
| **Python 3**           | Core programming language          |
| **Streamlit**          | Web app development framework      |
| **OpenWeatherMap API** | Real-time weather data source      |
| **Requests**           | API communication                  |
| **Matplotlib**         | Plotting the forecast graph        |
| **Datetime Module**    | Handling and formatting timestamps |


# 4. Features

#User Input

* City input box (`e.g., Kozhikode,IN`)
* Temperature unit selection: Celsius or Fahrenheit

#Current Weather

* Temperature display
* Humidity percentage
* Sunrise and sunset time (converted to human-readable format)
* Weather icon with description

#5-Day Forecast

* Line chart showing daily temperature trends at 12 PM (approx.)
* Forecast auto-adjusts to Indian Standard Time (UTC+5:30)
* Dynamic and visual representation using Matplotlib

#5. Architecture Overview

User Input (City & Unit)
        ↓
 Streamlit Interface
        ↓
API Requests (Current & Forecast)
        ↓
OpenWeatherMap API
        ↓
  Processed Data → Display (Weather, Icon, Forecast Chart)


#6. How It Works

1. The user enters a city name and selects the temperature unit.
2. The app sends HTTP GET requests to the OpenWeatherMap API.
3. Current weather data is fetched, parsed, and displayed.
4. Forecast data is filtered for 12 PM readings, processed, and plotted using Matplotlib.
5. The results are rendered live on the Streamlit app.


#. Challenges & Solutions

| Challenge                               | Solution                                                  |
| --------------------------------------- | --------------------------------------------------------- |
| Handling different time zones           | Manually adjusted to India Standard Time (+5.5 hours)     |
| Forecast data includes 3-hour intervals | Selected only 12 PM readings per day for consistency      |
| API limits on free plan                 | Minimized requests and added error-handling for stability |
| Invalid or misspelled city name         | Included error message using `st.error()`                 |


#8. Future Enhancements

* Add weather alerts (e.g., storm warnings)
* Include wind speed, pressure, and visibility
* Add geolocation-based default weather
* Allow graphical comparison between two cities
* Store weather logs and display trends over time


