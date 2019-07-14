# import Adafruit_DHT as sensor
import requests
import configparser
import random

config = configparser.ConfigParser()


def main():
    setup()
    temp = read_temperature()

    # TODO read values from file
    # if temp < 19 | temp > 24:
    message = compose_cold_message(temp)
    post_to_slack(message)


def setup():
    config.read('config.properties')


def read_temperature():
    # humidity, temp = sensor.read_retry(sensor.DHT22, 4)
    # return temp
    return 19


def compose_cold_message(temperature):
    cold_msg_config = config['COLD_MSG']

    cold_msgs_size = cold_msg_config['c_size']
    message_index = random.randint(1, int(cold_msgs_size))
    message = cold_msg_config['c_' + str(message_index)]

    return compose_message(message, temperature)


def compose_hot_message(temperature):
    cold_msg_config = config['HOT_MSG']

    cold_msgs_size = cold_msg_config['h_size']
    message_index = random.randint(1, int(cold_msgs_size))
    message = cold_msg_config['h_' + str(message_index)]

    return compose_message(message, temperature)


def compose_message(message, temperature):
    return message + ' ' + 'The temperature is {0:0.1f} *C'.format(temperature)


def post_to_slack(message):
    slack_config = config['SLACK']
    web_hook_url = slack_config['web_hook_url']
    username = slack_config['username']
    channel = slack_config['channel']
    incon_emoji = slack_config['icon_emoji']

    payload = {"channel": "#" + channel, "username": username, "text": message, "icon_emoji": incon_emoji}
    response = requests.post(url=web_hook_url, json=payload)
    print(response.status_code)


if __name__ == "__main__":
    main()
