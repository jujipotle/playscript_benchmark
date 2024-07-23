# Directory roadmap:

## data/
- train_premises.csv, test_premises.csv, example_playscripts.csv: ChatGPT generated data to prompt Llama with
- generated_playscripts.csv: Playscripts generated from Llama model on test_premises.csv
- generated_playscripts_edited.csv: Cleaned version of generated_playscripts.csv
- emotion_metris.csv: Emotion metrics on generated_playscripts_edited.csv

## representation-engineering/
- git clone https://github.com/andyzoujm/representation-engineering.git to get this directory. Follow their installation instructions.
- data/emotions/ is used to train emotion classifier
- examples/primary_emotions/emotion_concept.ipynb is used as reference code to write measure_emotions.ipynb

## scripts/
1. Run generate_playscripts.ipynb to generate playscripts from test_premises.csv (Can skip this, generated_playscripts.csv already populated)
2. Run measure_emotions.ipynb to measure emotions in the generated playscripts (Can skip this, emotion_metrics.csv already populated)
3. Run playscript_emotion_analytics.ipynb to analyze the emotion metrics of the generated playscripts

# Notes:
- generate_playscripts.ipynb handles most edge cases of generated playscripts. For example, it filters through lines that don't start with "Alice: "
 or "Bob: " and throws an error if the wrong character is speaking. There are sometimes still errors, so I manually edit and save to generated_playscripts_edited.csv.
- measure_emotions.ipynb uses a PCA approach to find directions that separate each of the emotions. Training data is from representation-engineering/data/emotions.
One thing I noticed while playing around with the emotion classifier is that strictly classifying positive scores=presence of emotion, negative scores=absence of emotion 
does NOT classify the training data the best. Fortunately our intended experiment only cares about delta (change in emotion score), so we can mostly ignore the
 classification accuracy issue.
