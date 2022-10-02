from flaskr import create_app
from flask_restful import Api

from flaskr.vistas.vistas import VistaReglas
from .vistas import VistaSensores
from .vistas import VistaAutorizacion
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()


api = Api(app)
api.add_resource(VistaSensores,'/sensores')
api.add_resource(VistaAutorizacion,'/autorizacion')
api.add_resource(VistaReglas,'/reglas')

jwt = JWTManager(app)