package com.example.operations;

import java.util.Map;

/**
 * Registers a SMAgent to a FileSMTaskServerImpl.
 *
 *
 *
 *
 * User: Dhawan Gajendran Gayash
 * Date: 1/29/14
 */

public class SMRegistration {
    /**
     * Handshake from SMAgent. After registration a SMAgent will have a
     * FileSMTaskServerImpl on the server side generated.
     *
     * @return True if a new FileSMTaskServerImpl has been assigned to the SMAgent
     */
    public long handShake(Map<String, String> agentRequest) {
        throw new UnsupportedOperationException("Need to understand " +
                "handshake before implementation");
    }
}
