---
title: "ImageNet"
slug: "imagenet"
lang: "base"

source_wiki_title: "ImageNet"
source_hash: "98dfde6a38a25b4a1cad09a0e54f4424"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:58:43.194953+00:00"

tags:
  []

keywords:
  - "train"
  - "tiny-imagenet-200"
  - "16 groups"
  - "Imagenet"
  - "Nibi cluster"
  - "ImageNet dataset"
  - "npz"
  - "validation"
  - "ILSVRC2012"
  - "opt-in service"
  - "winter21_whole"
  - "Digital Research Alliance of Canada"
  - "ImageNet"
  - "NFS3 mount"

questions:
  - "What steps must a user take to opt-in and legally access the ImageNet dataset on the Nibi cluster?"
  - "What are the different versions and variations of the ImageNet dataset currently available in the `/datashare` directory?"
  - "How can a user request additional versions of the dataset or data from other challenges that are not currently hosted?"
  - "What are the two main ImageNet dataset directories and their contents as listed in the structure?"
  - "What specific type of mount is used to host the ImageNet files?"
  - "Under what specific condition might a user encounter file access issues on this system?"
  - "What specific image resolutions and dataset splits are contained within the `part2_npz` directory?"
  - "Which file formats and specific archives are used to store the raw ImageNet data in the `ILSVRC2012` folder?"
  - "How does the directory structure separate the training, validation, and testing phases for the ILSVRC2012 dataset?"
  - "What are the two main ImageNet dataset directories and their contents as listed in the structure?"
  - "What specific type of mount is used to host the ImageNet files?"
  - "Under what specific condition might a user encounter file access issues on this system?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The Digital Research Alliance of Canada makes available on the [Nibi](../../clusters/nibi.md) cluster a copy of the ImageNet dataset, stored in the `/datashare` space. For the time being, this dataset is available only on Nibi, and you must opt-in to access this dataset by agreeing that you have registered for an ImageNet license:

!!! note "ImageNet License Agreement"
    By selecting this service you acknowledge that you have registered with the owner of the data (at http://image-net.org/download) and have agreed to ImageNet’s terms of use (https://image-net.org/download.php).

    En sélectionnant ce service, vous reconnaissez que vous êtes inscrit auprès du propriétaire des données (à l'adresse http://image-net.org/download) et que vous avez accepté les conditions d'utilisation d'ImageNet (https://image-net.org/download.php).

This dataset is provided as is and will only be updated based on image-net.org releases. If data from other challenges than the ones provided are required, please contact our [Technical support](../../support/technical_support.md) with the subject `ImageNet dataset`.

## Request access through the opt-in service
Please visit [this opt-in page](https://ccdb.computecanada.ca/services/opt_in) to request access by acknowledging that you have registered with the ImageNet providers and that you will comply with their terms and conditions.

## Available versions
The ImageNet directory in `/datashare` contains several versions of the ImageNet dataset:
*   Full dataset (ImageNet-21k): the Winter 2021 release of the full dataset can be found in `winter21_whole`. It contains 13,153,500 images divided into 19,167 classes. (Despite being less than 21k classes, this is indeed the latest version of the full ImageNet-21k dataset. The reduction in the number of classes was due to a [cleaning process in 2019](https://www.image-net.org/update-sep-17-2019.php) which redacted the majority of the images and classes in the `person` synset.)
*   [Large-scale Visual Recognition Challenge (LSVRC)](https://www.image-net.org/challenges/LSVRC/): the 2012 version can be found in `ILSVRC2012`. The dataset contains 1,281,167 images for training with a variable number of images for each of the 1,000 classes (synsets) ranging from 732 to 1300. The validation set contains 50,000 images with 50 images per synset and a testing dataset containing 100,000 images. **The ILSVRC datasets are generally the most commonly used versions of the ImageNet datasets.**
*   Tiny ImageNet: this is a downsampled and reduced dataset that contains 100,000 images of 200 classes downsized to 64×64 coloured images. It can be found in the directory `tiny-imagenet-200`.
*   [Downsampled](https://patrykchrabaszcz.github.io/Imagenet32/): In addition, we provide downsampled versions of ImageNet on `/datashare/ImageNet/DownSampled`. 8x8, 16x16, 32x32, and 64x64 versions are available. The number of training images, synsets, evaluation images, and testing images are unchanged from the original LSVRC datasets.

If you require a version not currently available, please make a request by sending an email to support@tech.alliancecan.ca.

## Location and contents
The files can be accessed at `/datashare/imagenet/`, and it contains:

```tree
├── DownSampled
│   ├── Imagenet16_train_npz
│   ├── Imagenet16_val_npz
│   ├── Imagenet32_train_npz
│   ├── Imagenet32_val_npz
│   ├── Imagenet64_train_part1_npz
│   ├── Imagenet64_train_part2_npz
│   ├── Imagenet64_val_npz
│   ├── Imagenet8_train_npz
│   └── Imagenet8_val_npz
├── ILSVRC2012
│   ├── ILSVRC2012_devkit_t12
│   ├── ILSVRC2012_devkit_t3
│   ├── ILSVRC2012_img_test_patch_v10102019.tar
│   ├── ILSVRC2012_img_test_v10102019.tar
│   ├── ILSVRC2012_img_train_t3.tar
│   ├── ILSVRC2012_img_train.tar
│   ├── ILSVRC2012_img_val.tar
│   ├── ILSVRC2012.md5
│   ├── test
│   ├── train
│   ├── train_T3
│   └── validation
├── tiny-imagenet-200
│   ├── test
│   ├── train
│   ├── val
│   ├── wnids.txt
│   └── words.txt
└── winter21_whole
    ├── n00004475
    ├── n00007846
    ├── n00017222
    ├── n00288384
    ├── n00324978
    ├── n00433458
    ├── n00433661
    .
    .
    .
    ├── n15092751
    ├── n15102359
    ├── n15102894
    └── tars
```

## NFS3 Mount Limitation

!!! warning "NFS3 Mount Limitation"
    The ImageNet data is hosted on an NFS3 mount. Users who belong to more than 16 groups in the Digital Research Alliance of Canada (the Alliance) may experience issues accessing these files.