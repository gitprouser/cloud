package com.example.rest.endpoints;


import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.util.Map;
import java.util.UUID;

import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import com.example.entities.SMTaskServer;
import com.example.rest.json.GenerateJSON;
import com.example.rest.json.ParseJSON;
import com.example.utils.SMProxyTaskMgr;
import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;


/**
 * Root resource (exposed at "myresource" path)
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

@Path("smproxy")
public class SMProxyServerEndPoint {
    /**
     * Recieves JSON from SMAgent call SMProxyTaskMgr
     *
     * @return
     */
    @GET
    @Path("hello-world")
    @Produces(MediaType.APPLICATION_JSON)
    public String getNextTask() {
        return "helloworld";
    }

    /**
     * Initial handshake from SMAgent and SMProxyserver
     */
    @POST
    @Path("handshake")
    @Produces(MediaType.APPLICATION_JSON)
    public JSONObject getFirstHandShake(JSONObject salt) {
        Map<String, String> firstMsg = ParseJSON.parseFirstReq(salt);
        SMTaskServer smTaskServer = SMProxyTaskMgr.SM_PROXY_TASK_MGR.getTaskServerForSMAgent(firstMsg);
        return GenerateJSON.getNextTaskJSON(smTaskServer.getNextTask());
    }

    /**
     *
     */
    @GET
    @Path("get-Task-Details")
    @Produces(MediaType.APPLICATION_JSON)
    public String getTaskDetails() throws Exception {
        JSONObject retVal = GenerateJSON.getScriptletJSON();
        return retVal.toString();
    }

    /**
     * Simple post request for getting back result of the action.
     */
    @POST
    @Path("receive-task-status")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response receiveTaskStatus(String result) throws JSONException {
        System.out.println(result);
        //Map<String, String> resMap = ParseJSON.parseResult(result);
        //System.out.println(resMap.get("output"));
        return Response.status(201).entity("received").build();
    }
}
