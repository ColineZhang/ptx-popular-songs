import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.spotify.com/v1/search?q=pentatonix&type=track&market=ES'
headers = {'Authorization':'Bearer '+'BQAl7gyKZD4jL4AXrWnczRqFylompQurBmKRXC23Aw4bMl2HqtpTrHtDmMFO0NvvQ48hFXIM673kRw28Dzp3mwkMblHlRLehAls3khj05qzt8_3N8ufU1xlb05qCfTnBIS22ov4-0STetQz61PrNsfTGnCXkhKgIcOsSGqc9KTUslYk1akAy4Pe-IrVNBEu9hBA'}

r = requests.get(url, headers = headers)
r_d = r.json()

tracks = {}

for track in r_d['tracks']['items']:
    name = track['name']
    pop = track['popularity']
    url = track['external_urls']['spotify']
    link = f"<a href='{url}'>{name}</a>"
    tracks[link] = pop

tracks = sorted(tracks.items(), key=lambda x: x[1], reverse=True)

colors = [list(range(0,len(tracks)))]


data = [{
    'type':'bar',
    'x': [x[0] for x in tracks],
    'y': [x[1] for x in tracks],
    'marker':{
            'color':colors,
            'colorscale':'solar',
}}]

my_layout = {
    'title':'Most Popular Songs of PTX',
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='ptx_tracks.html')


