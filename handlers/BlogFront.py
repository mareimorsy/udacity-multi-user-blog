from handlers.Handler import Handler
from models.Post import Post

# Home page
class BlogFront(Handler):
    def get(self):
        q = Post.query().order(-Post.created)
        posts = q.fetch(limit = 10)
        self.render("front_page.html", posts = posts, nav_home="active")