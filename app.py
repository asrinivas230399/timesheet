from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('customer_add.html')

@app.route('/projects')
def projects():
    return render_template('project_listing.html')

if __name__ == '__main__':
    app.run(debug=True)