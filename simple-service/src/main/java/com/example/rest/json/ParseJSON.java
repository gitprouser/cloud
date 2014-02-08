package com.example.rest.json;

import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

import java.util.HashMap;
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

    private final static String outputData = "output";

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

    /**
     *
     *
     */
    public Map<String, String> parseResult(JSONObject json) throws JSONException {
        Map<String, String> result = new HashMap<String, String>();
        Iterator<JSONObject> iter = json.keys();
        while(iter.hasNext()) {
            JSONObject key = iter.next();
            if (iter.next().toString() == outputData)  {
                result.put(outputData, (String) json.get(key.toString()));
            }

        }
        return result;
    }
}
