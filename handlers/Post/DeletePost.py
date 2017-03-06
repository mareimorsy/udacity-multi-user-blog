from handlers.Handler import Handler
from models.Post import Post

# Delete Post
class DeletePost(Handler):
    def post(self, post_id):
        post = Post.getById(post_id)

        if not post:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return
        # You must be authenticated in order to Delete the post
        self.is_authenticated()
        # check if the user who want to edit article is the owner
        if post.author != self.user.name:
            self.render("permalink.html", post = post, title = post.subject, error = "You're not allowed to Delete this article!")
            return
        # Delete the post
        post.key.delete()
        # Redirect to the main page
        self.redirect('/')