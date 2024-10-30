
my_dict={} # initiate empty dictionary
def lst_to_dic(): # function changing list to dictionary
    strings=['calculator','matherboard','computer','programming'] # list of strings 
    my_dict={string:len(string) for string in strings} # dictionary of string and their lenght
    print(my_dict)
lst_to_dic() # function call

