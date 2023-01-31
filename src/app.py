from flask import Flask

from config import config

from routes import RestauranteRoute


app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>" , 404
    


if __name__ == '__main__':
    
    app.config.from_object(config['development'])



    app.register_blueprint(RestauranteRoute.main, url_prefix='/api/Restaurante')

    app.register_error_handler(404,page_not_found)
    
    app.run(port=6969)
