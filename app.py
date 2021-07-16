'''
Import package or module area
'''
from flask import (
    Flask,
    render_template,
)

# Creating instance of Flask class 
app = Flask(__name__)

posts = [
    {"name":"Tejas Dixit",
     "content":"Inside templates you also have access to the config,\
      request, session and g 1 objects as well as the url_for() and get_flashed_messages() functions.",
      "date":"17 nov 2001"},
      {"name":"Vignesh Gawali",
     "content":"Inside templates you also have access to the config,\
      request, session and g 1 objects as well as the url_for() and get_flashed_messages() functions.",
      "date":"18 nov 2001"},
      {"name":"Datta kale",
     "content":"Inside templates you also have access to the config,\
      request, session and g 1 objects as well as the url_for() and get_flashed_messages() functions.",
      "date":"19 nov 2001"},
      {"name":"Kunal jagate",
     "content":"Inside templates you also have access to the config,\
      request, session and g 1 objects as well as the url_for() and get_flashed_messages() functions.",
      "date":"18 nov 2001"},      
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about()->None:
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True,)