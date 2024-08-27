import time

import adafruit_dht
import board

def get_data():  
    data = {}
    temp_sum = 0
    humidity_sum = 0
    counter = 1

    try:
        # initialize sensor
        DHT_SENSOR = adafruit_dht.DHT22(board.D4)
        while (counter <= 5):
            try:
                temperature = DHT_SENSOR.temperature
                humidity = DHT_SENSOR.humidity
                if humidity is not None and temperature is not None:
                    print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))

                    # add data to dict
                    data[counter] = {
                        'temperature': temperature,
                        'humidity': humidity
                    }
                    temp_sum += temperature
                    humidity_sum += humidity
                else:
                    print("Sensor failure. Check wiring.")
            except RuntimeError as error:
                print(f'RuntimeError: {error}') 
                continue           
            time.sleep(1)
            counter += 1
    finally:
        # free sensor
        DHT_SENSOR.exit()


    # calculate averages
    if counter > 1: # if there were successful readings
        avg_temperature = temp_sum / (counter - 1)
        avg_humidity = humidity_sum / (counter - 1)
    else:
        avg_temperature = 0
        avg_humidity = 0

    rounded_humidity = round(avg_humidity, 1)
    rounded_temperature = round(avg_temperature, 2)
    
    data['average'] = {
        'temperature': rounded_temperature,
        'humidity': rounded_humidity
    }

    return data if data else {}