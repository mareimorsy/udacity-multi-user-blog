from handlers.Handler import Handler
from helpers import functions
from models.User import User
# Register
class SignUp(Handler):

    def get(self):
        self.render('register.html', title = 'Register', body_class="auth-page", nav_register="active")
    def post(self):
            have_error = False
            self.username = self.request.get('username')
            self.password = self.request.get('password')
            self.verify = self.request.get('confirm_password')
            self.email = self.request.get('email')

            params = dict(username = self.username,
                          email = self.email)

            if not functions.valid_username(self.username):
                params['error_username'] = "That's not a valid username."
                params['has_error_username'] = "has-error" # css styling
                have_error = True

            if not functions.valid_password(self.password):
                params['error_password'] = "That wasn't a valid password."
                params['has_error_password'] = "has-error" # css styling
                have_error = True
            elif self.password != self.verify:
                params['error_confirm'] = "Your passwords didn't match."
                params['has_error_confirm'] = "has-error" # css styling
                have_error = True

            if not functions.valid_email(self.email):
                params['error_email'] = "That's not a valid email."
                params['has_error_email'] = "has-error" # css styling
                have_error = True

            if have_error:
                self.render('register.html', title="Register", body_class="auth-page", nav_register="active", **params)
                # self.write(params)
            else:
                self.done()

    def done(self, *a, **kw):
        # make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            # self.write(a)
            # return
            self.render('register.html', error_username = msg, title = "Register", nav_register = "active", body_class = "auth-page", has_error_username = "has-error", username = self.username, email = self.email)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            # login
            self.login(u)
            self.redirect('/')