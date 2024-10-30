sentence= input("enter your sentence: ")
my_list=sentence.split() 
my_dict={}
def lst_to_dict():
    for string in my_list:
        if string not in my_dict:
            my_dict[string]=1
        else:
            my_dict[string]+=1
        
    print(my_dict)

lst_to_dict()
    