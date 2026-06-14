# test_hardware_rig.py

def test_instruments_identify_correctly(multimeter, power_supply):
    """Verify that both instruments respond to standard SCPI identity queries."""
    dmm_idn = multimeter.query("*IDN?")
    ps_idn = power_supply.query("*IDN?")
    
    assert "Digital Multimeter" in dmm_idn
    assert "Programmable Power Supply" in ps_idn

def test_voltage_measurement_within_bounds(multimeter):
    """Simulate checking a 3.3V power rail on a circuit board."""
    raw_reading = multimeter.query("MEASure:VOLTage:DC?")
    voltage = float(raw_reading)
    
    # Assert that the voltage is 3.3V +/- 5% tolerance
    assert 3.135 <= voltage <= 3.465

def test_power_supply_state_toggle(power_supply):
    """Verify we can turn the power supply on and its internal state registers it."""
    # Check initial state
    initial_state = power_supply.query("OUTPUT:STATE?")
    assert initial_state == "OFF"
    
    # Act: Turn it on
    power_supply.write("OUTPUT:STATE ON")