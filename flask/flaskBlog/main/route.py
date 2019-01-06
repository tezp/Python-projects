from flask import Blueprint, render_template, request
from flask_login import login_required

from flaskBlog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', posts=posts)


@main .route('/about')
@login_required
def about():
    return render_template('about.html', title="About")


