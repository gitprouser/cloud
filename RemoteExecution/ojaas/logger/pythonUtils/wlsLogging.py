#!/usr/bin/python

__author__ = 'drowland'

# This is the WLS specific logging module.
# It is used by commonLogging.py to support WLS logging
# when python logging is not available.

import os
import java
from weblogic.logging import NonCatalogLogger
import commonLogging

LEVELS = {commonLogging.DEBUG : 'Debug',
          commonLogging.INFO : 'Info',
          commonLogging.WARNING : 'Warning',
          commonLogging.ERROR : 'Error',
          commonLogging.CRITICAL : 'Critical'}


#setup cps defaults as applicable to wls logging
#  log file
if java.lang.System.getProperty('weblogic.log.FileName') == None:
    java.lang.System.setProperty('weblogic.log.FileName', commonLogging.LOG_FILE_NAME)

if java.lang.System.getProperty('weblogic.log.LogFileSeverity') == None:

    java.lang.System.setProperty('weblogic.log.LogFileSeverity', LEVELS.get(commonLogging.LOG_FILE_SEVERITY.upper()))

#  Currently only support rotation type based on size
if java.lang.System.getProperty('weblogic.log.RotationType') == None:
    java.lang.System.setProperty('weblogic.log.RotationType', "bySize")

if java.lang.System.getProperty('weblogic.log.FileCount') == None:
    java.lang.System.setProperty('weblogic.log.FileCount', str(commonLogging.LOG_FILE_COUNT))

if java.lang.System.getProperty('weblogic.log.FileMinSize') == None:
    java.lang.System.setProperty('weblogic.log.FileMinSize', str(commonLogging.LOG_FILE_MIN_SIZE_KILOBYTES))

if java.lang.System.getProperty('weblogic.log.NumberOfFilesLimited') == None:
    java.lang.System.setProperty('weblogic.log.NumberOfFilesLimited',"true")

#  console severity
if  java.lang.System.getProperty('weblogic.log.StdoutSeverity') == None:
    java.lang.System.setProperty('weblogic.log.StdoutSeverity', LEVELS.get(commonLogging.CONSOLE_SEVERITY.upper()))

# WLS logging configurations properties not supported
# weblogic.log.StdoutLogStack
# weblogic.log.LogFileRotationDir
# weblogic.log.FileTimeSpan
# weblogic.log.BufferSizeKB
# weblogic.log.RotateLogOnStartup
# weblogic.log.RotationTime


def getLogger(loggerName=commonLogging.LOGGER_NAME):
    return NonCatalogLogger(loggerName)


def getFileName():
    return os.path.abspath(java.lang.System.getProperty("weblogic.log.FileName"))


def setFileName(fileName):
    java.lang.System.setProperty("weblogic.log.FileName",fileName)


def getLogFileSeverity():
    return str(java.lang.System.getProperty("weblogic.log.LogFileSeverity"))


def setLogFileSeverity(level):
    java.lang.System.setProperty("weblogic.log.LogFileSeverity",LEVELS.get(level.upper()))


def getFileCount():
    return str(java.lang.System.getProperty("weblogic.log.FileCount"))


def setFileCount(count):
    java.lang.System.setProperty("weblogic.log.FileCount",str(count))


def getFileMinSize():
    return str(java.lang.System.getProperty("weblogic.log.FileMinSize"))


def setFileMinSize(size):
    java.lang.System.setProperty("weblogic.log.FileMinSize",str(size))


def getConsoleSeverity():
    return str(java.lang.System.getProperty("weblogic.log.StdoutSeverity"))


def setConsoleSeverity(level):
    java.lang.System.setProperty("weblogic.log.StdoutSeverity",LEVELS.get(level.upper()))







