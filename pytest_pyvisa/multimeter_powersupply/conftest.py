# conftest.py
import pytest
import pyvisa

# Tell PyVISA to load our local simulated device configuration
SIMULATION_CONFIG = "simulation_devices.yaml@sim"

@pytest.fixture(scope="session")
def visa_manager():
    """Provides the VISA resource manager using the simulation backend."""
    return pyvisa.ResourceManager(SIMULATION_CONFIG)

@pytest.fixture(scope="function")
def multimeter(visa_manager):
    """Connects to our simulated multimeter, yields it, and closes connection."""
    instr = visa_manager.open_resource("ASRL1::INSTR")
    yield instr
    instr.close()

@pytest.fixture(scope="function")
def power_supply(visa_manager):
    """Connects to our simulated power supply and ensures it is turned off afterward."""
    instr = visa_manager.open_resource("USB0::0x1234::0x5678::MY12345678::0::INSTR")
    yield instr
    # Teardown safety: Always turn off power supplies after a test finishes!
    try:
        instr.write("OUTPUT:STATE OFF")
    except:
        pass
    instr.close()