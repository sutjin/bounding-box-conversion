
# Bounding Box Conversion
Bounding Box Conversion is a tool to help convert image annotations into different versions in case we generate our annotation data in different format. Current conversion:
* PASCAL VOC to AWS GroundTruth
* PASCAL VOC to TF Records
* More to come...


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -Ur requirements/base.txt
```

## Usage

**IMPORTANT**

Make sure you update the `resources\labelmap.json` to match the labels that you are using. Each label should have a unique ID. (see file for example)


```
positional arguments:
  mode
    options: options: [pascal_to_groundtruth, pascal_to_tfrecords]

optional arguments:
--s3_path            S3 path needed for Groundtruth, should be where you images are stored
--pascal_label_path  Directory to pascal label path
--output             Output path

```

**Example**
```bash
python main.py pascal_to_groundtruth --s3_path s3://somepath/ --pascal_label_path local/path --output example.manifest
python main.py pascal_to_tfrecords --pascal_label_path local/path --output example.records
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.