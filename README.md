# slacky-ai-plugin
gpt2 Powered Slacky Plugin for Autoreply

# Setup

Make sure you have Slacky setup and working.

In your config add:

```
"ai_channels_to_respond_in": [],
"ai_users_to_respond_to": [],
"ai_username": "<your name from dataset>"
```

You will need to install tensorflow 1.15.0rc3 and gpt2-simple. This will allow you to load checkpoints from gpt2 simple models and use those for generation. You will need to change `run_name` in `slacky_ai_plugin/genlog.py` to your models run_name. If you trained on Colab you can run the bot on colab and mount your drive to easily load pretrained models. Uptime may be effected if you do this however.
