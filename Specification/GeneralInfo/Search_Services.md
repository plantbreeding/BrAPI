
### Search Services

---
** NOTE ** : There have been significant changes to the structure of the Search Service calls in BrAPI v1.3. If you are looking for the v1.2 Search Service documentation please look <a href="https://github.com/plantbreeding/API/blob/V1.2/Specification/GeneralInfo/Search_Services.md">HERE</a>.

---

** NOTE **: Throughout this article, the word "entity" is used as a general term to describe a number of BrAPI objects which have search services available. This includes "germplasm", "images", "markers", "observationtables", "observationunits", "programs", "samples", "studies", and "variables"

---

There are several "Search" calls specified in BrAPI. The calls all start with `/search/...`, and are used to search for entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a candidate key, which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its fields. 

### Changes from v1.2

Most Search service calls in BrAPI v1.2 had two calls with the following structures:

```
    GET /entity-search?param=value...
      Returns -> A list of "entities" filtered by the parameters
    
    POST /entity-search
      Body -> {"param": ["value1", "value2"...]}
      Returns -> A list of "entities" filtered by the parameters
```

In BrAPI v1.3 we have shifted to a more RESTful paradigm. 

The original v1.2 `GET` call has simply removed the `-search` postfix, so the client is getting a filtered list of entities based on query parameters. The new call should work the same as its predecessor.

The original v1.2 `POST` call has been split into two calls: a `POST` for submitting a new search request object, and a `GET` for retrieving the results of that search.

```
    GET /entity?param=value...
      Returns -> A list of "entities" filtered by the parameters
    
    POST /search/entity
      Body -> {"param": ["value1", "value2"...]}
      Returns -> A search results DbId to be used to retrieve the results
    
    GET /search/entity/{searchResultsDbId}
      Returns -> A list of "entities" filtered by the parameters in the related POST call
```

#### Rational

There have been many questions about why we chose to move to a more complex searching structure. The new `/search` calls do increase the complexity of implementation, but they also improve the flexibility of implementation. By separating the search request and the response data, the server has some control over when and how often a database query is run. By providing a persistent search results DbId, it becomes possible for a client to make a single search request, then repeatedly reference the same results URL as many times as needed. This new paradigm will also open the door to much more complex query requests in future iterations of BrAPI. 

Below are descriptions of two possible implementation paths. The first is the simplest and is meant to act the most like the original, the second is a more complex implementation but more fully allows for the advantages described above. 


### v1.3 Implementation Options

#### Option #1: Store the Request

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

#### Option #2: Store the Results

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

### General Implementation Notes

#### GET Entity

The entity filter services (previously the `GET /entity-search` services) have the form `GET /entity?param=value`. Each optional parameter these services should act as a filter on the data being returned. This means the filter parameters should always have an 'AND' type relationship with the others. If NO parameters are used in the request, the service should return ALL entities of the given type, since no filters are being applied (Normal pagination defaults still apply). If one parameter is used, the service should return the entities that match the parameter. If two parameters are used, the service should return the entities that match both parameters. 

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


#### POST Search, GET Results

As of BrAPI v1.3, searching for entities using the POST method has been split into two calls. The first call `POST /search/entity` submits a new search request to the server and returns an ID unique to that search instance. The second call `GET /search/entity/{searchResultsDbId}` returns the results of that search. Each POST call has a different Body object specification with search parameters specific to the given entity. The GET call has pagination parameters available so the client can limit the amount of data they get back for a given search. 

Most parameters in the POST Body object are arrays of strings. The array should be populated with all the search terms the client wishes to filter on, so each element in the array should have an "OR" relationship with the others. For example, using the data above, the search request object `{"first":["Alice", "Cathy", "Dave"]}` should return the records where `first` equals "Alice" OR "Cathy" OR "Dave". "Dave" has no record in our data, but records for "Alice" and "Cathy" will be returned. This can also be considered a 'WHERE value IN array' type operation by a database.

```
POST /search/names
    {
        "first":["Alice", "Cathy", "Dave"]
    }

GET /search/names/a1b2c3
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

As above, when multiple parameters are used together, they have an "AND" relationship. For example, search request object `{"first":["Bob"], "last": ["Jones"]}` will return the records where `first` equals "Bob" AND `last` equals "Jones". There is only one record in our data set which matches this criteria.

```
POST /search/names
    {
        "first":["Bob"], 
        "last": ["Jones"]
    }

GET /search/names/b2c3d4
    {
        id: "1",
        first: "Bob",
        last: "Jones"
    }
```

Combining these ideas, each array parameter should be resolved independently, then "ANDed" together. For example, search request object `{"first":["Alice", "Bob", "Cathy"], "last": ["Jones"]}` will return the records where (`first` equals "Alice" OR "Bob" OR "Cathy") AND (`last` equals "Jones"). This criteria matches "Alice Jones" and "Bob Jones" but it does not match "Cathy Evans". 

```
POST /search/names
    {
        "first":["Alice", "Bob", "Cathy"], 
        "last": ["Jones"]
    }

GET /search/names/c3d4e5
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

#### A Note on Pagination
It has come to my attention that some of the search services still have their "page" and "pageSize" keys as part of the search request object. This is an accident, generated from a line of reasoning which is no longer relevent. Any "page" and "pageSize" keys found in `POST` seach request object should be ignored. The "page" and "pageSize" query parameters in the `GET` call should be used instead. The `POST` call is meant to establish the parameters of the search, the `GET` call is responsible for how the client gets that data back. This will be cleaned up in v1.4.


