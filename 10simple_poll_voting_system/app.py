from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Poll question and options
poll_question = "What is your favorite fruit?"
poll_options = ["Apple", "Banana", "Orange", "Mango"]

# Vote counts dictionary
votes = {option: 0 for option in poll_options}

@app.route('/')
@app.route('/poll/', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        selected = request.form.get('option')
        if selected in votes:
            votes[selected] += 1
            return redirect(url_for('results', vote=selected))
    return render_template('poll.html', question=poll_question, options=poll_options)

@app.route('/results/')
def results():
    user_vote = request.args.get('vote')
    return render_template('results.html', votes=votes, user_vote=user_vote)

if __name__ == "__main__":
    app.run(debug=True)
