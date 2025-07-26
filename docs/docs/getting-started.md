Getting started
===============

## Install `uv`

To get started, first make sure that you have `uv` installed. In your terminal run:

```bash
(base) spencervenancio@Spencers-Air ~ % pip install uv
```

You can check that you have it installed correctly by running

```bash
(base) spencervenancio@Spencers-Air ~ % uv --version 
uv 0.8.3 (7e78f54e7 2025-07-24)
``` 

## Set Up Virtual Environment
Now that `uv` is installed we can use it to manage our dependencies. Check that you are in the `bennethypothesisvalidation/` directory. Then again in your terminal run 

```bash
(base) spencervenancio@Spencers-Air ~ % uv venv
(base) spencervenancio@Spencers-Air ~ % source .venv/bin/activate 
(base) spencervenancio@Spencers-Air bennethypothesisvalidation % uv pip install . 
```

You should see something like 

```bash
Resolved 29 packages in 1.19s
      Built src @ file:///Users/spencervenancio/Downloads/Personal%20Projects/bennethypothesisvalidation
Prepared 29 packages in 1.51s
Installed 29 packages in 24ms
 + click==8.2.1
 + ghp-import==2.1.0
 + jinja2==3.1.6
 + loguru==0.7.3
...
```

## Download the data
The data can be downloaded [here](https://collegescorecard.ed.gov/data). You should download the file titled **Most Recent Institution-Level Data**. 

You should ensure that your `data/` directory is structructed like

```
├── data
   ├── external       <- Data from third party sources.
   ├── interim        <- Intermediate data that has been transformed.
   ├── processed      <- The final, canonical data sets for modeling.
   └── raw            <- The original, immutable data dump.

```

The `Most-Recent-Cohorts-Institution_05192025.csv` should go in to the `data/raw/` directory