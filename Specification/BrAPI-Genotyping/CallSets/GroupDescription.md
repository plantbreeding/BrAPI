# Group CallSets

A `CallSet` represents a `Sample` that was used during some sequencing event. In most cases, the `CallSet` will have a 1-to-1 relationship with a given `Sample`. However, in some cases, a single `Sample` may be used in multiple different sequencing events or experiments. The `CallSet` gives an identifier to the relationship between a `Sample` and a genotype sequencing event. 

In a VCF file, `CallSets` are the columns are the data matrix. 
