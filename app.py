from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tickets = []

@app.route('/')
def home():
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=['POST'])
def create_ticket():
    issue = request.form['issue']
    tickets.append({"id": len(tickets)+1, "issue": issue, "status": "Open"})
    return redirect('/')

@app.route('/resolve/<int:id>')
def resolve_ticket(id):
    for t in tickets:
        if t['id'] == id:
            t['status'] = "Resolved"
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)