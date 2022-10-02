from ast import operator
from flask_jwt_extended import  create_access_token
class verificador:

   

    def generaToken(idUsuario):
        return create_access_token(identity=idUsuario)
    

    def validaUsuario(idUsuario,operacion):
        respuesta = True
        operacion = operacion.replace("/","")
        permisos = {
            '12345':['sensores','autorizacion'],
            '99999':['sensores','autorizacion','reglas']
        }

        if(idUsuario not in permisos):
            respuesta = False
        else:
            if(operacion not in permisos[idUsuario]):
               respuesta = False 

        return respuesta

