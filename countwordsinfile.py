
"""
Explanation of the Changes
File Handling with with open(...):

This automatically closes the file after reading, even if an error occurs.
Simplified for Loops:

Each line of text is cleaned in a more streamlined way, replacing punctuation and ignoring specified words.
Enhanced Readability:

The code structure and indentation are optimized for clarity.
Error-Handled Output for Less Than 10 Words:

The for loop prints only the available words (up to 10) to avoid errors if there are fewer than 10 unique words




"""





def word_anaylsis(article="deneme.txt"):

    # Open the file in read mode

    with open(article, 'r') as f:

        # Initialize dictionary and variables
        
        #w_dict is an empty dictionary that will store each unique word as a key, with its frequency (the number of times it appears) as the value.
        w_dict = {}

        #punctuations is a list of characters that will be removed from the text, as they don’t add meaningful information to word frequency.
        punctuations = ['`', '\'', '=', '//', '-', ',', '.', ':', '"', '[', ']', '(', ')', ';', '!', '?', '\n']

        #less_meaningful is a list of common words that don’t contribute significantly to the analysis (known as stop words), which will be removed from the text as well.
        less_meaningful = ['the', 'a', 'an', 'to', 'of', 'and', 'was', 'is', 'are', 'in', 'on']

        #words_total will store the total number of words counted in the text, unique_count will keep track of the number of unique words. 
        words_total, unique_count = 0, 0
        
        # Process each line in the file

        #This loop iterates over each line in the file f, allowing the function to process the text one line at a time.
        for line in f:

            # Remove punctuation by replacing with spaces

            #This inner loop goes through each punctuation character in the punctuations list and replaces it with a space in the current line (line), effectively removing it. This cleanup step makes it easier to split words accurately by spaces.
            for p in punctuations:
                line = line.replace(p, ' ')
            
            # Remove less meaningful words

            #This loop removes each word in the less_meaningful list from the line,Both lowercase and capitalized versions of the words are replaced with spaces.
            for word in less_meaningful:
                line = line.replace(f' {word} ', ' ')
                line = line.replace(f' {word.capitalize()} ', ' ')
            
            # Split cleaned line into words

            #After cleaning the line, line.split() splits the line into a list of individual words, using whitespace as the separator without any punctuation or less meaningful words
            words = line.split()
            
            # Count total and unique words
            for word in words:
                if word:  # Skip empty words
                    #If the word is not an empty string (in case of extra spaces), words_total is incremented by 1.
                    words_total += 1  



                    #If the word is not already in w_dict, it’s added with an initial frequency of 1, and unique_count is incremented by 1.
                    if word not in w_dict:

                        unique_count += 1  #If the word is not already in w_dict and unique_count is incremented by 1.
                        w_dict[word] = 1 #If the word is not already in w_dict, it’s added with an initial frequency of 1
                    else:
                        w_dict[word] += 1  #If the word is already in w_dict, its count is incremented by 1.
    
    # Sort dictionary by frequency in descending order
    sorted_words = sorted(w_dict.items(), key=lambda item: item[1], reverse=True)
    
    return words_total, sorted_words

# Run the function and display results
result = word_anaylsis()
print(f"The article has {result[0]} words in total")  # result[0] holds the total word count, which is printed.
print(f"The number of unique words used is {len(result[1])}") #result[1] is the sorted list of unique words, and its length is printed as the number of unique words.

# Print the 10 most common words
for i in range(min(10, len(result[1]))):
    print(f'Word "{result[1][i][0]}" used {result[1][i][1]} times.')
