
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
from ..componentes import verificador

class VistaSensores(Resource):
    @jwt_required()
    def post(self):
        uid = get_jwt_identity()
        if(verificador.validaUsuario(uid,request.path)):
            return "ok operacion sensores"
        else:
            return "sin permisos operacion sensores"


class VistaAutorizacion(Resource):

    def post(self):
        if(verificador.validaUsuario(request.json["id_usuario"],request.path)):
            token = verificador.generaToken(request.json["id_usuario"])
            return {'token':token}
        else:
            return "usuario no autorizado"

class VistaReglas(Resource):
    @jwt_required()
    def post(self):
        uid = get_jwt_identity()
        if(verificador.validaUsuario(uid,request.path)):
            return "ok operacion reglas"
        else:
            return "sin permisos operacion reglas"

