num_names = {
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine',
        '10':'ten',
        '11':'eleven',
        '12':'twelve',
        '13':'thirteen',
        '14':'fourteen',
        '15':'fifteen',
        '16':'sixteen',
        '17':'seventeen',
        '18':'eighteen',
        '19':'nineteen',
        '20':'twenty',
        '30':'thirty',
        '40':'forty',
        '50':'fifty',
        '60':'sixty',
        '70':'seventy',
        '80':'eighty',
        '90':'ninety',
        }



def num_to_words(i):
    #written for numbers from 1-1000
    digits = str(i)
    if len(digits) == 3:
        words = num_names[ digits[0] ] + 'hundred'
        if digits[1] == '0':
            if digits[2] == '0':
                return words
            else:
                words += 'and' + num_names[digits[2]]
        elif digits[1] == '1':
            words += 'and' + num_names[digits[1:]]
        else:
            words += 'and' + num_names[digits[1] + '0']
            if digits[2] != '0':
                words += num_names[digits[2]]
        return words
    elif len(digits) == 2:
        if digits[0] == '1':
            words = num_names[digits]
        else:
            words = num_names[digits[0] + '0']
            if digits[1] != '0':
                words += num_names[digits[1]]
            
    elif len(digits) == 1:
        words = num_names[ digits[0] ]
    elif len(digits) == 4:
        return 'onethousand'
    else:    
        raise ValueError

    return words

word_gen = (num_to_words(i) for i in range(1,1001))
len_gen = (len(s) for s in word_gen)

print(sum(len_gen)) 





