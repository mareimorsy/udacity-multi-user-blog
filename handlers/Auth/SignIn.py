from handlers.Handler import Handler
from models.User import User
# Login
class SignIn(Handler):
    def get(self):
        self.render('login.html', title = 'Login', body_class="auth-page", nav_login="active")
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password) # login in hander model
        if u:
            self.login(u) # login in handler
            self.redirect('/')
        else:
            msg = 'Invalid username or password!'
            self.render('login.html', title = 'Login', error_password = msg, body_class="auth-page", nav_login="active", has_error_username='has-error', has_error_password="has-error", username=username)