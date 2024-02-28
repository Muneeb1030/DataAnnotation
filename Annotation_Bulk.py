# Bulk Provide Embedding for text

import pandas as pd
from umap import UMAP
from sklearn.pipeline import make_pipeline 

# pip install "embetter[text]"
from embetter.text import SentenceEncoder

# Build a sentence encoder pipeline with UMAP at the end.
text_emb_pipeline = make_pipeline(
  SentenceEncoder('all-MiniLM-L6-v2'),
  UMAP()
)

# Load sentences COpy Paste since laziness is my motto
sentences = list(pd.read_csv("Data/Corona_NLP_test.csv")['OriginalTweet'])

# Calculate embeddings 
X_tfm = text_emb_pipeline.fit_transform(sentences)

# Write to disk. Note! Text column must be named "text"
df = pd.DataFrame({"text": sentences})
df['x'] = X_tfm[:, 0]#X direction embedding 
df['y'] = X_tfm[:, 1]#Y direction embedding
df.to_csv("Output.csv", index=False)
# It will take some time depending on ammount of Data
# When embbeding process ends, we will see a csv file names output in file explorer