from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests
import os
import geocoder
from plyer import gps


class GPSApp(App):
    def build(self):
        self.label = Label(text="Waiting for GPS data...")
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        g = geocoder.ip("me")
        self.update_location(coords=g.latlng)


        return layout


    def update_location(self, coords):
        print(coords[0],coords[1])
        response = requests.get(f"https://api.geoapify.com/v2/places?categories=commercial&filter=circle:{coords[0]},{coords[1]},15000&limit=20&apiKey=95d1097e14424eb28f6d468a8e8745ad")
        webdata = response.json()
        print(webdata)
        
        # Extracting names of places from the web data
        place_names = [feature["properties"]["name"] for feature in webdata.get("features", [])]
        
        # Update label text to show the place names
        if place_names:
            self.label.text = "Nearby Places:\n" + "\n".join(place_names)
        else:
            self.label.text = "No places found nearby."
        
        print(self.label.text)

    def on_stop(self):
        print("exit")


if __name__ == '__main__':
    GPSApp().run()
