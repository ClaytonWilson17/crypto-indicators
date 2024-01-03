# Clayton's test channel
# https://discord.com/api/webhooks/1191903241185800257/pSn6-r7T98c_t59qPLJ43mIN4AiKPIDNNvZOMMRbjCPY_7g9QQyZH8kuKlxAtfm-mLmE

from discord import SyncWebhook

def send_message(message):
    hook = SyncWebhook.from_url('https://discord.com/api/webhooks/1191903241185800257/pSn6-r7T98c_t59qPLJ43mIN4AiKPIDNNvZOMMRbjCPY_7g9QQyZH8kuKlxAtfm-mLmE') 
    hook.send(content=message)

