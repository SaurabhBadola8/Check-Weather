![image](https://github.com/SaurabhBadola8/Check-Weather/assets/173368852/7f45d262-00d4-4b3f-ad7f-fb12096aba81)

## Weather Information Retrieval

This project utilizes the OpenWeatherMap API to retrieve current weather information based on user-provided city names. It is implemented in Python and demonstrates basic usage of HTTP requests and JSON parsing.

### Features:
- **City Weather Retrieval**: Enter a city name and get real-time weather data including temperature and description.
- **Error Handling**: Handles API request errors gracefully to ensure smooth operation.
- **Metric Units**: Temperature is provided in Celsius by default.

### How to Use:
1. **API Key**: Obtain your API key from [OpenWeatherMap](https://openweathermap.org/) and replace `'YOUR_API_KEY'` in the code with your actual API key.
2. **Dependencies**: Ensure you have the `requests` library installed (`pip install requests`).
3. **Run**: Execute `weather.py`, enter a city name when prompted, and view the current weather information.

### Example Output:
```
Enter city name: London
Weather in London:
Temperature: 18.75°C
Description: scattered clouds
```
