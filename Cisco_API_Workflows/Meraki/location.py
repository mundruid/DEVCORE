from flask import Flask, json, request

# init a flash web app
app = Flask(__name__)

# validate web server from meraki
@app.route('/', methods=['GET'])
def get_validator():
    return "d6aa8dcdc508ca5ded5ab54032fb3680cb2e3cf5"

# receive location data
@app.route('/', methods=['POST'])
def get_cmxJSON():
    cmxdata = request.json

    # Determine device type
    if cmxdata['type'] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif cmxdata['type'] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")

    return "CMX POST Received"


if __name__ == '__main__':
    # run app
    app.run(port=5000, debug=False)
                                    


