import sys
sys.path.append("..")

import requests
import ctypes


class InternetManager:
    def __init__(self):
        # Initialisation des librairies si nécessaire
        self.InternetGetConnectedState = ctypes.windll.Wininet.InternetGetConnectedState

    def isInternetAcces(self, url="https://www.google.com"):
        try:
            response = requests.get(url, timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def isWifiConnected(self):
        return self.InternetGetConnectedState(0, 0) != 0

    def geocode_location(self, location_name):
        api_url = f"https://nominatim.openstreetmap.org/search?q={location_name}&format=json"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
        return None, None