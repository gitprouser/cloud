#!/usr/bin/python

# This is the common logging module.
# At the core it relies on python logging that was introduced in v 2.3
# however in wlst the supported pythong version is 2.2.1.
# To support a common logging of both python and wlst (jython), this
# module provides a common jacket around the WLS logging option when
# using WLST and python logging when using version 2.3 or higher of python
#
import sys,os

#If running in the wlst environment then supported version is currently
# 2.2.1, which means SafeConfigParser is not support (2.3)
if sys.version_info < (2,3):
    from ConfigParser import ConfigParser as CParser
else:
    from ConfigParser import SafeConfigParser as CParser


#Constants
DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"
CRITICAL = "CRITICAL"


# Default values
# (can be overridden with config files defined below)
LOG_FILE_NAME = 'cps.log'
LOGGER_NAME = 'CPSLogger'
LOG_FILE_SEVERITY = DEBUG
LOG_FILE_COUNT = 7
LOG_FILE_MIN_SIZE_KILOBYTES = 500
CONSOLE_SEVERITY = INFO

#Process config file
clc = os.getenv('COMMON_LOGGING_CFG')
if clc:
    config_path = clc
else:
    pu_config = os.getenv('PYTHONUTILSPATH')
    if pu_config:
        config_path = pu_config + '/config.ini'

cls = os.getenv('COMMON_LOGGING_SECTION')
if cls:
    config_section = cls
else:
    config_section = 'defaults'

if config_path and os.path.exists(config_path):
    cParser = CParser()
    cParser.read(config_path)

    if cParser.has_section(config_section):
        if cParser.has_option(config_section,'LOG_FILE_NAME'):
            LOG_FILE_NAME = cParser.get(config_section,'LOG_FILE_NAME')

        if cParser.has_option(config_section,'LOGGER_NAME'):
            LOGGER_NAME = cParser.get(config_section,'LOGGER_NAME')

        if cParser.has_option(config_section,'LOG_FILE_SEVERITY'):
            LOG_FILE_SEVERITY = cParser.get(config_section,'LOG_FILE_SEVERITY')

        if cParser.has_option(config_section,'LOG_FILE_COUNT'):
            LOG_FILE_COUNT = int(cParser.get(config_section,'LOG_FILE_COUNT'))

        if cParser.has_option(config_section,'LOG_FILE_MIN_SIZE_KILOBYTES'):
            LOG_FILE_MIN_SIZE_KILOBYTES = int(cParser.get(config_section,'LOG_FILE_MIN_SIZE_KILOBYTES'))

        if cParser.has_option(config_section,'CONSOLE_SEVERITY'):
            CONSOLE_SEVERITY = cParser.get(config_section,'CONSOLE_SEVERITY')


#If running in the wlst environment then supported version is currently
# 2.2.1, which means python logging is not supported (2.3)
# Also note that import of the logging needs to be done after the
# processing of configuration information

if sys.version_info < (2,3):
    import wlsLogging as logging
else:
    import pyLogging as logging


# methods
def getLogger(loggerName=LOGGER_NAME):
    return logging.getLogger(loggerName)

def setFileName(fileName):
    logging.setFileName(fileName)

def getFileName():
    return logging.getFileName()

def setLogFileSeverity(level):
    logging.setLogFileSeverity(level.upper())

def getLogFileSeverity():
    return logging.getLogFileSeverity()

def setFileCount(count):
    logging.setFileCount(count)

def getFileCount():
    return logging.getFileCount()

def setFileMinSize(size):
    logging.setFileMinSize(size)

def getFileMinSize():
    return logging.getFileMinSize()

def setConsoleSeverity(level):
    logging.setConsoleSeverity(level.upper())

def getConsoleSeverity():
    return logging.getConsoleSeverity()

# Display configuration status to console and log
def displayConfigStatus(logger=None):
    fileNameStatus(logger)
    logFileSeverfityStatus(logger)
    fileCountStatus(logger)
    fileMinSizeStatus(logger)
    consoleSeverityStatus(logger)

def fileNameStatus(logger=None):
    msg = " >>>> Log file: " + getFileName()
    outputStatus(msg,logger)

def logFileSeverfityStatus(logger=None):
    msg = " >>>> Log file severity: " + getLogFileSeverity()
    outputStatus(msg,logger)

def fileCountStatus(logger=None):
    msg = " >>>> Log file count: " + logging.getFileCount()
    outputStatus(msg,logger)

def fileMinSizeStatus(logger=None):
    msg = " >>>> Log file Min Size: " + logging.getFileMinSize()
    outputStatus(msg,logger)

def consoleSeverityStatus(logger=None):
    msg = " >>>> Console severity: " + logging.getConsoleSeverity()
    outputStatus(msg,logger)

def outputStatus(msg, logger=None):
    if (logger != None):
        logger.debug(msg)
    print msg




