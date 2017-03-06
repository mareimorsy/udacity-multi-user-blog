from handlers.Handler import Handler
# Logout
class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/signin')