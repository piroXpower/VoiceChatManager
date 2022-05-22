
from pytgcalls import PyTgCalls
from pytgcalls import Client
from pytgcalls import idle 
from config import app

app = PyTgCalls(client)

app.join_group_call(
    -1001185324811,  
), 
app.get_participants(
    -1001185324811,
     video_camera(user_id) 
), 

await app.message(chat_id=CHAT_ID, "@admins {} **Is Sharing Video Camera**") 

app.start()
idle()
