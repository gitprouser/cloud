package com.example.entities;

import com.example.rest.json.JobTypes;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.UUID;

/**
 * File implementation SMTaskServer. The SMAgent tasks are written in a file
 * FileSMTaskServerImpl reads the file and creates the payload and sends it to
 * RESTEndPoint for converstion to JSON and streaming through SMProxyServerEndPoint.
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

public class FileSMTaskServerImpl implements SMTaskServer{
    /**
     * smAgentsDetails[0] = ID
     * smAgentsDetails[1] = IP
     */
    String[] smAgentDetails = new String[2];


    //TODO timeout for each job queue... We should check if the job executed or not.

    /**
     * The current Job ID being executed by the SMAgent
     */
    private String jobID;

    /**
     * pointer on file
     */
    private Scanner sc;

    private File logDir;

    /**
     * Every SMAgent on client side will have a SMTaskServer on server.
     * SMProxyTaskMgr will instantiate <strong>this</strong> after registration.
     *
     * @param smAgentID
     * @param smAgentIP
     */

    public FileSMTaskServerImpl(String smAgentID, String smAgentIP) throws
            FileNotFoundException
    {
        smAgentDetails[0] = smAgentID;
        smAgentDetails[1] = smAgentIP;
        sc = new Scanner(new File("CommandList"));
        logDir = new File("/tmp/SMAgent" + smAgentID);
        logDir.mkdirs();
    }

    /**
     * Read file and get the next action.
     * Generate JOB_ID for each action.
     * @return
     */
    public Map<String, String> getNextTask() {
        /**
         * 1.) Read the CommandList file
         * 2.) Generate a unique job id for the parsed line
         * 3.) return Map
         */
        Map<String, String> job = new HashMap<String, String>();
        if(sc.hasNextLine()) {
            String cmd = sc.nextLine();
            jobID = generateJobID();
            job.put("JOB_ID", jobID);
            job.put(JobTypes.execute_task.toString(), cmd);
        } else {
            //TODO NEED TO REMOVE THIS BLOCK AS JOBS NEVER STOP!
            job.put("COMPLETED", "True");
        }
        return job;
    }

    /**
     * TODO: Figure out what's the goal here.
     *
     * @return
     */
    public Map<String, String> getTaskStatus() {
        /**
         * 1.) Generate a unique job id for the parsed line
         * 3.) construct JSONObject with the payload.
         * 4.) return JSONObject to caller.
         */
        return null;
    }

    /**
     * Updates the Job as completed.
     *
     * @param
     * @return
     */
    public boolean receiveTaskStatus(Map<String, String> taskStatus) {

        return false;
    }

    public String getCurrJobID() {
        return jobID;
    }

    public String getSMAgent() {
        return smAgentDetails[1];
    }

    /**
     * Generates a job Id for each line in the file.
     * @return
     */
    private String generateJobID() {
        return UUID.randomUUID().toString();
    }
}
