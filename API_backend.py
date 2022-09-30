from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import pandas as pd
import numpy as np
import json
from transformers import AutoModelForTokenClassification, AutoTokenizer

def get_class_map_from_message_NEW(input_message:str) -> dict:

    class_number_to_name_dict = {0 : '',
                                1 : 'btst',
                                2 : 'delivery',
                                3 : 'enter',
                                4 : 'momentum',
                                5 : 'exit',
                                6 : 'exit2',
                                7 : 'exit3',
                                8 : 'intraday',
                                9 : 'sl',
                                10 : 'symbol',
                                11 : 'momentum'}
    # class_number_to_name_dict

    ########### PREDICT TEXT AND CLASSIFY WORDS ##########
    print(input_message)
    print(type(input_message))
    input_message = str(input_message)
    print(input_message)
    print(type(input_message))
    
    ip1 = tokenizer(input_message,return_tensors='pt')
    op1 = model(**ip1)

    current_word = ''
    sentence = []
    sentence_class= []
    sentence_class_name= []
    list_of_decoded_words = tokenizer.batch_decode(ip1['input_ids'][0])
    last_word_contained_hash = False
    last_classification_numner = 0
    last_decoded_word = ''

    for onet in range(len(ip1['input_ids'][0])):
        this_token = ip1['input_ids'][0][onet]
        this_classification = op1.logits[0][onet].tolist()
        this_decoded_word = list_of_decoded_words[onet]
        this_classification_number = np.argmax(this_classification)

        if(this_decoded_word=='[CLS]' or this_decoded_word=='[SEP]'):
            continue

#         print(f'{this_decoded_word=}')
# #         print(f'{this_classification=}')
#         print(f'{this_classification_number=}')

        this_word_contains_hash= '#' in this_decoded_word

        if('#' in this_decoded_word):
            hash_replaced_word = this_decoded_word.replace('#','')
#             print(f'''{hash_replaced_word=}''')
            current_word = current_word+hash_replaced_word
#             print(f'{current_word=}')
            last_word_contained_hash=True

        elif((this_classification_number==last_classification_numner) and ((this_decoded_word=='.') or (last_decoded_word=='.'))):
            last_classification_numner = this_classification_number
            current_word = current_word+this_decoded_word
                
        else:
#             print('========== insidious ===============')
            sentence.append(current_word)
            sentence_class.append(last_classification_numner)
            sentence_class_name.append(class_number_to_name_dict[last_classification_numner])
#             print(f'{current_word=}')
#             print(f'{sentence=}')
#             print(f'{last_classification_numner=}')
#             print(f'{sentence_class=}')
#             print(f'{current_word=}')
            current_word=this_decoded_word
            last_classification_numner = this_classification_number
            
            last_word_contained_hash=False
        last_decoded_word = this_decoded_word


#         print('======================================')

    sentence.append(current_word)
    sentence_class.append((last_classification_numner))
    sentence_class_name.append(class_number_to_name_dict[last_classification_numner])
    results_json = {'sentence':str(sentence),
                        'sentence_class':str(sentence_class),
                        'sentence_class_name':str(sentence_class_name),
                       }
    #resultsdf = pd.DataFrame(results_json)
    
#     display(resultsdf)
    return results_json


app = Flask(__name__)
api = Api(app)

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')
def convert(o):
    if isinstance(o, np.generic): return o.item()  
    raise TypeError
# Define how the api will respond to the post requests
class MessageNER(Resource):
    def post(self):
        args = parser.parse_args()
        X = np.array(json.loads(args['data']))
        prediction = get_class_map_from_message_NEW(X)
        #return jsonify(prediction)
        return prediction

api.add_resource(MessageNER, '/classifyner')

if __name__ == '__main__':
    ###### LOAD PRETRAINED MODEL FROM HUGGINGFACE autoTrain #################
    model = AutoModelForTokenClassification.from_pretrained("hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086", use_auth_token=True)
    tokenizer = AutoTokenizer.from_pretrained("hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086", use_auth_token=True)

    app.run(debug=True,port=3737)
