package com.example.rest.json;

/**
 * Defines the types of jobs supported by the Remote Execution Agents.
 * @author Dhawan Gajendran Gayash
 */
public enum JobTypes {

    /**
     * JOB TYPE: EXECUTE_TASK
     * Executing a given task.
     */
    execute_task,
    /** JOB TYPE: UPDATE_SMPROXY
     * Downloads the new SMPROXY and updates with the new software
     * and starts the new sm-proxy
     */
    update_smproxy,

    /**
     * JOB TYPE: STATUS_SMPROXY
     * Returns the status of the sm-proxy.
     */
    status_smproxy,

    /**
     * JOB TYPE: ABORT_TASK
     * Aborts a running task, killing a process if running.
     */
    abort_task;
}
