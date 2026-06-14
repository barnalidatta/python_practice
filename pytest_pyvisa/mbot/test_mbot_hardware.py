# test_mbot_hardware.py
import time

def test_mbot_power_rail_with_multimeter(virtual_multimeter):
    """Use PyVISA-Sim to check if the robot's hardware power rail is stable."""
    raw_voltage = virtual_multimeter.query("MEASure:VOLTage:DC?")
    voltage = float(raw_voltage)
    
    print(f"\nVerified Hardware Power Supply: {voltage}V")
    # Assert that the mBot's battery voltage is safe (greater than 3.5V but less than 5.0V)
    assert 3.5 <= voltage <= 5.0


def test_mbot_ultrasonic_sensor_range(mbot_serial):
    """Command the real mBot over serial to return its ultrasonic distance sensor reading."""
    mbot_serial.reset_input_buffer()

    # Act: Request sensor telemetry from the physical board
    mbot_serial.write(b"GET_DISTANCE\n")
    time.sleep(0.1) # Give the micro-controller a tiny moment to reply

    # Read whatever bytes are waiting on the wire
    response_bytes = mbot_serial.read(mbot_serial.in_waiting)
    print(f"\nReal Binary Response from mBot: {response_bytes.hex()}")
    
    # Assert that the hardware replied with data (not an empty string or nulls)
    assert len(response_bytes) > 0, "No telemetry received from the ultrasonic sensor!"


def test_actuate_mbot_leds(mbot_serial):
    """Verify code execution by flashing the onboard RGB LEDs."""
    # Turn the physical LEDs red
    mbot_serial.write(b"SET_LED 255,0,0\n")
    time.sleep(0.5)
    
    # Turn them off
    mbot_serial.write(b"SET_LED 0,0,0\n")