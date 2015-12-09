Phidgeter - logging, network, display and convenience functions for
Phidgets.

Usage:

Work with relays:

    import phidgeter
    phd_relay = phidgeter.Relay()
    phd_relay.toggle_two()
    phd_relay.one_on()

Emit data from a Phidget IR sensor on the command line:
   
    python scripts/ir_demo.py

Visualize the data with the ![BlueGraph] (https://github.com/WasatchPhotonics/BlueGraph, "BlueGraph package"):

    python scripts/TempGraph.py

![BlueGraph Screenshot] (/docs/IR_Temp_BlueGraph.gif "IR Temp BlueGraph screenshot")
