# tello-udp
Connecting to the Ryze Tello with udp and python

## Usage
* Connect to the tello's network
* ```python tello.py ```
* now you can send messages to the tello.

## Message Guide
* ```connect``` = reconnect and exit emergency mode
* ```takeoff``` = take off, hovering at approximately 1 meter
* ```land``` = gradually land
* ```emergency``` = immediately stop all motors, causing the drone to fall out of the sky
* ```forward x``` = go forward ```x``` centi-meters (cm)
* ```back x``` = go back ```x``` cm
* ```left x``` = go left ```x``` cm
* ```right x``` = go right ```x``` cm
* ```ccw x``` = rotate counter-clockwise ```x``` degrees
* ```cw x``` = rotate clockwise ```x``` degrees
* ```flip f/b/l/r``` = flip forward/back/left/right


## Known Issues
* The Tello connection will time out in 15 seconds of no messages, causing the drone to land.
This should be resolved when threading to periodically send messages is implemeneted.
