from handlers.Handler import Handler
from models.Like import Like
from models.Post import Post

# Toggle like status (Like or Unlike)
class LikeToggle(Handler):
    def post(self, post_id):
        # check post state (liked or unliked)
        like = Like.getByPostAndAuthor(post_id, self.user.name)

        # You must be authenticated in order to Like or Unlike the post
        self.is_authenticated()

        if like:
            # Unlike the post
            Like.unlike(like.key.id())
        else:
            # Like the post
            Like.like(post_id, self.user.name)

        self.redirect('/article/%s' % post_id)