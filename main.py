from handler import *

class MainHandler(Handler):
    def get(self):
        self.render("main.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)