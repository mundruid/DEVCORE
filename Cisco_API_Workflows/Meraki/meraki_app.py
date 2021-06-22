from flask import Flask, request, render_template, redirect, url_for, json

app = Flask(__name__)

global base_grant_url
base_grant_url = ""
global user_continue_url
user_continue_url = ""
global success_url
success_url = ""


@app.route("/click", methods=["GET"])
def get_click():
    global base_grant_url
    global user_continue_url
    global success_url


    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac '
    splashclick_time = request.args.get('splashclick_time')
    success_url = host + "dev/success"
    network_id=request.args.get("network_id")
    camera_serial=request.args.get("camera_serial")
    api_key=request.args.get("api_key")

    return render_template("click.html", client_ip=client_ip,
    client_mac=client_mac, node_mac=node_mac,
    user_continue_url=user_continue_url,success_url=success_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=False)

