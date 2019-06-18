
# Group Markerprofiles

For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*

Basic concepts in the **Breeding API**:

- *markerprofile*: A set of marker scores for a specific extract from a specific germplasm.
- *extract* : a preparation from a germplasm for an analysis. 
- *sample*: an individual plant or tissue from a plant of a particular germplasm
- *germplasm*: a single genetic entity (cultivar, variety, accession, breeding line) used for analysis
- *marker*: a DNA sequence polymorphism, potentially localized to a single genomic location
- *allele*: one of the two possible states of a marker in each haploid chromosome complement of a specified germplasm, as determined in a specified experiment. A diploid organism has two alleles per marker.
- *missing*: a germplasm/marker/experiment combination for which no allele result is available, whether it was tested for or not
