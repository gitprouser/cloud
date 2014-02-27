#!/bin/sh

#This is a example of two methods of calling the common logging from shell script

echo "Embedded Style"
echo ""
python <<END
import pythonUtils.commonLogging as commonLogging
commonLogging.setFileName("test.log")
shellLogger = commonLogging.getLogger('testShell')
commonLogging.displayConfigStatus(shellLogger)
shellLogger.info("Debug Message from embedded shell script")
shellLogger.info("Info Message from embedded shell script")
shellLogger.info("Warning Message from embedded shell script")
shellLogger.info("Error Message from embedded shell script")
shellLogger.info("Critical Message from embedded shell script")
END


echo ""
echo "cmd option using script provided in pythonUtils"
echo ""
# p1 = message type (DEBUG, INFO, WARNING, ERROR, CRITICAL) - Required
# p2 = message - Required
# p3 = log file name - Optional - (default cps.log)
# p4 = logger name - Optional - (default CPSLogger)
# p5 = Status output flag  - Optional - (default False)
python ${PYTHONUTILSPATH}/shellLogging.py Debug "Debug message from shell utility" test.log shell-logger True
python ${PYTHONUTILSPATH}/shellLogging.py Info "Info message from shell utility" test.log shell-logger
python ${PYTHONUTILSPATH}/shellLogging.py Warning "Warning message from shell utility" test.log shell-logger
python ${PYTHONUTILSPATH}/shellLogging.py Error "Error message from shell utility" test.log shell-logger
python ${PYTHONUTILSPATH}/shellLogging.py Critical "Critical message from shell utility" test.log shell-logger