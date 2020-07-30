from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates', static_folder='static')
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('presentation.html')


@app.route('/whoami')
def whoami():
    return render_template('whoami.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=1)