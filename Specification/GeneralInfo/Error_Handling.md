
### Error Handling

HTTP error codes are used as required, e.g., 200 for ok, 404 for page not found, 401 for not authorized, 501 for not implemented, 201 for created in a PUT, 202 for request received but not yet processed, etc.

All capturable errors should be responded to with the appropriate HTTP error code and a well formulated JSON structure that includes a message describing the error.  The error code is intended as a debugging tool for the service provider.