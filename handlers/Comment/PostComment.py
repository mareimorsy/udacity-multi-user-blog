from handlers.Handler import Handler
from models.Post import Post
from models.Comment import Comment
# Add new comment
class PostComment(Handler):
    def post(self, post_id):
        # You must be authenticated in order to comment on the post
        self.is_authenticated()
        post = Post.getById(post_id)
        if post and self.user:
            comment = self.request.get('comment')
            Comment.create(post_id, comment, self.user.name)
            self.redirect('/article/%s' % post_id)