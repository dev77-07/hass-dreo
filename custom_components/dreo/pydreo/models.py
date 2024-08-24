"""Supported device models for the PyDreo library."""
from dataclasses import dataclass

from .constant import (
    PresetFanMode,
    PresetHeaterMode,
    TEMP_RANGE,
    TARGET_TEMP_RANGE,
    TARGET_TEMP_RANGE_ECO,
    HeaterOscillationAngle,
    HUMIDITY_RANGE,
    SWING_ON,
    SWING_OFF,
    PRESET_NONE,
    PRESET_ECO,
    HVACMode,
    HVACMode
)


@dataclass
class DreoDeviceDetails:
    """Represents a Dreo device model and capabilities"""

    preset_modes: list[str]
    """List of possible preset mode names"""

    range: dict
    """Dictionary of different ranges"""

    hvac_modes: list[str]
    """List of possible HVAC mode names"""

    swing_modes: list[str]
    """List of possible swing modes"""

    def __init__(self,
                 preset_modes: list[PresetFanMode | PresetHeaterMode],
                 device_ranges: dict,
                 hvac_modes: list[HVACMode] = None,
                 swing_modes: list[str] = None, 
                 fan_modes: list[str] = None):
        self.preset_modes = preset_modes
        self.range = device_ranges
        self.hvac_modes = hvac_modes
        self.swing_modes = swing_modes
        self.fan_modes = fan_modes

@dataclass
class DreoFanDeviceDetails(DreoDeviceDetails):
    """Represents a Dreo fan device model and capabilities"""

    def __init__(self,
                 preset_modes: list[PresetFanMode] = None,
                 speed_range: tuple[int, int] = None,
                 device_ranges: dict = None,
                 hvac_modes: list[HVACMode] = None,
                 swing_modes: list[str] = None,
                 fan_modes: list[str] = None):
        super().__init__(preset_modes, device_ranges, hvac_modes, swing_modes, fan_modes)
        self.speed_range = speed_range

@dataclass
class DreoHeaterDeviceDetails(DreoDeviceDetails):
    """Represents a Dreo heater device model and capabilities"""

    def __init__(self,
                 preset_modes: list[PresetFanMode] = None,
                 heat_range: tuple[int, int] = None,
                 eco_level_range: tuple[int, int] = None,
                 hvac_modes: list[HVACMode] = None,
                 swing_modes: list[str] = None,
                 fan_modes: list[str] = None):
        super().__init__(preset_modes, None, hvac_modes, swing_modes, fan_modes)
        self.heat_range = heat_range
        self.eco_level_range = eco_level_range

@dataclass
class DreoACDeviceDetails(DreoDeviceDetails):
    """Represents a Dreo air conditioner device model and capabilities"""

    def __init__(self,
                 preset_modes: list[PresetFanMode] = None,
                 speed_range: tuple[int, int] = None,
                 device_ranges: dict = None,
                 hvac_modes: list[HVACMode] = None,
                 swing_modes: list[str] = None,
                 fan_modes: list[str] = None):
        super().__init__(preset_modes, device_ranges, hvac_modes, swing_modes, fan_modes)
        self.speed_range = speed_range

# Supported prefixes.
# These prefixes will be listed along with the models in the below collections.
SUPPORTED_MODEL_PREFIXES = {
    "DR-HTF",
    "DR-HAF",
    "DR-HPF",
    "DR-HCF",
    "DR-HSH",
    "WH", 
    "DR-HAC"
}

SUPPORTED_FANS = {
    "DR-HTF": DreoFanDeviceDetails(),
    "DR-HAF": DreoFanDeviceDetails(),
    "DR-HPF": DreoFanDeviceDetails(),
    "DR-HCF": DreoFanDeviceDetails()
}


SUPPORTED_HEATERS = {
    "DR-HSH": DreoHeaterDeviceDetails(
        heat_range = (1, 3),
        eco_level_range = (41, 85),
        hvac_modes=[HVACMode.COOL, 
                    HVACMode.HEAT,
                    HVACMode.ECO, 
                    HVACMode.OFF],
        swing_modes=[SWING_OFF, SWING_ON]
    ),
    "WH": DreoHeaterDeviceDetails(
        heat_range = (1, 3),
        eco_level_range = (41, 95),
        hvac_modes=[HVACMode.COOL,
                    HVACMode.HEAT,
                    HVACMode.ECO,
                    HVACMode.OFF],
        swing_modes=[HeaterOscillationAngle.OSC,
                     HeaterOscillationAngle.SIXTY,
                     HeaterOscillationAngle.NINETY,
                     HeaterOscillationAngle.ONE_TWENTY]
    )
}

SUPPORTED_ACS = {
    "DR-HAC005S": DreoDeviceDetails(
        device_ranges={
            TEMP_RANGE: (60, 95),
            TARGET_TEMP_RANGE: (64, 86),
            TARGET_TEMP_RANGE_ECO: (75, 86),
            HUMIDITY_RANGE: (30, 80),
        },
        # TODO Eco is a Present, not HVAC mode (HVACMode.AUTO)
        hvac_modes=[HVACMode.COOL,
                    HVACMode.FAN_ONLY,
                    HVACMode.DRY],
        swing_modes=[SWING_OFF, SWING_ON],
        preset_modes=[PRESET_NONE, 
                      PRESET_ECO],
        # TODO Add fan modes, windlevel: 1,2,3,4 (Auto)
        #fan_modes=[FAN_LOW, FAN_MEDIUM, FAN_HIGH, FAN_AUTO],
    )
}

SUPPORTED_DEVICES = [
    ("PyDreoFan", SUPPORTED_FANS),
    ("PyDreoHeater", SUPPORTED_HEATERS),
    ("PyDreoAc", SUPPORTED_ACS)
]
