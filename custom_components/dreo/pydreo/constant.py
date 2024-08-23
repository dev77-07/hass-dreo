"""Constants for the PyDreo library."""
import sys
from enum import Enum, IntEnum

if sys.version_info.minor >= 11:
    # Needs Python 3.11
    from enum import StrEnum  # # pylint: disable=no-name-in-module
else:
    try:
        # https://github.com/home-assistant/core/blob/dev/homeassistant/backports/enum.py
        # Considered internal to Home Assistant, can be removed whenever.
        from homeassistant.backports.enum import StrEnum
    except ImportError:
        from enum import Enum

        class StrEnum(str, Enum):
            pass

LOGGER_NAME = "pydreo"

# Various keys read from server JSON responses.
ACCESS_TOKEN_KEY = "access_token"
REGION_KEY = "region"
DATA_KEY = "data"
LIST_KEY = "list"
MIXED_KEY = "mixed"
DEVICEID_KEY = "deviceid"
DEVICESN_KEY = "deviceSn"
REPORTED_KEY = "reported"
STATE_KEY = "state"
POWERON_KEY = "poweron"
WINDTYPE_KEY = "windtype"
WINDLEVEL_KEY = "windlevel"
SHAKEHORIZON_KEY = "shakehorizon"
MODE_KEY = "mode"
HTALEVEL_KEY = "htalevel"
OSCON_KEY = "oscon"
OSCMODE_KEY = "oscmode"
OSCANGLE_KEY = "oscangle"
CRUISECONF_KEY = "cruiseconf"
TEMPERATURE_KEY = "temperature"
TARGET_TEMPERATURE_KEY = "templevel"
VOICEON_KEY = "voiceon"
LEDALWAYSON_KEY = "ledalwayson"
LIGHTSENSORON_KEY = "lightsensoron"
MUTEON_KEY = "muteon"
FIXEDCONF_KEY = "fixedconf"
DEVON_KEY = "devon"
TIMERON_KEY = "timeron"
COOLDOWN_KEY = "cooldown"
PTCON_KEY = "ptcon"
LIGHTON_KEY = "lighton"
CTLSTATUS_KEY = "ctlstatus"
TIMEROFF_KEY = "timeroff"
ECOLEVEL_KEY = "ecolevel"
ECOLEVEL_RANGE_KEY = "ecolevel_range"
CHILDLOCKON_KEY = "childlockon"
TEMPOFFSET_KEY = "tempoffset"
HUMIDITY_KEY = "rh"
TARGET_HUMIDITY_KEY = "rhlevel"



# No preset is active
PRESET_NONE = "none"

# Device is running an energy-saving mode
PRESET_ECO = "eco"

# Device is in away mode
PRESET_AWAY = "away"

# Device turn all valve full up
PRESET_BOOST = "boost"

# Device is in comfort mode
PRESET_COMFORT = "comfort"

# Device is in home mode
PRESET_HOME = "home"

# Device is prepared for sleep
PRESET_SLEEP = "sleep"

# Device is reacting to activity (e.g. movement sensors)
PRESET_ACTIVITY = "activity"


# Possible swing state
SWING_ON = "on"
SWING_OFF = "off"
SWING_BOTH = "both"
SWING_VERTICAL = "vertical"
SWING_HORIZONTAL = "horizontal"


DREO_API_URL_FORMAT = (
    "https://app-api-{0}.dreo-cloud.com"  # {0} is the 2 letter region code
)

DREO_API_LIST_PATH = "path"
DREO_API_LIST_METHOD = "method"

DREO_API_LOGIN = "login"
DREO_API_DEVICELIST = "devicelist"
DREO_API_DEVICESTATE = "devicestate"

DREO_APIS = {
    DREO_API_LOGIN: {
        DREO_API_LIST_PATH: "/api/oauth/login",
        DREO_API_LIST_METHOD: "post",
    },
    DREO_API_DEVICELIST: {
        DREO_API_LIST_PATH: "/api/v2/user-device/device/list",
        DREO_API_LIST_METHOD: "get",
    },
    DREO_API_DEVICESTATE: {
        DREO_API_LIST_PATH: "/api/user-device/device/state",
        DREO_API_LIST_METHOD: "get",
    },
}

DREO_AUTH_REGION_NA = "NA"
DREO_AUTH_REGION_EU = "EU"

DREO_API_REGION_US = "us"
DREO_API_REGION_EU = "eu"

class PresetFanMode(StrEnum):
    """Fan mode for fan devices."""
    NORMAL = "normal"
    NATURAL = "natural"
    AUTO = "auto"
    SLEEP = "sleep"
    TURBO = "turbo"

class PresetHeaterMode(StrEnum):
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"

class HVACMode(StrEnum):
    """HVAC mode for heaters and air conditioner devices."""

    OFF = "off"
    HEAT = "heat"
    COOL = "cool"
    AUTO = "auto"
    DRY = "dry"
    ECO = "eco"
    FAN_ONLY = "fan_only"
    
MODE_LEVEL_MAP = {
    "H1" : 1,
    "H2" : 2,
    "H3" : 3
}

LEVEL_MODE_MAP = {
    1 : "H1",
    2 : "H2",
    3 : "H3"
}

AC_ECO_LEVEL_MAP = {
    1 : "10%",
    2 : "20%",
    3 : "30%"
}

HORIZONTAL_OSCILLATION_KEY = "hoscon"
HORIZONTAL_OSCILLATION_ANGLE_KEY = "hoscangle"

VERTICAL_OSCILLATION_KEY = "voscon"
VERTICAL_OSCILLATION_ANGLE_KEY = "voscangle"

MIN_OSC_ANGLE_DIFFERENCE = 30

# Heater oscillation
OSCILLATION_KEY = "oscon"
OSCILLATION_ANGLE_KEY = "oscangle"

WIND_MODE_KEY = "mode"

SPEED_RANGE = "speed_range"
HEAT_RANGE = "heat_range"
ECOLEVEL_RANGE = "ecolevel_range"
TEMP_RANGE = "temp_range"
TARGET_TEMP_RANGE = "target_temp_range"
TARGET_TEMP_RANGE_ECO = "target_temp_range_eco"
HUMIDITY_RANGE = "humidity_range"

class TemperatureUnit(Enum):
    """Valid possible temperature units."""
    CELCIUS = 0
    FAHRENHEIT = 1

# Fan oscillation modes
class OscillationMode(IntEnum):
    """Possible oscillation modes.  These are bitwise flags."""
    OFF = 0,
    HORIZONTAL = 1,
    VERTICAL = 2,
    BOTH = 3

# Heater oscillation modes
class HeaterOscillationAngle(IntEnum):
    """Possible Heat"er oscillation angles"""
    OSC = 0,
    SIXTY = 60,
    NINETY = 90,
    ONE_TWENTY = 120

class ACMode(IntEnum):
    """Possible AC modes."""
    COOL = 1,
    DRY = 2,
    FAN = 3,
    ECO = 5

class ACFanMode(IntEnum):
    """Possible AC Fan modes."""
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3,
    AUTO = 4,
