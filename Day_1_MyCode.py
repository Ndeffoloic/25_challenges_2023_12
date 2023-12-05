import math

day_1_input = "Day_1_Input_1.txt"
mes_chifres = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def find_first_and_last_digit(file_txt_input):
    with open(file_txt_input, 'r') as f:
        
        file_numbers_sum = 0
        for line in f:
            new_line = convert_numbers_in_letters_to_numbers_in_digits(line)
            print(new_line)
            first_digit = find_first_digit(new_line) 
            last_digit = find_last_digit(new_line) 
            line_numer = int(str(first_digit) + str(last_digit))
            file_numbers_sum += line_numer
    return file_numbers_sum

        
def find_first_digit(lineString) :
    for letter in lineString:
        if letter.isdigit() :
            return letter
            
    
    
def find_last_digit(lineString):
    inversed_line_Stream = lineString[::-1]
    return find_first_digit(inversed_line_Stream)



def convert_numbers_in_letters_to_numbers_in_digits(line):
    out_line = line
    for chiffre in mes_chifres:
        if(chiffre in line):
            out_line = out_line.replace(chiffre,chiffre + str(mes_chifres.index(chiffre)) + chiffre)
    return out_line

print(find_first_and_last_digit(day_1_input))