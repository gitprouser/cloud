package com.example.rest.endpoints;


import javax.ws.rs.core.MediaType;
import java.util.UUID;

import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
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
    @Path("get-next-task")
    @Produces(MediaType.APPLICATION_JSON)
    public JSONObject getNextTask() {
        return null;
    }

    /**
     *
     */
    @GET
    @Path("get-task-details")
    @Produces(MediaType.APPLICATION_JSON)
    public String getTaskDetails() {
        return null;
    }

    /**
     * Simple post request for getting back result of the action.
     */
    @POST
    @Path("receive-task-status")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response receiveTaskStatus(JSONObject result) {
        return Response.status(201).entity("recieved").build();
    }
}
