import webapp2
import jinja2

# Import Helpers
from helpers import functions

# Import Models
from models.Like import Like
from models.Post import Post
from models.Comment import Comment
from models.User import User

# Import Handlers
from handlers.Handler import Handler
from handlers.BlogFront import BlogFront
from handlers.Post.NewPost import NewPost
from handlers.Post.PostPage import PostPage
from handlers.Auth.SignUp import SignUp
from handlers.Auth.SignIn import SignIn
from handlers.Auth.Logout import Logout
from handlers.Post.EditPost import EditPost
from handlers.Post.DeletePost import DeletePost
from handlers.Comment.PostComment import PostComment
from handlers.Comment.DeleteComment import DeleteComment
from handlers.Comment.EditComment import EditComment
from handlers.LikeToggle import LikeToggle
from handlers.Post.UserPosts import UserPosts


# Define app routes
app = webapp2.WSGIApplication([
    ('/', BlogFront),
    ('/article/([0-9]+)', PostPage), # handlers/Post/PostPage
    ('/article/([0-9]+)/edit', EditPost), # handlers/Post/EditPost
    ('/article/([0-9]+)/delete', DeletePost), # handlers/Post/DeletePost
    ('/article/([0-9]+)/comment', PostComment), # handlers/Comment/PostComment
    ('/article/([0-9]+)/comment/([0-9]+)/delete', DeleteComment), # handlers/Comment/DeleteComment
    ('/article/([0-9]+)/comment/([0-9]+)/edit', EditComment), # handlers/Comment/EditComment
    ('/article/([0-9]+)/like', LikeToggle), # handlers/LikeToggle
    ('/myposts', UserPosts), # handlers/Post/UserPosts
    ('/newpost', NewPost), # handlers/Post/NewPost
    ('/signin', SignIn), # handlers/Auth/SignIn
    ('/signup', SignUp), # handlers/Auth/SignUp
    ('/logout', Logout) # handlers/Auth/Logout
], debug=True)
