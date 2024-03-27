import serial
import time


if __name__ == '__main__':
    # ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    # ser.flush()
    # ser.write(b"1\n")

    ser = serial.Serial('COM3', 9600, timeout=1)
    print(ser.isOpen())

    ser.write(b'none\n')

    ser.write(b'open_claw\n')
    time.sleep(2)
    ser.write(b'position_down_left\n')
    time.sleep(5)
    ser.write(b'close_claw\n')
    time.sleep(2)
    ser.write(b'home_position\n')
    time.sleep(5)
    ser.write(b'position_top_left\n')
    time.sleep(5)
    ser.write(b'open_claw\n')
    time.sleep(2)
    ser.write(b'home_position\n')
    time.sleep(5)
    ser.write(b'close_claw\n')
    time.sleep(2)

    ser.write(b'open_claw\n')
    time.sleep(2)
    ser.write(b'position_top_left\n')
    time.sleep(5)
    ser.write(b'close_claw\n')
    time.sleep(2)
    ser.write(b'home_position\n')
    time.sleep(5)
    ser.write(b'position_down_left\n')
    time.sleep(5)
    ser.write(b'open_claw\n')
    time.sleep(2)
    ser.write(b'home_position\n')
    time.sleep(5)
    ser.write(b'close_claw\n')
    time.sleep(2)

    # ser.write(b'position_down_right\n')
    # ser.write(b'position_down_left\n')

    # ser.write(b'position_top_right\n')
    # ser.write(b'position_top_left\n')

    # ser.write(b'open_claw\n')
    # ser.write(b'close_claw\n')
    # ser.write(b'home_position\n')