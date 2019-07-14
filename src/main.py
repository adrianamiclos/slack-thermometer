import Adafruit_DHT as sensor


def main():
    temp = read_temperature()
    # TODO read values from file
    # if temp < 19 | temp > 24:
    message = compose_message(temp)
    post_to_slack(message)


def read_temperature():
    humidity, temp = sensor.read_retry(sensor.DHT22, 4)
    return temp


def compose_message(temperature):
    return f'The temperature is {temperature}'


def post_to_slack(message):
    print(message)


if __name__ == "__main__":
    main()
