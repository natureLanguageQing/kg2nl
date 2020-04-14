import os

import pandas as pd

entity_double_dir = os.listdir(os.path.join('entity_double'))
question_answer = pd.read_csv("question_answer/question_answer.csv").values.tolist()
word_models = []
for i in entity_double_dir:
    print(i)
    a = pd.read_csv(os.path.join('entity_double', i)).values.tolist()
    # for j in a:
    #     question = "{}的{}是什么？".format(j[1], j[0])
    #     print(j)
    #     print(question)
    #     question = "{}的{}有什么？".format(j[1], j[0])
    #     print(question)
    #     question = "{}的{}是{}么？".format(j[1], j[0], j[2])
    #       print(question)
    for k in a:
        entity = k[1].strip("<")
        entity = entity.strip(">")
        relation = k[0].strip("<")
        relation = relation.strip(">")
        for l in question_answer:
            if entity in l[2] or relation in l[2]:
                question_model = l[2].replace(entity, "<entity>")
                question_model = question_model.replace(relation, "<relation>")
                if question_model not in word_models:
                    word_models.append(question_model)
pd.DataFrame(word_models).to_csv("words_model.csv", index=False)
