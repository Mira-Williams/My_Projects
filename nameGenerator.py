# Random name generator. Function takes two arguments - how many letters you want each name to have, 
# and how many names you want listed at once.

import random


def nameGenerator(name_length, num_names):

    coin_toss = ['heads', 'tails']
    list_vowels = ['a','e','i','o','u','y']
    list_consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    weight_list_vow = [8.12, 12.02, 7.31, 7.68, 2.88, 2.11]
    weight_list_cons = [1.49, 2.71, 4.32, 2.30, 2.03, 5.92, 0.10, 0.69, 3.98, 2.61, 6.95, 1.82, 0.11, 6.02, 6.28, 9.10, 1.11, 2.09, 0.17, 0.07]
    list_names = []

    for i in range(num_names):

        letter_1 = ''
        letter_2 = ''
        letter_3 = ''
        letter_count = 1
        name = ''
        
        for i in range(name_length):
            if letter_count == (name_length + 1):
                break
            if letter_3 in list_vowels and letter_2 in list_vowels:
                letter_1 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                letter_1 = letter_1[0]
                name += letter_1
            elif letter_3 in list_consonants and letter_2 in list_consonants:
                letter_1 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                letter_1 = letter_1[0]
                name += letter_1
            else:
                coin_flip = random.choice(coin_toss)
                if coin_flip == 'heads':
                    letter_1 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                    letter_1 = letter_1[0]
                    name += letter_1
                else:
                    letter_1 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                    letter_1 = letter_1[0]
                    name += letter_1
            letter_count += 1

            if letter_count == (name_length + 1):
                break
            if letter_1 in list_vowels and letter_3 in list_vowels:
                letter_2 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                letter_2 = letter_2[0]
                name += letter_2
            elif letter_1 in list_consonants and letter_3 in list_consonants:
                letter_2 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                letter_2 = letter_2[0]
                name += letter_2
            else:
                coin_flip = random.choice(coin_toss)
                if coin_flip == 'heads':
                    letter_2 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                    letter_2 = letter_2[0]
                    name += letter_2
                else:
                    letter_2 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                    letter_2 = letter_2[0]
                    name += letter_2
            letter_count += 1

            if letter_count == (name_length + 1):
                break
            if letter_2 in list_vowels and letter_1 in list_vowels:
                letter_3 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                letter_3 = letter_3[0]
                name += letter_3
            elif letter_2 in list_consonants and letter_1 in list_consonants:
                letter_3 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                letter_3 = letter_3[0]
                name += letter_3
            else:
                coin_flip = random.choice(coin_toss)
                if coin_flip == 'heads':
                    letter_3 = random.choices(list_vowels, weights=weight_list_vow, k=1)
                    letter_3 = letter_3[0]
                    name += letter_3
                else:
                    letter_3 = random.choices(list_consonants, weights=weight_list_cons, k=1)
                    letter_3 = letter_3[0]
                    name += letter_3
            letter_count += 1    
        list_names.append(name)

    for i in range(len(list_names)):
        print(list_names[i])

nameGenerator(7,5)