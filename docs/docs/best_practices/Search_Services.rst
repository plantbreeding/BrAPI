Search Services
===============


**NOTE**: Throughout this article, the word "entity" is used as a general term to describe a number of BrAPI objects which have search
services available.


GET Entity
----------

The entity filter services have the form ``GET /entity?param=value``. Each optional parameter these services should act as a filter on the
data being returned. This means the filter parameters should always have an 'AND' type relationship with the others. If NO parameters are used in
the request, the service should return ALL entities of the given type, since no filters are being applied (Normal pagination defaults still
apply). If one parameter is used, the service should return the entities that match the parameter. If two parameters are used, the service should
return the entities that match both parameters.

Example: Given the entity "Names" and this data ("Names" is a fake entity for simple example purposes only)

+------+---------+---------+
| id   | first   | last    |
+======+=========+=========+
| "01" | "Bob"   | "Jones" |
+------+---------+---------+
| "02" | "Bob"   | "Smith" |
+------+---------+---------+
| "03" | "Alice" | "Jones" |
+------+---------+---------+
| "04" | "Cathy" | "Evans" |
+------+---------+---------+

The request ``GET /names``, with no parameters, will return ALL of the names available in the database.

   
.. code-block:: json

   [
      {
         "id": "1",
         "first": "Bob",
         "last": "Jones"
      },
      {
         "id": "2",
         "first": "Bob",
         "last": "Smith"
      },
      {
         "id": "3",
         "first": "Alice",
         "last": "Jones"
      },
      {
         "id": "4",
         "first": "Cathy",
         "last": "Evans"
      }
   ]


The request ``GET /names?first=Bob`` will return all the records where the ``first`` field equals "Bob". In this case, there are two records.

.. code-block:: json

   [
      {
         "id": "1",
         "first": "Bob",
         "last": "Jones"
      },
      {
         "id": "2",
         "first": "Bob",
         "last": "Smith"
      }
   ]


The request ``GET /names?first=Bob&last=Smith`` will return all the records where the ``first`` field equals "Bob" AND where the ``last``
field equals "Smith". Only one record matches those criteria.


.. code-block:: json

   [
      {
         "id": "2",
         "first": "Bob",
         "last": "Smith"
      }
   ]


The request ``GET /names?first=Bob&last=Evans`` will return no records because there are no records where the ``first`` field equals "Bob" AND
where the ``last`` field equals "Evans".


POST Search Entity
------------------

V2_search_scenarios.png

There are several "Search" calls specified in BrAPI. The calls all start with ``/search/...``, and are used to search for entities without knowing
the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a
candidate key, which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its
fields.

Every search in BrAPI is split into two endpoints. The ``POST /search/...`` endpoint is used to send a search request object. The
``GET /search/...`` endpoint is optional, and is used to retrieve the results of a search using a previously saved ``searchResultDbId``.

New in BrAPI V2.0, search endpoints allow servers to implement different types of searching for different entities and use cases, while
maintaining a consistent response procedure for client applications. There are three acceptable server implementation options: Immediate
Response Search, Saved Search, and Asynchronous Search. A client application can quickly determine which implementation is being used by
looking at the HTTP status codes and applying the correct procedure for retrieving data.


Immediate Response Search
^^^^^^^^^^^^^^^^^^^^^^^^^

The Immediate Response Search implementation is similar to how searching was done in BrAPI V1.2.

#. The client makes a POST request with the search parameters
#. The server performs the search query synchronously
#. The server responds with a 200 HTTP status, and the search results.

The ``GET /search/...`` endpoint is not required in this case. A ``searchResultsDbId`` is not created and can not be used as a reference
ID later. Every page of data requires a new POST request with the same parameters.


Saved Search
^^^^^^^^^^^^

The Saved Search implementation is similar to how searching was done in BrAPI V1.3.

#. The client makes a POST request with the search parameters
#. The server stores the search parameters and associates them with a ``searchResultsDbId``
#. The server responds with a 202 HTTP status, and the ``searchResultsDbId``
#. The client makes a GET request with the ``searchResultsDbId`` and pagination parameters (if needed)
#. The server performs the search query synchronously
#. The server responds with a 200 HTTP status, and the search results
#. Repeat from step 4 with modified pagination parameters as needed

The client application can make multiple GET requests using the same ``searchResultsDbId`` without making the POST request again.

Asynchronous Search
^^^^^^^^^^^^^^^^^^^

The Asynchronous Search implementation is useful when the search query has the potential to take a long time.

#. The client makes a POST request with the search parameters
#. The server stores the search parameters and associates them with a ``searchResultsDbId``
#. The server begins the search query in an asynchronous process
#. The server responds with a 202 HTTP status, and the ``searchResultsDbId``
#. The client makes a GET request with the ``searchResultsDbId``
#. The server responds with a 202 HTTP status, indicating that the search query is not complete yet. **NOTE** If the server has any progress 
   information, either an estimated time remaining or a number of records processed so far, it is recommended to report this information in a "status" message.
#. Time passes. The client may poll the GET request regularly looking for a change in HTTP status
#. The server completes the asynchronous process, stores the search results, and marks the query as completed
#. The client makes a GET request with the ``searchResultsDbId``
#. The server responds with a 200 HTTP status, and the search results
#. Repeat from step 8 with modified pagination parameters as needed


Generic Client Pseudo Code
^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating a generic BrAPI client application which uses a search function, it is important to be prepared for the different types of
responses from different servers. Search endpoints can respond with a ``200 OK`` status202 Accepted`` status, or a ``4XX Error`` status.
The pseudo-code below is an example of how a client application might handle these different possible response codes.

::

  request = buildSearchRequest()
  response = POSTSearchRequest(request)
  
  if (response.httpStatus == '200'):
    results = response.body
  
  else if (response.httpStatus == '202'):
    response = GETSearchResults(response.body.searchResultsDbId)
  
    while(response.httpStatus == '202'):
      sleep(5)
      response = GETSearchResults(response.body.searchResultsDbId)
  
      if(response.httpStatus == '200'):
        results = response.body
      else:
        error()
  else:
    error()


Request and Response Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each POST call has a different request body schema with search parameters specific to the given entity. The GET call has pagination
parameters available so the client can limit the amount of data they get back for a given search. Most parameters in the POST body object are
arrays of strings. The array should be populated with all the search terms the client wishes to filter on. Each element in the array should
have an "OR" relationship with the other elements in the same array. For example, using the data above, the search request object
``{"first":["Alice", "Cathy", "Dave"]}`` should return the records where ``first`` equals "Alice" OR "Cathy" OR "Dave". "Dave" has no record in
our data, but records for "Alice" and "Cathy" will be returned. In SQL, this code might look like this: ``... WHERE first IN ["Alice", "Cathy", "Dave"]``.

REQUEST JSON

.. code-block:: json

       {"first":["Alice", "Cathy", "Dave"]}
   

RESPONSE JSON
   
.. code-block:: json

   [
      {
         "id": "3",
         "first": "Alice",
         "last": "Jones"
      },
      {
         "id": "4",
         "first": "Cathy",
         "last": "Evans"
      }
   ]
   

When multiple array parameters are used together in the same request, they have an "AND" relationship. For example, the request object
``{"first":["Bob"], "last": ["Jones"]}`` will return the records where ``first`` equals "Bob" AND ``last`` equals "Jones". There is only one
record in our data set which matches this criteria.

REQUEST JSON
   
.. code-block:: json

   {
      "first":["Bob"],
      "last": ["Jones"]
   }

RESPONSE JSON
   
.. code-block:: json

   [
      {
         "id": "1",
         "first": "Bob",
         "last": "Jones"
      }
   ]
   

Combining these ideas, each array parameter should be resolved independently, then "ANDed" together. For example, search request object
``{"first":["Alice", "Bob", "Cathy"], "last": ["Jones"]}`` will return the records where (``first`` equals "Alice" OR "Bob" OR "Cathy") AND
(``last`` equals "Jones"). This criteria matches "Alice Jones" and "Bob Jones" but it does not match "Cathy Evans".

REQUEST JSON
   
.. code-block:: json

   {
      "first":["Alice", "Bob", "Cathy"],
      "last": ["Jones"]
   }
   

RESPONSE JSON
   
.. code-block:: json

   [
      {
         "id": "1",
         "first": "Bob",
         "last": "Jones"
      },
      {
         "id": "3",
         "first": "Alice",
         "last": "Jones"
      }
   ]
   

Some searchable entities have non-array parameters in their request body objects. These are generally for things like numbers and dates where a
client might be interested in a certain range instead of an exact value. Numeric fields with the suffix "Min" or "Max" describe the minimum and
maximum values to search for (inclusive). Date string fields with the suffix "Start" or "End" should be treated as the beginning and ending
(respectively) of a time range (inclusive).


How to save a Search
^^^^^^^^^^^^^^^^^^^^

Option #1: Store the Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this implementation, you will need to create a new table in your database, which can hold the search parameters submitted by the ``POST``
call. The exact structure of this table depends on your database technology and your organizations best practices for databases. In this
table, you need to record a unique ID for each search, what type of search it is, and the parameters of the search request. Below is an
example table that could do the job, though it is simplified for the purposes of this example. Always consider proper normalization and
indexing techniques when building a new table.

::

   search_request_id   | search_request_type    | parameter_name   | parameter_value 
   --------------------+------------------------+------------------|------------------------
   a1b2c3              | germplasm              | germplasmDbIds   | GERM01, GERM02, GERM03
   a1b2c3              | germplasm              | germplasmNames   | Germ 01, Germ 02
   b2c3d4              | studies                | programNames     | Program_1, Program_2
   b2c3d4              | studies                | germplasmDbIds   | GERM01

With each new search request stored, the unique search id (``search_request_id`` from above) can be returned to the client as the
``searchResultsDbId`. When the client makes a subsequent ``GET`` request, all the information about the search parameters can be
collected from this table and the appropriate query can be generated. This means you are running a potentially slow query during the ``GET``
request, and it will be re-run on every subsequent ``GET`` request to the same ID. This is the most similar to the v1.2 version of the search
service.

- Pros: Easy to implement, Most similar to the previous behavior, smallest data foot print
- Cons: A potentially expensive search query must be run on the database for every GET request
- Fits best with a "Search once, retrieve once" client expectation


Option #2: Store the Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this implementation, you will need two new tables, one to store some request data (as in Option #1), and one to store the results of each
search. You will be consuming the search parameters immediately during the ``POST`` call, so it is not necessary to store all the parameter
data, but it might be useful for audit purposes. The second table for storing results will be a join table between the search request and the
primary entity being searched for. For example, if you are implementing the search for Germplasm, the table might look something like the table
below. You might decide to create one table per search type, or group all your search results records into one table for all search types.

::

   search_request_id   | germplasm_id    
   --------------------+-----------------
   a1b2c3              | GERM010590
   a1b2c3              | GERM010571
   a1b2c3              | GERM010542
   a1b2c3              | GERM010402
   b2c3d4              | GERM010542
   b2c3d4              | GERM010402

A word of caution in this implementation: recording the results of every search has the potential to make very large tables. The purpose of this
design is to cache the results of a query and make subsequent search requests faster. If the search query you are using is already fast
enough, this solution might not be right for you. Another option to think about is putting an expire time on each set of search results, and
an automatic process for removing expired results. This can make the service a much more complicated to implement but it means you do not
have to maintain all search results forever. Make sure your implementation is well documented so clients and other developers are
not surprised if the search results they had cached yesterday are gone today.

- Pros: Provides cached result for quick retrieval, the search results will be maintained statically
- Cons: More complicated to implement and maintain 
- Fits best with a "Search once, retrieve many times" client expectation

V1 Search Services
------------------

The following are notes from BrAPI V1 about how to implement search services. Searching in BrAPI has changed drastically between V1 and V2.

There are several "Search" calls specified in BrAPI. These calls have a post-fix of "-search" in the name, and are used to search for a set of
entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to
access an entity using a candidate key which is not the DbId. All search calls should have a set of optional parameters, which are specific to
that entity and its fields.

Each optional parameter included in any search service call should act as a filter on the data being returned. This means the search parameters
should always have an 'AND' type relationship with each other.

For example: Given this data

.. code-block:: json

   [
      {
         "id": "1",
         "first": "Bob",
         "last": "Jones"
      },
      {
         "id": "2",
         "first": "Bob",
         "last": "Smith"
      },
      {
         "id": "3",
         "first": "Alice",
         "last": "Jones"
      },
      {
         "id": "4",
         "first": "Cathy",
         "last": "Evans"
      }
   ]


The call ``/person-search?first=Bob&last=Jones`` will only return entity "1". The parameter ``first`` filters the data to just entities where
the first name is ``"Bob (entities "1" and "2"). The parameter ``last`` is an additional filter and further limits the data returned,
resulting in just entity "1" satisfying both filters.

When parameters are defined as lists, each item in the list acts as an accepted value for that parameter. This can be thought of as an 'OR'
relationship for items within the same list parameter, or it could be considered a 'value IN array' type operation by a database.

For example: Given the data above, the call ``/person-search?first=Alice,Bob&last=Jones`` will return entities
"1" and "3". In this case, the parameter ``first`` filters the data to the first 3 entities, including all entities where the first
name is 'Alice' OR 'Bob'. Again, the parameter ``last`` is an additional filter, further limiting the data returned, resulting in just entities
"1" and "3" satisfying both filters.

These rules for search parameters apply to both GET call query parameters and POST call body parameters.

