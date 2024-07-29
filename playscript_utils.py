import pandas as pd

model_name_dict = {
    "llama2_13b_chat": "meta-llama/Llama-2-13b-chat-hf",
    "llama3_8b": "meta-llama/Meta-Llama-3-8B",
    "llama3_8b_instruct": "meta-llama/Meta-Llama-3-8B-Instruct",
    "llama3_70b": "meta-llama/Meta-Llama-3-70B",
    "llama3_70b_instruct": "meta-llama/Meta-Llama-3-70B-Instruct",
    "test": "test"
}

emotions = ["happiness", "sadness", "anger", "fear", "disgust", "surprise"]

def filter_csv_by_columns(csv_file_path, filter_criteria):
    df = pd.read_csv(csv_file_path)
    filtered_df = df
    for column, value in filter_criteria.items():
        filtered_df = filtered_df[filtered_df[column] == value]
    return filtered_df