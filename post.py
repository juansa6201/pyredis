import redis
import time

conexion = redis.Redis(host='redis', port='6379', db=0)

iterator = 0

while True:
    conexion.publish('channel', f'mensaje {iterator}')
    print(f'Mensaje: {iterator}')
    iterator += 1
    time.sleep(2)