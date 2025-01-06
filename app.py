from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///siteflask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка при добавлении"
    else:
        return render_template('create.html')



if __name__ == '__main__':
    app.run(debug=True)
