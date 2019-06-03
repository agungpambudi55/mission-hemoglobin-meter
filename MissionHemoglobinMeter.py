'''
Created on Jun 2019
'''

import serial

try:
    serCom = serial.Serial('/dev/ttyUSB0', 9600)
    
    dataRow0 = serCom.readline()
    dataRow1 = serCom.readline()
    dataRow2 = serCom.readline()
    dataRow3 = serCom.readline()
    dataRow4 = serCom.readline()
    dataRow5 = serCom.readline()

    hb = dataRow2.decode('utf-8').replace('HB:','').replace('g/dL','').replace('\r\n','')
    hct = dataRow3.decode('utf-8').replace('HCT:','').replace('%','').replace('\r\n','')

    print('HB {} g/dL , HCT {} %'.format(hb, hct))    
        
except KeyboardInterrupt:
    print('Terminate')
except:
    print('Something went wrong')
finally:
    serCom.close()