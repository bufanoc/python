from flask import Flask as f
app = f(__name__)
@app.route('/')

def home():
    return "Mobiieus inc"
if __name__ == "__main__":
    app.run(debug=True)
