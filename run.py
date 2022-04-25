from slack_sdk.webhook import WebhookClient
import requests

import os

time_url = "https://worldtimeapi.org/api/timezone/America/New_York"

if __name__ == '__main__':
    url = os.environ['WEBHOOK_URL']
    
    tz_check = requests.get(time_url)
    day_of_week = tz_check.json().get('day_of_week')
    
    if day_of_week >= 1 and day_of_week <= 5:
        webhook = WebhookClient(url)
        t = """Respond to this thread with the following:
        - What did you do yesterday?
        - What do you plan to do today?
        - What, if anything, is preventing you from completing your tasks?
        """
        response = webhook.send(text=t)


