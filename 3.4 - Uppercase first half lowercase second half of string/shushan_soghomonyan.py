text = input("Type your text here: ")
half_text = int(len(text)/2)

part_a = text[:half_text].upper() 
part_b = text[half_text:].lower()
 
print(part_a + part_b)

