Como levantar la API

-crear un entorno virtual de python para que se ejecute la API
vamos a la carpeta donde se encuentra el proyecto en la terminal
una vez alli copiamos el comando:
python -m virtualenv venv
-activamos el entorno virtual con el comando:
.\venv\Scripts\activate
-actualizar el pip para la instalacion de las librerias con el comando:
python -m pip install -U pip
-instalamos las librerias necesarias para el proyecto: 
flask,flask-cors, psycopg2 , python-decouple,python-dotenv

-crear un usuario: "siata" con clave: "siata"
-crear la BD en postgreSQL con el nombre DB_restaurante
-crear un schema con el nombre "siatasiata"
-crear una tabla con el nombre restaurante

creamos la estructura de la tabla con el comando SQL:

ALTER TABLE IF EXISTS siatasiata.restaurante
    ADD COLUMN nombreRestaurante character varying(100);
    ADD COLUMN identificacionUsuario bigint,
    ADD COLUMN menu text,
    ADD COLUMN valorMenu bigint,
    ADD COLUMN fechaPago bigint,
    ADD COLUMN valorPagado date

Para recibir las peticiones usaremos un cliente REST, en este caso usé insomnia

Una vez en el software crearemos 2 peticiones una para el metodo GET y otra para el POST

a la peticion GET le daremos la URL: http://127.0.0.1:6969/api/Restaurante/

a la peticion POST le daremos el URL: http://127.0.0.1:6969/api/Restaurante/add
como parametro le pasaremos un objeto JSON tal que:

{
    "nombreRestaurante": "El antojo",
    "identificacionUsuario": 1039472567,
    "menu": "pastas,carnes, 3 bebidas",
    "valorMenu": 72000,
    "valorPagado": 71000,
    "fechaPago": "22/12/2021"
}



