package com.example.rest.json;

import org.codehaus.jettison.json.JSONObject;

import java.util.Map;

/**
 * Parse JSON from SMAgent and store object as a Map.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

public class ParseJSON {

    /**
     * First time handshake from SMAgent with SMProxyServer
     */
    public Map<String, String> parseFirstReq(JSONObject json) {
        return null;
    }

    /**
     * Parse a JSON from SMAgent and store as a map.
     * @return
     */
    public Map<String, String> parseTaskStatusJSON(JSONObject json) {
        return null;
    }
}
