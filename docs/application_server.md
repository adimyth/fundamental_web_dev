# Application Server
Application Server is a term that sometimes is mixed with a web server. While a web server handles mainly HTTP protocols, the application server deals with several different protocols, including, but not limited, to HTTP.

An application server's fundamental job is to provide its clients with access to what is commonly called **business logic**, which generates *dynamic content*.
On the other hand a web server's fundamental job is to accept & fulfill request from clients for **static contents**


## Application & Web Server Together
In a typical deployment, a website that provides both static & dynamic content uses web server for static content & application server for dynamic content. 
A reverse proxy and load balancer sits infront of one or more web servers and one or more application server to route traffic to the appropriate server first 
based on the type of content requested & then based on the load-balancing algorithm. Most load balancers also act as reverse proxy servers.

The Web server's main job is to display the site content and the application server is in charge of the logic, the interaction between the user and the displayed content. The application server is working in conjunction with the web server, where one displays and the other one interacts.
