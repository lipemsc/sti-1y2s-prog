from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import requests

class Meteo(BoxLayout):
    city_id = 0
    list_of_cities = ["Faro", "Coimbra", "Olhão", "Moncarapacho", "Tavira"]
    data = {}
    apikey = ""

    def update_meteo_data(self,dt):
        self.data = {}
        for city in self.list_of_cities:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.apikey}&units=metric"
            self.data[city] = requests.get(url).json()
        #print(self.data)
    
    def update_gui(self, dt):
        city = self.list_of_cities[self.city_id]
        self.ids.lb_cidade.text = city
        #print(self.data)
        self.ids.temperatura.text = str(self.data[city]["main"]["temp"]) + " ºC"
        self.ids.velocidade_vento.text = str(self.data[city]["wind"]["deg"]) + "º, " + str(self.data[city]["wind"]["speed"]) + " m/s"
        icon_code = self.data[city]["weather"][0]["icon"]
        url_image = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        self.ids.image.source = url_image
        self.city_id = (self.city_id + 1) % len(self.list_of_cities)

class MeteoApp(App):
    def build(self):
        root = Meteo()
        Clock.schedule_once(root.update_meteo_data)
        Clock.schedule_interval(root.update_meteo_data, 60)
        Clock.schedule_interval(root.update_gui, 5)
        return root

MeteoApp().run()
