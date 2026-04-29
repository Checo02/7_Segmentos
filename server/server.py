from flask import Flask, send_from_directory
import serial
import time
import os

app = Flask(__name__)

PUERTO_ARDUINO = "/dev/ttyUSB0"  # Cambia a /dev/ttyACM0 si ese es tu puerto
BAUDIOS = 9600

arduino = None


def conectar_arduino():
    global arduino

    try:
        arduino = serial.Serial(PUERTO_ARDUINO, BAUDIOS, timeout=1)
        time.sleep(2)
        print("Arduino conectado en", PUERTO_ARDUINO)
    except Exception as e:
        arduino = None
        print("No se pudo conectar al Arduino:", e)


conectar_arduino()


@app.route("/")
def index():
    return send_from_directory(os.getcwd(), "index.html")


@app.route("/<num>")
def numero(num):
    global arduino

    print("Número recibido:", num)

    if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return "Número inválido", 400

    try:
        if arduino is None or not arduino.is_open:
            conectar_arduino()

        if arduino is None:
            return "Arduino no conectado", 500

        arduino.write(num.encode())
        return "ok"

    except Exception as e:
        return "Error serial: " + str(e), 500


app.run(host="0.0.0.0", port=5000)
