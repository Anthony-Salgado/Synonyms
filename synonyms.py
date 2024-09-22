
import math
import re

##SUBPART A
def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    denominator = norm(vec1) * norm(vec2)
    
    #Determine the vaue of numerator
    for key, value in vec1.items():
        for key_1, value_1 in vec2.items():
            if key == key_1:
                numerator += value * value_1

    return numerator/denominator


#SUBPART B
def build_semantic_descriptors(sentences):
    res = {}
    for sentence in sentences:
        for word in sentence:
            if word in res:
                for word2 in sentence:
                    if word2 != word:
                        if word2 in res[word]:
                            res[word][word2] += 1
                        else:
                            res[word][word2] = 1
            else:
                res[word] = {}
                for word2 in sentence:
                    if word2 != word:
                        if word2 in res[word]:
                            res[word][word2] += 1
                        else:
                            res[word][word2] = 1
    return res



##SUBPART C
#function to build semantic descriptor from files
def build_semantic_descriptors_from_files(filenames):
    list_for_file = []
    for i in range(len(filenames)):
        try:
            with open(filenames[i], "r", encoding = "UTF-8") as f:
                content = f.read()
                content = content.lower()
                last_i = 0
                punc_separate_list = [".", "!", "?"]
                for i in range(len(content)):
                    list = []
                    #IMPROVE THE ALGORITHM HERE. ISSUES SO FOR
                    #1. some "." don't separate the sentences ie. St. Petersburg
                    #2. words/numbers in between two punctutations are not shown ie. Harry, Tony, and Kyle blacked out. --> Tony is not shown
                    if content[i] in punc_separate_list:
                        list = re.sub(r'[,-:;]', '', content[last_i : i]).split()
                        list_for_file.append(list)
                        #i is the punctutation index --> want to get rid of it
                        last_i = i + 1
        except FileNotFoundError:
            print("File not found. Check the path variable and filename")
            exit()   
            
    return build_semantic_descriptors(list_for_file)


#SUBPART D
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    highest_value = -1
    highest_i = 0
    if word in semantic_descriptors.keys():
        for i in range (len(choices)):
            #looping through every string of choices compared with the word given
            #highest_value = 0
                #each string of choice is taken from semantic descriptor and so is the word
                #the similarity function would return 
                    #highest_value = the similarity value of the two strings
                    #higest_value = -1 if no string of choices is found in semantic descriptors
            #return 
            if choices[i] in semantic_descriptors.keys():
                current_value = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[i]])
                if current_value > highest_value:
                    highest_i = i
                    highest_value = max (current_value, highest_value)
            else:
                highest_value = max (-1, highest_value)

        return choices[highest_i]
    else:
        return choices[highest_i]


#Subpart E
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct_ans = 0
    final_list = []
    #build the final list
    with open(filename, "r", encoding = "UTF-8") as f:
        content = f.read()
        content = content.split()
        list = []
        for i in range (len(content)):
            if i % 4 == 0 and i != 0:
                final_list.append(list)
                list = []
            list.append(content[i])
        final_list.append(list)
    
    for i in range (len(final_list)):
        word = final_list[i][0]
        choices = final_list[i][2:4]
        ans = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if ans == final_list[i][1]:
            correct_ans += 1
    return (float(correct_ans / len(final_list))) * 100



if __name__ == '__main__':
    sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    res = run_similarity_test ("test.txt", sem_descriptors, cosine_similarity)
    print(res)
    # print(build_semantic_descriptors_from_files(["test1.txt"]))
