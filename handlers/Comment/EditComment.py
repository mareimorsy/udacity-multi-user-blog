from handlers.Handler import Handler
from models.Comment import Comment

# Update comment
class EditComment(Handler):
    def post(self, post_id, comment_id):
        newComment = self.request.get('comment')
        comment = Comment.getByID(comment_id)
        if not comment:
            self.error(404)
            self.write("<h1>404 Not Found</h1>The resource could not be found.")
            return
        # You must be authenticated in order to Edit the comment
        self.is_authenticated()
        # only update when the comment author submitted the request
        if comment.author == self.user.name :
            comment.comment = newComment
            comment.put()
            self.redirect('/article/%s' % post_id)