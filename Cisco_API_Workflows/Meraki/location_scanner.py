from flask import Flask, json, request

# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def get_validator():
    return "<Your validator from meraki dashboard>"

# receive location data
@app.route("/", methods=["POST"])
def get_locationJSON():
    global locationdata

    if not request.json or not "data" in request.json:
        return ("invalid data", 400)

    locationdata = request.json
    pprint(locationdata, indent=1)
    print("Received POST from ", request.environ["REMOTE_ADDR"])

    # Verify secret
    if locationdata["secret"] != secret:
        print("secret invalid:", locationdata["secret"])
        return ("invalid secret", 403)

    else:
        print("secret verified: ", locationdata["secret"])

    # Verify version
    if locationdata["version"] != version:
        print("invalid version")
        return ("invalid version", 400)

    else:
        print("version verified: ", locationdata["version"])

    # Determine device type
    if locationdata["type"] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif locationdata["type"] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")
        return ("invalid device type", 403)

    # Return success message
    return "Location Scanning POST Received"
