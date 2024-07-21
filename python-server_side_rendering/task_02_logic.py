from flask import Flask, render_template
from json import load

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json') as f:
        data = load(f)
        items = data.get('items') or []
        
    return render_template('items.html', items=items)

app.run(port=5000, debug=True)