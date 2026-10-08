# GPCR Mutation Atlas

Interactive maps of documented variants in human G protein-coupled receptors, with functional effects, condition annotations and source links. Data snapshot: **8 October 2026**.

**[Open the interactive atlas](https://kilianmaire.github.io/gpcr-mutation-atlas/)**

## Explore

- **Aggregate snake plots:** structurally equivalent GPCRdb positions, compared within each of nine identified receptor classes.
- **Individual receptors:** snake plots and complete reference sequences for all 845 human entries, including explicitly labelled candidates and pseudogenes.
- **Amino-acid substitutions:** reference → alternative matrix, with source annotations available for each label.

Hover for one second or click a position to see substitutions, functional effects, associated conditions and references. The interface is in French. The HTML contains its data and individual viewer, so it also opens offline in a recent browser; keep the adjacent files for data downloads.

## What the colors measure

The atlas indexes **104,042 distinct gene–position–alternative labels**, including **58,890 labels at standard generic positions in identified classes** and **1,448 labels with classified functional effects**. A label found in multiple sources or assays is counted once. Six reference-equal-alternative source entries are flagged as non-substitutions; 37 source `X` labels are retained separately from `*`.

Density is the number of documented labels divided by the number of selected receptors where that generic position is assigned. Positions assigned in fewer than **50%** of selected receptors are hatched, excluded from the density color scale and ranking, and remain clickable. This is a display rule, not a statistical significance test. The color scale uses `log(1+n)` and is recalculated for the selected subset.

Colors describe indexed documentation, not allele frequencies, patient counts or biological enrichment. Red/blue/yellow denote LOF/GOF/no effect detected in the described assays; gray denotes unclassified functional direction. Shared sectors indicate known categories present, without quantitative proportions. Clinical pathogenicity is not inferred from functional colors. Association and causality remain distinct. Coverage differs substantially between receptors and sources.

## Public sources

- [HGNC](https://www.genenames.org/): inventory and gene symbols.
- [UniProt](https://www.uniprot.org/): reference sequences and variant annotations.
- [GPCRdb](https://gpcrdb.org/): generic positions, topology, mutagenesis observations and population variants from ExAC.
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/): variants and condition-specific classifications retained with review information.
- Scientific publications linked in the relevant variant cards, with targeted functional re-readings.

Mappings, descriptive aggregations and targeted annotation checks are derived from these sources. Some functional annotations were extracted automatically and should be read with their assay context. Upstream sources retain their attribution and terms. No private project documents are included.

## Files

| File | Content |
| --- | --- |
| `index.html` | Standalone interactive atlas |
| `variantes_placees.csv` | Placed labels, annotations and source links |
| `comptages_positions_equivalentes_par_classe.csv` | Counts, coverage denominators and exclusive effect categories |
| `comptages_regions_par_classe.csv` | All regional counts, aligned and unaligned positions |
| `matrice_types_substitutions.csv` | Reference → alternative counts |
| `sequences_reference_845.fasta` | Reference sequences |
| `coordonnees_source_non_rapprochees.csv` | 56,863 source-coordinate rows excluded from reference placement; these may overlap placed labels |
| `methodes_et_comptages.json` | Definitions and counts |
| `Carte_*.svg`, `Carte_*.png`, `Types_substitutions_GPCR.*` | Static previews |
| `src/` | Readable interface templates and compressed source data |

## Rebuild and verify

Python 3, standard library only:

```sh
python3 scripts/build.py
python3 scripts/verify.py
```

The build embeds the viewer and compressed dataset into `index.html`. Verification checks labels, coordinates, aggregation counts, coverage handling, embedded sources and local file links. Interaction checks were performed separately in an isolated DOM on the full dataset; static SVG renders were visually reviewed. These checks do not establish clinical validity or universal source completeness.

GitHub Pages serves `index.html` from the `main` branch root. No application backend or network request is required to load the atlas; external scientific links require an internet connection.
