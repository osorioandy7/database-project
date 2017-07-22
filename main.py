#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from artist import Artist
from song import Song
import webapp2
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template("output.html")
        self.response.write(main_template.render())
    def post(self):
        result_template = env.get_template("results.html")
        template_variables = {
            'artist_name':self.request.get('artist_name'),
            'year_of_birth':self.request.get('year_of_birth'),
            'month_of_birth':self.request.get('month_of_birth'),
            'day_of_birth':self.request.get('day_of_birth'),
            'song_name':self.request.get('song_name'),
            'genre':self.request.get('genre'),
            'year_of_release':self.request.get('year_of_release'),
        }

        theSong = Song(song_name = template_variables['song_name'], genre = template_variables['genre'], year_of_release = template_variables['year_of_release'])

        Artist(artist_name = template_variables['artist_name'],year_of_birth = template_variables['year_of_birth'],month_of_birth = template_variables['month_of_birth'], day_of_birth = template_variables['day_of_birth'],artist_song = theSong).put()


        self.response.write(result_template.render(template_variables))









app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
