import serial
from datetime import datetime
import modules.my_serial as my_serial

import sys
sys.path.append ( "/Users/mzeml/python/uart_logger/modules/" )

import modules.my_serial as my_serial

log_filename = "logs/2023.12.05.txt"

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


try:
    while com.is_open :
        # Odczytanie linii z portu COM
        line = com.readline ().decode ( 'utf-8' ).rstrip ( '\n' )

        if line:
            timestamp = datetime.now ().strftime ( '%Y.%m.%d %H:%M:%S:%f' )[:-3]

            # Otwarcie pliku w trybie aktualizacji i zapisanie linii
            with open ( log_filename , 'a' ) as f:
                f.write ( f'{timestamp},{line}\n' )
                f.flush()  # Zapewnienie natychmiastowego zapisu do pliku

except KeyboardInterrupt:
    print ( 'Przerwano przez użytkownika.' )

finally:
    # Zamknięcie portu COM
    my_serial.close_serial_ports ( com )
