# WSGI Framework Implementations
A web framework consists of a set of libraries and a **main handler** within which you can build custom code to implement a web application (i.e. an interactive web site). Most web frameworks include patterns and utilities to accomplish at least the following:

**URL Routing** - Matches an incoming HTTP request to a particular piece of Python code to be invoked
**Request and Response Objects** - Encapsulates the information received from or sent to a user’s browser
**Template Engine** - Allows for separating Python code implementing an application’s logic from the HTML (or other) output that it produces
**Development Web Server** - Runs an HTTP server on development machines to enable rapid development; supports auto-reload

---
**Django**

Django is a “batteries included” web application framework, and is an excellent choice for creating content-oriented websites. By providing many utilities and patterns out of the box, Django aims to make it possible to build complex, database-backed web applications quickly, while encouraging best practices in code written using it.

The community has many pre-built re-usable modules that can be incorporated into any new project. The majority of new Python web applications today are built with Django.

---
**Flask**

Flask is a “microframework” for Python, and is an excellent choice for building smaller applications, APIs, and web services. Building an app with Flask is a lot like writing standard Python modules, except some functions have routes attached to them. It’s really beautiful.

Rather than aiming to provide everything you could possibly need, Flask implements the most commonly-used core components of a web application framework, like URL routing, request and response objects, and templates.

For other things like database access, form validation you can use many extensions that are available. For projects that don't need Django, Flask is a good choice

---
**Falcon**

Falcon is a good choice when your goal is to build RESTful API microservices that are fast and scalable.
* Class-based (a great advantage for REST APIs)
* Only 2 minor dependencies
* Performance is amazing
* Intended only for APIs which makes it more focused and minimal
* Excellent design, documentation and codebase

---
**Sanic**

---
**FastAPI**
FastAPI is a modern web framework for building APIs with Python 3.6+.

It has very high performance as it is based on Starlette and Pydantic.

FastAPI takes advantage of standard Python type declarations in function parameters to declare request parameters and bodies, perform data conversion (serialization, parsing), data validation, and automatic API documentation with OpenAPI 3 (including JSON Schema).

It includes tools and utilities for security and authentication (including OAuth2 with JWT tokens), a dependency injection system, automatic generation of interactive API documentation, and other features.

---
**Bottle**
* Decorator-based
* No dependencies
* Very similar to Flask but a lot faster
* No new releases for over a year

---
**OTHERS**
* Tornado
* Pyramid
* Masonite

# WSGI Server Implementations
Stand-alone WSGI servers typically use less resources than traditional web servers and provide top performance

---
**Gunicorn**

Gunicorn (Green Unicorn) is a pure-Python WSGI server used to serve Python applications. Unlike other Python web servers, it has a thoughtful user interface, and is extremely easy to use and configure.

Gunicorn has sane and reasonable defaults for configurations. However, some other servers, like uWSGI, are tremendously more customizable, and therefore, are much more difficult to effectively use.

Gunicorn is the recommended choice for new Python web applications today.

---
**Waitress**

Waitress is a pure-Python WSGI server that claims “very acceptable performance”. Its documentation is not very detailed, but it does offer some nice functionality that Gunicorn doesn’t have (e.g. HTTP request buffering).

---
**uWSGI**


---
**Meinhald (offers workers for Gunicorn)**

---
**Others**
* Bjoern - Written in C & very lightweight. One of the highest performing WSGI servers available. Considered faster than Gunicorn & less bloated than uWSGI.
* CherryPy
* Tornado

## References
https://fastapi.tiangolo.com/alternatives/
https://fgimian.github.io/blog/2018/05/17/choosing-a-fast-python-api-framework/
https://docs.python-guide.org/scenarios/web/
