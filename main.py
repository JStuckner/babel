#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World")


app = webapp2.WSGIApplication([('/',MainPage),
                               ],
                              debug=True)

import cgi

from google.appengine.api import users
import webapp2
import random

def babel(string):
    letters = {'ё': ['ë'],
               'й': [],
               'ц': [],
               'у': ['y'],
               'к': ['κ'],
               'е': ['e'],
               'н': [],
               'г': [],
               'ш': [],
               'щ': [],
               'з': [],
               'х': ['x'],
               'ъ': [],
               'ф': [],
               'ы': [],
               'в': [],
               'а': ['a'],
               'п': [],
               'р': ['p'],
               'о': ['o', 'ο'],
               'л': [],
               'д': [],
               'ж': [],
               'э': [],
               'я': [],
               'ч': [],
               'с': ['c'],
               'м': [],
               'и': [],
               'т': [],
               'ь': [],
               'б': [],
               'ю': [],
               'Ё': ['Ë'],
               'Й': [],
               'Ц': [],
               'У': [''],
               'К': ['K', 'Κ'],
               'Е': ['E', 'Ε'],
               'Н': ['H', 'Η'],
               'Г': ['Γ'],
               'Ш': [],
               'Щ': [],
               'З': [],
               'Х': ['X'],
               'Ъ': [],
               'Ф': [],
               'Ы': [],
               'В': ['B', 'B'],
               'А': ['A', 'Α'],
               'П': ['Π'],
               'Р': ['P', 'Ρ'],
               'О': ['O', 'Ο'],
               'Л': [],
               'Д': [],
               'Ж': [],
               'Э': [],
               'Я': [],
               'Ч': [],
               'С': ['C'],
               'М': ['M', 'Μ'],
               'И': [],
               'Т': ['T', 'Τ'],
               'Ь': [],
               'Б': [],
               'Ю': []}    
    out = ''
    for l in string:
        l = l.encode("utf-8")
        try:
            sub_list = letters[l]
        except KeyError:
            out = ''.join((out,l))
            continue
        if len(sub_list) > 0:
            out = ''.join((out, random.choice(sub_list)))
        else:
            out = ''.join((out, l))
    return out.decode("utf-8")

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/sign" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Babel"></div>
              </form>
            </body>
          </html>""")

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(babel(cgi.escape(self.request.get('content'))))
        self.response.out.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
