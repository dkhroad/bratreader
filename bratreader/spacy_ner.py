#spacy NER translation
BRAT_TO_SPACY_KEYS = {
    'Organization':'ORG',
    'Person':'PERSON',
    'Location':'GPE',
    'Tech':'TECHNOLOGY',
    'Job':'JOB',
    'Abbr':'ABBR',
    'Misc':'MISC'
}

import pdb
def get_annotated_sents(doc, keys=BRAT_TO_SPACY_KEYS):
    ann_sents = []
    # pdb.set_trace()
    for sent in doc.sentences:
        anns = []
        ann_sent=u" ".join([x.form for x in sent.words])
        for word in sent.words:
            if word.annotations:
                for ann in word.annotations:
                    for label, valency in ann.labels.items():
                        anns.append((ann.realspan[0]-sent.start, ann.realspan[1]-sent.start, keys.get(label,label)))
        if anns:
            ann_sents.append((ann_sent,{'entities': anns}))
    return ann_sents


