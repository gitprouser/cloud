package com.example.rest.json;

import org.codehaus.jettison.json.JSONObject;

import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Parse JSON from SMAgent and store object as a Map.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

public class ParseJSON<T> {

    /**
     * First time handshake from SMAgent with SMProxyServer
     * {
     *   TOKEN : 12354,
     * }
     */
    public static Map<String, String> parseFirstReq(JSONObject json) {
        Map<String, String> map = new LinkedHashMap<String, String>();
        Iterator keys = json.keys();
        while(keys.hasNext()) {
            System.out.println(keys);
            keys.next();
        }
        return map;
    }

    /**
     * Parse a JSON from SMAgent and store as a map.
     * @return
     */
    public static Map<String, String> parseTaskStatusJSON(JSONObject json) {
        return null;
    }
}
