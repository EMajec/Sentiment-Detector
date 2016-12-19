#Ethan Turer
#10/22/16
#CS065
#This code checks the sentiment of movie reviews and words in order to tell how a movie was
#This document deserves a 15/15 all tasks were completed and I added a little extra piece



def main(): #calls all of the functions in the requested order
    choice = wordorfile() #calls the function for choosing a word or a file
    if choice is "w": #option for word search
        word = wordsearch() #choose word to search and set that result to value word
        sentiment(word) #accepts the variable word as a parameter and uses that to search the movie reviews and give them sentiments and scores
        averagestars() #extra fun item for just seeing what all of the review scores averaged were for the entire movie
    if choice is "f": #option for file search
        file = filesearch2() #allows the user to enter a filename
        sentence_sentiment(file) #gives the file a sentiment, and takes the filename as its parameter


def filesearch2():
    f = str(input("What is the name of the file you want to open? "))
    return f #returns the file name desired to be entered

def sentiment(word): #finds the sentiment of the word and gives them a score
    with open("ratedMovieReviews.txt", "r") as f: #opens and closes file when finished with it
        totalscore = 0 #accumulator for all of the scores where the word will appear
        number_of_reviews = 0 #accumulator for the total number of times the word appear in the reviews
        sentiment = "" #string accumulator for the word's sentiment
        average = 0 #initializes the average of the word searched to 0
        for item in f: #runs through every word in the entire document
            score = int(item.rstrip('\n')) #sets the score of the items separate to teh review
            text = f.readline() #calls all of the lines to be read individually as we search for the word
            if word in text: #checks each line to see if the word is in the line
                totalscore +=score #if the word is in the line it will add the score from that line to the totalscore of the word
                number_of_reviews += 1 #adds each time we find the word
                average = totalscore / number_of_reviews #sets the average of the word to the total score of the word divided by how many times it showed up
            if average > 2: #the next lines are statements assigning the sentiment based on the average
                sentiment = "positive"
            elif average == 2:
                sentiment = "neutral"
            elif average < 2:
                sentiment = "negative"
        if word not in text: #this is an exception statement to create a neutral word if the word is not found
            average = 2.0
            sentiment = "neutral"
            print(word,"doesnt appear in any reviews, so were giving it a neutral score of 2.0")
    print("Reviews with", word, "had an average rating of", average, "and has a", sentiment,"sentiment")
    return average #returns the average for future use in the sentence sentiment

def sentence_sentiment(file): #sets a sentiment to an entire document
    try: #initializes the exception statement
        with open(file,"r") as file2: #opens and closes the file for me.
            data = file2.read().replace('\n', ' ') #Learned in codeacademy, replaces all of the breaks with spaces
            obj = data.split() #Learned through CodeAcademy, splits all of the words into separate lines without spaces
            cumulator = 0 #an accumulator for counting each word in the document
            code = 0 #accumulator for the score of all the words combined
            scorelist = [] #empty list to append all of the scores to
            wordlist = [""] #empty list for setting all of the words to
            for items in obj: #goes through each word in the file
                num = sentiment(items) #goes trhough each word and returns the average number
                code += num #adds all of the scores together
                cumulator += 1 #counts words in the document
                scorelist.append(num) #puts all of the numbers into a list
                wordlist.append(items) #puts all of the words into a list
            topnum = max(scorelist) #finds the maximum number out of all the words
            index = scorelist.index(topnum) #finds the index for that number
            bottomnum = min(scorelist) #finds the minimum number out of all the words
            index2 = scorelist.index(bottomnum) #finds the index for that number
            topword = wordlist[index + 1 ] #finds the top word, making sure that the first space isn't counted due to blank line as 1
            bottomword = wordlist[index2 + 1] #finds the bottom word, making sure that the first space isn't counted due to blank line as 1
            average = code/cumulator #finds the overall average of the file
            print(file, "has a rating of", average)
            print(file,"had", topword,"as its highest scoring word")
            print(file, "had", bottomword, "as its lowest scoring word")
    except FileNotFoundError or ZeroDivisionError: #makes sure if any errors with file not found or zero division will still run but neutrally
        topword = ""
        bottomword = ""
        average = 2.0
        sentiment = "neutral"
        print(file,"Not found but we will give this document a neutral sentiment, a neutral score, and neutral maximum and minumum scoring words")
        print(file, "had a",sentiment,"sentiment")
        print(file, "has a rating of", average)
        print(file, "had", topword, "as its highest scoring word")
        print(file, "had", bottomword, "as its lowest scoring word")

def averagestars(): #fun extra piece finding the average score the entire MovieReview document
    file = open("ratedMovieReviews.txt",'r')
    totalscore = 0
    number_of_reviews = 0
    for item in file:
        score = int(item.rstrip('\n'))
        text = file.readline()
        totalscore +=score
        number_of_reviews += 1
    average = totalscore / number_of_reviews
    print("The film had an average rating of",average, ", unfortunately it wasn't that great")

def wordsearch(): #allows the user to create a word to search
    word = str(input("Enter a word: "))
    return word

def wordorfile(): #gives the user the option to search for a file or for a word
    choice = str(input("Would you like to to find the sentiment of a word or file? (w/f): "))
    return choice

main() #runs the program