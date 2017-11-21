import time
def get_temp(sensor):
    fi = open(sensor)
    try:
        data = fi.read()
    finally:
        fi.close()
    try:
        value = float(data.split('\n')[1].split(' ')[9][2:])/1000
    except IndexError as ex:
        print data
        raise
    return value

while True:
    print get_temp('/sys/bus/w1/devices/28-03166391e2ff/w1_slave')
    time.sleep(0.5)

