from sia import create_app
from flask import render_template

app = create_app()

@app.errorhandler(404) 

def not_found(e): 
  return render_template("404.html") , 404


if __name__ == '__main__':
    app.run(debug=True)
