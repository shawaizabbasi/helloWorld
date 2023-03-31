from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Shawaiz Abbasi! I am adding my first code change.'

@app.route('/favorite-course')
def favorite():
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
