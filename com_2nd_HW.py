my_list1 = [1,2,'a',"Hello"]
my_list2 = [1,'a',3,67]
        #index 0 1 2 3
my_list1[1]= 67
my_list2.append(89)



#Tuple
my_t1 = ('Wahid', 2001)
my_t23 = (1991, 2003)
print(my_t23[0])	#my_t23[0]='Wahid'
my_t23 = (100,1000)



#dictionary
my_dict = {
    "name" : "Wahid",
    "list" : my_list1,
    "tup" : (1,2,3)
    }
my_dict['tup']= (1,4,5)
my_dict['name']+ "Brian"


Set1 = {1,2,'a', "Hello"}
Set2 = {2,3, 'b', "Hello"}

union_set = set1 | set2
intersection_set = set1 & set2
diff_set = set1 - set2
sym_diff_set= set1 ^ set2
    print('u:', union_set)
    print('i:', intersection_set)
    print('d:', diff_set)
    print('sd:', sym_diff_set)