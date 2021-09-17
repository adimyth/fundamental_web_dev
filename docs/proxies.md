# Forward Proxy Server
A forward proxy, often called a proxy, proxy server, or web proxy, is a server that sits in front of a group of client machines. When those computers make requests to sites and services on the Internet, the proxy server intercepts those requests and then communicates with web servers on behalf of those clients, like a middleman.

![Forward Proxy](https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/forward-proxy-flow.svg)

In a standard Internet communication, computer A would reach out directly to computer C, with the client sending requests to the origin server and the origin server responding to the client. When a forward proxy is in place, A will instead send requests to B, which will then forward the request to C. C will then send a response to B, which will forward the response back to A.

* **To block access to certain content** - Conversely, proxies can also be set up to block a group of users from accessing certain sites. For example, a school network might be configured to connect to the web through a proxy which enables content filtering rules, refusing to forward responses from Facebook and other social media sites.
* **To protect their identity online** - In some cases, regular Internet users simply desire increased anonymity online, but in other cases, Internet users live in places where the government can impose serious consequences to political dissidents. Criticizing the government in a web forum or on social media can lead to fines or imprisonment for these users. If one of these dissidents uses a forward proxy to connect to a website where they post politically sensitive comments, the IP address used to post the comments will be harder to trace back to the dissident. Only the IP address of the proxy server will be visible.
* **Bypass a content restriction.** Famously, your UK Netflix subscription won’t work in the USA. But if you connect to a UK proxy server it looks like you are watching TV from the UK and everything works as expected.

# Reverse Proxy Server
A reverse proxy is a server that sits in front of one or more web servers, intercepting requests from clients. This is different from a forward proxy, where the proxy sits in front of the clients. With a reverse proxy, when clients send requests to the origin server of a website, those requests are intercepted at the network edge by the reverse proxy server. The reverse proxy server will then send requests to and receive responses from the origin server.

![Reverse Proxy](https://www.cloudflare.com/img/learning/cdn/glossary/reverse-proxy/reverse-proxy-flow.svg)

Typically all requests from D would go directly to F, and F would send responses directly to D. With a reverse proxy, all requests from D will go directly to E, and E will send its requests to and receive responses from F. E will then pass along the appropriate responses to D.

* **Load balancing** - A popular website that gets millions of users every day may not be able to handle all of its incoming site traffic with a single origin server. Instead, the site can be distributed among a pool of different servers, all handling requests for the same site. In this case, a reverse proxy can provide a load balancing solution which will distribute the incoming traffic evenly among the different servers to prevent any single server from becoming overloaded. In the event that a server fails completely, other servers can step up to handle the traffic.
* **Protection from attacks** - With a reverse proxy in place, a web site or service never needs to reveal the IP address of their origin server(s). This makes it much harder for attackers to leverage a targeted attack against them, such as a DDoS attack. Instead the attackers will only be able to target the reverse proxy
Global Server Load Balancing (GSLB) - In this form of load balancing, a website can be distributed on several servers around the globe and the reverse proxy will send clients to the server that’s geographically closest to them. This decreases the distances that requests and responses need to travel, minimizing load times.
* **Caching** - A reverse proxy can also cache content, resulting in faster performance
* **SSL encryption** - Encrypting and decrypting SSL (or TLS) communications for each client can be computationally expensive for an origin server. A reverse proxy can be configured to decrypt all incoming requests and encrypt all outgoing responses, freeing up valuable resources on the origin server.

# Forward vs Reverse Proxy
The difference between a forward and reverse proxy is subtle but important. A simplified way to sum it up would be to say that a forward proxy sits in front of a client and ensures that no origin server ever communicates directly with that specific client. On the other hand, a reverse proxy sits in front of an origin server and ensures that no client ever communicates directly with that origin server.

# VPN vs Forward Proxy
Proxy servers act as relays between the website you’re visiting and your device. Your traffic goes through a middle-man, a remote machine used to connect you to the host server. The proxy server hides your original IP address so that the website sees the IP of the proxy.

Problems with proxies:
1. All of the web traffic that passes through a proxy can be seen by the server owner. Do you know the proxy owner? Can they be trusted?
2. Web traffic between your computer and proxy, and proxy and website is unencrypted, so a skilled hacked can intercept sensitive data in transit and steal it.
3. Proxies only work on the application level, meaning it only reroutes the traffic coming from a single app you set your proxy up with. Hence for each app u need to setup a separate proxy

**HTTP Proxies** – These only cater to web pages. If you set up your browser with an HTTP proxy, all your browser traffic will be rerouted through it. They are useful for web browsing and accessing geo-restricted websites.

**SOCKS Proxies** – These proxies are not limited to web traffic but still only work on the application level. For example, you can set it up on a game, video streaming app, or a P2P platform. Although they can handle all kinds of traffic, they are usually slower than HTTP proxies because they are more popular and often have a higher load.

## VPNs
A VPN is quite similar to a proxy. Your computer is configured to connect to another server, and it may be that your route web traffic through that server. But where a proxy server can only redirect web requests, a VPN connection is capable of routing and anonymising all of your network traffic. VPN works on the operating system level, meaning that it redirects all your traffic, whether it’s coming from your browser or a background app.

But there is one significant advantage of the VPN – **all traffic is encrypted**. This means that hackers cannot intercept data between your computer and the VPN server, so your sensitive personal information cannot be compromised.

Routing your web traffic through an advanced VPN helps you avoid malware infections, phishing scams and fake websites.

> It’s important to note that both VPN and proxy providers can log user data such as user IP addresses, DNS requests, and other details. You should avoid such providers because they can give this information to law enforcement agencies, advertisers, or hackers if their servers get breached.
