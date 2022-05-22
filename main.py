
from pytgcalls import PyTgCalls
from pytgcalls import Client
from pytgcalls import idle 
from config import Config

CHAT = Config.CHAT                                                                                                                                                                                                                                                                                                                                    
APP_ID = Config.API_ID                                                                                                                                                                                                                                                                                                                                        
API_HASH = Config.API_HASH                                                                                                                                                                                                                                                                                                                                    
SESSION_NAME = Config.STRING_SESSION  

app = Client(SESSION_NAME, API_ID, API_HASH)


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
