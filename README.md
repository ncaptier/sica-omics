# sica-omics

This repository proposes a computational toolbox to complement the Python package [stabilized-ica](https://github.com/ncaptier/stabilized-ica) for the analysis of omics data.   

* sicaomics.singlecell proposes an adaptation of stabilized-ica for the special case of [AnnData](https://anndata.readthedocs.io/en/latest/) format. It is modeled after the [scanpy](https://scanpy.readthedocs.io/en/stable/) package that deals with single-cell gene expression data.
* sicaomics.annotate proposes tools to annotate the extracted stabilized ICA sources with functionnal enrichment analysis (using [Reactome](https://reactome.org/) or [ToppGene](https://toppgene.cchmc.org/) knowledge databases).

