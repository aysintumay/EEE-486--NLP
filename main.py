
import os
import matplotlib.pyplot as plt

from helpers import getridGutenberg,init_tokenization,stop_word_removal,type_frequency,tokensize_freq,best_fit,\
    group_freely,plot_Zipf,plot_Zipf_v2,plot_tokensize,plot_tokensize_v2,random_text_generator


if __name__ == "__main__":
    file_path = os.path.join("C:\\Users\\User\\Desktop\\SPRING 2023\\EEE 486\\Assignment1\\texts")
    by_author_file = os.path.join(file_path, "by_author")
    by_author_list = os.listdir(by_author_file)

    gutenberg_removed_all_author = getridGutenberg(by_author_file,by_author_list)
    tokenized_all_author = init_tokenization(gutenberg_removed_all_author)
    stop_word_removed_All_author = stop_word_removal(tokenized_all_author)
    freq_list_author_stopped = type_frequency(stop_word_removed_All_author)
    freq_list_author = type_frequency(tokenized_all_author)
    #group_author_stopped = groupby_author(freq_list_author_stopped)
    #group_author = groupby_author(freq_list_author)
    """ PART F"""
    plt.figure(1)
    plot_Zipf(group_author_stopped,normal_scale = False, stop_word_removed = True)
    plt.figure(2)
    plot_Zipf(group_author,normal_scale = True, stop_word_removed = True)
    plt.figure(3)
    plot_Zipf(group_author,normal_scale = False, stop_word_removed = False)
    plt.figure(4)
    plot_Zipf(group_author,normal_scale = True, stop_word_removed = False)
    group_free_stopped = group_freely(freq_list_author_stopped)
    group_free = group_freely(freq_list_author)
    plt.figure(1)
    plot_Zipf_v2("Dickens", group_free_stopped["Dickens"], normal_scale=False, stop_word_removed=True)
    plt.figure(2)
    plot_Zipf_v2("Tolstoy", group_free_stopped["Tolstoy"], normal_scale=False, stop_word_removed=True)
    plt.figure(3)
    plot_Zipf_v2("Smollett", group_free_stopped["Smollett"], normal_scale=False, stop_word_removed=True)
    plt.figure(4)
    plot_Zipf_v2("Dickens", group_free["Dickens"], normal_scale=False, stop_word_removed=True)
    plt.figure(5)
    plot_Zipf_v2("Tolstoy", group_free["Tolstoy"], normal_scale=False, stop_word_removed=True)
    plt.figure(6)
    plot_Zipf_v2("Smollett", group_free["Smollett"], normal_scale=False, stop_word_removed=True)

    """ PART G"""

    tokensize_Dict = tokensize_freq(tokenized_all_author, author_corpora=True)
    tokensize_Dict_stopped = tokensize_freq(stop_word_removed_All_author, author_corpora=True)
    plt.figure(1)
    plot_tokensize(tokensize_Dict,normal_scale = False, stop_word_removed = False )
    plt.figure(2)
    plot_tokensize(tokensize_Dict,normal_scale = True, stop_word_removed = False )
    plt.figure(3)
    plot_tokensize(tokensize_Dict_stopped,normal_scale = False, stop_word_removed = True )
    plt.figure(4)
    plot_tokensize(tokensize_Dict_stopped,normal_scale = True, stop_word_removed = True )

    """ PART H """
    tokensize_Dict_all = tokensize_freq(tokenized_all_author, author_corpora=False)
    tokensize_Dict_stopped_all = tokensize_freq(stop_word_removed_All_author, author_corpora=False)
    plt.figure(1)
    plot_tokensize_v2(tokensize_Dict_all, normal_scale=False, stop_word_removed=False)
    plt.figure(2)
    plot_tokensize_v2(tokensize_Dict_stopped_all, normal_scale=False, stop_word_removed=True)
    """ PART I"""
    tokensize_Dict_author = tokensize_freq(tokenized_all_author, author_corpora=True)
    tokensize_Dict_stopped_author = tokensize_freq(stop_word_removed_All_author, author_corpora=True)
    best_fit(tokensize_Dict_author,  stop_word_removed = False,theme=False, grouped = True)
    best_fit(tokensize_Dict_stopped_author, stop_word_removed = True,theme=False, grouped = True)

    best_fit(tokensize_Dict_all,  stop_word_removed = False,theme=False,grouped = False)
    best_fit(tokensize_Dict_stopped_all, stop_word_removed = True,theme=False,grouped = False )


    """ THEME BOOKS """
    by_theme_file = os.path.join(file_path, "by_theme")
    by_theme_list = os.listdir(by_theme_file)
    gutenberg_removed_all_theme = getridGutenberg(by_theme_file,by_theme_list)
    tokenized_all_theme = init_tokenization(gutenberg_removed_all_theme)
    stop_word_removed_All_theme = stop_word_removal(tokenized_all_theme)
    freq_list_theme_stopped = type_frequency(stop_word_removed_All_theme)
    freq_list_theme = type_frequency(tokenized_all_theme)
    #group_theme_stopped = groupby_author(stop_word_removed_All_theme,theme = True)
    #group_theme = groupby_author(tokenized_all_theme,theme = True)
    """ H """
    tokensize_Dict_theme_ones = tokensize_freq(tokenized_all_theme, author_corpora=False)
    tokensize_Dict_stopped_theme_ones = tokensize_freq(stop_word_removed_All_theme, author_corpora=False)
    tokensize_Dict_all_theme = tokensize_freq(tokenized_all_theme, author_corpora=False)
    tokensize_Dict_stopped_all_theme = tokensize_freq(stop_word_removed_All_theme, author_corpora=False)
    plt.figure(1)
    plot_tokensize_v2(tokensize_Dict_all_theme, normal_scale=False, stop_word_removed=False, theme=True, grouped=True)
    plt.figure(2)
    plot_tokensize_v2(tokensize_Dict_stopped_all_theme, normal_scale=False, stop_word_removed=True, theme=True, grouped=True)


    """ I """
    plt.figure(1)
    best_fit(tokensize_Dict_all_theme,  stop_word_removed = False,theme = True,grouped = False)
    plt.figure(2)
    best_fit(tokensize_Dict_stopped_all_theme, stop_word_removed = True,theme = True,grouped = False )
    best_fit(tokensize_Dict_theme_ones, stop_word_removed=False, theme=True, grouped=True)
    best_fit(tokensize_Dict_stopped_theme_ones, stop_word_removed=True, theme=True, grouped=True)

    """ PART M"""
    random_text_generator(8, 500000)
