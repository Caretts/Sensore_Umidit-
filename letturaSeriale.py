import serial
import mysql.connector

#cnx = msql.connector.connect(user= 'Admin', password: 'Prova12345', host= '127.0.0.1', database= 'dati_sensori_lora')

mySerial = serial.Serial('COM6', 115200)
while True:
    BiteData = mySerial.readline()
    print(BiteData)
    prova = BiteData.decode()
    str(prova)
    #print(type(prova))
    #stringSplitted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stringSplitted = prova.split(" ")
    print(stringSplitted)
    SensorId = stringSplitted[0]
    print("Sensor ID: ", SensorId)
    #print(len(stringSplitted))
    SoilIndex = stringSplitted[4].split(":")
    print("Soil index: ", SoilIndex[1])
    H = stringSplitted[5].split(":")
    print("Humidity: ", H[1])
    T = stringSplitted[6].split(":")
    print("Temperature: ", T[1])
    SoilHum = stringSplitted[7].split(":")
    print("Soil humidity: ", SoilHum[1])
    Battery = stringSplitted[8].split(":")
    print("Battery: ", Battery[1])
