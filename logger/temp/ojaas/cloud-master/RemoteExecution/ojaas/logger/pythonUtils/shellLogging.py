import sys
import commonLogging

#This script is used to aid in invoking the python common
#logging from a shell script
#
# Example:
#   python ./cpsUtils/shellLogging.py Debug "Debug message" ext.log shell-logger True
#   python ./cpsUtils/shellLogging.py INFO "Info message" ext.log shell-logger
#
# Usage
# p1 = message type (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# p2 = message
# p3 = log file name (default cps.log)     (optional)
# p4 = logger name (default CPSLogger)     (optional)
# p5 = Status output flag (default False)  (optional)
def out(messageType,
        message,
        fileName=commonLogging.LOG_FILE_NAME,
        loggerName=commonLogging.LOGGER_NAME,
        displayStatus='False'
        ):

    commonLogging.setFileName(fileName)
    logger = commonLogging.getLogger(loggerName)

    if displayStatus.upper() == 'TRUE':
       commonLogging.displayConfigStatus(logger)


    if (messageType.upper() == commonLogging.DEBUG):
        logger.debug(message)
    elif (messageType.upper() == commonLogging.INFO):
        logger.info(message)
    elif (messageType.upper() == commonLogging.WARNING):
        logger.warning(message)
    elif (messageType.upper() == commonLogging.ERROR):
        logger.error(message)
    elif (messageType.upper() == commonLogging.CRITICAL):
        logger.critical(message)
    else:
        logger.info("invalid message type specified " + messageType + "default to INFO")
        logger.info(message)


if len(sys.argv) < 3:
    sys.exit("Usage:  __module__  messageType messageType <fileName> <loggerName> <displayStatus>")
else:
    numberArgs = len(sys.argv)
    if numberArgs == 3:
        out(sys.argv[1],sys.argv[2])
    elif numberArgs == 4:
        out(sys.argv[1],sys.argv[2],sys.argv[3])
    elif numberArgs == 5:
         out(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    else:
         out(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])


