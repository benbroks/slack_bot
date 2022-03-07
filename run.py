from slack_sdk.webhook import WebhookClient

if __name__ == '__main__':
    url = ""
    webhook = WebhookClient(url)
    t = """Respond to this thread with the following:
    - What did you do yesterday?
    - What do you plan to do today?
    - What, if anything, is preventing you from completing your tasks?
    """
    response = webhook.send(text=t)


