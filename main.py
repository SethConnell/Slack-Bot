from slackeventsapi import SlackEventAdapter
import os

slack_signing_secret = os.environ["slack_signing_secret"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, endpoint="/slack/events")

# Create an event listener for "reaction_added" events and print the emoji name
@slack_events_adapter.on("app_mention")
def reaction_added(event_data):
  from slackclient import SlackClient
  slack_token = os.environ["slack_token"]
  sc = SlackClient(slack_token)
  mytext = "You said something."
  sc.api_call("chat.postMessage", channel="#general", text=mytext)


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))
slack_events_adapter.start(port=3000)
