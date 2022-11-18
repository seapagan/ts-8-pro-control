"""Define Error Handlers for the PoECtrl class."""


class CannotConnectError(Exception):
    """Raised when we cannot connect to a device."""


class BadAuthenticationError(Exception):
    """Raised if the user/pass is incorrect."""


class CannotReadSettingsError(Exception):
    """Raised if the device settings cannot be read."""


class CannotWriteSettingsError(Exception):
    """Raised if the device settings cannot be written."""
