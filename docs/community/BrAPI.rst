
What Is BrAPI?
==============

The Breeding API specifies a standard interface for plant phenotype/genotype databases to serve their data to crop breeding applications. 
It is a shared, open API, to be used by all data providers and data consumers who wish to participate. Initiated in June 2014, the BrAPI 
community has grown to over 200 software developers and agricultural scientists from 36 international institutions. A wide network of 
interconnected software has begun to emerge as more groups use BrAPI as the common language for communicating data. 

The BrAPI specification is free and open source, and the BrAPI community is very welcoming and knowledgable. All the specification documentation
can be found on `brapi.org <https://brapi.org/specification>`__ and the `BrAPI Getting Started Guide <https://brapi.org/get-started>`__ guide 
is a great place to start. To become part of this community, consider joining `the mailing list <https://brapi.org/contact>`__, connecting on 
`Slack <https://join.slack.com/t/plantbreedingapi/shared_invite/enQtNjA4NTA3OTI5NjUxLWE5ZmI0NDE0NGM1ODkxMjVmMDU1MGVjY2Q5M2QxNGNkYzMyODhkNDVmZjM0ZGI1YzEwYjEwNmY0MDM1YjllZDU>`__, 
or following the project on `Twitter <https://twitter.com/breedingapi>`__. 


Definitions
-----------


.. image:: images/BrAPI_Domains.png
   :width: 800
   :alt: BrAPI Domains

BrAPI
   The Breeding API (BrAPI) is a **Standardized RESTful Web Service API Specification** for communicating Plant Breeding Data. BrAPI allows
   for easy data sharing between databases and tools involved in plant breeding.

API
   An Application Programming Interface (API) is used to interact with and control an application programatically. Just as a User Interface
   (UI) allows a human user to interact with an application, an API allows a separate piece of code to interact with an application. An
   API can be used to send input data, receive output data, configure settings, and trigger actions within an application.
   
Web Service
   Web Services are computational services accessed over a computer network. Typically, when people talk about web services, they are
   referring to a standardized web service communication protocol. The two web service protocols which are currently the most popular are SOAP
   and REST.
   
REST
   Although the above paragraph indicates REpresentational State Transfer (REST) is a web service protocol, strictly speaking, it is
   an architecture or design framework. The REST architectural ideas are applied by using the HTTP protocol for information transport. REST
   uses the standard HTTP verbs (GET, POST, PUT, etc) to define different types of actions, and URLs to indicate where a request
   should be sent and what input data to use. When sending or receiving data, complex data structures are typically defined using JSON or
   XML.
   
Standardized
   BrAPI is an attempt to standardize the commands and data structures needed for typical plant breeding applications.
   
Specification
   At the core, BrAPI is a standardized Specification. BrAPI is not a tool for transporting data, it only documentation which describes how
   to transport data.


Project History
---------------

The BrAPI Project was initiated in June 2014, when a small group of plant breedning software teams met to discuss interoperability. This initial
group consisted of representatives from Breedbase, BMS, T3, and ICRISAT. By September, they had grown to include developers from JHI, DArT, 
B4R, and PhenoApps. The leaders and developers from these organizations met regularly and laid the ground work for what would become the BrAPI
specification. They organized the first community hackathons which have become a staple of the BrAPI community. 

Over the next year, the group continued to grow with organizations like INRA, GOBii, and The Crop Ontology joining the discussion. Eventually, 
they had enough web service endpoints defined that they released an initial V1 of the specification document. This initial V1 document had 36
endpoints defined focused on studies, germplasm, phenotypes, and genotype data. To this day, these categories remain as the central pilars of 
the BrAPI spec. In September of 2015, the GitHub repository was created and the initial spec document was copied in. This made it far easier
to work simultaniously, make changes when nessesary, and log issues which could be fixed later. 


More BrAPI Resources
--------------------

- :doc:`Best Practices <Best_Practices>`
- :doc:`Use Cases <Use_Cases>`
- :doc:`Hackathons <Hackathons>`
- :doc:`Old Documentation <Old_Documentation>`
- :doc:`GitHub <https://github.com/plantbreeding/API>`
- :doc:`Apiary <https://brapi.docs.apiary.io/#>`
- :doc:`SwaggerHub <https://app.swaggerhub.com/apis/PlantBreedingAPI/BrAPI/1.2>`
- :doc:`BrAPPs <https://brapi.org/brapps.php>`
- :doc:`BrAPI Test Server <https://test-server.brapi.org/>`
- :doc:`BrAVA Validation Server <http://webapps.ipk-gatersleben.de/brapivalidator/>`
