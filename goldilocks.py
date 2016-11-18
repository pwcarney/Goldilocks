
def choose_chairs(input):
    
    with open(input) as file:
        input_text = file.read().splitlines() 
        
    goldi_weight, goldi_temp = map(int, input_text[0].split(' '))
    input_text.pop(0)
    
    good_chairs = []
    for ind, input in enumerate(input_text):
        input_weight, input_temp = map(int, input.split(' '))
        
        if (goldi_weight < input_weight) and (goldi_temp > input_temp):
            good_chairs.append(ind+1)

    print(good_chairs)
        
        
if __name__ == "__main__":
    choose_chairs('challenge_input.txt')
