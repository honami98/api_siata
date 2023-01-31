from flask import Blueprint, jsonify, request

from models.RestauranteModel import RestauranteModel

from models.entities import Pago

from datetime import datetime

main = Blueprint('restaurante_blueprint', __name__)


@main.route('/')
def get_Pagos():

    try:
        pagos=RestauranteModel.get_pagos()
        return jsonify(pagos)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/add',methods=['POST'])
def add_Pagos():

    def isnumber(cadena):
        try:
            int(cadena)
            return True
        except ValueError:
            return False
    def isstring(cadena):
        try: 
            return cadena.isalpha()
        except ValueError:
            return False

    try:
        nombreRestaurante= str(request.json['nombreRestaurante'])
        identificacionUsuario=int(request.json['identificacionUsuario'])
        menu=str(request.json['menu'])
        valorMenu=int(request.json['valorMenu'])
        valorPagado=int(request.json['valorPagado'])
        fechaPago=request.json['fechaPago']
        fechaPagoReal=datetime.strptime(fechaPago,"%d/%m/%Y")

        nombreConvertido=nombreRestaurante.replace(' ', '')
        menuConvertido=menu.replace(' ', '')
        menuConvertido2=menuConvertido.replace(',','')


        pago=Pago.Pago(nombreRestaurante,identificacionUsuario,menu,valorMenu,valorPagado,fechaPagoReal)

        affected_rows=RestauranteModel.add_pagos(pago)

        
        if(isstring(nombreConvertido)==True and isnumber(identificacionUsuario==True) and menuConvertido2.isalnum()==True
        and isnumber(valorMenu)==True and isnumber(valorPagado==True)):
            if(valorMenu-valorPagado==0):
                
                if(affected_rows==1):                   
                    return jsonify({'respuesta': str("gracias por pagar todo tu arriendo")}), 200
                else:
                    return jsonify({'message': "Error on Insert"}),500
            elif (valorMenu-valorPagado>0):
                deuda=valorMenu-valorPagado
                fechaConvertida=fechaPago.split("/")
                diaFecha=int(fechaConvertida[0])
                
                if(diaFecha % 2 !=1):
                    return jsonify({'respuesta': str("lo siento pero no se puede recibir el pago por decreto de administración")}), 400
                else:
                    return jsonify({'respuesta': str("gracias por tu abono, sin embargo recuerda que te hace falta pagar $"+str(deuda))})

        else:
            return jsonify({'respuesta': str("Formato de nombre incorrecto")}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
