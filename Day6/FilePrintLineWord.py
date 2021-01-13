
word_count=0
line_count=0
char_count=0
with open("sample.txt",'r') as fp:
    lines=fp.readlines()
    for i in lines:
        line_count+=1
        words=i.split()
        word_count+=len(words)
        rem_line=i.strip('\n')
        

        for j in rem_line:
            
            char_count+=1
    print("No of lines Present in a file is:",line_count)
    print("No of Word present in a file:",word_count)
    print("No of char present in a file:",char_count)
    