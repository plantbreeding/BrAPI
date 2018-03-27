
### Search Services

There are several "Search" calls specified in BrAPI. These calls have a postfix of "-search" in the name, and are used to search for a set of entities without knowing the primary key (DbId). These calls can be used when presenting search options to a user, or when a system needs to access an entity using a candidate key which is not the DbId. All search calls should have a set of optional parameters, which are specific to that entity and its fields. 

Each optional parameter included in any search service call should act as a filter on the data being returned. This means the search parameters should always have an 'AND' type relationship with each other. 

If NO parameters are used in the request, the search service should return ALL entities of the given type, since no filters are being applied. (Normal pagination defaults still apply)

Example: Given this data
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
    last: "Jones"
}
```
The call `/person-search?first=Bob&last=Jones` will only return entity "1". The parameter `first` filters the data to just entities where the first name is "Bob" (entities "1" and "2"). The parameter `last` is an additional filter and further limits the data returned, resulting in just entity "1" satisfying both filters.

When parameters are defined as lists, each item in the list acts as an accepted value for that parameter. This can be thought of as an 'OR' relationship for items within the same list parameter, or it could be considered a 'value IN array' type operation by a database.

For example: Given the data above, the call `/person-search?first=Alice,Bob&last=Jones` will return entities "1" and "3". In this case, the parameter `first` filters the data to the first 3 entities, including all entities where the first name is 'Alice' OR 'Bob'. Again, the parameter `last` is an additional filter, further limiting the data returned, resulting in just  entities "1" and "3" satisfying both filters.

These rules for search parameters apply to both GET call query parameters and POST call body parameters.
