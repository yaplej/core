"""Constants for the Mopeka integration."""

from typing import Final

from mopeka_iot_ble import MediumType

from .tanks import TankSize

DOMAIN = "mopeka"

CONF_MEDIUM_TYPE: Final = "medium_type"

DEFAULT_MEDIUM_TYPE = MediumType.PROPANE.value

CONF_TANK_SIZE: Final = "tank_size"

DEFAULT_TANK_SIZE = TankSize.HORIZONTAL_250_GAL.value
