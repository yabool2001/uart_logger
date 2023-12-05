import platform
import serial
import serial.tools.list_ports

def set_serials_cfg ( com , b , s ) :
    serial_ports =  serial.tools.list_ports.comports()
    for s_p in serial_ports:
        if s.lower () in s_p.description.lower () :
            if platform.system () == "Windows":
                com.port = s_p.name
            elif platform.system () == "Linux":
                com.port = '/dev/' + s_p.name
            else:
                print ( f"Error: No compatible os!")
    com.baudrate    = b
    com.bytesize    = serial.EIGHTBITS
    com.parity      = serial.PARITY_NONE
    com.stopbits    = serial.STOPBITS_ONE
    com.timeout     = 0.1

def close_serial_ports ( com ) :
    if com.is_open :
        try:
            com.close ()
        except serial.SerialException as e :
            print ( f"{com.name} port closing error: {str(e)}" )

def open_serial_ports ( com ) :
    try: 
        com.open ()
        print ( f"{com.name} port opened" )
    except serial.SerialException as e :
        print ( f"{com.name} port error opening: {str(e)}" )