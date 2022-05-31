# sica-omics

<p align="center">
    <img src="https://github.com/ncaptier/sica-omics/temporary_logo.png" width="400" height="400" />
</p>

This repository proposes a computational toolbox to complement the Python package [stabilized-ica](https://github.com/ncaptier/stabilized-ica) for the analysis of omics data.   

* sicaomics.singlecell proposes an adaptation of stabilized-ica for the special case of [AnnData](https://anndata.readthedocs.io/en/latest/) format. It is modeled after the [scanpy](https://scanpy.readthedocs.io/en/stable/) package that deals with single-cell gene expression data.
* sicaomics.annotate proposes tools to annotate the extracted stabilized ICA sources with functionnal enrichment analysis (using [Reactome](https://reactome.org/) or [ToppGene](https://toppgene.cchmc.org/) knowledge databases).


### Install from source
```
pip install git+https://github.com/ncaptier/sica-omics
```


## Acknowledgements

This package was created as a part of the PhD project of Nicolas Captier in the [Computational Systems Biology of Cancer group](https://sysbio.curie.fr/) of Institut Curie.

## References

[1] Chen,J. et al. (2009) ToppGene Suite for gene list enrichment analysis and candidate
gene prioritization. Nucleic Acids Res., 37 (Suppl. 2), W305--W311   
[2] Gillespie,M. et al. (2021) The reactome pathway knowledgebase 2022, Nucleic Acids Research, 2021; gkab1028, https://doi.org/10.1093/nar/gkab1028   
[3] Wolf,F. et al. (2018) SCANPY: large-scale single-cell gene expression data analysis. Genome Biol 19, 15. https://doi.org/10.1186/s13059-017-1382-0   