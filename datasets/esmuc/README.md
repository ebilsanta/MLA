# Steps to generate dataset similar to MUSDB18-HQ from Esmuc Choir Dataset

* Download and unzip Esmuc Choir Dataset and add the folder to this directory  
for eg.
```
/datasets/esmuc/EsmucChoirDataset_v1.0.0
```

* Install dependencies
```
pip install pydub
```

* If you need to generate different names, you can get_modified_filename (line 77)
  * The files are grouped by voice type at this stage, so edit the values of the output_mapping for different filenames
  * Additionally, if you're running on Windows, you need to change to split by "\\"
```
def get_modified_filename(source_filename):
    output_mapping = {
        "Bass": "bass",
        "Tenor": "vocals",
        "Alto": "drums",
        "Soprano": "other"
    }
    parts = source_filename.split(".")[0].split('/') # need to change to '\\' for windows
    voice_type = parts[-2]
    modified_name = output_mapping[voice_type] 
    return modified_name
```

* Check folder locations specified at the bottom of `preprocess_esmuc_like_musdb.py`

```
if __name__ == "__main__":
    raw_esmuc_dataset = "./EsmucChoirDataset_v1.0.0"
    output_dir = "./processed_data"
    preprocess_esmuc_for_bsrnn(raw_esmuc_dataset, output_dir)
```

`raw_esmuc_dataset` should be the correct folder name of the Esmuc Choir Dataset you downloaded
`output_dir` can be any folder you want the preprocessed data to be output into. It will be created

* Open command line or terminal in this directory (`/datasets/esmuc/`)

* Run the preprocess script
```
python preprocess_esmuc_like_musdb.py
```

It should take 5 minutes or so...
* The result should be a folder similar to MUSDB18-HQ
- processed_esmuc
  - test
    - Mix1
      - bass.wav
      - drums.wav
      - mixture.wav
      - other.wav
      - vocals.wav
    - Mix2
  - train
    - Mix1
    - Mix2




