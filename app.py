from flask import Flask, render_template

app = Flask(__name__)

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
    # Define some example blog posts
    posts = [
        {
            'title': 'First Blog Post',
            'content': 'This is my first blog post!',
            'author': 'John Doe',
            'date_posted': 'May 1, 2023'
        },
        {
            'title': 'Second Blog Post',
            'content': 'This is my second blog post!',
            'author': 'Jane Smith',
            'date_posted': 'May 7, 2023'
        }
    ]
    return render_template('blog.html', posts=posts)
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
