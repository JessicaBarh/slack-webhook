#!/bin/python3

import os
import sys

from slack_webhook import Slack

WEBHOOK = os.getenv('SLACK_WEBHOOK', None)

if WEBHOOK is None:
    print("****** webhook is empty ******")
else:
    # Send to Slack
    slack = Slack(url=WEBHOOK)
    slack.post(text="Hey there! I just made a slack webhook!")
