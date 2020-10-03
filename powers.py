from flask import Flask
app = Flask(__name__)

@app.route('/powers/<int:n>')

# def bala(n=12):
# 	return ', '.join(str(3**i)for i in range(n))

def powers(n=10):
	return ', '.join(str(2**i)for i in range(n))
