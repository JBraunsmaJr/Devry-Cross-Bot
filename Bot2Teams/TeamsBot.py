# -*- coding: utf-8 -*-
"""
Bot for Teams
"""

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class TeamsBot(ActivityHandler):
    def __init__(self):
        pass

    async def on_message_activity(  # pylint: disable=unused-argument
        self, turn_context: TurnContext
    ):
        await turn_context.send_activity(f"You said '{turn_context.activity.text}'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

