from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('main.html')

@app.route('/pm', methods=["GET", "POST"])
def pm():
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run()
