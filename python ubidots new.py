# import RPi.GPIO as GPIO
# import  time
# 
# import time
# import math
# import random
# import time
# 
# import requests
# from ubidots import ApiClient
# 
# # Pin definition
# touchSensorPin = 13
# pirSensorPin = 16
# 
# TOKEN = "BBFF-Zt0sPxgse1FsUiDFBVaRDHQubmVUXe"  # Put your TOKEN here
# DEVICE_LABEL = "technomedia"  # Put yourBBFF-Zt0sPxgse1FsUiDFBVaRDHQubmVUXe device label here
# VARIABLE_LABEL_1 = "touch sensor"  # Put your first variable label here
# VARIABLE_LABEL_2 = "pir sensor"  # Put your second variable label here
# VARIABLE_LABEL_3 = "map"
# 
# 
# def build_payload(variable_1, variable_2, variable_3, value_1, value_2):
#     # Creates a random gps coordinates
#     lat = random.randrange(34, 36, 1) + \
#         random.randrange(1, 1000, 1) / 1000.0
#     lng = random.randrange(-83, -87, -1) + \
#         random.randrange(1, 1000, 1) / 1000.0
#     payload = {variable_1: value_1,
#                variable_2: value_2,
#                variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}
#     
#     return payload
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# 
# def post_request(payload):
#     # Creates the headers for the HTTP requests
#     url = "http://industrial.api.ubidots.com"
#     url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
#     headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
# 
#     # Makes the HTTP requests
#     status = 400
#     attempts = 0
#     while status >= 400 and attempts <= 5:
#         req = requests.post(url=url, headers=headers, json=payload)
#         status = req.status_code
#         attempts += 1
#         time.sleep(1)
# 
#     # Processes results
#     print(req.status_code,req.json())
#     if status >= 400:
#         print("[ERROR] Could not send data after 5 attempts, please check \
#             your token credentials and internet connection")
#         return False
# 
#     print("[INFO] Request made properly, your device is updated")
#     return True
# 
# 
# 
# def setup_pin():
#     # Setup pin output/input
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(touchSensorPin, GPIO.IN)
#     GPIO.setup(pirSensorPin, GPIO.IN)
# 
# def read_sensor_touch():
#     # True: Ada kebocoran gas / False: Tidak ada kebocoran gas
#     value = GPIO.input(touchSensorPin) 
# 
#     return value
# 
# def read_sensor_pir():
#     # True: Ada kebocoran gas / False: Tidak ada kebocoran gas
#     value = GPIO.input(pirSensorPin) 
# 
#     return value
# 
# if __name__ == '__main__':
#     setup_pin()
#     try:
#         while True:
#             touch_sensor_value = read_sensor_touch()
#             pir_sensor_value = read_sensor_pir()
#             
#             print(f'Touch Sensor: {touch_sensor_value}, PIR Sensor: {pir_sensor_value}')
#             
#             payload = build_payload(
#             VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, touch_sensor_value, pir_sensor_value)
#             
#             print("[INFO] Attemping to send data")
#             post_request(payload)
#             print("[INFO] Finished")
#     except KeyboardInterrupt:
#         print('Exit!')