# pip install notify-py
from notifypy import Notify
noti=Notify()

noti.title="this is a title"
noti.message=("please like and subscribe")

noti.send()