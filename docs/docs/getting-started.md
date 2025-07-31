Getting started
===============

## Install `uv`

To get started, first make sure that you have `uv` installed. In your terminal run:

```bash
(base) % pip install uv
```

You can check that you have it installed correctly by running

```bash
(base) % uv --version 
uv 0.8.3 (7e78f54e7 2025-07-24)
``` 

## Set Up Virtual Environment
Now that `uv` is installed we can use it to manage our dependencies. Check that you are in the `bennethypothesisvalidation/` directory. Then again in your terminal run 

```bash
(base)  % make create_environment
(base)  % source .venv/bin/activate
(.venv) (base)  % make requirements
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
The data can be downloaded [here](https://collegescorecard.ed.gov/data). You should download the file titled **All Data Files**. 

You should ensure that your `data/` directory is structructed like

```
├── data
   ├── interim                <- Intermediate data that has been transformed.
   ├── processed              <- The final, canonical data sets for modeling.
   └── raw                    <- The original, immutable data dump.
      └─ college_scorecard    <- The new data.

```
The directory `College_Scorecard_Raw_Data_05192025` should be inside the `data/raw/` folder, and renamed to `college_scorecard`. 

### Building the DataFrame
Build the `df` needed for analysis by running in your terminal

```bash 
(bhp) % python -m src.dataset 
```

Now there is a `data/interim/tuition.csv` file.

