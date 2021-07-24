import json
import requests
import HIDDEN


headers = {
    "Authorization": "Bearer %s" % HIDDEN.token,
}

response = requests.get('https://api.lifx.com/v1/lights/all',
                        headers=headers)


def off():
    """
    Turns off light
    """
    print("turning off")
    payload = {
        "power": "off",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    return response


def on():
    """
    Turns on light
    """
    print("turning on")
    payload = {
        "power": "on",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    return response


def show_scenes():
    """
    it returns a list containing the name of all scenes
    """
    list = []
    response = requests.get('https://api.lifx.com/v1/scenes', headers=headers)
    x = response.json()
    for i in range(0, len(x)):
        list.append(x[i].get("name"))
    return list


# given scene name, return the scene id
def show_scene_id(scene_name):
    """
    :param scene_name the name of the scene you want the id for

    returns the id of a given scene
    """
    response = requests.get('https://api.lifx.com/v1/scenes', headers=headers)
    x = response.json()
    for i in range(0, len(x)):
        if x[i].get("name") == scene_name:
            return x[i].get("uuid")


def show_bulbs():
    """
    returns the id of the bulb (currently unused)
    """
    print("show light bulbs")
    response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
    return response.json()


def activate_scene(scene_id):
    """
    :param scene_id the id of the scene you want to activate

    activates a scene
    """
    response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' %
                            scene_id, headers=headers)
    return response
