package com.example.rest.json;

import org.codehaus.jettison.json.JSONObject;

import java.util.Map;

/**
 * Generates a JSON for SMProxyTaskMgr.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

//TODO append doc with actual json format

public final class GenerateJSON {

    /**
     * Generates a JSON with the command execution payload for the SMAgent.
     *
     * @return
     */
    public JSONObject getNextTaskJSON(Map<String, String> json) {
        return null;
    }

    /**
     * Generates a JSON polling (single request) for the task status details
     * from SMAgent.
     *
     * @return
     */
    public JSONObject getTaskStatusJSON(Map<String, String> json) {
        throw new RuntimeException("Unimplemented for now");
    }

}
