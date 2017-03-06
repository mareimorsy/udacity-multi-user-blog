from handlers.Handler import Handler
from models.Post import Post

# Update post
class EditPost(Handler):
    def get(self, post_id):
        post = Post.getById(post_id)

        if not post:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return
        # You must be authenticated in order to Edit the post
        self.is_authenticated()
        # check if the user who want to edit article is the owner
        if post.author != self.user.name:
            self.render("permalink.html", post = post, title = post.subject, error = "You're not allowed to edit this article!")
            return
        back = self.request.referer

        # User got to edit page directly (he might be copied the edit url)
        if back is None:
            # set cancel link to the post page
            back = "/article/%s" % post_id
        self.render('edit_post.html', post = post, title="Edit Post", back = back)
    def post(self, post_id):

        post = Post.getById(post_id)

        if not post:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return
        # check if the user who want to edit article is the owner
        if post.author != self.user.name:
            self.render("permalink.html", post = post, title = post.subject, error = "You're not allowed to edit this article!")
            return
        post.subject = self.request.get('subject')
        post.content = self.request.get('content')
        post.put()
        self.redirect('/article/%s' % post_id)