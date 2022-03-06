import requests
from pyfiglet import Figlet
import folium

def get_info(ip='127.0.0.1'):
  try:
    response = requests.get(url = f'http://ip-api.com/json/{ip}').json()
    data = {
      '[IP]': response['query'],
      '[Country]': response['country'],
      '[Contry Code]': response['countryCode'],
      '[Region]': response['regionName'],
      '[Region Number]': response['region'],
      '[City]': response['city'],
      '[ZIP]': response['zip'],
      '[Int prov]': response['isp'],
      '[Lat]': response['lat'],
      '[Lon]': response['lon']
    }

    for i, j in data.items():
      print(f"{i}: \t {j}")
    map = folium.Map(location=[response['lat'], response['lon']])
    map.save(f'IP_{response["query"]}_{response["city"]}.html')
  except requests.exceptions.ConnectionError:
    print("[!] Please check your network connection  [!]")

def main():
  title_text = Figlet(font='starwars')
  print(title_text.renderText('IP HACK'))
  ip = input("Enter a target IP: ")

  get_info(ip=ip)

if __name__ == '__main__':
  main()
