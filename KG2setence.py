import os

import pandas as pd

entity_double_dir = os.listdir(os.path.join('entity_double'))
question_answer = pd.read_csv("key_list.csv").values.tolist()
word_models = []
word_set = []
for i in entity_double_dir:
    print(i)
    a = pd.read_csv(os.path.join('entity_double', i)).values.tolist()
    for k in a:
        entity = k[1].strip("<")
        entity = entity.strip(">")
        relation = k[0].strip("<")
        relation = relation.strip(">")
        end_entity = k[2].strip("<")
        end_entity = end_entity.strip(">")
        for l in question_answer:
            l = l[0]
            if isinstance(l, str) and 10<len(l)<20 and entity in l and end_entity in l:
                question_model = l.replace(entity, "<entity>")
                question_model = question_model.replace(end_entity, "<end_entity>")
                if entity+end_entity+question_model not in word_set:
                    word_models.append([entity, end_entity, question_model])
                    word_set.append(entity+end_entity+question_model)
pd.DataFrame(word_models).to_csv("entity_words_labels_end_entity_test.csv", index=False)
