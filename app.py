from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask is frábært...</h1><a href ="/sida1">Síða 1<a/></h1><a href ="/sida2">Síða 2<a/>'

@app.route('/sida1')
def sida1():
    return '<a href="/"> Aftur á forsíðu</a><br><h1>Síða númer 1...</h1>'

@app.route('/sida2')
def sida2():
    return render_template("http.html")

if __name__ == "__main__":
	app.run(debug = True)