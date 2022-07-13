Error Handling
==============

HTTP Error Codes
----------------

Following the RESTful architecture standard, most errors in BrAPI should
be reported back to the client using the appropriate HTTP status code.
The status codes that BrAPI officially supports are outlined below. Any
response which has an error status code (4XX and 5XX) should have a
plain text body with a reasonable error message which can be displayed
to a user if necessary.

+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| Code | Description           | Use Case                                                                                                   |
+======+=======================+============================================================================================================+
| 200  | OK                    | Use code 200 for every successful JSON response. The 'status' array in a response                          |
|      |                       | metadata may contain addition logged errors as described below.                                            |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 202  | Accepted              | Use code 202 when a request has been received and "Accepted" by the server, but                            |
|      |                       | more processing time is needed before a complete response is ready. See BrAPI documentation                |
|      |                       | on Search Services for more details on when to use this code.                                              |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 400  | Bad Request           | Use code 400 when there is something wrong with the request. This could be a problem with any of the query |
|      |                       | parameters or request body object.                                                                         |
|      |                       |                                                                                                            |
|      |                       | \- Example: A malformed JSON object which does not match the expected schema.                              |
|      |                       |                                                                                                            |
|      |                       | \- Example: A parameter is sent as a alphanumeric string but is expected to be an integer                  |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 401  | Unauthorized          | Use code 401 when the request does not pass authorization checks. This                                     |
|      |                       | could be caused by a missing Authorization token header, if the token is                                   |
|      |                       | expired, or can not be verified. 401 can be replaced by 403 if desired.                                    |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 403  | Forbidden             | Use code 403 when the user is not allowed to access the requested resource. This                           |
|      |                       | could be caused by a system level authorization error (as described by 401) or                             |
|      |                       | by a more granular user permission issue.                                                                  |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 404  | Not Found             | Most servers and libraries have automatic 404 errors built in for unknown paths tried against              |
|      |                       | the server. Use 404 explicitly when there is a path parameter which can not be found. Most                 |
|      |                       | path parameters in BrAPI are DbIds of specific objects, so if a requested DbId doesn't exist in            |
|      |                       | the database, return a 404.                                                                                |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+
| 500  | Internal Server Error | Status code 500 indicates that the server has malfunctioned in some way. Use 500 for                       |
|      |                       | all unexpected exceptions, code defects, or configuration issues. For security, it                         |
|      |                       | is a best practice to implement an explicit error handler which can hide the cause                         |
|      |                       | of the error from the client and return a generic error message.                                           |
+------+-----------------------+------------------------------------------------------------------------------------------------------------+


Metadata Status Array
---------------------

**When to use an ERROR in the 'status' array?**


As of BrAPI v1.3, the 'status' array in the response metadata is
reserved for sending additional logging messages from the server to the
client. These status messages may contain "ERROR" logs, but they should
not supersede HTTP status codes or be relied upon for critical error
handling. For most errors, it is a best practice to use the appropriate
HTTP status code. However, there are a few cases where it is acceptable
to return an error message to a user via the "status" array in the
return objects metadata. Generally, this is acceptable when the request
is valid, but the server has determined the response is not what the
user is intending. Another way to think about this is the difference
between errors intended for a developer vs errors intended for an end
user. HTTP status code errors should be primarily directed at developers
building a tool, but status error log messages should be directed at the
user of a system.

For example, making the request \`GET /trials?locationDbId=abc123`. If
there are no locations with the DbId of "abc123", then the server will
not be able to find any trials which have that locationDbId. This is a
valid request, and an empty "data" array is the correct response, but it
would be nice to notify the user that they will never find any trials
with this locationDbId.

Another example, making the request \`GET
/studies?studyType=Genotyping`. If the database does not contain any
information about study types, then it is important to notify the user
that the study type query parameter will be ignored.
