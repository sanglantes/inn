import requests
import json
from http.server import *
import feedparser
from datetime import date

f = open('site.html', 'r')  # Import site.html
html = f.read()
host = "localhost"  # Host at 127.0.0.1
port = 1337  # Custom port


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Send OK header.
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f'{html}', 'utf-8'))  # Read site.html

        self.wfile.write(bytes(
            f'''
            <div class="logo">
                <p style="left: 10px; font-size: 45px; color: #ed4040;">BREAKING NEWS: <span style="color: black; font-size: 35px;">{entries[i].title}</span></p>
            </div>''',
            'utf-8'))

        self.wfile.write(bytes('''
        <div class="live-header">
            <p style="position: relative; color: #b32020; left: 10px; top: 10px;">
                <b>LIVE • </b><span style="color:black;"> Recent news updates</span> 
            </p>
        </div>''', 'utf-8'))  # Live header

        self.wfile.write(bytes(f'''
        <div class="live">
            <a href="{entries[f].link}">
                <span class="live-news">{entries[f].title}</span>
            </a>
        </div>''', 'utf-8'))  # BBC RSS live news

        self.wfile.write(bytes(
            f'''<div class="live">
                <a href="{entries[g].link}">
                    <span class="live-news">{entries[g].title}</span>
                </a>
            </div>''',
            'utf-8'))

        self.wfile.write(bytes(
            f'''<div class="live">
                <a href="{entries[h].link}">
                    <span class="live-news">{entries[h].title}</span>
                </a>
            </div>''',
            'utf-8'))

        self.wfile.write(bytes(
            f'''<div class="live">
                <a href="{entries[k].link}">
                    <span class="live-news">{entries[k].title}</span>
                </a>
            </div>''',
            'utf-8'))

        self.wfile.write(bytes(
            f'''<div class="live">
                        <a href="{entries[l].link}">
                            <span class="live-news">{entries[l].title}</span>
                        </a>
                    </div>''',
            'utf-8'))

        self.wfile.write(bytes(f'''
        <div class="main-article-container">
            <img class="main-article-image" src="{headline_image(0)}">
        </div>''', 'utf-8'))

        self.wfile.write(bytes(f'''
        <a href<div class="main-article-title-container">
            <a href="{headline_url(0)}"><div class="main-article-title">{headline(0)}</div></a>
        </div>''', 'utf-8'))
        #  API sub news
        self.wfile.write(bytes(f'''
        <div class="flexbox-container">
            <div class="gallery">
                <a href="{headline_url(1)}">
                    <img src="{headline_image(1)}">
            <div class="desc">{headline(1)}</div>
            </div></a>
            <div class="gallery">
                <a href="{headline_url(2)}">
                    <img src="{headline_image(2)}">
            <div class="desc">{headline(2)}</div>
            </div></a>
            <div class="gallery">
                <a href="{headline_url(3)}">
                    <img src="{headline_image(3)}">
            <div class="desc">{headline(3)}</div>
            </div></a>
        </div>''', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))

# API
# API
response = requests.get(
    f'https://newsapi.org/v2/everything?q=Ukraine AND Russia&from={date.today()}&sortBy=popularity&apiKey=cad6e5d9560248eba80f70befa340eda')
data = response.json()  # Parse JSON
articles = data["articles"]  # Select 'articles' values
results = [arr["title"] for arr in articles]  # From 'articles' select 'title'
results_images = [arr["urlToImage"] for arr in articles]  # From 'articles' select 'urlToImage'
results_url = [arr["url"] for arr in articles]  # From 'articles' select 'url'


def headline(x):  # Generate four headlines
    for i, arr in enumerate(results, x):
        if i > 3:
            return arr


def headline_image(x):  # Generate corresponding images for the four headlines
    for i, arr in enumerate(results_images, x):
        if i > 3:
            return arr


def headline_url(x):  # Generate corresponding URLs for the four headlines
    for i, arr in enumerate(results_url, x):
        if i > 3:
            return arr


#  RSS
newsfeed = feedparser.parse('https://feeds.bbci.co.uk/news/rss.xml?edition=int')  # Define feed
entries = newsfeed.entries
i = 0
while 'Ukraine' and 'Russia' not in entries[i].title:
    i = i + 1

f = i + 1
while 'Ukraine' and 'Russia' not in entries[f].title:
    f = f + 1

g = f + 1
while 'Ukraine' and 'Russia' not in entries[g].title:
    g = g + 1

h = g + 1
while 'Ukraine' and 'Russia' not in entries[h].title:
    h = h + 1

k = h + 1
while 'Ukraine' and 'Russia' not in entries[k].title:
    k = k + 1

l = k + 1
while 'Ukraine' and 'Russia' not in entries[l].title:
    l = l + 1

if __name__ == '__main__':
    webServer = HTTPServer((host, port,), Server)
    print(f'Server is hosting at {host}')
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print('Server stopped.')
