from itertools import chain
import simplejson as json
from .spacy_ner import get_annotated_sents
from .utils import _to_json


class AnnotatedDocument(object):
    """Represent a document in a Brat Corpus."""

    def __init__(self, key, sentences):
        """
        Create a brat document.

        :param key: (string) The key of the document.
        Generally the name of the file without the extension
        (e.g. "022.ann" becomes 022)
        :param sentences: A list of dictionaries containing words.
        Represents the text of the review on a word-by-word basis.
        :return: None
        """
        self.sentences = sentences
        annotations = [chain.from_iterable([w.annotations for w in x.words])
                       for x in sentences]
        self.annotations = list(chain.from_iterable(annotations))

        self.key = key

        self.text = u"\n".join([u" ".join([x.form for x in s.words])
                               for s in sentences])


    def export_spacy_ner_json(self,pathtofile):
        """
        Export the current document to an Spacy JSON format file at the specified location.

        :param pathtofile: The path where the .XML file needs to be saved.
        :return: None
        """
            
        spacy_json=get_annotated_sents(self)
        with open(pathtofile, 'w') as f:
            json.dump(spacy_json,f,default=_to_json,tuple_as_array=False,indent=4)


