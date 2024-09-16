import os

os.system("pip install -U scratchattach")
import scratchattach as scratch3

import scratchattach as scratch3

session = scratch3.login("midoriyohi", "#doara73")
conn = session.connect_cloud("1068139990")
events = scratch3.CloudEvents("1068139990")
@events.event
def on_set(event): #Called when a cloud var is set
    conn.set_var("aaa", "1") #the variable name is specified without the cloud emoji
events.start()
