from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import userRegister
from resources.item import Itemlist , Item
from resources.constants import UPLOAD_DIRECTORY ,SECRET


app = Flask(__name__)
app.secret_key = SECRET
api = Api(app)
jwt =JWT(app,authenticate,identity) # /auth


api.add_resource(Itemlist,'/files')
api.add_resource(Item,'/files/<name>')
api.add_resource(userRegister,'/register')

app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

if __name__ == "__main__":
    app.run("0.0.0.0",port=5001,debug=True)