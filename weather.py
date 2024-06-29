import requests

def get_weather(city):
      # this is apikey get from there official website
    api_key = 'Apikey'

    
    # this is link of open Weather map 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'



    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            return weather_info
        else:
            print("Error:", data['message'])
            return None
    except requests.RequestException as e:
        print("Error fetching weather data:", str(e))
        return None

def main():
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    if weather_info:
        print(f"Weather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Description: {weather_info['description']}")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
