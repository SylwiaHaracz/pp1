class Song():
    def __init__(self, performer, title, album, year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return "Artist:\t" + self.performer + "\nSong:\t" + self.title + "\nAlbum:\t" + self.album + "\nYear:\t" + str(self.year)
    

song1 = Song("JK", "Too Sad To Dance","Golden", 2023)


print(song1)