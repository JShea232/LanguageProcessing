"""
Modified by: Jordan Edward Shea <jes7923>
Modification Date: 3/5/17
This program is used to analyze the probabilities for a particular word or set of words
to appear given a sample piece of text
"""
import nltk

"""
This function works to output the unigram probability for a word
For error-checking purposes, if the text read contains no words, the function
will automatically return a value of zero
"""
def computeUnigramProb(word, unigram, totalWords):
    if(totalWords != 0):
        return unigram[(word)] / totalWords
    else:
        return 0

"""
This function works to output the bigram probability for a word
For error-checking purposes, if the text read contains no words, the function
will automatically return a value of zero
"""
def computeBigramProb(word1, word2, unigram, bigram):
    bigramVal = bigram[(word1, word2)]
    unigramVal = unigram[(word1)]
    if(unigramVal != 0):
        return bigramVal / unigramVal
    else:
        return 0

"""
This function works to output the probability for a sentence to appear based off of the sample text.
@param sentence - the sentence that the user wants to calculate the probability of appearing in the text
@param unigram - the unigram distribution generated based off of reading through an input file
@param bigram - the bigram distribution generated based off of reading through an input file
@param totalWords - the total number of words in the original input file (not counting spaces and special characters)
"""
def computeSentenceProb(sentence, unigram, bigram, totalWords):
    words = []
    # Spilts the user-sentence into tokens
    for word in nltk.word_tokenize(sentence):
        # Removes non-alphabetical words
        if word.isalpha():
            words.append(word)
    sentenceProb = 1
    for i in range(len(words)):
        if(i != len(words) - 1):
            newProb = computeBigramProb(words[i], words[i+1], unigram, bigram)
            # Computes unigram probability if a bigram probability does not exist
            if(newProb == 0):
                newProb = computeUnigramProb(words[i], unigram, totalWords)
            sentenceProb = sentenceProb * newProb
        # Handles the situation where the last word could not be put into a bigram
        if(i == len(words) and computeBigramProb(words[i-1], words[i], unigram, bigram) == 0):
            sentenceProb = sentenceProb * computeUnigramProb(words[i], unigram, totalWords)
    return sentenceProb

"""
This function works to output the most likely sentence to appear in the sample text using a greedy algorithm
@param sentenceLength - the number of words in the sentence that the user wants to generate
@param unigram - the unigram distribution generated based off of reading through an input file
@param bigram - the bigram distribution generated based off of reading through an input file
"""
def mostCommonSentence(sentenceLength, unigram, bigram):
    bestSentence = ""
    previousWord = ""
    for i in range(sentenceLength):
        if(i == 0):
            bestFrequency = 0
            bestWord = ""
            for item in unigram:
                # First word should be uppercase
                if(item[0].isupper()):
                    if(unigram[(item)] > bestFrequency):
                        # Keeps track of the current highest frequency and word associated with it
                        bestFrequency = unigram[(item)]
                        bestWord = item
            bestSentence = bestSentence + bestWord + " "
            # Saves the most probable word to be used in the next iteration
            previousWord = bestWord
        if(i > 0):
            bestFrequency = 0
            bestWord = ""
            for item in unigram:
                # All following words should be lowercase
                if(item[0].islower()):
                    if(computeBigramProb(previousWord, item, unigram, bigram) > bestFrequency):
                        # Keeps track of the current highest frequency and word associated with it
                        bestFrequency = computeBigramProb(previousWord, item, unigram, bigram)
                        bestWord = item
            bestSentence = bestSentence + bestWord + " "
            # Saves the most probable word to be used in the next iteration
            previousWord = bestWord
    return bestSentence

def main():
    ## open a file, read it in as tokens
    f = open('pg31547.txt')
    raw = f.read()
    rawtokens = nltk.word_tokenize(raw)

    ## throw out punctuation and funny business
    tokens = []
    for t in rawtokens:
        if t.isalpha():
            tokens.append(t)

    ## Create bigrams
    bgs = nltk.bigrams(tokens)

    ## compute frequency distribution for all the bigrams in the text
    bigramfdist = nltk.FreqDist(bgs)

    ## compute unigram frequency distribution
    unigramfdist = nltk.FreqDist(tokens)

    # TEST CASES
    print(computeUnigramProb("cook", unigramfdist, len(tokens)))
    print(computeBigramProb("your", "father", unigramfdist, bigramfdist))
    print(computeSentenceProb("You should have been a fellow", unigramfdist, bigramfdist, len(tokens)))
    print(mostCommonSentence(6, unigramfdist, bigramfdist))

main()



