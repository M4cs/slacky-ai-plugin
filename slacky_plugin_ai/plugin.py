from slacky import client, config, check_user, bot, version, Prefixes
from slack.errors import SlackApiError
from .genlog import generate_res

def cmd_setup(command, **payload):
    data = payload['data']
    channel_id = data['channel']
    user = data.get('user')
    timestamp = data.get('ts')
    web_client = client
    text = data.get('text')
    if text and check_user(user):
        text_split = text.split(' ')
        cmd = text_split[0]
        if cmd == config['prefix'] + command:
            print(Prefixes.event + 'Ran Command: {}'.format(command))
            bot.command_count += 1
            return data, channel_id, user, timestamp, web_client, text, text_split
        else:
            return None, None, None, None, None, None, None
    else:
        return None, None, None, None, None, None, None

def daemon_setup(**payload):
    data = payload['data']
    channel_id = data['channel']
    user = data.get('user')
    timestamp = data.get('ts')
    web_client = client
    text = data.get('text')
    if text and check_user(user):
        text_split = text.split(' ')
        print(Prefixes.event + 'Ran Command: {}'.format(command))
        bot.command_count += 1
        return data, channel_id, user, timestamp, web_client, text, text_split
    else:
        return None, None, None, None, None, None, None

def airesponse(**payload):
    data, channel_id, user, timestamp, web_client, text, text_split = daemon_setup(**payload)
    if data:
        if channel_id in config['ai_channels_to_respond_in']:
            if user in config['ai_users_to_respond_to']:
                match = None
                try:
                    ulist = web_client.users_list()
                    for wuser in ulist['members']:
                        if wuser == user:
                            match = wuser
                except SlackApiError as e:
                    bot.error(e)
                gen_res = generate_res(match['name'] + '\n' + text)
                for index, line in enumerate(gen_res.splitlines()):
                    if config['ai_username'] in line:
                        response = gen_res.splitlines()[index + 1]
                        break
                try:
                    web_client.chat_postMessage(
                        channel=channel_id,
                        ts=timestamp,
                        text=gen_res
                    )
                except SlackApiError as e:
                    bot.error(e)