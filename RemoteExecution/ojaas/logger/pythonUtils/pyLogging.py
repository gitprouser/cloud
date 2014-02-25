#!/usr/bin/python

__author__ = 'drowland'

# This is the python specific logging module.
# It is used by commonLogging.py to support python logging
# when available.


import os
import sys
import logging.config
import commonLogging

#setup the default cpsLogger
cps_formatter = logging.Formatter("<%(asctime)s> <%(levelname)s> <%(name)s> <%(message)s> ")
cps_fileName = commonLogging.LOG_FILE_NAME
cps_maxBytes = commonLogging.LOG_FILE_MIN_SIZE_KILOBYTES * 1024
cps_backupCount = commonLogging.LOG_FILE_COUNT
cps_fh_level = commonLogging.LOG_FILE_SEVERITY
cps_ch_level = commonLogging.CONSOLE_SEVERITY
cps_encoding="utf8"


# Used to map cps logging levels to python loggings
LEVELS = {commonLogging.DEBUG : logging.DEBUG,
          commonLogging.INFO : logging.INFO,
          commonLogging.WARNING : logging.WARNING,
          commonLogging.ERROR : logging.ERROR,
          commonLogging.CRITICAL : logging.CRITICAL}


NLEVELS = {10 : commonLogging.DEBUG,
           20 : commonLogging.INFO,
           30 : commonLogging.WARNING,
           40 : commonLogging.ERROR,
           50 : commonLogging.CRITICAL}


def getLogger(loggerName=commonLogging.LOGGER_NAME):
    logger = logging.getLogger(loggerName)
    if not len(logger.handlers):
        #file handler
        cps_fh = logging.handlers.RotatingFileHandler(cps_fileName,
                                              maxBytes=cps_maxBytes,
                                              backupCount=cps_backupCount,
                                              encoding=cps_encoding)
        cps_fh.setFormatter(cps_formatter)
        cps_fh.setLevel(LEVELS.get(cps_fh_level))
        logger.addHandler(cps_fh)
        # console handler
        cps_ch = logging.StreamHandler(sys.stdout)
        cps_ch.setFormatter(cps_formatter)
        cps_ch.setLevel(LEVELS.get(cps_ch_level))
        logger.addHandler(cps_ch)
        #set the logger to the highest level and control at the handler level
        logger.setLevel(logging.DEBUG)
    return logger

def getFileName():
    return os.path.abspath(cps_fileName)

def setFileName(fileName):
    global cps_fileName
    cps_fileName = fileName

def getLogFileSeverity():
    return cps_fh_level

def setLogFileSeverity(level):
    global cps_fh_level
    cps_fh_level = level

def getFileCount():
    return str(cps_backupCount)

def setFileCount(count):
    global cps_backupCount
    cps_backupCount =  count

def getFileMinSize():
    return str(cps_maxBytes / 1024)

def setFileMinSize(size):
    global cps_maxBytes
    cps_maxBytes =  size * 1024

def getConsoleSeverity():
    return str(cps_ch_level)

def setConsoleSeverity(level):
    global cps_ch_level
    cps_ch_level = level


