from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from flaskBlog.models import Post


class NewPostForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    content = TextAreaField('Content: ', validators=[DataRequired()])
    submit = SubmitField('Post')

    def validate_title(self, title):
        title = Post.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('Title already taken. Please try another.')
