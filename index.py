import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_lyrics(artist, song_title):
    api_url = f"https://api.lyrics.ovh/v1/{artist}/{song_title}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data.get('lyrics', 'Lyrics not found')
        
        if '\n' in lyrics:
            lyrics = lyrics.split('\n', 1)[1]
        
        return lyrics
    else:
        return "Lyrics not found or API request failed"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        artist = request.form['artist']
        song_title = request.form['song_title']
        lyrics = get_lyrics(artist, song_title)
        return render_template('index.html', lyrics=lyrics, artist=artist, song_title=song_title)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
