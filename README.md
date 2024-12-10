# Spencer Parker - public repo
## Hugging Face Dataset Downloader

A Python script to dynamically download datasets from [Hugging Face](https://huggingface.co/) and save them as .csv files locally.

<div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
requirements

* python 3.7 or later
* Hugging Face `datasets` library: 
    * `pip install datasets`
* HF acct/token for access: https://huggingface.co/settings/tokens
</div>

### Features

* Dynamically specify the dataset name and split (e.g., `train`, `test`, etc.):
    * default split value is `train`
    * Use the `--split` argument for a custom split:  
    ```
    python hf.py <dataset_name> --split <split_name>
    ```  
    **e.g.**:  
    ```
    python hf.py HuggingFaceTB/smoltalk --split test
    ```
* Save the CSV file to a custom output directory
    * default location/filename: `C:\data\hf_csvs\output.csv` 
    * Use the `--output_file` argument for custom file output:  
    ```
    python hf.py <dataset_name> --output_file <path_to_csv>
    ```  
    **e.g.**:  
    ```
    python hf.py HuggingFaceTB/smoltalk --output_file C:\Users\username\some_folder\hf_smoltalk.csv
    ```




## NBA data retrieval (wip)
