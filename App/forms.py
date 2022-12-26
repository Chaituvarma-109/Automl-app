from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, length


class FileForm(FlaskForm):
    train_file = FileField("train_file", validators=[FileRequired()])
    Type_of_Problem = SelectField("type_of_problem", choices=["Classification", "Regression", "Clustering"])
    Type_of_Dataset = SelectField("type_of_dataset", choices=["csv", "tsv", "xlsx", "json"])
    Output_Column = StringField("output_column", validators=[InputRequired(message='Medicine Name required'),
                                                             length(max=100)])
    submit = SubmitField("Submit")
