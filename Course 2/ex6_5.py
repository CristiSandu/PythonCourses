#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

index = text.find(' ')
text_end = text[index:100]
text_end = text_end.strip()
text_end_nr = float(text_end) 
print(text_end_nr)
text_end.rs