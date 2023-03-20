import numpy as np
import pandas as pd
import string
import os
import matplotlib.pyplot as plt
import random

"""get rid of Gutenberg Project information"""
def getrifof_ONE_gutenberg(name):
    for idx, lin in enumerate(name):
        start1 =  '*** START OF THIS PROJECT GUTENBERG'
        start2 = '*** START OF THE PROJECT GUTENBERG'
        end1 =  "*** END OF THIS PROJECT GUTENBERG"
        end2 = "*** END OF THE PROJECT GUTENBERG"
        if start1 in lin:
            start_idx = idx
        elif start2 in lin:
            start_idx = idx

        elif end1 in lin:
            end_idx = idx
            break
        elif end2 in lin:
            end_idx = idx
            break
        else:
            end_idx = -1



    name = name[start_idx+1:end_idx]
    return name


def getridGutenberg(paths, filenames):
    kilciksiz= []
    for namess in filenames:
        whole_path = os.path.join(paths, namess)
        with open(whole_path, encoding = "utf8", mode = "r") as f:
            lines = f.readlines()
        kilciksiz.append(getrifof_ONE_gutenberg(lines))
    return kilciksiz


"""get rid of every punctuation marks and cast every word to lowercase"""


def init_tokenization(name_list):
    books = []
    for book in name_list:
        book = " ".join(book)
        book = book.replace("\n", "")
        book = book.split()
        a_book = []
        for lines in book:
            lines = lines.translate(str.maketrans('', '', string.punctuation))
            lines = lines.lower()
            a_book.append(lines)

        books.append(a_book)
    return books


"""Search for and determine a common English Language stop-word list"""
"""obtain stopword-removed versions of your texts above"""

def stop_word_removal(books):
    print("stop  word removal")
    with open("stop_words_english.txt", encoding = "utf-8", mode="r") as f:
        stop_file = f.readlines()
    stop_file = " ".join(stop_file)
    stop_file = stop_file.replace("\n", " ")
    stop_file = stop_file.split()
    new_book_list = []

    for book in books:
        book = " ".join(book)
        book = " " + book + " "
        for stop_word in stop_file:
            book = book.replace(" "+stop_word+ " ", " ")
        book = book.split()
        new_book_list.append(book)
    return new_book_list


"""create vocabulary files carrying the word types along with their frequencies"""


def type_frequency(book_list):
    print("type-frequency")
    freq_type_dict = {}
    for one_book in book_list:
        i = book_list.index(one_book)
        types, freq = np.unique(np.array(one_book), return_counts= True)
        one_dict = dict(zip(types, freq))
        # sort in the ascending order
        one_dict = dict(sorted(one_dict.items(), key = lambda one_dict:one_dict[1], reverse=True))
        freq_type_dict[i+1] = one_dict
    return freq_type_dict


"""Compose corresponding larger author corpora by combining all three books of each author"""


def groupby_author(authorlist, theme=None):
    print("groupby")
    if theme:
        author_map = ["Autobiography", "Classic Novel", "Romance"]
    else:
        author_map = ["Dickens", "Smollett", "Tolstoy"]
    global_dict = {}
    for j in np.arange(1,4):
        one_freq = {
            i: authorlist[j].get(i, 0) + authorlist[j+1].get(i, 0) + authorlist[j+2].get(i, 0) for i in
            set(authorlist[j]).union(set(authorlist[j+1]).union(authorlist[j+2]))}
        one_freq = dict(sorted(one_freq.items(), key=lambda one_freq: one_freq[1], reverse=True))
        global_dict[author_map[j-1]] = one_freq
    return global_dict

def group_freely(freq_list, theme=None):
    if theme:
        labels = ["Autobiography", "Classic Novel", "Romance"]
    else:
        labels = ["Dickens", "Smollett", "Tolstoy"]
    dict_authors_stopped = {}
    index_map = {3: 0, 6: 1, 9: 2}
    for k in np.arange(3, 10, 3):
        dict_authors_stopped[labels[index_map[k]]] = [freq_list[k], freq_list[k - 1],freq_list[k - 2]]
    return dict_authors_stopped


def plot_Zipf(many_dict, normal_scale = None, stop_word_removed = None):
    if normal_scale:
        for author in list(many_dict.keys()):
            plt.scatter(np.arange(len(many_dict[author])), list(many_dict[author].values()), s=3)
    else:
        for author in list(many_dict.keys()):
            plt.scatter(np.log(np.arange(len(many_dict[author]))+1), np.log(list(many_dict[author].values())), s=3)
    if stop_word_removed:
        if normal_scale:
            plt.title("Zipf's Law Curves for 3 Author in Normal Scale Stop Words Removed")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.legend(list(many_dict.keys()))
            plt.show()
        else:
            plt.title("Zipf's Law Curves for 3 Author Stop Words Removed log")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.legend(list(many_dict.keys()))
            plt.show()
    else:
        if normal_scale:

            plt.title("Zipf's Law Curves for 3 Author in Normal Scale with Stop Words ")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.legend(list(many_dict.keys()))
            plt.show()
        else:

            plt.title("Zipf's Law Curves for 3 Author with Stop Words log")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.legend(list(many_dict.keys()))
            plt.show()
    return


def plot_Zipf_v2(name, list_freq, normal_scale = None, stop_word_removed = None):

    if normal_scale:
        for book in list_freq:
            plt.scatter(np.arange(len(book)), list(book.values()), s=3)
    else:
        for book in list_freq:
            plt.scatter(np.log(np.arange(len(book))+1), np.log(list(book.values())), s=3)
    if stop_word_removed:
        if normal_scale:
            plt.title(f"Zipf's Law Curves for {name} in Normal Scale Stop Words Removed")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.show()
        else:
            plt.title(f"Zipf's Law Curves for {name} Stop Words Removed log")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.show()
    else:
        if normal_scale:

            plt.title(f"Zipf's Law Curves for {name} in Normal Scale with Stop Words ")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.show()
        else:

            plt.title(f"Zipf's Law Curves for {name} with Stop Words log")
            plt.xlabel("Word Rank")
            plt.ylabel("Number of Occurrences")
            plt.show()
    return

def tokensize_freq(authorslist, author_corpora=None):

    all_list =[]
    if author_corpora:
        merged = []
        new_list = authorslist.copy()
        for j in np.arange(0,9,3):
            temp1= new_list[j] + new_list[j+1]
            temp1 = temp1 + new_list[j + 2]
            merged.append(temp1)
    else:
        merged = authorslist
    for author in merged:
        vocabsize = []
        tokensize = []
        token_now = []
        distinct = []
        rate = 5000
        for i, token in enumerate(author):
            if (i+2)%rate == 0:
                temp = set(token_now)
                temp = np.asarray(list(temp))
                intercept, arr1idx, arr2idx = np.intersect1d(np.asarray(distinct), temp, return_indices =True)
                temp = np.delete(temp, arr2idx)
                distinct = np.append(distinct, temp)
                vocabsize.append(len(distinct))
                tokensize.append(i)
                token_now=[]
            else:
                token_now.append(token)
        all_list.append([tokensize, vocabsize])
    return all_list


def plot_tokensize(tokenlist, normal_scale = None, stop_word_removed = None, theme = None):
    if theme:
        name_lsit = ["Autobiography", "Classic Novel", "Romance"]
    else:
        name_lsit = ["Dickens", "Smollett", "Tolstoy"]
    if normal_scale:
        for author in tokenlist:
            plt.plot(author[0], author[1])
    else:
        for author in tokenlist:
            plt.plot(np.log(author[0]), np.log(author[1]))
    if stop_word_removed:
        if normal_scale:
            plt.title("Token Size vs Vocabulary Size for 3 Authors in Normal Scale Stop Words Removed")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.legend(name_lsit)
            plt.show()
        else:
            plt.title("Token Size vs Vocabulary Size for 3 Authors Stop Words Removed log")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.legend(name_lsit)
            plt.show()
    else:
        if normal_scale:

            plt.title("Token Size vs Vocabulary Size for 3 Authors in Normal Scale with Stop Words ")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.legend(name_lsit)
            plt.show()
        else:

            plt.title("Token Size vs Vocabulary Size for 3 Authors with Stop Words log")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.legend(name_lsit)
            plt.show()
    return


def plot_tokensize_v2(tokenlist, normal_scale = None, stop_word_removed = None, theme = None, grouped =None):
    if theme:
        name_lsit = ["Autobiography", "Classic Novel", "Romance"]
    else:
        name_lsit = ["Dickens", "Smollett", "Tolstoy"]
    if grouped:
        plt.plot(np.log(tokenlist[0][0]), np.log(tokenlist[0][1]), c="r")
        plt.plot(np.log(tokenlist[1][0]), np.log(tokenlist[1][1]), c="g")
        plt.plot(np.log(tokenlist[2][0]), np.log(tokenlist[2][1]), c="b")
        plt.legend(name_lsit)
    else:
        if normal_scale:
            for i in np.arange(0,3):
                plt.plot(tokenlist[i][0], tokenlist[i][1], c = "r")
                plt.plot(tokenlist[i+3][0], tokenlist[i+3][1],c = "g")
                plt.plot(tokenlist[i+6][0], tokenlist[i+6][1],c = "b")
                if i == 0:
                    plt.legend(name_lsit)

        else:
            for i in np.arange(0, 3):
                plt.plot(np.log(tokenlist[i][0]), np.log(tokenlist[i][1]),c = "r")
                plt.plot(np.log(tokenlist[i+3][0]), np.log(tokenlist[i+3][1]),c = "g")
                plt.plot(np.log(tokenlist[i+6][0]), np.log(tokenlist[i+6][1]),c = "b")
                if i == 0:
                    plt.legend(name_lsit)

    if stop_word_removed:
        if normal_scale:
            if theme:
                plt.title("Token Size vs Vocabulary Size for 3 Categories in Normal Scale Stop Words Removed")
            else:
                plt.title("Token Size vs Vocabulary Size for 3 Authors in Normal Scale Stop Words Removed")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.show()
        else:
            if theme:
                plt.title("Token Size vs Vocabulary Size for 3 Categories in log Scale Stop Words Removed")
            else:
                plt.title("Token Size vs Vocabulary Size for 3 Authors in log Scale Stop Words Removed")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.show()
    else:
        if normal_scale:

            if theme:
                plt.title("Token Size vs Vocabulary Size for 3 Authors in Normal Scale with Stop Words")
            else:
                plt.title("Token Size vs Vocabulary Size for3 Categories in Normal Scale with Stop Words")

            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.legend(name_lsit)
            plt.show()
        else:

            if theme:
                plt.title("Token Size vs Vocabulary Size for 3 Categories in log Scale  with Stop Words")
            else:
                plt.title("Token Size vs Vocabulary Size for 3 Authors in log Scale with Stop Words")
            plt.xlabel("Token Size")
            plt.ylabel("Word Types")
            plt.show()
    return


"""" FIND SLOPE"""


def best_fit(all_books, stop_word_removed = None,theme = None, grouped = None):
    if theme:
        name_lsit = ["Autobiography","Classic Novel", "Romance"]
    else:
        name_lsit = ["Dickens",  "Smollett",  "Tolstoy", ]

    def slope_finder(X, y):
        data = np.polyfit(X, y, deg=1)
        print(data[0], data[1])
        line_data = (pd.Series(X).mul(data[0])).to_numpy() + data[1]
        return line_data

    if grouped:
        plt.plot(np.log(all_books[0][0]), slope_finder(np.log(all_books[0][0]), np.log(all_books[0][1])), c="r")
        plt.plot(np.log(all_books[1][0]), slope_finder(np.log(all_books[1][0]), np.log(all_books[1][1])),
                 c="g")
        plt.plot(np.log(all_books[2][0]), slope_finder(np.log(all_books[2][0]), np.log(all_books[2][1])),
                 c="b")
        plt.plot(np.log(all_books[0][0]), np.log(all_books[0][1]), c="r")
        plt.plot(np.log(all_books[1][0]), np.log(all_books[1][1]), c="g")
        plt.plot(np.log(all_books[2][0]), np.log(all_books[2][1]), c="b")
        plt.legend(name_lsit)

    else:
        for i in np.arange(0,3):
            plt.plot(np.log(all_books[i][0]), slope_finder(np.log(all_books[i][0]), np.log(all_books[i][1])),c="r")
            plt.plot(np.log(all_books[i + 3][0]), slope_finder(np.log(all_books[i + 3][0]), np.log(all_books[i + 3][1])),c="g")
            plt.plot(np.log(all_books[i + 6][0]), slope_finder(np.log(all_books[i + 6][0]), np.log(all_books[i + 6][1])),c="b")
            plt.plot(np.log(all_books[i][0]), np.log(all_books[i][1]),  c="r")
            plt.plot(np.log(all_books[i + 3][0]), np.log(all_books[i + 3][1]), c="g" )
            plt.plot(np.log(all_books[i + 6][0]), np.log(all_books[i + 6][1]), c="b")
            if i == 0:
                plt.legend(name_lsit)

    if stop_word_removed:
        if theme:
            plt.title("Token Size vs Vocabulary Size for 3 Categories in log Scale Stop Words Removed")
        else:
            plt.title("Token Size vs Vocabulary Size for 3 Authors in log Scale Stop Words Removed")
        plt.xlabel("Token Size")
        plt.ylabel("Word Types")
        plt.show()
    else:
        if theme:
            plt.title("Token Size vs Vocabulary Size for 3 Categories in log Scale  with Stop Words")
        else:
            plt.title("Token Size vs Vocabulary Size for 3 Authors in log Scale with Stop Words")
        plt.xlabel("Token Size")
        plt.ylabel("Word Types")
        plt.show()
    return


def random_text_generator(max_word_len,max_text_len):
    alfphabet = string.ascii_lowercase
    word_count = 0
    book = []
    while word_count < max_text_len:
        curr_word_len = random.randint(1, max_word_len)
        curr_word = ''.join(random.choice(alfphabet) for x in range(curr_word_len))
        book.append(curr_word)
        word_count += 1

    print(book)
    my_book_freq = type_frequency([book])
    plt.scatter(np.arange(len(my_book_freq[1].keys())), list(my_book_freq[1].values()), s=3)
    plt.title("Artificial Text Zipf's Law Plot on Normal Scale")
    plt.xlabel("Word Rank")
    plt.ylabel("Number of Occurences")
    plt.show()
    print()

    plt.scatter(np.log(np.arange(len(my_book_freq[1].keys())) + 1), np.log(list(my_book_freq[1].values())), s=3)
    plt.title("Artificial Text Zipf's Law Plot on log-log Scale")
    plt.xlabel("Word Rank")
    plt.ylabel("Number of Occurences")
    plt.show()
    print()
    return
