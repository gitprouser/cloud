package com.example.entities;

import org.codehaus.jettison.json.JSONObject;

import java.util.Map;

/**
 * Defines tasks for the SMAgent. One to one mapping from SMAgent and
 * FileSMTaskServerImpl.
 * In future this will become an entity for persisting.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

public interface SMTaskServer {

    /**
     * Provide next task for execution from queue or file.
     */
    public Map<String, String> getNextTask();

    /**
     * Query task details from SMAgent.
     */
    public Map<String, String> getTaskStatus();

    /**
     * Receive task status from SMAgent.
     * Updates the cache after job status completed.
     */
    public boolean receiveTaskStatus( Map<String, String> taskStatus);
}
