# Aplicación Web MyCrypto

- Programa hecho en python con el framework Flask, App MyCrypto, con motor de base de datos SQLite

## En su entorno de python ejecutar el comando

```
pip install -r requirements.txt
```
las libreria utilizada flask https://flask.palletsprojects.com/en/2.2.x/


## Renombrar el archivo .env_template a .env y agregar las siguientes lineas
```
FLASK_APP=main.py
FLASK_DEBUG=true
```
## Renombrar el archivo .config_template a .config y agregar las siguientes lineas
```
ORIGIN_DATA = 'Data/Movimientos.sqlite'
API_KEY =  'Aqui ponga su clave'
```
## Ejecucion con el .env
```
flask run
```
## Comando para ejecutar el servidor:
```
flask --app main run
```

## Comando para actualizar el servidor con cambios de codigo en tiempo real

```
flask --app main --debug run
```

## Comando especial para lanzar el servidor en un puerto diferente
- Esto se utiliza en el caso que el puerto 5000 este ocupado

```
flask --app main run -p 5001
```

## Comando para lanzar en modo debug y con puerto cambiado
```
flask --app main --debug run -p 5001
```