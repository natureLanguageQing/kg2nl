import json

# entity_double_dir = os.listdir(os.path.join('entity_double'))
# for i in entity_double_dir:
#     a = pd.read_csv(os.path.join('entity_double', i)).values.tolist()
#     for j in a:
#         question = "{}的{}是什么？".format(j[1], j[0])
#         print(j)
#         print(question)
#         question = "{}的{}有什么？".format(j[1], j[0])
#         print(question)
#         question = "{}的{}是{}么？".format(j[1], j[0], j[2])
#         print(question)

# 读取关系的映射信息

filename = "relations_labels.json"


def KG2question(entity, relations):
    with open(filename, "r") as file:
        if file:
            relations_labels = json.load(file)

    questions_message = []
    relation_words = relations_labels[relations]
    questions_message.append(entity + relations)
    for relation_instance in relation_words:
        questions_message.append(entity + relation_instance + "?")
    return questions_message


def relation_to_words(relation, new_relation_word):
    with open(filename, "r") as file_obj:
        relations_labels = json.load(file_obj)

    if relation in relations_labels.keys():
        relation_words = relations_labels[relation]
        if new_relation_word not in relation_words:
            relation_words.append(new_relation_word)
        relations_labels[relation] = relation_words
    else:
        relations_labels[relation] = [new_relation_word]
    with open(filename, 'w') as file_obj:
        json.dump(relations_labels, file_obj, ensure_ascii=False)


def KG2question_answer(entity, relations, end_entity):
    with open(filename, "r") as file:
        if file:
            relations_labels = json.load(file)

    questions_answer = []
    relation_words = relations_labels[relations]
    questions_answer.append(entity + relations)
    for relation_instance in relation_words:
        questions_answer.append(entity + "的" + relation_instance + "是" + end_entity)
    return questions_answer


if __name__ == '__main__':
    relation_to_words("治疗", "推荐用药")
    relation_to_words("治疗", "治疗方案")
    questions = KG2question("糖尿病", "治疗")
    for question in questions:
        print(question)
    question_answers = KG2question_answer("糖尿病", "治疗", "胰岛素")
    for questions_answer in question_answers:
        print(questions_answer)
