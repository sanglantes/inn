import requests
import json
from http.server import *
import feedparser
from datetime import date

f = open('site.html', 'r')
html = f.read()
host = "localhost"
port = 1337


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f'{html}', 'utf-8'))

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
        </div>''', 'utf-8'))

        self.wfile.write(bytes(f'''
        <div class="live">
            <a href="{entries[f].link}">
                <span class="live-news">{entries[f].title}</span>
            </a>
        </div>''', 'utf-8'))

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

        self.wfile.write(bytes('''
        <div class="main-article-container">
            <img class="main-article-image" src="https://media-cldnry.s-nbcnews.com/image/upload/newscms/2022_08/3536943/220224-lugansk-ukraine-troops-mb-1258.jpg">
        </div>''', 'utf-8'))

        self.wfile.write(bytes('''
        <div class="main-article-title-container">
            <a href="https://www.bbc.com"><div class="main-article-title">Lacus viverra vitae congue eu consequat ac felis donec</div></a>
        </div>''', 'utf-8'))

        self.wfile.write(bytes('''
        <div class="flexbox-container">
            <div class="gallery">
                <a href="https://google.com">
                    <img src="https://static.dw.com/image/60797294_303.jpg">
                </a>
            <div class="desc">Est lorem ipsum dolor sit amet consectetur</div>
            </div>
            <div class="gallery">
                <a href="https://google.com">
                    <img src="https://foreignpolicy.com/wp-content/uploads/2022/02/Poland-Ukraine-Russia-crisis-GettyImages-1238647296.jpg">
                </a>
            <div class="desc">Pellentesque habitant morbi tristique senectus</div>
            </div>
            <div class="gallery">
                <a href="https://google.com">
                    <img src="https://www.aljazeera.com/wp-content/uploads/2022/02/2022-02-25T063531Z_831409522_RC2UQS9TNQXW_RTRMADP_3_UKRAINE-CRISIS.jpg">
                </a>
            <div class="desc">Morbi tincidunt augue interdum velit euismod in pellentesque massa placerat</div>
            </div>
        </div>''', 'utf-8'))
        self.wfile.write(bytes('</body></html>', 'utf-8'))


# API
url = (f'''https://newsapi.org/v2/everything?q=Russia&from={date.today()}
        &sortBy=popularity&apiKey=cad6e5d9560248eba80f70befa340eda''')
r = requests.get(url)
parsed_json = json.loads(r.text)
json_news = json.dumps(parsed_json, indent=4, sort_keys=True)
print(json_news)

#  RSS
newsfeed = feedparser.parse('https://feeds.bbci.co.uk/news/rss.xml?edition=int')
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

#  ^ THIS IS NOT ACCEPTABLE. USE RESTful API OR AUTOMATE THE PROCESS.
if __name__ == '__main__':
    webServer = HTTPServer((host, port,), Server)
    print(f'Server is hosting at {host}')
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print('Server stopped.')
