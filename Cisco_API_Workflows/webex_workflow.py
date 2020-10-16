"""Simple workflow to get resources and post a message """
import requests
import os
import pprint


def get_rooms(url, token):
    headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    section = "rooms"

    resp = requests.get(url=f"{url}{section}", headers=headers, verify=True)

    return resp.json()


def find_room(rooms_json, new_room):
    rooms_list = (room["title"] for room in rooms_json["items"])

    return new_room in rooms_list


def create_room(url, token, new_room):
    headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    section = "rooms"
    data = {"title": new_room}

    resp = requests.post(url=f"{url}{section}", headers=headers, json=data, verify=True)

    return resp.ok


def extract_id(rooms_json, room_title):
    for room in rooms_json["items"]:
        print(room['title'])
        print(room['id'])
        if room_title == room["title"]:
            return room["id"]


def add_person(url, token, room_id, person):
    headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    section = "memberships"
    data = {
        "roomId": room_id,
        "personEmail": f"{person}@email.com",
        "isModerator": False,
    }

    resp = requests.post(url=f"{url}{section}", headers=headers, json=data, verify=True)

    return resp.ok


def post_message(url, token, room_id, message):
    headers = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    section = "messages"
    data = {"roomId": room_id, "text": message}

    resp = requests.post(url=f"{url}{section}", headers=headers, json=data, verify=True)

    return resp.ok


if __name__ == "__main__":
    env = os.environ.get
    token = env("WEBEX_TOKEN", "")
    url = "https://api.ciscospark.com/v1/"

    new_room = "yet another super hero room"
    new_person = "another_drx"
    message = "Hello X Men!"

    # validate there is a room id
    rooms_json = get_rooms(url, token)
    pprint.pprint(rooms_json)

    # find if room already exists
    if not find_room(rooms_json, new_room):
        # create new room
        room_created = create_room(url, token, new_room)
    else:
        print(f"Room {new_room} already exists")

    # add person
    if room_created:
        print(f"New room {new_room} was created successfully")
        # need to get rooms again to get updated json
        rooms_json = get_rooms(url, token)
        room_id = extract_id(rooms_json, new_room)
        print(room_id)
        person_added = add_person(url, token, room_id, new_person)

    # post message
    if person_added:
        print(f"New person {new_person} was created successfully")
        message_posted = post_message(url, token, room_id, message)

    if message_posted:
        print("Message was posted successfully")

    # cleanup: delete person & message
    # if person_added and message_posted:
    # delete_person(url, token, person)
    # delete_message(url, token, message)
