# Steps to generate dataset similar to MUSDB18-HQ from Choral Singing Dataset

* Download and unzip Esmuc Choir Dataset and add the folder to this directory  
for eg.
```
/datasets/esmuc/ChoralSingingDataset
```

* Install dependencies
```
pip install pydub
pip install soundfile
```

* If you need to generate different names, you can change get_modified_filename (line 62)
  * The files are grouped by voice type at this stage, so edit the **values** of the output_mapping for different filenames
  * Additionally, you will have to change to split by "\\" if you're on Windows
```
def get_modified_filename(source_filename):
    output_mapping = {
        "bass": "bass",
        "tenor": "vocals",
        "alto": "drums",
        "soprano": "other"
    }
    parts = source_filename.split('/') # need to change to '\\' for windows
    voice_type = parts[-2]
    modified_name = output_mapping[voice_type] 
    return modified_name + ".wav"
```

* Check folder locations specified at the bottom of `preprocess_csd_like_musdb.py`

```
if __name__ == "__main__":
    # path to raw csd dataset
    root_dir = "./ChoralSingingDataset"
    output_dir = "./processed_csd"
    preprocess_csd_like_musdb(root_dir, output_dir)
```

`root_dir` should be the correct folder name of the ChoralSingingDataset you downloaded
`output_dir` can be any folder you want the preprocessed data to be output into. It will be created

* Open command line or terminal in this directory (`/datasets/csd/`)

* Run the preprocess script
```
python preprocess_csd_like_musdb.py
```

It should take 5 minutes or so...
* The result should be a folder similar to MUSDB18-HQ
- processed_csd
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




