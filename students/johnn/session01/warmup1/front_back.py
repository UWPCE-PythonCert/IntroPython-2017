
def front_back(string):
    string_list=list(string)
    index_last_char=len(string_list)-1
    first_char=string_list[0]
    last_char=string_list[index_last_char]
    string_list[0]=last_char
    string_list[index_last_char]=first_char
    new_string="".join(string_list)    
    return new_string

print(front_back("code"))
print(front_back("a"))
print(front_back("ab"))
