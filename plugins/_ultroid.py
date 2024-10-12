# Ult.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **OreO UserBot** •\n
• Repo - [Click Here](https://github.com/btworeo/ultroid)
• Addons - [Click Here](https://github.com/btworeo/ultroidAddons)
• Support - @OreoSupportChat
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/btworeo/ultroid"),
        Button.url("Addons", "https://github.com/btworeo/ultroidAddons"),
    ],
    [Button.url("Support Group", "t.me/OreoSupportChat")],
]

ULTSTRING = """🎇 **Thanks for Deploying OreO Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="oreo$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/54a917cc9dbb94733ea5f.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
