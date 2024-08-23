"""Definition of Dreo devices."""
from enum import Enum


class OscillationSupport(Enum):
    """Oscillation support."""
    NONE = 0
    HORIZONTAL = 1
    BOTH = 2


class HeaterOscillationAngle(Enum):
    """Heater oscillation angles."""
    OSC = 0
    SIXTY = 60
    NINETY = 90
    ONE_TWENTY = 120


class PyDreoFanDefinition():
    """Definition of a Dreo fan."""

    def __init__(self,
                 preset_modes: list,
                 speed_range: range,
                 oscillation_support: OscillationSupport):
        self.preset_modes = preset_modes
        self.speed_range = speed_range
        self.oscillation_support = oscillation_support


class PyDreoHeaterDefinition():
    """Definition of a Dreo heater."""

    def __init__(self,
                 preset_modes: list,
                 heat_range: range,
                 ecolevel_range: range,
                 oscillation_support: HeaterOscillationAngle):
        self.preset_modes = preset_modes
        self.heat_range = heat_range
        self.ecolevel_range = ecolevel_range
        self.oscillation_support = oscillation_support


class PyDreoACDefinition():
    """Definition of a Dreo AC."""

    def __init__(self,
                 preset_modes: list,
                 temperature_range: range,
                 fan_speed_range: range,
                 oscillation_support: OscillationSupport):
        self.preset_modes = preset_modes
        self.temperature_range = temperature_range
        self.fan_speed_range = fan_speed_range
        self.oscillation_support = oscillation_support
