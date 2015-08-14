Phidgeter - logging and convenience functions for phidgets devices.

Instead of using the demonstrated concepts of attachment and detach
handlers, create wrappers. Usage:

phd_relay = phidgeter.Relay()
phd_relay.zero_on()
phd_relay.two_toggle()

