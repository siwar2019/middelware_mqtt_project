
import paho.mqtt.client as mqtt




MQTT_HOST = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "sensor01/temperature"

 

def on_log(client, userdata, level, buf):
    print("log: ",buf)


def on_publish(client, userdata, mid):# just apres l'envoi de msg il affiche ..
    print ("Message Published...\n")

def on_connect(client, userdata, flags, rc):
    client.publish(MQTT_TOPIC, "siwar")
     


mqttc = mqtt.Client()

mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

mqttc.on_log=on_log


mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

mqttc.loop_forever()

