class Solution():
    def romanToInt(self, s):
        letter_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        explation = []
        result = 0
        for letter in reversed(s):
            last_state = None
            explation_len = len(explation)
            if explation_len != 0:
                last_state = explation[-1]
            if last_state is None:
                explation.append(letter)
            else:
                if letter_map[explation[-1][-1]] <= letter_map[letter]:
                    explation.append(letter)
                else:
                    current_word = explation[-1]
                    current_word_len = len(current_word)
                    for i, current_letter in enumerate(current_word):
                        if letter_map[letter] <= letter_map[current_letter]:
                            if i == 0:
                                current_word = letter + current_word
                                break
                            current_word = current_word[0:i] + \
                                letter+current_word[i+1:]
                        else:
                            if current_word_len == i - 1:
                                current_word = current_word + letter

                    explation[-1] = current_word

        for roman_numbers in explation:
            temp_result = 0
            last_state = None
            for i, roman_number in enumerate(reversed(roman_numbers)):
                if i == 0:
                    temp_result = letter_map[roman_number]
                else:
                    temp_result -= letter_map[roman_number]

            result += temp_result

        return result
