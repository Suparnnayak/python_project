from difflib import SequenceMatcher
with open ('ex1.txt') as one_file,open('ex3.txt') as two_file:
    data_file1=one_file.read()
    data_file2=two_file.read()
    matches=SequenceMatcher(None,data_file1,data_file2).ratio()
    print(f"The percentage plagiarized content is {matches*100}%")
    # HERE WE CAN OBSERVE PERCENTAGE OF PLAGARISM BETWEEN ex1 FILE with ex2 FILE & ex3 FILE.