from flask import Flask, jsonify
from flasgger import Swagger
app=Flask(__name__)
swagger=Swagger(app)
@app.route('/sum')
def sum():
    a=3
    b=4
    return str(a+b)
@app.route('/')
def home():
    """
    ___
    responses:
     200:
      description:Главная страница
    """
    return "Сервер жумыс истеп тур"
if __name__ == '__main__':
    app.run(port=5000)