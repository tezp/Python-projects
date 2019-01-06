import os
import secrets

from PIL import Image
from flask import url_for
from flask_mail import Message
from werkzeug.utils import secure_filename

from flaskBlog import mail, app


def save_profile_pic(profile_pic):
    random_hex = secrets.token_hex(8)

    _, file_extention = os.path.splitext(secure_filename(profile_pic.filename))
    picture_file_name = random_hex + file_extention
    picture_file_path = os.path.join(app.root_path, 'static/pics', picture_file_name)
    # profile_pic.save(picture_file_path) //This is used to save image without resizing
    img_size = (200, 200)
    img = Image.open(profile_pic)
    img.thumbnail(img_size)
    img.save(picture_file_path)
    return picture_file_name

def send_email(user):
    token = user.get_reset_token()
    print(app.config['MAIL_USERNAME'])
    msg = Message('Password Reset Request',
                  sender=str('sender@gmail.com'),
                  recipients=[user.email])
    msg.body = "To reset your password, visit the following link:{}".format(
        url_for('users.reset_password', token=token, _external=True))
    mail.send(msg)

