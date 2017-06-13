## Allele Matrices [/brapi/v1/allelematrices?studyDbId=307
Status: PROPOSED.

Implemented by: GOBII

Used by: Flapjack

This resource is used for reading and writing genomic matrices:
+ GET provides a list of available matrices, optionally filtered by study;
+ POST will provide a means for adding new matrices (content TBD).

### Matrices through GET [GET]


+ Parameters: studyDbId restricts the list of matrices to a specific study. 


+ Response 200 (application/json)


```
   {
      "data":[
                {
	             "name":"testDs1",
                     "matrixDbId":27,
		     "description":"a test dataset",
                     "lastUpdated":"2017-06-12",
  	             "studyDbId":13
                },
                {
                     "name":"testDs2",
                     "matrixDbId":28,
                     "description":"a second test dataset",
    	             "lastUpdated":"2017-06-12",
		     "studyDbId":13
                }
            ]
   }
```
															   

