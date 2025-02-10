from machine import UART, Pin
import time
import network
import urequests
import dht

# Define your WiFi credentials
ssid = "12345678"
passwd = "12345678"

# Firebase URL to post data
firebase_url = 'https://sensordataapp-13d9a-default-rtdb.firebaseio.com/sensorData.json'

# Initialize DHT11 sensor on pin 15
sensor = dht.DHT11(Pin(15))

# Initialize PIR sensor on pin 14
pir_sensor = Pin(14, Pin.IN)
  
# Initialize buzzer on pin 13
buzzer = Pin(13, Pin.OUT)

# Initialize UART for HC-05 communication
uart = UART(0, baudrate=9600, tx=0, rx=1)

detection_enabled = False
i=1

# Function to connect to WiFi
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    print(wlan.ifconfig())

# Connect to WiFi
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
print("Connection successful.")

while True:
    try:
        pir = 0
        if uart.any():
            command = uart.read()
            print(command)
            if b"on" in command:
                detection_enabled = True
                print('Motion and temperature detection enabled.')
            elif b"off" in command:
                detection_enabled = False
                print('Motion and temperature detection disabled.')

        if detection_enabled:
            # Read PIR sensor
            pir_detected = pir_sensor.value()

            # If motion is detected, ring the buzzer
            if pir_detected:
                print('Motion detected! Ringing buzzer.')
                buzzer.on()  # Turn on the buzzer
                time.sleep(1)  # Keep the buzzer on for 1 second
                buzzer.off()
                pir = 1  # Set pir to 1 when motion is detected

            # Measure temperature and humidity
            sensor.measure()
            temp_c = sensor.temperature()
            temp_f = temp_c * (9 / 5) + 32.0
            hum = sensor.humidity()

            # Calculate the heat index
            heat_index = (-42.379 + (2.04901523 * temp_f) + (10.14333127 * hum)
                          - (0.22475541 * temp_f * hum) - (0.00683783 * temp_f * temp_f)
                          - (0.05481717 * hum * hum) + (0.00122874 * temp_f * temp_f * hum)
                          + (0.00085282 * temp_f * hum * hum)
                          - (0.00000199 * temp_f * temp_f * hum * hum))

            # Round the heat index to one decimal place
            heat_index = round(heat_index, 1)

            # Print sensor readings
            print('Temperature: %3.1f C' % temp_c)
            print('Temperature: %3.1f F' % temp_f)
            print('Humidity: %3.1f %%' % hum)
            print('Heat Index: %3.1f F' % heat_index)

            # Get current time in ISO 8601 format
            current_time = time.time()
            time_tuple = time.localtime(current_time)
            time_string = "Date: {:04d}-{:02d}-{:02d} Time:{:02d}:{:02d}:{:02d}".format(
                time_tuple[0], time_tuple[1], time_tuple[2],
                time_tuple[3], time_tuple[4], time_tuple[5])

            # Prepare data dictionary
            sensor_data = {
                "l"+str(i): {
                    "humidity": hum,
                    "temperature": temp_c,
                    "heatIndex": heat_index,
                    "timestamp": time_string,
                    "pir": bool(pir_detected)
                }
            }
            

            # Send data to Firebase
            response = urequests.patch(firebase_url, json= sensor_data)
            response.close()
            uart_data = "Temperature: {:.1f} C, Humidity: {:.1f} %, Heat Index: {:.1f} F, PIR: {}\n".format(temp_c, hum, heat_index, bool(pir_detected))
            uart.write(uart_data)
            print("Data sent to Bluetooth")
            time.sleep(1)
            
            print("l"+str(i)+"sent")
            i=i+1
            
    except OSError as e:
        print('Failed to read sensor.')
        uart1="data not sent"
        uart.write(uart1)
