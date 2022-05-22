from pytgcalls.types.list import List                                           
from pytgcalls.methods.groups import get_participants                           
from pytgcalls.types import GroupCallParticipant                                
from pytgcalls import PyTgCalls                                                 
from pyrogram import Client                                                     
from pytgcalls import idle                                                      
from config import Config

CHAT = Config.CHAT
API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION_NAME = Config.STRING_SESSION                                            
                                                                                
client = Client(SESSION_NAME, API_ID, API_HASH)                                 
                                                                                
app = PyTgCalls(client)                                                         
app.start                                                                       
                                                                                
list = app.get_participants(                                                           
   -1001185324811,                                                                                      
)                                                                               
print(list)
                                                                       
client.send_message(CHAT, " {} Is Sharing Video Camera")                    
                                                                                
idle()
