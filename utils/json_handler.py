import json

json_file = "./utils/hyperparameters.json"    # JSON file path

#Sample JSON dictionary
"""
{
    "dataset_csv": "/workspace/Machine Translation Code/Dataset/text/Hindi_Visual_Genome_Merged_Pre_Processed_non_leaked.csv",
    "src_column": "English Text Pre",
    "tgt_column": "Hindi Text Pre",
    "img_id_column": "image_id",
    "wave_pickle_path": "/workspace/Machine Translation Code/Dataset/audio/audio_data.pickle",
    "img_pickle_path": "/workspace/Machine Translation Code/Dataset/images/image_features.pickle",
    "max_wave_len": 48000,
    "src_min_word_freq": 3,
    "src_max_sent_len": 10,
    "tgt_min_word_freq": 3,
    "tgt_max_sent_len": 10,
    "src_vocab_size": 5450,
    "enc_word_embd_dim": 256,
    "enc_hidden_dim": 256,
    "enc_word_embd_dropout": 0.3,
    "enc_rnn_dropout": 0,
    "enc_rnn_layers": 1,
    "enc_bidirectional": 1,
    "tgt_vocab_size": 6941,
    "dec_word_embd_dim": 256,
    "dec_hidden_dim": 256,
    "dec_word_embd_dropout": 0.3,
    "dec_rnn_dropout": 0,
    "dec_rnn_layers": 1,
    "approach_type": 1,
    "device": "cuda",
    "batch_size": 512
}
"""


def get_parm(key):
    """
       function will take the key as input and return the corresponding value from the json file.
       Input  : "wave_pickle_path" 
       Output : "/workspace/Machine Translation Code/Dataset/audio/audio_data.pickle"
    """
    # Reading JSON file
    with open(json_file,'r') as f:
        parm_dict = json.load(f)       
    return parm_dict[key]            

def put_parm(key, value):
    """
       function will take the key and value as input and will save the key, value in the json file.
       Input  : "tgt_max_sent_len", 11
    """
    # Reading JSON file
    with open(json_file,'r') as f:
        parm_dict = json.load(f)

    parm_dict[key] = value          # Adding key, value to the json dict
    
    # Saving JSON file
    with open(json_file,'w') as f:
        json.dump(parm_dict, f)

