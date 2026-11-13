from abc import ABC, abstractmethod 


class Sensor(ABC):
     @abstractmethod
     def get_reading(self):
         pass
        
class pHSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"

my_sensor1 = pHSensor()
my_sensor2 = TempSensor()

def read():
    print(f"""--- Lab Inventory System ---
{my_sensor1.get_reading()}
{my_sensor2.get_reading()}""")

read()
