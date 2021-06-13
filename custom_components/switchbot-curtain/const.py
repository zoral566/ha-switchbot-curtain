"""Constants for the switchbot integration."""

DOMAIN = "switchbot-curtain"
MANUFACTURER = "switchbot"

ATTR_CURTAIN = "curtain"
ATTR_BOT = "bot"
DEFAULT_NAME = "Switchbot"
DEFAULT_RETRY_COUNT = 3
DEFAULT_RETRY_TIMEOUT = 1
DEFAULT_TIME_BETWEEN_UPDATE_COMMAND = 1

# Config Options
CONF_TIME_BETWEEN_UPDATE_COMMAND = "update_time"
CONF_RETRY_COUNT = "retry_count"
CONF_RETRY_TIMEOUT = "retry_timeout"

# Data
DATA_COORDINATOR = "coordinator"
DATA_UNDO_UPDATE_LISTENER = "undo_update_listener"
