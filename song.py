from google.appengine.ext import ndb
class Song (ndb.Model):
    song_name = ndb.StringProperty()
    genre = ndb.StringProperty()
    year_of_release = ndb.StringProperty()
