from utils.DateFormat import DateFormat

class Pago():

    

    def __init__(self, nombreRestaurante, identificacionUsuario, menu, valorMenu, valorPagado, fechaPago)->None: 
        self.nombreRestaurante = nombreRestaurante
        self.identificacionUsuario = identificacionUsuario
        self.menu = menu
        self.valorMenu = valorMenu
        self.valorPagado = valorPagado
        self.fechaPago = fechaPago

    def to_JSON(self):
        return {
        'nombreRestaurante': self.nombreRestaurante,
        'identificacionUsuario': self.identificacionUsuario,
        'menu':self.menu,
        'valorMenu': self.valorMenu,
        'valorPagado': self.valorPagado,
        'fechaPago': DateFormat.convert_date(self.fechaPago)
    }
