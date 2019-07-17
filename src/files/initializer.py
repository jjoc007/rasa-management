import os.path

def initialize_folders():

    nlu_path = "C:\\dev\\rasa-chat\\nlu-files\\"
    nlu_intent_path = nlu_path+"intent"
    nlu_synonym_path = nlu_path + "synonym"
    nlu_lookup_path = nlu_path + "lookup"

    if not os.path.isdir(nlu_intent_path):
        os.makedirs(nlu_intent_path)

    if not os.path.isdir(nlu_synonym_path):
        os.makedirs(nlu_synonym_path)

    if not os.path.isdir(nlu_lookup_path):
        os.makedirs(nlu_lookup_path)
