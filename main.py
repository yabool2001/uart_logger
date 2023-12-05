import serial
import time
import modules.my_serial as my_serial

import sys
sys.path.append ( "/Users/mzeml/python/sim_nmea_uart/modules/" )

import modules.my_serial as my_serial

#nmea_source_filename = "source/2023.10.01.22.57_L86.txt"
#nmea_source_filename = "source/2023.10.28.03_L86.bin"
nmea_source_filename = "source/2023.10.28.04_L86.bin"
#nmea_source_filename = "source/2023.10.28.04-1_L86.bin"

# Otwórz port szeregowy COM
com = serial.Serial ()
my_serial.set_serials_cfg ( com , 115200 , 'STLink' )
my_serial.open_serial_ports ( com )

#with open ( nmea_source_filename , 'r' ) as f :
#    lines = f.readlines ()
#    for line in lines :
#        #com.write ( line.encode() )
#        com.write ( line.encode() )
#        #com.write ( line )
#        print ( com.read (1) )
#        #time.sleep ( 0.1 )

with open ( nmea_source_filename , 'r' ) as f :
    nmea = f.read ()
    for c in nmea :
        com.write ( c.encode() )
        #print ( com.read (1) )
#        time.sleep ( 0.1 )


my_serial.close_serial_ports ( com )
