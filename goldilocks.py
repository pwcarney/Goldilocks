
def choose_chairs(input):
    
    with open(input) as file:
        input_text = file.readlines()
        
    goldi_weight, goldi_temp = input_text[0].split(' ')
    input_text.pop(0)
    
    for input in input_text:
        pass
    

if __name__ == "__main__":
    choose_chairs('input.txt')
