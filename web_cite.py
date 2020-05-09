from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
@app.route('/index')
def meet_hello():
    return render_template('site_file.html')

if __name__ == '__main__':
    app.run(port=8087, host='127.0.0.1')