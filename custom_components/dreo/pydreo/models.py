"""Supported device models for the PyDreo library."""
from dataclasses import dataclass

from .constant import (
    PresetFanMode,
    PresetHeaterMode,
    SPEED_RANGE,
    HEAT_RANGE,
    ECOLEVEL_RANGE,
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
                 preset_modes: list[PresetFanMode],
                 device_ranges: dict = None,
                 hvac_modes: list[HVACMode] = None,
                 swing_modes: list[str] = None,
                 fan_modes: list[str] = None):
        super().__init__(preset_modes, device_ranges, hvac_modes, swing_modes, fan_modes)


SUPPORTED_FANS = {
    "DR-HAF001S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL, 
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HAF003S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HAF004S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HPF002S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HPF004S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HPF005S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL, 
                      PresetFanMode.NATURAL,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HTF001S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF002S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL, 
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF004S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF005S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF007S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF008S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF009S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HTF010S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HAF002S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    ),
    "DR-HAF005S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HAF006S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HPF001S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HPF003S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO,
                      PresetFanMode.TURBO]
    ),
    "DR-HCF002S": DreoFanDeviceDetails(
        preset_modes=[PresetFanMode.NORMAL,
                      PresetFanMode.NATURAL,
                      PresetFanMode.SLEEP,
                      PresetFanMode.AUTO]
    )
}


SUPPORTED_HEATERS = {
    "DR-HSH004S": DreoDeviceDetails(
        preset_modes=[PresetHeaterMode.H1,
                      PresetHeaterMode.H2,
                      PresetHeaterMode.H3],
        device_ranges={
            HEAT_RANGE: (1, 3),
            ECOLEVEL_RANGE: (41, 85)
        },
        hvac_modes=[HVACMode.COOL, 
                    HVACMode.HEAT,
                    HVACMode.ECO, 
                    HVACMode.OFF],
        swing_modes=[SWING_OFF, SWING_ON]
    ),
    "DR-HSH009S": DreoDeviceDetails(
        preset_modes=[PresetHeaterMode.H1,
                      PresetHeaterMode.H2,
                      PresetHeaterMode.H3],
        device_ranges={
            HEAT_RANGE: (1, 3),
            ECOLEVEL_RANGE: (41, 95)
        },
        hvac_modes=[HVACMode.COOL, 
                    HVACMode.HEAT,
                    HVACMode.ECO, 
                    HVACMode.OFF],
        swing_modes=[HeaterOscillationAngle.OSC,
                     HeaterOscillationAngle.SIXTY,
                     HeaterOscillationAngle.NINETY,
                     HeaterOscillationAngle.ONE_TWENTY]
    ),
    "DR-HSH009AS": DreoDeviceDetails(
        preset_modes=[PresetHeaterMode.H1,
                      PresetHeaterMode.H2,
                      PresetHeaterMode.H3],
        device_ranges={
            HEAT_RANGE: (1, 3),
            ECOLEVEL_RANGE: (41, 95)
        },
        hvac_modes=[HVACMode.COOL, 
                    HVACMode.HEAT,
                    HVACMode.ECO, 
                    HVACMode.OFF],
        swing_modes=[HeaterOscillationAngle.OSC,
                     HeaterOscillationAngle.SIXTY,
                     HeaterOscillationAngle.NINETY,
                     HeaterOscillationAngle.ONE_TWENTY]
    ),
    "WH719S": DreoDeviceDetails(
        preset_modes=[PresetHeaterMode.H1,
                      PresetHeaterMode.H2,
                      PresetHeaterMode.H3],
        device_ranges={
            HEAT_RANGE: (1, 3),
            ECOLEVEL_RANGE: (41, 95)
        },
        hvac_modes=[HVACMode.COOL,
                    HVACMode.HEAT,
                    HVACMode.ECO,
                    HVACMode.OFF],
        swing_modes=[HeaterOscillationAngle.OSC,
                     HeaterOscillationAngle.SIXTY,
                     HeaterOscillationAngle.NINETY,
                     HeaterOscillationAngle.ONE_TWENTY]
    ),
    "WH739S": DreoDeviceDetails(
        preset_modes=[PresetHeaterMode.H1,
                      PresetHeaterMode.H2,
                      PresetHeaterMode.H3],
        device_ranges={
            HEAT_RANGE: (1, 3),
            ECOLEVEL_RANGE: (41, 95)
        },
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
