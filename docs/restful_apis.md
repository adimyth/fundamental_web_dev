# REpresentational STate Transfer (REST)
REST is an architectural style, or design pattern for APIs. REST stands for REpresentational State Transfer.

> REST was defined by Roy Fielding, a computer scientist. He presented the REST principles in his PhD dissertation in 2000.

* Client - the client is the person or software who uses the API. It can be a developer a web browser, etc
* Resource - a resource can be any object the API can provide information about. *In Instagram’s API, for example, a resource can be a user, a photo, a hashtag. Each resource has a unique identifier.*

**A RESTful web application provides information about itself in the form of information about its resources.** It also enables users to take action on those resources (CRUD). In order for your APIs to be RESTful we have to follow a set of constraints when writing them.

> When a RESTful API is called, the server will transfer to the client the representation of the state of the requested resource. Hence the abrreviation, REpresentational State Transfer. This representation can be in any format example JSON, XML, HTML, etc

What the server does when you, the client, call one of its APIs depends on 2 things that you need to provide to the server:
1. An identifier for the resource you are interested in. This is the URL for the resource, also known as the endpoint. In fact, URL stands for Uniform Resource Locator.
2. The operation you want the server to perform on that resource, in the form of an HTTP method, or verb. The common HTTP methods are GET, POST, PUT, and DELETE.

## Constraints
### Uniform Interface
### Client-Server Separation
The client and the server act independently. Interaction between them is only in the form of requests, initiated by the client only, and responses, which the server send to the client only as a reaction to a request. The server doesn’t start sending away information about the state of some resources on its own.

### Stateless
As per the REST architecture, **the server does not store any state about the client session on the server-side.** This restriction is called *Statelessness*. *Each request from the client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.* Client is responsible for storing and handling all application state-related information on client side.
> Each request MUST stand alone and should not be affected by the previous conversation happened from the same client in past.

### Layered System
Between the client who requests a representation of a resource’s state, and the server who sends the response back, there might be a number of servers in the middle. These servers might provide a security layer, a caching layer, a load-balancing layer, or other functionality. Those layers should not affect the request or the response. The client is agnostic as to how many layers, if any, there are between the client and the actual server responding to the request.

### Cacheable
Cache constraints require that the data within a response to a request be implicitly or explicitly labeled as cacheable or non-cacheable. Caching is the ability to store copies of frequently accessed data in several places along the request-response path. *When a consumer requests a resource representation, the request goes through a cache or a series of caches (local cache, proxy cache, or reverse proxy) toward the service hosting the resource. If any of the caches along the request path has a fresh copy of the requested representation, it uses that copy to satisfy the request.* If none of the caches can satisfy the request, the request travels to the service (or origin server as it is formally known).

> By using HTTP headers, an origin server indicates whether a response can be cached and, if so, by whom, and for how long

* `GET` requests should be cacheable by default
* `POST` requests are not cacheable by default but can be made cacheable if either an `Expires` header or a `Cache-Control` header with a directive, to explicitly allows caching, is added to the response.
	* `Expires` - The Expires HTTP header specifies an absolute expiry time for a cached representation. Beyond that time, a cached representation is considered stale and must be re-validated with the origin server.
	* `Cache-Control` - These directives determine whether a response is cacheable, and if so, by whom, and for how long e.g. max-age or s-maxage directives. 	
* Responses to `PUT` and `DELETE` requests are not cacheable at all.

### Code on Demand
Optional. The client can request code from the server, and then the response from the server will contain some code, usually in the form of a script. The client then can execute that code.

## Compression
### Accept-Encoding
While requesting resource representations – along with an HTTP request, the client sends an `Accept-Encoding` *header* that says what kind of compression algorithms the client understands. The two standard values for Accept-Encoding are `compress` and `gzip`.
```bash
GET        /employees         HTTP/1.1
Host:     www.domain.com
Accept:     text/html
Accept-Encoding:     gzip,compress
```
`406 (Not Acceptable)` - When the server cannot send what the client understands (specified in `Accept*` in request)

### Content-Encoding
If the server understands one of the compression algorithms from `Accept-Encoding`, it can use that algorithm to compress the representation before serving it. When successfully compressed, server lets know the client of encoding scheme by another *HTTP header* i.e. `Content-Encoding`. The original media/content type is specified in the `Content-Type` header.
```bash
200 OK
Content-Type:     text/html
Content-Encoding:     gzip
```
`415 (Unsupported Media Type)` - Return if the `Accept-Encoding` from client request has something that the server does not understand

## Extras
### Application State vs Resource State
*Application state* is server-side data which servers store to identify incoming client requests, their previous interaction details, and current context information.

*Resource state* is the **current state of a resource** on a server at any point of time – and it has nothing to do with the interaction between client and server. It is what you get as a response from the server as API response. You refer to it as resource representation. REST statelessness means being free on application state.

### Advantages of Statelessness
There are some very noticeable advantages for having REST APIs stateless -
1. Statelessness helps in scaling the APIs to millions of concurrent users by deploying it to multiple servers. Any server can handle any request because there is no session related dependency.
2. Being stateless makes REST APIs less complex – by removing all server-side state synchronization logic.
3. A stateless API is also easy to cache as well. Specific software can decide whether or not to cache the result of an HTTP request just by looking at that one request. There’s no nagging uncertainty that state from a previous request might affect the cacheability of this one. It improves the performance of applications.
4. The server never loses track of “where” each client is in the application because the client sends all necessary information with each request.

### Content Negotiation
Generally, resources can have multiple representations.

#### Content Negotiation using `HTTP Headers`
`Content-Type` can be used by both clients & servers to identify the format of the data in the request(client) or response(server) and therefore help the other part interpret the information correctly

`Accept` header is used by clients to tell the server which type of content they expect/prefer as response. It is possible to have multiple values in Accept header. The client may want to give multiple values in the accept header when the client is not sure about if its desired representation is present or supported by the server at that time. Example - `Accept: application/json,application/xml;q=0.9,*/*;q=0.8`

#### Content negotiation using URL patterns
Another way to pass content type information to the server, the client may use the specific extension in resource URIs. For example, a client can ask for details using:
```bash
http://rest.api.com/v1/employees/20423.xml
http://rest.api.com/v1/employees/20423.json
```
Here the client is requesting for XML in the first request & JSON in the second

## Resources
https://restfulapi.net/statelessness/
https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f
https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-2-rest-constraints-129a4b69a582


