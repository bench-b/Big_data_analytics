import os                   # Import os to work with file paths and directories
import re, nltk             # Import regex (re) and nltk for natural language processing
from nltk.corpus import stopwords  # Import stopwords list from nltk
nltk.download('stopwords')  # Download stopwords if not already installed

print("Current working directory: ", os.getcwd())  # Print the current working directory

# --- Open the text file and read content ---
with open("../data/sample_text.txt", "r", encoding="utf-8") as f:  
    text = f.read()          # Read the entire file as a single string
    print(text[:500])        # Print the first 500 characters to preview the content

# --- Clean the text ---
stop_words = set(stopwords.words('english'))   # Load English stopwords into a set

# Convert text to lowercase, remove non-letters, split into words,
# filter out stopwords, then join back into a clean string
clean_text = ' '.join([
    w for w in re.sub(r'[^a-z\s]', '', text.lower()).split()
    if w not in stop_words
])

print("\nClean text:", clean_text[:500])   # Print the first 500 characters of the cleaned text

# --- Word frequency analysis ---
from collections import Counter            # Import Counter to count word occurrences
freq = Counter(clean_text.split())         # Count word frequencies in the cleaned text
freq.most_common(10)                       # Get the 10 most common words (but not printed yet)

# --- WordCloud visualization ---
from wordcloud import WordCloud            # Import WordCloud library
import matplotlib.pyplot as plt            # Import matplotlib for plotting

# Generate a word cloud from the cleaned text
wc = WordCloud(width=800, height=400, background_color='white').generate(clean_text)

plt.figure(figsize=(15,8))                 # Create a figure with custom size
plt.imshow(wc, interpolation='bilinear')   # Display the word cloud image
plt.axis('off')                            # Hide the axis for a cleaner look
plt.show()                                 # Show the plot on screen
