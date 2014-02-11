package com.example;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.codehaus.jettison.json.JSONObject;
import org.glassfish.grizzly.http.server.HttpServer;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertEquals;

public class MyResourceTest {

    private HttpServer server;
    private WebTarget target;

    @Before
    public void setUp() throws Exception {
        // start the server
        server = Main.startServer();
        // create the client
        Client c = ClientBuilder.newClient();

        // uncomment the following line if you want to enable
        // support for JSON in the client (you also have to uncomment
        // dependency on jersey-media-json module in pom.xml and Main.startServer())
        // --
        // c.configuration().enable(new org.glassfish.jersey.media.json.JsonJaxbFeature());

        target = c.target(Main.BASE_URI);
    }

    @After
    public void tearDown() throws Exception {
        server.stop();
    }

    /**
     * Test to see that the message "Got it!" is sent in the response.
     */
    @Test
    public void testGetIt() {
      //String str = "{\"data-bag\":{\"N\":30,\"M\":15,\"nested\":{\"k\":10,\"i\":10}},\"script\":\"#\"import math\\ndef fib(n):\\n\\tif n == 1:\\n\\t\\treturn 1\" +\n#\"\\n\\tif n==0:\\n\\t\\treturn 0\\n\\telse:\\n\\t\\treturn fib(n-1)\" +\n#\" + fib(n-2)\\n\\ndef execute(dict):\\n\\tprint fib(dict[\\\"nested\\\"][\\\"k\\\"])\\nprint math.sin(30)\";\nimport math\n\n\ndef fib(n):\n    if n == 1:\n        return 1\n    if n == 0:\n        return 0\n    else:\n        return fib(n - 1) + fib(n - 2)\n\n\ndef execute(dict):\n    print fib(dict[\"nested\"][\"k\"])\n    print math.sin(30)\"}";
      Response responseMsg = target.path("/smproxy/receive-task-status").request().post(Entity.entity(new String("hello world"),
              MediaType.valueOf(MediaType.APPLICATION_JSON)));
      assertEquals(201, responseMsg.getStatus());
    }
}
