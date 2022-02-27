from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileField, FileAllowed


class UploadForm(FlaskForm):
    file = FileField("Image Upload",validators=[FileAllowed(['jpg', 'png'], 'ONLY SPECIFIED FORMATS ALLOWED!'),FileRequired()])