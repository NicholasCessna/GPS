from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
from plyer import gps
import threading
import requests

class GPSApp(App):
    def build(self):
        self.label = Label(text="Waiting for GPS data...")
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        
        # Start GPS service
        gps.configure(on_location=self.on_location)
        gps.start()
        
        return layout

    @mainthread
    def on_location(self, **kwargs):
        # Extract latitude and longitude
        latitude = kwargs['lat']
        longitude = kwargs['lon']
        coords = [latitude, longitude]

        # Update location with extracted coords
        threading.Thread(target=self.update_location, args=(coords,)).start()

    def update_location(self, coords):
        response = requests.get(f"https://api.geoapify.com/v2/places?categories=commercial&filter=circle:{coords[1]},{coords[0]},15000&limit=20&apiKey=YOUR_API_KEY")
        webdata = response.json()

        # Extracting names of places from the web data
        place_names = [feature["properties"]["name"] for feature in webdata.get("features", [])]

        # Update label text to show the place names
        if place_names:
            self.label.text = "Nearby Places:\n" + "\n".join(place_names)
        else:
            self.label.text = "No places found nearby."

        print(self.label.text)

    def on_stop(self):
        gps.stop()
        print("exit")

if __name__ == '__main__':
    GPSApp().run()
