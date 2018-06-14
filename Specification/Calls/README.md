# Group Calls
The '/calls' call is used to find the available BrAPI calls on a particular server. 




## Calls [Get /brapi/v1/calls{?datatype}{?pageSize}{?page}]

<strong>Implementation Notes</strong>
Having a consistent structure for the path string of each call is very important for teams to be able to connect and find errors. Read more on <a href="https://github.com/plantbreeding/API/issues/144">Github</a>.
Here are the rules for the path of each call that should be returned
<ul>       
  <li>Every word in the call path should match the documentation exactly, both in spelling and capitalization. Note that path strings are all lower case, but path parameters are camel case.</li>        
  <li>Each path should start relative to '/' and therefore should not include '/'</li>
  <li>No leading or trailing slashes ('/') </li>
  <li>Path parameters are wrapped in curly braces ('{}'). The name of the path parameter should be spelled exactly as it is specified in the documentation.</li>        
</ul>
<table>
  <tr>
    <th>Examples</th>
  </tr>
  <tr>
    <td><strong>GOOD</strong></td>
    <td>"call": "germplasm/{germplasmDbId}/markerprofiles"</td>
  </tr> 
  <tr>
    <td>BAD</td>
    <td>"call": "germplasm/{<strong>id</strong>}/markerprofiles"</td>
  </tr> 
  <tr>
    <td>BAD</td>
    <td>"call": "germplasm/{germplasmDbId}/marker<strong>P</strong>rofiles"</td>
  </tr>
  <tr>
    <td>BAD</td>
    <td>"call": "germplasm/{germplasm<strong>dbid</strong>}/markerprofiles"</td>
  </tr> 
  <tr>
    <td>BAD</td>
    <td>"call": "<strong>brapi/v1</strong>/germplasm/{germplasmDbId}/markerprofiles"</td>
  </tr>
  <tr>
    <td>BAD</td>
    <td>"call": "<strong>/g</strong>ermplasm/{germplasmDbId}/markerprofile<strong>s/</strong>"</td>
  </tr> 
  <tr>
    <td>BAD</td>
    <td>"call": "germplasm/<strong>&lt</strong>germplasmDbId<strong>&gt</strong>/markerprofiles"</td>
  </tr> 
</table>

<a href="https://test-server.brapi.org/brapi/v1/calls"> test-server.brapi.org/brapi/v1/calls</a> 

+ Parameters
    + datatype (Optional, string) ... The data format supported by the call. Example: `json`
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "versions": [
                    "1.0",
                    "1.1"
                ],
                "call": "token",
                "methods": [
                    "POST",
                    "DELETE"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.0",
                    "1.1",
                    "1.2"
                ],
                "call": "calls",
                "methods": [
                    "GET"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.0"
                ],
                "call": "allelematrix",
                "methods": [
                    "GET",
                    "POST"
                ],
                "datatypes": [
                    "json",
                    "tsv"
                ]
            },
            {
                "versions": [
                    "1.0",
                    "1.1",
                    "1.2"
                ],
                "call": "observationLevels",
                "methods": [
                    "GET"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.0",
                    "1.1",
                    "1.2"
                ],
                "call": "germplasm-search",
                "methods": [
                    "GET",
                    "POST"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.0",
                    "1.1",
                    "1.2"
                ],
                "call": "germplasm/{germplasmDbId}",
                "methods": [
                    "GET"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.1",
                    "1.2"
                ],
                "call": "germplasm/{germplasmDbId}/pedigree",
                "methods": [
                    "GET"
                ],
                "datatypes": [
                    "json"
                ]
            },
            {
                "versions": [
                    "1.1",
                    "1.2"
                ],
                "call": "germplasm/{germplasmDbId}/markerprofiles",
                "methods": [
                    "GET"
                ],
                "datatypes": [
                    "json"
                ]
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "totalCount": 8,
            "totalPages": 1,
            "currentPage": 0
        },
        "datafiles": []
    }
}
```