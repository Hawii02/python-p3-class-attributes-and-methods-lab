# class Song:
#     count = 0
#     genres = []
#     artists = []
#     genre_count = {}
#     artist_count = {}
#     def __init__(self, name, artist, genre):
#         Song.count += 1
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         Song.add_song_to_count()
#         Song.add_to_genres()
#         Song.add_to_artists()
#         Song.add_to_genre_count()

#     @classmethod    
#     def add_song_to_count(cls):
#         cls.count += 1

#     @classmethod
#     def add_to_genres(cls): 
#         if cls.genre not in cls.genres:
#             cls.genres.append(cls.genre)  
#     @classmethod
#     def add_to_artists(cls):
#         if cls.artist not in cls.artists:
#             cls.artists.append(cls.artist)
#     @classmethod
#     def add_to_genre_count(cls):
#         if cls.genre in cls.genre_count:
#             cls.genre_count[cls.genre] += 1
#         else:
#             cls.genre_count[cls.genre] = 1

# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        Song.count += 1
        self.name = name
        self.artist = artist
        self.genre = genre

        if genre not in Song.genres:
            Song.genres.append(genre)

        if artist not in Song.artists:
            Song.artists.append(artist)

        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1

    @classmethod            
    def add_to_genres(cls):
        return set(cls.genres)
    
    @classmethod            
    def add_to_artists(cls):
        return set(cls.artists)
    
    @classmethod            
    def add_to_genre_count(cls):
        return set(cls.genre_count)
    
    @classmethod            
    def add_to_artist_count(cls):
        return set(cls.artist_count)