Server Implementation
=====================

BrAPI server implementations are generally more work than client implementations. A server has all the code to 
search, retrieve, and load new data into a database. Some groups decided to implement a large number of BrAPI 
endpoints so they are ready for any new use cases, other groups only implement the minimum number BrAPI 
endpoints required to solve a specific use case. The former groups use a lot of development time in the 
beginning on potentially unused code, but the latter groups have to spend extra time on each new use case. 
Both approaches are acceptable and both are considered BrAPI compliant.

Usually, a BrAPI server sits in front of a database with plant breeding related data. A lot of the work when 
building a BrAPI server is the mapping from the database data model to the BrAPI data model. This can be a 
complex and iterative process, often involving collaboration between developers and scientists.

Server Stub
-----------
SwaggerHub has a built in tool called swagger-code-gen. This tool allows you to generate a server stub for a 
variety of languages, and download it directly from the SwaggerHub documentation page. This server code will 
have all the BrAPI model objects and RESTful endpoints, but it will have blank spaces for building JSON 
responses. This blank space should be filled with code to perform the mapping between database models and BrAPI 
models. On any BrAPI SwaggerHub Page, click the "Export" menu in the top right corner, hover over "Server Stub", 
then select from the list of languages/frameworks.

Note on generated code. Swagger-code-gen is a useful tool for converting API specs into code, but it is not 
perfect. Generated libraries will not be perfect, so be sure to review and test them before using in production.

Testing
-------
Depending on the programming language/framework being used, there are many generic testing tools available for 
any level of testing. For developer testing, Postman is highly recommended as a generic client for working with 
RESTful web services. For BrAPI compliance testing, BRAVA is a tool developed by the BrAPI community to 
specifically test BrAPI endpoints. There is a public version of BRAVA, as well as dockerized versions for CI/CD 
environments.

Documentation
-------------
It is highly recommended that every BrAPI server have a documentation page showing the available BrAPI 
endpoints. Each server has special requirements, additional fields, and unsupported parameters. It is 
important to have a place to record these small deviations from the specification. If several groups have the 
same deviation from the spec, the community might decide to add that as part of the next version of BrAPI.

Authorization
-------------
The BrAPI Community made a decision that the BrAPI standard is not responsible for how different groups 
implement security. Your user authentication, authorization, and user management systems are your own 
responsibility. However, the community agreed that an OAuth-like pattern is a best practice for communicating 
data over an API between systems. Every BrAPI endpoint definition includes an “Authorization” header parameter. 
This header is used by things like OAuth/OpenID for passing an authorization token from the client to the 
server. It was added to support authorization best practices in BrAPI, but it is never required for BrAPI 
compliance.

A client application will get an authorization token (BrAPI does not care how), then make a BrAPI request with 
that token in the “Authorization” header. The server can validate the token (again, BrAPI does not care how 
this happens) and decide to return a response or not. That token might also be used to identify a specific 
user, so the server will only return the users specific data.

There are many resources/tools online for setting up an OAuth/OpenID pattern. Some basic material has been 
gathered in this BrAPI Wiki article. Reach out to the BrAPI Coordinator or the community Slack channel to 
discuss options and security patterns in more detail.

Example
-------
The brapi-intro-class github is a repository with example BrAPI implementations. All implementations follow 
the same use case where a user is browsing through Programs, Trials, and Studies. The code for getting Programs 
is included, but the critical code for Trials and Studies is missing. Choose a programming language you are
most familiar with, and then fill in the missing code to complete the use case. 
 

