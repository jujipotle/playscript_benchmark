import pandas as pd

model_name_dict = {
    "llama2_13b_chat": "meta-llama/Llama-2-13b-chat-hf",
    "llama3_8b": "meta-llama/Meta-Llama-3-8B",
    "llama3_8b_instruct": "meta-llama/Meta-Llama-3-8B-Instruct",
    "llama3_70b": "meta-llama/Meta-Llama-3-70B",
    "llama3_70b_instruct": "meta-llama/Meta-Llama-3-70B-Instruct",
    "llama3p1_8b_instruct": "meta-llama/Meta-Llama-3.1-8B-Instruct",
}

model_generation_dict = {
    "llama2_13b_chat": "llama2",
    "llama3_8b": "llama3",
    "llama3_8b_instruct": "llama3",
    "llama3_70b": "llama3",
    "llama3_70b_instruct": "llama3",
    "llama3p1_8b_instruct": "llama3p1"
}

emotions = ["happiness", "sadness", "anger", "fear", "disgust", "surprise"]

def filter_csv_by_columns(csv_file_path, filter_criteria):
    df = pd.read_csv(csv_file_path, dtype=str)
    filtered_df = df
    for column, value in filter_criteria.items():
        filtered_df = filtered_df[filtered_df[column] == value]
    return filtered_df

def chat_template(model_name):
    model_generation = model_generation_dict[model_name] 
    if model_generation == "llama2":
        user_tag = "[INST] "
        assistant_tag = " [/INST] "
    elif model_generation == "llama3":
        user_tag = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n"
        assistant_tag = "<|eot_id|>"
    elif model_generation == "llama3p1":
        user_tag = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n"
        # user_tag = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nCutting Knowledge Date: December 2023\nToday Date: 26 Jul 2024\n\nYou are a helpful Assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        assistant_tag = "<|eot_id|>"
    return user_tag, assistant_tag

def filter_criteria_to_string(filter_criteria, output_format):
    filter_criteria_string = ""
    for column, value in filter_criteria.items():
        if output_format == "file_name":
            value = str(value).replace('.', 'p')
            filter_criteria_string += f"{column}-{value}-"
        elif output_format == "display":
            filter_criteria_string += f"{column}: {value}, "
    if output_format == "file_name":
        return filter_criteria_string[:-1]
    elif output_format == "display":
        return filter_criteria_string[:-2]