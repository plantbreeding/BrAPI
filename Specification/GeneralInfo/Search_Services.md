
### Search Services

---

**NOTE**: Throughout this article, the word "entity" is used as a general term to describe a number of BrAPI objects which have search services available. 

---

#### GET Entity

The entity filter services have the form `GET /entity?param=value`. Each optional parameter these services should act as a filter on the data being returned. This means the filter parameters should always have an 'AND' type relationship with the others. If NO parameters are used in the request, the service should return ALL entities of the given type, since no filters are being applied (Normal pagination defaults still apply). If one parameter is used, the service should return the entities that match the parameter. If two parameters are used, the service should return the entities that match both parameters. 

Example: Given the entity "Names" and this data ("Names" is a fake entity for simple example purposes only) 

```
    id   | first   | last
    -----+---------+--------
    "01" | "Bob"   | "Jones"
    "02" | "Bob"   | "Smith"
    "03" | "Alice" | "Jones"
    "04" | "Cathy" | "Evans"
```

The request `GET /names`, with no parameters, will return ALL of the names available in the database.

```
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    },{
        id: "2",
        first: "Bob",
        last: "Smith"
    },{
        id: "3",
        first: "Alice",
        last: "Jones"
    },{
        id: "4",
        first: "Cathy",
        last: "Evans"
    }
```

The request `GET /names?first=Bob` will return all the records where the `first` field equals "Bob". In this case, there are two records.

```
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    },{
        id: "2",
        first: "Bob",
        last: "Smith"
    }
```

The request `GET /names?first=Bob&last=Smith` will return all the records where the `first` field equals "Bob" AND where the `last` field equals "Smith". Only one record matches those criteria.

```
    {
        id: "2",
        first: "Bob",
        last: "Smith"
    }
```

The request `GET /names?first=Bob&last=Evans` will return no records because there are no records where the `first` field equals "Bob" AND where the `last` field equals "Evans". 



#### POST Search Entity

There are several "Search" calls specified in BrAPI. The calls all start with `/search/...`, and are used to search for entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a candidate key, which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its fields. 

Every search in BrAPI is split into two endpoints. The `POST /search/...` endpoint is used to send a search request object. The `GET /search/...` endpoint is optional, and is used to retrieve the results of a search using a previously saved `searchResultDbId`. 

New in BrAPI V2.0, search endpoints allow servers to implement different types of searching for different entities and use cases, while maintaining a consistent response procedure for client applications. There are three acceptable server implementation options: Immediate Response Search, Saved Search, and Asynchronous Search. A client application can quickly determine which implementation is being used by looking at the HTTP status codes and applying the correct procedure for retrieving data. 

**Immediate Response Search**

The Immediate Response Search implementation is similar to how searching was done in BrAPI V1.2. 

1. The client makes a POST request with the search parameters
2. The server performs the search query synchronously 
3. The server responds with a 200 HTTP status, and the search results.

The `GET /search/...` endpoint is not required in this case. A `searchResultsDbId` is not created and can not be used as a reference ID later. Every page of data requires a new POST request with the same parameters.

**Saved Search**

The Saved Search implementation is similar to how searching was done in BrAPI V1.3.

1. The client makes a POST request with the search parameters
2. The server stores the search parameters and associates them with a `searchResultsDbId`
3. The server responds with a 202 HTTP status, and the `searchResultsDbId`
4. The client makes a GET request with the `searchResultsDbId` and pagination parameters (if needed)
5. The server performs the search query synchronously 
6. The server responds with a 200 HTTP status, and the search results
7. Repeat from step 4 with modified pagination parameters as needed

The client application can make multiple GET requests using the same `searchResultsDbId` without making the POST request again. 

**Asynchronous Search** 

The Asynchronous Search implementation is useful when the search query has the potential to take a long time.

1. The client makes a POST request with the search parameters
2. The server stores the search parameters and associates them with a `searchResultsDbId`
3. The server begins the search query in an asynchronous process 
4. The server responds with a 202 HTTP status, and the `searchResultsDbId`
5. The client makes a GET request with the `searchResultsDbId`
6. The server responds with a 102 HTTP status, indicating that the search query is not complete yet
7. Time passes. The client may poll the GET request regularly looking for a change in HTTP status
8. The server completes the asynchronous process, stores the search results, and marks the query as completed
8. The client makes a GET request with the `searchResultsDbId`
9. The server responds with a 200 HTTP status, and the search results
7. Repeat from step 8 with modified pagination parameters as needed

**Request and Response Rules**

Each POST call has a different request body schema with search parameters specific to the given entity. The GET call has pagination parameters available so the client can limit the amount of data they get back for a given search. Most parameters in the POST body object are arrays of strings. The array should be populated with all the search terms the client wishes to filter on. Each element in the array should have an "OR" relationship with the other elements in the same array. For example, using the data above, the search request object `{"first":["Alice", "Cathy", "Dave"]}` should return the records where `first` equals "Alice" OR "Cathy" OR "Dave". "Dave" has no record in our data, but records for "Alice" and "Cathy" will be returned. In SQL, this code might look like this: `... WHERE first IN ["Alice", "Cathy", "Dave"]`.

```
REQUEST JSON
    {
        "first":["Alice", "Cathy", "Dave"]
    }

RESPONSE JSON
    {
        id: "3",
        first: "Alice",
        last: "Jones"
    },{
        id: "4",
        first: "Cathy",
        last: "Evans"
    }
```

When multiple array parameters are used together in the same request, they have an "AND" relationship. For example, the request object `{"first":["Bob"], "last": ["Jones"]}` will return the records where `first` equals "Bob" AND `last` equals "Jones". There is only one record in our data set which matches this criteria.

```
REQUEST JSON
    {
        "first":["Bob"], 
        "last": ["Jones"]
    }

RESPONSE JSON
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    }
```

Combining these ideas, each array parameter should be resolved independently, then "ANDed" together. For example, search request object `{"first":["Alice", "Bob", "Cathy"], "last": ["Jones"]}` will return the records where (`first` equals "Alice" OR "Bob" OR "Cathy") AND (`last` equals "Jones"). This criteria matches "Alice Jones" and "Bob Jones" but it does not match "Cathy Evans". 

```
REQUEST JSON
    {
        "first":["Alice", "Bob", "Cathy"], 
        "last": ["Jones"]
    }

RESPONSE JSON
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    },{
        id: "3",
        first: "Alice",
        last: "Jones"
    }
```

Some searchable entities have non-array parameters in their request body objects. These are generally for things like numbers and dates where a client might be interested in a certain range instead of an exact value. Numeric fields with the suffix "Min" or "Max" describe the minimum and maximum values to search for (inclusive). Date string fields with the suffix "Start" or "End" should be treated as the beginning and ending (respectively) of a time range (inclusive).

**How to save a Search** 

###### Option #1: Store the Request

In this implementation, you will need to create a new table in your database, which can hold the search parameters submitted by the `POST` call. The exact structure of this table depends on your database technology and your organizations best practices for databases. In this table, you need to record a unique ID for each search, what type of search it is, and the parameters of the search request. Below is an example table that could do the job, though it is simplified for the purposes of this example. Always consider proper normalization and indexing techniques when building a new table. 

```
    search_request_id   | search_request_type    | parameter_name   | parameter_value 
    --------------------+------------------------+------------------|------------------------
    a1b2c3              | germplasm              | germplasmDbIds   | GERM01, GERM02, GERM03
    a1b2c3              | germplasm              | germplasmNames   | Germ 01, Germ 02
    b2c3d4              | studies                | programNames     | Program_1, Program_2
    b2c3d4              | studies                | germplasmDbIds   | GERM01
```

With each new search request stored, the unique search id (`search_request_id` from above) can be returned to the client as the `searchResultsDbId`. When the client makes a subsequent `GET` request, all the information about the search parameters can be collected from this table and the appropriate query can be generated. This means you are running a potentially slow query during the `GET` request, and it will be re-run on every subsequent `GET` request to the same ID. This is the most similar to the v1.2 version of the search service. 

```
Pros: Easy to implement, Most similar to the previous behavior, smallest data foot print
Cons: A potentially expensive search query must be run on the database for every GET request

Fits best with a "Search once, retrieve once" client expectation
```

###### Option #2: Store the Results

In this implementation, you will need two new tables, one to store some request data (as in Option #1), and one to store the results of each search. You will be consuming the search parameters immediately during the `POST` call, so it is not necessary to store all the parameter data, but it might be useful for audit purposes. The second table for storing results will be a join table between the search request and the primary entity being searched for. For example, if you are implementing the search for Germplasm, the table might look something like the table below. You might decide to create one table per search type, or group all your search results records into one table for all search types. 

```
    search_request_id   | germplasm_id    
    --------------------+-----------------
    a1b2c3              | GERM010590
    a1b2c3              | GERM010571
    a1b2c3              | GERM010542
    a1b2c3              | GERM010402
    b2c3d4              | GERM010542
    b2c3d4              | GERM010402
```

A word of caution in this implementation: recording the results of every search has the potential to make very large tables. The purpose of this design is to cache the results of a query and make subsequent search requests faster. If the search query you are using is already fast enough, this solution might not be right for you. Another option to think about is putting an expire time on each set of search results, and an automatic process for removing expired results. This can make the service a much more complicated to implement but it means you do not have to maintain all search results forever. Make sure your implementation is well documented so clients and other developers are not surprised if the search results they had cached yesterday are gone today.

```
Pros: Provides cached result for quick retrieval, the search results will be maintained statically
Cons: More complicated to implement and maintain

Fits best with a "Search once, retrieve many times" client expectation
```
