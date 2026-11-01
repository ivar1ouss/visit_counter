from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'super_secret_visit_key'


@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    return render_template('index.html', visits=session['visits'])


@app.route('/reset')
def reset():
    session.pop('visits', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)