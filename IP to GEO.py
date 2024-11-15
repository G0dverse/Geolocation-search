import requests

def get_ip_geolocation(ip_address):
    # Replace 'YOUR_API_KEY' with your actual API key from IPinfo
    api_key = 'YOUR_API_KEY'
    url = f'https://ipinfo.io/{ip_address}/json?token={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract and print geolocation details
            ip = data.get('ip', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            loc = data.get('loc', 'N/A').split(',')
            latitude = loc[0] if loc != 'N/A' else 'N/A'
            longitude = loc[1] if len(loc) > 1 else 'N/A'

            print(f"IP Address: {ip}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print("Error: Unable to fetch data.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter IP address to get geolocation: ")
    get_ip_geolocation(ip_address)

#made with love by G0dverse