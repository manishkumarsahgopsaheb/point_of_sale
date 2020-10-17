import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="Aisa manish ne kaha hai bhai pani ni piyega to aane vale dino me mar jayega",
            app_icon=r"C:\Users\hp\PycharmProjects\drink water notification\waterglass.ico",
            timeout=15  # notification will live for 15 sec
        )
        # time.sleep(60)  # this process will be repeat again and again after every 60 sec
        time.sleep(60*60)  # this process will be repeat again and again after every 1 hr
