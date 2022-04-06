from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileField, FileAllowed


class UploadForm(FlaskForm):
    photo = FileField("Photo",validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'ONLY SPECIFIED FORMATS ALLOWED!'),FileRequired()])