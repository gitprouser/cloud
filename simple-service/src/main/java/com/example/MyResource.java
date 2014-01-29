package com.example;

import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;


import java.util.concurrent.atomic.AtomicInteger;

/**
 * Root resource (exposed at "myresource" path)
 */
@Path("myresource")
public class MyResource {
    private String[] commands = {"ls -a", "du -h", "whoami", 
                        "echo \"guest\" | sudo -S du -h /tmp"};
    private String script = "def fib(n):\n\tif n == 1:\n\t\treturn 1\n\tif n==0:\n\t\treturn 0\n\telse:\n\t\treturn fib(n-1) + fib(n-2)\nprint fib(%s)"; 
    private boolean isCompleted = false;
    private static int incr = 0;
    private static int N = 0;

    /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     *
     * @return String that will be returned as a text/plain response.
     */
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getIt() {
      String val; 
      synchronized (this) {
        System.out.println(this.hashCode());
        if (incr > (commands.length - 1))
          incr = 0;
        System.out.println(incr);
        val = commands[incr++];
      }
      return val; 
    }

    @GET
    @Path("script")
    @Produces(MediaType.TEXT_PLAIN)
    public String getScript() {
      String s = String.format(script, Integer.toString(N++)); 
      System.out.println(String.format(script, Integer.toString(N++)));
      return s; 
    }

    /**
     * Simple post request for getting back result of the action.
     *
     */
    @POST
    @Consumes("text/plain")
    public void postClichedMessage(String log) {
      System.out.println(log); 
    }
}
