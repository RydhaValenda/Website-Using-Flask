from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    # konfigurasi debug dibawah berfungsi flask mengambil perubahan2 dalam html
    # app.config['DEBUG'] = True

    # file config diambil dari file mode py
    app.config.from_pyfile('settings.py')

    # "route" alamat url yang akan ditangani oleh app ini
    @app.route('/') #decorator(akan memastikan fungsi index akan bisa dipanggil oleh flask)
    def index():
        return render_template('index.html', TITLE='Flask-01')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-01')

    return app

# # IP "0.0.0.0" bisa dites diinternal network
# app.run('0.0.0.0', debug=True)