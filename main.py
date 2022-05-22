from pyrogram import Client

from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls import idle
from pytgcalls.media_devices import MediaDevices
from pytgcalls.types import CaptureVideoDesktop

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

print("VCMANAGER STARTED!! ") 

idle()
