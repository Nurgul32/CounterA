from app import app
from flask import render_template, url_for, request
from werkzeug.datastructures import CombinedMultiDict
from app.forms import Upload
from config import Config
from werkzeug.utils import secure_filename
import os
@app.route('/')
@app.route('/index')
def index():
    data = 'Welcome username'
    dictionary = {'Россия' : 'Москва', 'Казахстан' : 'Нур-Султан(Астана)', 'США' : 'Вашингтон'}
    return render_template('index.html', title = data, dictionary = dictionary)
#app.config.update(dict(
  #  SECRET_KEY=config.SECRET_KEY,
   # WTF_CSRF_SECRET_KEY=config.WTF_CSRF_SECRET_KEY
#))
@app.route('/upload', methods=('GET', 'POST'))
def upload():
    form = Upload()
    if form.validate_on_submit():
        data = {}
        data['name'] = form.name.data
        data['second_name'] = form.second_name.data
        data['email'] = form.email.data

        f = form.file.data
        filename = secure_filename(f.filename)
        files_dir=os.path.join(os.getcwd(), 'files')
        filename = os.path.join(files_dir, filename)
        if not os.path.exists(files_dir):
            os.mkdir(files_dir)
        f.save(filename)
        return render_template('result.html', data = data)

   
    return render_template('upload.html', form = form)
