from slack_sdk.webhook import WebhookClient

if __name__ == '__main__':
    url = "https://hooks.slack.com/services/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"
    webhook = WebhookClient(url)
    t = """Respond to this thread with the following:
    - What did you do yesterday?
    - What do you plan to do today?
    - What, if anything, is preventing you from completing your tasks?
    """
    response = webhook.send(text=t)


