Planning a Use Case
===================

Know Your Use Case
------------------

*"We want all the databases and tools to talk to each other automatically."*

This phrase comes up a lot in different forms when people first start talking about how to integrate 
different tools and systems. This is a nice overall goal or theme, but it is too vague to develop code. 
A good use case should be able to tell you specifically what you want to do, and why you want to do it. 
For additional help when creating use cases, look at a more formal syntax like Gherkin user stories.

BrAPI use cases can also be described, with more technical detail, using a series of RESTful web 
service calls. BrAPI endpoints are designed to be modular and flexible. This means several web service 
calls can be combined to accomplish a complex goal. For example, to show all the locations used in a 
breeding program, first get all the active studies in the program, then get all the locations 
associated with that list of studies.

Client and Server
-----------------
BrAPI is a standard for automatically communicating data between systems, so your use case should 
involve at least two software applications. These applications will always fill two rolls: a client 
and a server. The client will make requests and the server will accept the requests and process them. 
It is important to have a clear understanding of which application will be a client versus server. 
If the use case involves more than two applications, there may be multiple clients or servers. In some 
cases, an application might change between roles. Use cases can quickly become complicated, which 
is why Sequence Diagrams are a helpful tool.

Sequence Diagram
----------------
A Sequence Diagram is a diagram which shows the order of events over time across multiple software 
applications. The diagram below shows an example with three applications making requests to each 
other. Time increases as we move down the diagram, so we can see that App 1 first makes a request to 
App 2, then App 1 makes a request to App 3, then a chain of requests is passed from 1 to 2 to 3. In 
this case, App 1 is always a client and App 3 is always a server. App 2 is a server until the end 
when it becomes a client to pass a request to App 3. This kind of diagram can help clarify what 
applications are involved, the role and responsibilities of each, and the order in which the 
operations should take place. 

