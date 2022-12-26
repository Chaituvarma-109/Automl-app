import os

import pandas as pd

from flask import render_template, request
from werkzeug.utils import secure_filename

from App.forms import FileForm
from App import app

from Automl.Data_Validation.data_validation import DataValidation
from Automl.Encoding.encoding import Encoding
from Automl.Database.database import Mongo
from Automl.Logging.logs import logging

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# mongo = Mongo('mldata', 'csvfile')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()
    if form.validate_on_submit():
        problem_type = request.form['Type_of_Problem']
        dataset_type = request.form['Type_of_Dataset']
        output_col = request.form['Output_Column']
        csv_file = form.train_file.data
        logging.info(f"saving csv file.")
        file_name = secure_filename(csv_file.filename)
        path1 = os.path.join(data_dir, file_name)
        csv_file.save(path1)
        logging.info(f"saved csv file.")
        df = pd.read_csv(path1)
        null_df = DataValidation(df).check_null_values()
        transform_df = Encoding(null_df).encoding(output_col)
        out_df = DataValidation(transform_df).outliers()

    logging.info("rendering index template.")
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
