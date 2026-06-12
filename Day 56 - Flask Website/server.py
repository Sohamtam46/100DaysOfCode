from flask import Flask,render_template

app = Flask(__name__)

# @app.route("/")
# def dog_home():
#     return render_template('dogs.html')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
