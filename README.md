# IS460: Machine Learning and Applications Project G1T4

## Datasets
This repository contains scripts we used for data processing. The raw datasets have to be downloaded from their original sources as they are too large to host here.

* [Choral Singing Dataset](https://zenodo.org/records/1286570), put inside the folder ```datasets/csd```
* [Esmuc Choir Dataset](https://zenodo.org/records/5848990), put inside the folder ```datasets/esmuc```

After the datasets are download, follow these steps in order:
1. Instructions to set up and run the scripts are found in the respective folders eg. ```datasets/[dataset]```.
2. run preprocess_csd_and_esmuc.py, check that now there exists the folder ```datasets/combined_processed_dataset```. This will be used specifically for Open-Unmix.
3. run batch_convert_mono_to_stereo_for_bsrnn.py, check that now there exists the folder ```datasets/combined_processed_dataset_converted_stereo```. This will be used specifically for BSRNN.
4. [for jukebox] bla bla

## Training the Models
Since the 3 models are very different from each other, we have put them individually inside their respective directories in ```models/model```. Inside each directory, please follow the respective README.md

## Results
1. [ add SDR table here ]
2. Some sample inferece outputs from our models can be seen in the drive: https://smu-my.sharepoint.com/:f:/g/personal/kevano_2020_business_smu_edu_sg/Ek2286izPx5Lkbew-vrgjUEBGDwSNMoahMWTMByRZ9-tzA?e=qj7A4L
