package com.example.utils;

import com.example.entities.SMTaskServer;

import java.util.HashMap;
import java.util.Map;

/**
 * SMProxyTaskMgr provides SM-agents with FileSMTaskServerImpl. Each
 * FileSMTaskServerImpl is assigned to a specific SM-agent after a Registration
 * process.
 *
 * TODO This has to be thread safe as multiple requests from same agent might
 *      lead to multiple SMTaskServers being created for the same SMAgent
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */


public enum SMProxyTaskMgr {
    SM_PROXY_TASK_MGR;

   // A map between {FileSMTaskServerImpl : SMAgentID}
   private Map<Integer, SMTaskServer> taskServerTable = new HashMap <Integer, SMTaskServer>();

    /**
     * Update the taskServerTable
     * @param agentReq
     * @return
     */
   public SMTaskServer getTaskServerForSMAgent(Map<String, String> agentReq) {
       /**
        * 1.) If table entry does not exists
        *   1.1.) Register the SMAgent via SMRegistration
        *   1.2.) Create new SMTaskServer for SMAgent
        *   1.4.) Call setTaskServerForSMAgent synchronously and update table.
        *   1.5.) call the FileSMTaskServerImpl.getNextTask()
        * 2.) If Table entry exits
        *   2.1) Get Instance and call the getNextTask()
        */
       return null;
   }

    /**
     * A thread safe method which should append table entries in a thread safe
     * manner. When a agent's request is being process all other agents must
     * wait...
     *
     * @TODO should design this better for more concurrency.
     * @param request
     * @return
     */
   public boolean setTaskServerForSMAgent(Map<String, String> request) {
       return false;
   }

}
