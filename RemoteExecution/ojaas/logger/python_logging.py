import pythonUtils.commonLogging as commonLogging

#Set configuration value
commonLogging.setFileName("test.log")
commonLogging.setLogFileSeverity(commonLogging.DEBUG)
commonLogging.setFileCount(10)
commonLogging.setFileMinSize(1000)
commonLogging.setConsoleSeverity(commonLogging.INFO)

#Display the status of Configuration
commonLogging.displayConfigStatus()

#create a logger
cpsLogger = commonLogging.getLogger('CPSLogger')

#log desired level messages
cpsLogger.debug('Debugging Message from python logging')
cpsLogger.info('informational message from python logging')
cpsLogger.warning('Warning message from python logging')
cpsLogger.error('Error message from python logging')
cpsLogger.critical('Critical message from python logging')

#Can have multiple loggers
ocsLogger = commonLogging.getLogger('OCSLogger')

ocsLogger.debug('Debugging Message from python logging')
ocsLogger.info('informational message from python logging')
ocsLogger.warning('Warning message from python logging')
ocsLogger.error('Error message from python logging')
cpsLogger.critical('Critical message from python logging')
