from flask import Flask, render_template, Blueprint

app = Flask(__name__)
post_pages = Blueprint("post_pages", __name__)

@post_pages.get("/post/<int:post_id>")
def display_post(title: str):
    return "Display post page."

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "post":
        title = request.form.get("title")
        content = request.form.get("content")
        return redirect(url_for("post_pages.display_post", title=title))
    return "Create post page."

# Define the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/search', methods=['GET', 'POST'])
# @login_required
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect((url_for('search_results', query=form.search.data)))  # or what you want
    return render_template('search.html', form=form)
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
