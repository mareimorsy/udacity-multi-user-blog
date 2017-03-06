import webapp2
import jinja2
import os
import datetime
# Import Helpers
from helpers import functions
# Import user Model
from models.User import User
# Define jinja2 templates directory.
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
# Instantiate new jinja2 environment.
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, title = "Your gateway to the open world!", **kw):
        # Define the host url for static assets address
        url = self.request.host_url
        # Render the template
        self.write(jinja_env.get_template(template).render(kw, url = url, title = title, user = self.user))

    def set_secure_cookie(self, name, val):
        cookie_val = functions.make_secure_val(val)
        # expires in 30 days
        expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        expiration_date = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        # Set-Cookie there's an easier way : self.response.set_cookie(...)
        self.response.headers.add_header('Set-Cookie','%s=%s; Expires=%s; Path=/' % (name, cookie_val, expiration_date))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and functions.check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key.id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def is_authenticated(self):
        if not self.user:
            self.redirect('/signin')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        # if user_id cookie exists, store the actual User object in self.user
        self.user = uid and User.by_id(int(uid))