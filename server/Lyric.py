import lyricWiki.LyricWiki_client

def FindLyric(artist,title):
    soap = LyricWiki_client.LyricWikiBindingSOAP("http://lyrics.wikia.com/server.php")
    song = LyricWiki_client.getSongRequest()
    song.Artist = artist
    song.Song = title
    result = soap.getSong(song)

    return result.Return.Lyrics
