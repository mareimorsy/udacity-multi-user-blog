from handlers.Handler import Handler
from models.Comment import Comment
# Delete comment
class DeleteComment(Handler):
    def post(self, post_id, comment_id):
        comment = Comment.getByID(comment_id)
        if not comment:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return
        # You must be authenticated in order to Delete the comment
        self.is_authenticated()
        # only delete when the comment author submitted the request
        if comment.author == self.user.name :
            Comment.delete(comment_id)
            self.redirect('/article/%s' % post_id)