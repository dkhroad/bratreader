# bratreader
Python code for reading Brat Repositories and converting standoff annotations
to JSON format suitable for training Spacy NER  

# Version

0.1

# License

MIT

# Installation


```python 
pip install -e git://github.com/dkhroad/bratreader.git@0.2#egg=bratreader-0.p install -e git://github.com/dkhroad/bratreader.git@0.1#egg=bratreader-0.2
```

# Usage

### To use BratReader, 

```bash
brat2spacy --brat_datadir <brat_dir> --spacy_datadir <dest>

```
where `brat_dir`  the directory containing both your `.ann` and `.txt` files.


### To load converted SpaCy annotations 

```python
from bratreader import utils
utils.load_ner_json("<entities_annotations_file_in_spacy_format>.json")
```

