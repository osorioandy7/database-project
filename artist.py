from google.appengine.ext import ndb
class Artist(ndb.Model):
    artist_name = ndb.StringProperty()
    year_of_birth = ndb.StringProperty()
    month_of_birth = ndb.StringProperty()
    day_of_birth = ndb.StringProperty()
    artist_song = ndb.KeyProperty(Song)
