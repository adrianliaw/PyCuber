from handler import *

class MainHandler(Handler):
    def get(self):
        self.render("main.html")

class WebGL(Handler):
	def get(self):
		self.render("webglandthreejs/index.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler), 
    ('/webgl', WebGL)
], debug=True)
