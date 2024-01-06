# Clayton's test channel
# https://discord.com/api/webhooks/1191903241185800257/pSn6-r7T98c_t59qPLJ43mIN4AiKPIDNNvZOMMRbjCPY_7g9QQyZH8kuKlxAtfm-mLmE

# Connors channel
# https://discord.com/api/webhooks/1192326221346918480/EMz20c66WIzkY3j8_kNpCKsB7CD0XrsNhH6-Pd6XBn0hFYCyjHCnkeqhEFV8VqZZS8gn


from discord import SyncWebhook

def send_message(message):
    hook = SyncWebhook.from_url('https://discord.com/api/webhooks/1192326221346918480/EMz20c66WIzkY3j8_kNpCKsB7CD0XrsNhH6-Pd6XBn0hFYCyjHCnkeqhEFV8VqZZS8gn') 
    hook.send(content=message)

