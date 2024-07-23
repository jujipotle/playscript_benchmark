# Directory Roadmap

#### `data/`
Contains datasets and generated playscripts.
- `generic_emotion/`: The first dataset created, with prompts that are more diverse but potentially force the model to generate text with a certain emotion. The prompting is done with no control over the resulting emotion.
  - `train_premises.csv`, `test_premises.csv`: ChatGPT generated data to prompt Llama with.
  - `example_playscripts.csv`: Example playscripts for multi-shot prompting.
  - `generated_playscripts.csv`: Playscripts generated from Llama model based on `test_premises.csv`.
  - `generated_playscripts_edited.csv`: Cleaned version of `generated_playscripts.csv`.
  - `emotion_metrics.csv`: 
- `controlled_emotion/`: The second dataset created, with more open-ended prompts. The prompting can be done with control over Alice and Bob's emotions, independent of each other.
  - `test_premises.csv`: ChatGPT generated prompts that are more open-ended.
  - `example_playscripts.csv`: Example playscripts from ChatGPT.
  - `generated_playscripts.csv`: Playscripts generated from gpt-4o-mini-2024-07-18.

#### `representation-engineering/`
Contains code and resources for emotion classification.
- **Setup:**
  - Clone the repository: `git clone https://github.com/andyzoujm/representation-engineering.git`
  - Follow the installation instructions provided in the repository.
- **Important Subdirectories:**
  - `data/emotions/`: Used to train the emotion classifier.
  - `examples/primary_emotions/`: Contains example Jupyter notebooks.
    - `emotion_concept.ipynb`: Reference code for writing `measure_emotions.ipynb`.

#### `scripts/`
Scripts for generating playscripts and analyzing emotion metrics.
- **Notebooks:**
  1. `generate_playscripts.ipynb`: Generates playscripts from `test_premises.csv`. This step can be skipped if `generated_playscripts.csv` is already populated. Playscripts can be generated with generic_emotion (open-ended generation) or controlled_emotion (ground-truth emotions for Alice and Bob).
  2. `measure_emotions.ipynb`: Measures emotions in the generated playscripts. This step can be skipped if `emotion_metrics.csv` is already populated.
  3. `playscript_emotion_analytics.ipynb`: Analyzes the emotion metrics of the generated playscripts.

### Additional Notes
- **Handling of Generated Playscripts:**
  - `generate_playscripts.ipynb` accounts for edge cases, such as filtering lines not starting with "Alice: " or "Bob: ". Errors are manually corrected and saved in `generated_playscripts_edited.csv`.
- **Emotion Measurement:**
  - `measure_emotions.ipynb` by employs a PCA approach to identify directions that separate each of the emotions. Other options in the representation engineering paper are cluster means and logistic regression, but I haven't tested their code yet.