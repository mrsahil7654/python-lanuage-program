# |write a program to fill in a letter template given below with name and data 
# letter = '''dear<|name|>
#          you are selected !
#         <|date|>


letter = '''dear
            <|name|>
            you are selected
            <|date|>'''

print(letter.replace("<|name|>","sahil").replace("<|date|>" , "24 june 2024"))