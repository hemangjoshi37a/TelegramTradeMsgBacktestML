def convert_label_studio_to_hngFace_autoTrain_dataset(csv_import):
    '''Converts export file from Label-Studio to HuggingFace autoTrain trainable dataset
    Example : 
    *****   INPUT of this function  **** (file : ../project-1-at-2022-09-13-06-14-0f0c0db3.csv))
    text	id	annotator	annotation_id	created_at	updated_at	lead_time	label
    KEEP   JAGSNPHARM ON RADAR... 	1001	1	1007	2022-09-13T05:51:47.578986Z	2022-09-13T05:51:47.579052Z	4.298	[{"start": 7, "end": 17, "text": "JAGSNPHARM", "labels": ["symbol"]}]
    INTRADAY : BUY JAGSNPHARM ABOVE 306 SL 302 TARGET 312 - 316 - 320 	1000	1	1006	2022-09-13T05:51:41.795524Z	2022-09-13T05:51:41.795587Z	6.055	[{"start": 15, "end": 25, "text": "JAGSNPHARM", "labels": ["symbol"]}, {"start": 32, "end": 35, "text": "306", "labels": ["enter"]}, {"start": 39, "end": 42, "text": "302", "labels": ["sl"]}, {"start": 50, "end": 53, "text": "312", "labels": ["exit"]}]
    SUPER DUPER FUNDAMENTALS IN JAGSNPHARM... 	999	1	1005	2022-09-13T05:51:34.283369Z	2022-09-13T05:51:34.283431Z	2.903	[{"start": 28, "end": 38, "text": "JAGSNPHARM", "labels": ["symbol"]}]
    *****   OUTPUT of this function  **** (file : ./dataset_for_huggingface_autoTrain_label_vlassification.csv)
    text	label
    ['KEEP', 'JAGSNPHARM', 'ON', 'RADAR']	['NANA', 'symbol', 'NANA', 'NANA']
    ['INTRADAY', 'BUY', 'JAGSNPHARM', 'ABOVE', '306', 'SL', '302', 'TARGET', '312', '316', '320']	['NANA', 'NANA', 'symbol', 'NANA', 'enter', 'NANA', 'sl', 'NANA', 'exit', 'NANA', 'NANA']
    ['SUPER', 'DUPER', 'FUNDAMENTALS', 'IN', 'JAGSNPHARM']	['NANA', 'NANA', 'NANA', 'NANA', 'symbol']
    '''
    dataset_map_list  = []
    for _,data in tqdm(csv_import.iterrows()):
        this_text = data['text']
        this_label = data['label']
    #     print(this_text)
    #     print(this_label)
        if(not pd.isna(this_label)):

            message_plit = re.findall(r"[\w']+", this_text)

            this_symbol =''
            this_enter = 0.0
            this_sl = 0.0
            this_exit = 0.0

            this_literal_list = ast.literal_eval(this_label)

            for one_literal in this_literal_list:
                if(one_literal['labels'][0]=='symbol'):
                    this_symbol = one_literal['text']
                if(one_literal['labels'][0]=='enter'):
                    this_enter = one_literal['text']
                if(one_literal['labels'][0]=='sl'):
                    this_sl = one_literal['text']
                if(one_literal['labels'][0]=='exit'):
                    this_exit = one_literal['text']
    #         print(f'{this_symbol=}')
    #         print(f'{this_enter=}')
    #         print(f'{this_sl=}')
    #         print(f'{this_exit=}')

            label_list = []

            for one_word in message_plit:
                if(one_word==this_symbol):
                    label_list.append('symbol')
                    continue
                if(one_word==this_enter):
                    label_list.append('enter')
                    continue
                if(one_word==this_sl):
                    label_list.append('sl')
                    continue
                if(one_word==this_exit):
                    label_list.append('exit')
                    continue        
                label_list.append('NANA')

            dataset_map_list.append({'text':message_plit,'label':label_list})
    pd.DataFrame(dataset_map_list).to_csv('./dataset_for_huggingface_autoTrain_label_vlassification.csv',index=False)


def get_class_map_from_message_OLD(input_message:str) -> dict:
    ########### PREDICT TEXT AND CLASSIFY WORDS ##########
    ip1 = tokenizer(input_message,return_tensors='pt')

    op1 = model(**ip1)

    current_word = ''
    sentence = []
    sentence_class= []
    list_of_decoded_words = tokenizer.batch_decode(ip1['input_ids'][0])
    last_word_contained_hash = False
    last_classification_numner = 0

    for onet in range(len(ip1['input_ids'][0])):

        this_token = ip1['input_ids'][0][onet]
        this_classification = op1.logits[0][onet].tolist()
        this_decoded_word = list_of_decoded_words[onet]
        this_classification_number = np.argmax(this_classification)

        if(this_decoded_word=='[CLS]' or this_decoded_word=='[SEP]'):
            continue

    #     print(f'{this_decoded_word=}')
    #     print(f'{this_classification=}')
    #     print(f'{this_classification_number=}')

        this_word_contains_hash= '#' in this_decoded_word

        if('#' in this_decoded_word):
    #         print(f'''{this_decoded_word.replace('#','')=}''')
            current_word = current_word+this_decoded_word.replace('#','')
    #         print(f'{current_word=}')
    #         print('======================================')  
            last_word_contained_hash=True
            continue
        else:
            sentence.append(current_word)
            sentence_class.append(last_classification_numner)
            current_word=this_decoded_word
            last_classification_numner = this_classification_number
    #         print(f'{current_word=}')
    #         print('======================================')        
            last_word_contained_hash=False
            continue

    #     current_word=''

        print('======================================')

#     display(sentence)
#     display(sentence_class)

    #    "0": "NANA",
    #    "1": "enter",
    #    "2": "exit",
    #    "3": "sl",
    #    "4": "symbol"
    this_selected_symbol = ''
    this_enter = 0.0
    this_sl = 0.0
    this_exit  = 0.0
    for one_class_index in range(len(sentence_class)):
        one_class = sentence_class[one_class_index]
        if(one_class==1):
#             print(f'Enter : {sentence[one_class_index]}')
            this_enter = sentence[one_class_index]
        if(one_class==2):
#             print(f'exit : {sentence[one_class_index]}')
            this_exit = sentence[one_class_index]
        if(one_class==3):
#             print(f'sl : {sentence[one_class_index]}')
            this_sl = sentence[one_class_index]
        if(one_class==4):
#             print(f'symbol : {sentence[one_class_index]}')
            this_selected_symbol = sentence[one_class_index]
            
    return {'this_selected_symbol':this_selected_symbol,'this_enter':this_enter,'this_sl':this_sl,'this_exit':this_exit}
