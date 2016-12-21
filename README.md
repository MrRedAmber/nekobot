v0.1 (BETA)

![](http://nekobot.xyz/img/Logo_lightbg.png)
###  Docker usage
_Building from source_
```bash
$ docker-compose up --build
```
_Don't forget to create a nekobot.rc in the compose root! It should look a little something like this..._
```bash
# The discord application token
NEKBOT_TOKEN=token

# The log level of nekobot.log
NEKOBOT_DEBUG=False

# Flask debug level
FLASK_DEBUG=False
```

[URL to invite Nekobot to your server!](https://discordapp.com/oauth2/authorize?permissions=2146958463&scope=bot&client_id=253499115667849216)

### Features
Plugin name | Plugin description | State
------------|--------------------|------
Channels | A plugin that creates voice/text channels specified in the plugin source | In development
Commands | A plugin that gives the users a list of executable commands inside their server | Tested
Giphy | A plugin that implements a search against the Giphy database of gifs against a keyword | Tested
Moderator | A plugin that implements commmands that would be useful to moderate a server; !BAN, !KICK | In development
Nekobot | A plugin that accompanies Nekobot, try !whoami in the Nekobot channel!| Tested