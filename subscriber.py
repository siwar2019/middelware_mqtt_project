
import paho.mqtt.client as mqtt # importation du package paho.mqtt.client

MQTT_HOST = "iot.eclipse.org" #broker en ligne 
MQTT_PORT = 1883 # Le port sur le quel MQTT fonctionne (il y a un autre port 8883 pour les communication chiffree)
MQTT_KEEPALIVE_INTERVAL = 45 #
MQTT_TOPIC = "sensor01/temperature" # topic/sujeto

def on_log(client, userdata, level, buf): #l'impression des logs 
    print("log: ",buf)
 
def on_connect(client, userdata, flags, rc):# Connexion au broker + souscription 
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg): # 1-action lors de la reception du msg
    print("\nTopic :" +msg.topic) # 1.1 impression du topic
    print("\n\n Le message  :" +msg.payload.decode('utf-8') +"\n") #1.2 impression du message 
    
    client.disconnect() #deconnexion just

# Initiate MQTT Client
mqttc = mqtt.Client() # creation  d'une instance client 
  


# Register publish callback(a chercher) function 
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log=on_log


# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)#connxion au broker avec les parametre pre-definie  



# Loop forever
mqttc.loop_forever()  #je me rappele pas exactement ,chnia el 7aja el sera en boucle toit le temps! lenvoie de msg en boucle?! attend je cherche  nnnn c pas grave , je cherche moi meme miselch ok je te repond apres meci 7ta ana je rafrechi ma memoire hh ok b1




