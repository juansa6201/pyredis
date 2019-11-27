import redis
import time

conexion = redis.Redis(host='localhost', port='6379', db=0)
pubsub = conexion.pubsub()
pubsub.subscribe('channel')

print('Introduzca con que frecuencia se consultaran los mensajes')
timer = float(input())

while True:
    message = pubsub.get_message()
    if message:
        print('Canal: ' + str(message['channel']) + ' || Mensaje: ' + str(message['data']))
    time.sleep(timer)