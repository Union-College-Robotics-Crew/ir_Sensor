@author: Edwin Garcia-Flores
  
import board
import analogio
from ulab import numpy as np
import time
class IR_sensor:
    
    def __init__(self, pinNum):
        adc= analogio.AnalogIn(pinNum)
        self.port = adc
        
    def __str__(self):
        return (self.ir_reading(),)
    
    #adc = analogio.AnalogIn(port)
    def median(self, lst = []):
        return np.median(lst)
        
    def ir_reading(self):
        adc_readings = []
        while True:
            adc_readings.append(self.port.value)
           # print("18ms have passed")
            time.sleep(.0018)
            if len(adc_readings) % 10 == 0:
                return_val= self.median(np.array(adc_readings))
                adc_readings=[]
                return return_val

# ir1 = IR_sensor(board.GP28)
# print(ir1)
# ir1.ir_reading()

def test_ir(amt_readings):
  ir_test = IR_sensor(board.GP28)
  for i in range(amt_readings):
    print(ir_test)
    
test_ir(1000)
