import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
SENSORS = {
    "Gauche": {"TRIG": 22, "ECHO": 27},
    "Droite": {"TRIG": 23, "ECHO": 24},
    "Arrière": {"TRIG": 5, "ECHO": 6}
}

GPIO.setmode(GPIO.BCM)

# Initialisation des capteurs
for sensor in SENSORS.values():
    GPIO.setup(sensor["TRIG"], GPIO.OUT)
    GPIO.setup(sensor["ECHO"], GPIO.IN)

def measure_distance(trig, echo):
    """Mesure la distance avec un capteur ultrasonique."""
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()
    
    while GPIO.input(echo) == 1:
        stop_time = time.time()
    
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Distance en cm

    return round(distance, 2)

try:
    while True:
        distances = {name: measure_distance(sensor["TRIG"], sensor["ECHO"]) for name, sensor in SENSORS.items()}
        
        # Déterminer la direction avec la plus grande distance
        best_direction = max(distances, key=distances.get)
        
        # Affichage des distances et du choix de direction
        print(f"Distances (cm) - Gauche: {distances['Gauche']}, Droite: {distances['Droite']}, Arrière: {distances['Arrière']}")
        print(f"➡️ Direction recommandée : {best_direction} (Distance: {distances[best_direction]} cm)")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nArrêt du programme.")
    GPIO.cleanup()