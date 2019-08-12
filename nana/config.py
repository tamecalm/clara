# Buat file config.py baru dalam dir dan impor yang sama, kemudian perpanjang kelas ini.
class Config(object):
	LOGGER = True
	
	# Must be filled!
	# Register here: https://my.telegram.org/apps
	api_id = 950408
	api_hash = "dfc24b8e2ed20ad740a0c8778843b308"
	DB_URL = "postgres://kharlm:md5d884551f9fa6407ca705b166f7e1bcb7'@localhost:5432/adsvim" # Your database URL

	# Version
	lang_code = "en" # Your language code
	device_model = "PC" # Device model
	system_version = "Linux" # OS system type

	# Use real bot for Assistant
	# Pass False if you dont want
	ASSISTANT_BOT = True
	ASSISTANT_BOT_TOKEN = "749700972:AAHeANosYybsrA06jfn1Tnjcm94dgKD2U5Y"

	# Required for some features
	# Owner and AdminSettings is for your Assistant bot only
	Owner = 494218147 # Insert your Telegram ID (go @EmiliaHikariBot, type /id)
	AdminSettings = [494218147] # Do like above, can insert multiple other user id, example [12345, 23456]
	Command = ["!", "."] # Insert command prefix, if you insert "!" then you can do !ping
	# WORKER must be int (number)
	NANA_WORKER = 8
	ASSISTANT_WORKER = 2

	# APIs token
	thumbnail_API = "" # Register free here: https://thumbnail.ws/
	screenshotlayer_API = "" # Register free here: https://screenshotlayer.com/

	# Load or no load plugins
	# userbot
	USERBOT_LOAD = []
	USERBOT_NOLOAD = []
	# manager bot
	ASSISTANT_LOAD = []
	ASSISTANT_NOLOAD = []
	

class Production(Config):
	LOGGER = False


class Development(Config):
	LOGGER = True
