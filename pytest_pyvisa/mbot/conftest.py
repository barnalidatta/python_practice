# conftest.py
import pytest
import serial
import pyvisa
import time

# !!! Change this to match your computer's port (e.g., 'COM3' on Windows or '/dev/tty.usbserial' on Mac)
MBOT_PORT = "COM5" 
BAUDRATE = 115200

@pytest.fixture(scope="session")
def mbot_serial():
    """Fixture to manage the physical USB serial connection to your real mBot."""
    print(f"\n[SETUP] Connecting to mBot on {MBOT_PORT}...")
    ser = serial.Serial(MBOT_PORT, BAUDRATE, timeout=1.0)
    
    # Optional: Clear initial buffers and give the mBot bootloader 1 sec to stabilize
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1.0)
    
    yield ser
    
    # Teardown: Always stop motors safely before closing port!
    print("\n[TEARDOWN] Stopping mBot safely & disconnecting...")
    try:
        ser.write(b"M1 0\nM2 0\n") # Generic example command to kill motors
    except:
        pass
    ser.close()

@pytest.fixture(scope="function")
def virtual_multimeter():
    """Fixture to talk to your pyvisa-simulated digital multimeter."""
    rm = pyvisa.ResourceManager("simulation_devices.yaml@sim")
    instr = rm.open_resource("ASRL1::INSTR")

    # Force the line endings directly on the connection instance
    instr.read_termination = "\n" # type: ignore
    instr.write_termination = "\n" # type: ignore
    
    yield instr
    instr.close()