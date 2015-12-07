Phidgeter - logging, network, display and convenience functions for
Phidgets.



Usage:

Work with relays:

    import phidgeter
    phd_relay = phidgeter.Relay()
    phd_relay.toggle_two()
    phd_relay.one_on()

Emit data from a Phidget IR sensor on the network:
   
    python scripts/ir_demo.py

Visualize the data with the GraphWrap package:

- graphwrap fast/slow display gif -
