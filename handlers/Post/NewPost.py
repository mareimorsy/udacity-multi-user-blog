from handlers.Handler import Handler
from models.Post import Post

# Create new post
class NewPost(Handler):
    def get(self):
        # You must be authenticated in order to view that page
        self.is_authenticated()
        self.render('new_post.html', title="Create a new article", nav_newpost = "active")

    def post(self):
        # You must be authenticated in order to save the post
        self.is_authenticated()
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            p = Post(subject = subject, content = content, author = self.user.name)
            p.put()
            self.redirect('/article/%s' % str(p.key.id()))
        else:
            self.render("new_post.html", subject = subject, content = content, error = "Both fields are required!")