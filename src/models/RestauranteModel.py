from database.db import get_connection
from .entities.Pago import Pago


class RestauranteModel():

    @classmethod
    def get_pagos(self):
        try:
            connection = get_connection()
            pagos = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM siatasiata.restaurante;")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    print(row[1],row[2],row[4],row[3],row[5],row[0])
                    pago = Pago(row[0], row[1], row[2], row[3], row[4], row[5])
                    
                    pagos.append(pago.to_JSON())
            connection.close()
            return pagos

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_pagos(self, pago):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:

                cursor.execute("""INSERT INTO siatasiata.restaurante("nombreRestaurante","identificacionUsuario", "menu",
                "valorMenu", "valorPagado","fechaPago")
                                VALUES (%s,%s,%s,%s,%s,%s)""", (pago.nombreRestaurante, pago.identificacionUsuario, pago.menu, pago.valorMenu, pago.valorPagado, pago.fechaPago))
                affected_rows= cursor.rowcount
                print(affected_rows)
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
