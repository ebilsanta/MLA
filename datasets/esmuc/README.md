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



