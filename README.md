# sica-omics

<p align="center">
    <img src="https://github.com/ncaptier/sica-omics/blob/main/temporary_logo.png" width="400" height="400" />
</p>

This repository proposes a computational toolbox to complement the Python package [stabilized-ica](https://github.com/ncaptier/stabilized-ica) for the analysis of omics data.   

* sicaomics.singlecell proposes an adaptation of stabilized-ica for the special case of [AnnData](https://anndata.readthedocs.io/en/latest/) format. It is modeled after the [scanpy](https://scanpy.readthedocs.io/en/stable/) package that deals with single-cell gene expression data.
* sicaomics.annotate proposes tools to annotate the extracted stabilized ICA sources with functionnal enrichment analysis (using [Reactome](https://reactome.org/) or [ToppGene](https://toppgene.cchmc.org/) knowledge databases).


## Installation

Install sica-omics package from source with the following command:

 ```
 pip install git+https://github.com/ncaptier/sica-omics
 ```

## Examples

#### Application of stabilized-ica to single-cell data

```python
import scanpy
from sicaomics.singlecell import ica

adata = scanpy.read_h5ad('GSE90860_3.h5ad')
adata.X -= adata.X.mean(axis =0)

ica(adata , observations = 'genes' , n_components = 30 , n_runs = 100)
```

#### Annotation of stabilized-ica components

```python
#### Perform stabilized-ica decomposition ####
import pandas as pd
from sica.base import StabilizedICA

df = pd.read_csv("data.csv", index_col=0)
sICA = StabilizedICA(n_components=45, n_runs=30 ,plot=True, n_jobs = -1)
sICA.fit(df)
Metagenes = pd.DataFrame(
    sICA.S_, 
    columns = df.columns,
    index = ['metagene ' + str(i) for i in range(sICA.S_.shape[0])]
)

#### Annotate metagenes with Reactome ####
from sicaomics.annotate import reactome

Rannot = reactome.ReactomeAnalysis(
    data = Metagenes,
    threshold = 3,
    method = 'std',
    tail = 'heaviest',
    convert_ids = False
)
Rannot.get_analysis(metagene = 'metagene 0')
```
**Note:** For more detailed examples please refer to [this jupyter notebook](https://github.com/ncaptier/stabilized-ica/blob/master/examples/transcriptomic_ICA.ipynb)

## Acknowledgements

This package was created as a part of the PhD project of Nicolas Captier in the [Computational Systems Biology of Cancer group](https://sysbio.curie.fr/) of Institut Curie.

## References

[1] Chen,J. et al. (2009) ToppGene Suite for gene list enrichment analysis and candidate
gene prioritization. Nucleic Acids Res., 37 (Suppl. 2), W305--W311   
[2] Gillespie,M. et al. (2021) The reactome pathway knowledgebase 2022, Nucleic Acids Research, 2021; gkab1028, https://doi.org/10.1093/nar/gkab1028   
[3] Wolf,F. et al. (2018) SCANPY: large-scale single-cell gene expression data analysis. Genome Biol 19, 15. https://doi.org/10.1186/s13059-017-1382-0   