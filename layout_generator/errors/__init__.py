class LayoutsBaseException(Exception):
    """
    Base Layout Error class
    """


class InvalidLayoutName(LayoutsBaseException):
    """
    Error if a layout name is not valid
    """

    message = "Layout name is not valid."


class ModuleImportError(LayoutsBaseException):
    """
    Error while importing the module
    """

    message = "Unable to import module"
