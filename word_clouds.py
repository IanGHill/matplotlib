import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use("ggplot")  # optional: for ggplot-like style

# Import Primary Modules:
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
from PIL import Image  # converting images into arrays

# import seaborn
import seaborn as sns

# import wordcloud
import wordcloud
import urllib
from wordcloud import WordCloud, STOPWORDS

print("Wordcloud imported!")


# check for latest version of Matplotlib and seaborn
print("Matplotlib version: ", mpl.__version__)  # >= 2.0.0
print("Seaborn version: ", sns.__version__)
print("WordCloud version: ", wordcloud.__version__)


# # open the file and read it into a variable alice_novel
alice_novel = (
    urllib.request.urlopen(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt"
    )
    .read()
    .decode("utf-8")
)

stopwords = set(STOPWORDS)
stopwords.add("said")  # add the words said to stopwords

# save mask to alice_mask
alice_mask = np.array(
    Image.open(
        urllib.request.urlopen(
            "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png"
        )
    )
)

# instantiate a word cloud object
alice_wc = WordCloud(
    background_color="white", max_words=2000, mask=alice_mask, stopwords=stopwords
)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud
fig = plt.figure(figsize=(14, 18))

plt.imshow(alice_wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# How to apply a wordcloud to our immigration data??

df_can = pd.read_csv("canada.csv")

print("Data read into a pandas dataframe!")
df_can.set_index("Country", inplace=True)
total_immigration = df_can["Total"].sum()

max_words = 90
word_string = ""
for country in df_can.index.values:
    # check if country's name is a single-word name
    if country.count(" ") == 0:
        repeat_num_times = int(
            df_can.loc[country, "Total"] / total_immigration * max_words
        )
        word_string = word_string + ((country + " ") * repeat_num_times)

# display the generated text
print(word_string)

# create the word cloud
wordcloud = WordCloud(background_color="white").generate(word_string)

print("Word cloud created!")
# display the cloud
plt.figure(figsize=(14, 18))

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
