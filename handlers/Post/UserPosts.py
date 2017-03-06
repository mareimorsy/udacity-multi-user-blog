from handlers.Handler import Handler
from models.Post import Post
# Get all posts for a specific user
class UserPosts(Handler):
    def get(self):
        # You must be authenticated in order to view your posts
        self.is_authenticated()
        posts = Post.query(Post.author == self.user.name).order(-Post.created)
        self.render("my_posts.html", posts = posts, nav_myposts="active")