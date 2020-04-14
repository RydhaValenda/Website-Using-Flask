from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # "route" alamat url yang akan ditangani oleh app ini
    @app.route('/') #decorator(akan memastikan fungsi index akan bisa dipanggil oleh flask)
    def index():
        return render_templates('index.html')

    @app.route('/abput')
    def about():
        return 'About me'

    return app

# # IP "0.0.0.0" bisa dites diinternal network
# app.run('0.0.0.0', debug=True)