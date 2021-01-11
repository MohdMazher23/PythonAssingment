word=input("ENTER ANY WORD OR SENTENCE :\n ")
l_word=list(word.lower())

vowel=['a','e','i','o','u']
print("VOWELS PRESENT IN A GIVEN WORD IS:")
count=0
for i in l_word:
    for j in vowel:
        if i==j:
            print(i,end=" ")
            count+=1
print("\nTHE TOTAL NO OF VOWELS PRESENT IN A GIVEN WORD OR SENTENCE IS: =",count)
        
#OUTPUT
"""
ENTER ANY WORD OR SENTENCE :
 HELLO MY NAME IS MOHD MAZHER UDDIN
VOWELS PRESENT IN A GIVEN WORD IS:
e o a e i o a e u i
THE TOTAL NO OF VOWELS PRESENT IN A GIVEN WORD OR SENTENCE IS: = 10
"""
        