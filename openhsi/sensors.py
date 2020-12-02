# AUTOGENERATED! DO NOT EDIT! File to edit: 06_sensors.ipynb (unless otherwise specified).

__all__ = ['Sensors']

# Cell
import time
import serial # pip install pyserial
import numpy

# Cell

class Sensors(object):

    def __init__(self,baudrate=19200,port="/dev/ttyTHS0"):
        self.ser = serial.Serial(port=port,
                                baudrate=baudrate,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                )
        self.ser.flushInput()
        time.sleep(1) # Wait a second to let the port initialize

    def readSerial(self):

        if ser.inWaiting() > 0:

            self.data = ser.readline().decode()
            #print(data.decode())

            #if data == "\r".encode():
            #    ser.write("\n".encode())

    def loopReadSerial(self):
        try:
            print("starting transmission")
            ser.write("UART Demonstration Program\r\n".encode())

            while True:
                self.readSerial()

                print(self.data)
                break

        except KeyboardInterrupt:
            print("Exiting Program")

        except Exception as exception_error:

            print("Error occurred. Exiting Program")
            print("Error: " + str(exception_error))

        finally:
            self.ser.close()

