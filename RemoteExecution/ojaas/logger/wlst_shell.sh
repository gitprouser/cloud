#!/bin/bash

export COMMON_LOGGING_CFG="test-config.ini"
export COMMON_LOGGING_SECTION="test"

python ${PYTHONUTILSPATH}/shellLogging.py Info "Informational message recorded from shell script start"

$WL_HOME/common/bin/wlst.sh<<END
import pythonUtils.commonLogging as commonLogging
wlstShellLogger = commonLogging.getLogger('wlstShell')
commonLogging.displayConfigStatus(wlstShellLogger)
wlstShellLogger.info("Debug Message from embedded wlst shell script")
wlstShellLogger.info("Info Message from embedded wslt shell script")
wlstShellLogger.info("Warning Message from embedded wlst shell script")
wlstShellLogger.info("Error Message from embedded wlst shell script")
wlstShellLogger.info("Critical Message from embedded wlst shell script")
END

python ${PYTHONUTILSPATH}/shellLogging.py Info "Informational message recorded from shell script finish"