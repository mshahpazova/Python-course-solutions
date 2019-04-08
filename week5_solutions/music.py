import math
import random
import json
from datetime import datetime, timedelta

class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return self.artist + ' - ' + self.title + ' from ' + self.album + ' - '  + self.length

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))

    def duration(self, minutes=False, seconds=False, hours=False):
           time = self.length.split(':')
           m = 0
           s = 0
           h = 0
           if len(time) == 2:
               m = int(time[0])
               s = int(time[1])
           else:
               m = int(time[1])
               s = int(time[2])
               h = int(time[0])
           if seconds is True:
               return h * 3600 + m * 60 + s
           elif minutes is True:
               return h * 60 + m
           elif hours is True:
               return h
           else:
               return self.length

class Playlist:
    # list_songs = []
    @staticmethod    
    def seconds_to_hours(seconds):
        seconds_in_day = 86400
        seconds_in_hour = 3600
        seconds_in_minute = 60
        days = seconds // seconds_in_day
        seconds = seconds - (days * seconds_in_day)
        hours = seconds // seconds_in_hour
        seconds = seconds - (hours * seconds_in_hour)
        minutes = seconds // seconds_in_minute
        seconds = seconds - (minutes * seconds_in_minute)
        return ("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

    def __init__(self, name, repeat, shuffle):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list_songs = []
        self.index = 0
        self.played = []

    def add_song(self, song):
        if song not in self.list_songs:
            self.list_songs.append(song)

    def remove_song(self, song):
        if song in list_songs:
            self.list_songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def list_duration(self):
        result = 0
        for song in self.list_songs:
            result += song.duration(seconds = True)
        return self.seconds_to_hours(result)
        
    def next_song(self):
        if self.shuffle == False:
            if len(self.list_songs) != 0:
                if self.index == len(self.list_songs) - 1 and self.repeat == True:
                    self.index = 0
                current_song = self.list_songs[self.index]
                self.index += 1
                return current_song
        else:
            if len(self.list_songs) != 0:
                random.shuffle(self.list_songs)
                current_song = self.list_songs.pop()
                self.played.append(current_song)
                return current_song
            if len(self.list_songs) == 0 and self.repeat == True and len(played) != 0:
                self.list_songs = self.played
                random.shuffle(self.list_songs)
                current_song = self.list_songs.pop()
                self.played = []
                self.played.append(current_song)
                return current_song
    def save(self):
        my_hash = { 'songs': [] }
        # for song in self.list_songs:
        #     # print(self.list_songs)
        my_hash['songs'] = list(map(lambda song : song.__dict__ , self.list_songs)) 
        if self.shuffle == True:
            my_hash['songs'] += list(map(lambda song : song.__dict__ , self.played)) 
        my_hash['shuffle'] = self.shuffle
        my_hash['repeat'] = self.repeat
        my_hash['name'] = self.name
        list_json = json.dumps(my_hash, indent = 4)
        # return lists_json
        file = self.name + '.json'
        print(file)
        with open(file, 'w') as f:
            f.write(list_json)

    @staticmethod
    def load(path):
        with open(path, 'r') as f:
            json_string = f.read()
        data = json.loads(json_string)
        print(data)
        songs = []
        for song in data['songs']:
            current = Song(song['title'], song['artist'], song['album'], song['length'])
            songs.append(current)
        pl = Playlist(data['name'], data['repeat'], data['shuffle'])
        pl.add_songs(songs)
        # print("list", pl.list_songs)
        return pl 


first = Song('My all', 'Mariah Carey', 'My all', '3:14')
second = Song('Jiva rana', 'Slavi Trifonov', 'Rana', '3:20')
playlist = Playlist('Fav', True, True)
playlist.add_song(first)
playlist.add_song(second)
print(playlist.next_song())
p = playlist.load('Fav.json')
print(p)
print(p.list_songs)