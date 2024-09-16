import os

os.system("pip install -U scratchattach")
import scratchattach as scratch3

session = scratch3.Session("eJxVj81qwzAQhN_F58aV9eO1cmtODQRDAyn0JNaSHCuOpCA7hLb03SuDL7nONzsz", username="midoriyohi") #The username field is case sensitive
conn = session.connect_cloud("882454152")
conn.set_var("aaa", "1") #the variable name is specified without the cloud emoji
