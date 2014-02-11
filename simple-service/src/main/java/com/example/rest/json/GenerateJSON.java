package com.example.rest.json;

import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.io.*;

/**
 * Generates a JSON for SMProxyTaskMgr.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

//TODO append doc with actual json format

public final class GenerateJSON {


    /**

    private static String scriptlet = "import math\ndef fib(n):\n\tif n == 1:\n\t\treturn 1" +
        "\n\tif n==0:\n\t\treturn 0\n\telse:\n\t\treturn fib(n-1)" +
        " + fib(n-2)\n\ndef execute(dict):\n\tprint fib(dict[\"nested\"][\"k\"])\nprint math.sin(30)";
     */


    /**
     * Generates a JSON with the command execution payload for the SMAgent.
     *
     * @return
     */
    public static JSONObject getNextTaskJSON(Map<String, String> json) {
        return null;
    }

    /**
     * Generates a JSON polling (single request) for the task status details
     * from SMAgent.
     *
     * @return
     */
    public static JSONObject getTaskStatusJSON(Map<String, String> json) {
        throw new RuntimeException("Unimplemented for now");
    }

    /**
     * Get Scriptlet for execution
     * JSON format
     * {
     *      "databag : [
     *          "variables" : "",
     *          "variable2" : ""
     *          // NESTING the data bag 
     *          "variable3" : {
     *            "var1" : "",
     *            "var2" : "",
     *          } 
     *      ],
     *      "script" : ""
     * }
     *
     *
     */
    public static JSONObject getScriptletJSON() throws Exception {
        JSONObject payload = new JSONObject();
 
        try {
            JSONObject var = new JSONObject();
            var.put("N", 30);
            var.put("M", 15);
            JSONObject nested = new JSONObject();
            nested.put("k", 10);
            nested.put("i", 10);
            var.put("nested", nested);
            payload.put("data-bag", var);
            payload.put("script", readFile());
            //payload.put("script", scriptlet);
        } catch (JSONException e) {
            e.printStackTrace();
            throw new Exception("Critical Failure");
        }
        return payload;
    }


    private static String readFile() {
      byte[] b = new byte[10000];
      BufferedInputStream bis = null;
      try {
        bis = new BufferedInputStream( new FileInputStream(new File("scriptlet.py")));
          for (int off = 0, len = 1024; off < b.length && bis.read(b, off, len)  > -1; off+= len)
              ;
      } catch (IOException e) {
        System.out.println("Couldn't copy the entire file" + e.getMessage());     
      } finally {
        try { if (bis != null) bis.close(); }
        catch(IOException io) {
            System.out.println("buffered input stream did not close");
        }
      }
      String retVal = new String(b);
      System.out.println(retVal);
      return retVal;
    }

}
