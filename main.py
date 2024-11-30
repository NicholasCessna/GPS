from kivy.app import App
from kivy.uix.label import Label
import requests
import os
from plyer import gps


class GPSApp(App):
    def build(self):
        self.label = Label(text="Waiting for GPS data...")
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        
        if platform == 'android':
            self.request_android_permissions()
            gps.start()
            gps.configure(on_location=self.update_location)
        else:
            self.label.text = "GPS is not supported on this platform"

        return layout

    def request_android_permissions(self):
        request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
        return self.label

    def update_location(self, lat, lon):
        response = requests.get(f"https://api.geoapify.com/v2/places?categories=commercial.supermarket,commercial.food_and_drink&filter=circle:{lat},{lon},5000&limit=20&apiKey=95d1097e14424eb28f6d468a8e8745ad")
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
        print("exit")


if __name__ == '__main__':
    GPSApp().run()
