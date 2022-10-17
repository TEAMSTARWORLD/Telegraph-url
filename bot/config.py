import os

class Config:
    API_ID=os.environ['API_ID']
API_HASH=os.environ['API_HASH']
    
BOT_TOKEN=int(os.environ['BOT_TOKEN'])
    
    if not BOT_TOKEN:
        raise ValueError('BOT_TOKEN not set')
    
    if not API_HASH:
        raise ValueError("API_HASH not set")

    if not API_ID:
        raise ValueError("API_ID not set")
