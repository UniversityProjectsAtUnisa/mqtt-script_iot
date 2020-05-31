import paho.mqtt.client as mqtt
import time
from ora import Ora, Interval


enabled = False
lastSent = None
interval = Interval.empty()

def publish_new(message, enabled):
    global lastSent
    if enabled == False:
        message = str(enabled)
    if lastSent != message:
        client.publish("new/dnd", str(message), qos=1, retain=True)
        print('Published:', message)
        lastSent = str(message)


def on_connect(client, userdata, flags, rc):
    client.subscribe("dnd/times")
    client.subscribe("dnd/enabled")


def on_message(client, userdata, msg):
    topic, payload = msg.topic, msg.payload
    print(topic, payload)
    global interval
    global enabled
    if topic == 'dnd/times':
        o1, o2 = payload.decode().split()
        interval = Interval(Ora(o1), Ora(o2))
        publish_new(interval.isNow(), enabled)
    elif topic == 'dnd/enabled':
        enabled = True if payload.decode() == 'true' else False
        publish_new(interval.isNow(), enabled)


try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print("Trying to connect")
    client.connect("test.mosquitto.org")
    client.loop_start()
    while True:
        time.sleep(15)
        publish_new(str(interval.isNow()), enabled)

except Exception as e:
    print('exception:', e)
finally:
    client.loop_stop()
