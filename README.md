# Synonyms
# Authors: Anthony Salgado & Harry Nguyen
# Date Completed: December 5, 2022
# Semantic Similarity Project

This project contains Python functions to compute semantic similarity between words using cosine similarity and semantic descriptors built from text files.

## Code Structure

### Subpart A - Vector Operations

- **`norm(vec)`**:  
  Computes the norm (magnitude) of a vector stored as a dictionary.
  
- **`cosine_similarity(vec1, vec2)`**:  
  Computes the cosine similarity between two vectors stored as dictionaries.

### Subpart B - Building Semantic Descriptors

- **`build_semantic_descriptors(sentences)`**:  
  Builds a dictionary where each word is associated with a dictionary of co-occurring words and their counts.

### Subpart C - Building Semantic Descriptors from Files

- **`build_semantic_descriptors_from_files(filenames)`**:  
  Reads text files, processes the sentences, and builds semantic descriptors for the words found in the text.  
  Handles punctuation and other text-cleaning tasks.

### Subpart D - Finding the Most Similar Word

- **`most_similar_word(word, choices, semantic_descriptors, similarity_fn)`**:  
  Given a word and a list of choices, finds the most semantically similar word from the list using the provided similarity function (e.g., cosine similarity).

### Subpart E - Running a Similarity Test

- **`run_similarity_test(filename, semantic_descriptors, similarity_fn)`**:  
  Reads a test file and compares the semantic similarity of words to measure accuracy of word similarity prediction.

## How to Use

1. **Prepare text files**:  
   Ensure the text files (`wp.txt`, `sw.txt`, etc.) are in the same directory as the script. The code reads text from these files to build semantic descriptors.

2. **Test file format**:  
   The test file (`test.txt`) should contain lines with the format:  
   `word correct_answer choice1 choice2`  
   For example:  
   `dog cat wolf bear`

3. **Run the script**:  
   The script can be run directly. It will build semantic descriptors from the text files and then run a similarity test using the descriptors:
   ```bash
   python semantic_similarity.py
   
4. Output:

The output is the accuracy percentage of the similarity test.

  ```bash
  if __name__ == '__main__':
      sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
      res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
      print(res)
    
This will build semantic descriptors from the files wp.txt and sw.txt and test the similarity predictions using test.txt.

Dependencies

  - Python 3.x

  - math and re libraries (built-in)

Notes

The text processing is case-insensitive and removes certain punctuation.
