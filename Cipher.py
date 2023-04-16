#!/usr/bin/env python3

import argparse
import sys


class Decoding:
    def __init__(self, t, lang, operation_name):
        self.original_text = t
        self.operation = operation_name
        if lang == "rus":
            self.alph = 33
            self.most_letter = 'о'
            self.lang = "rus"
            self.min_letter_up = 1040
            self.min_letter_low = 1072
            self.max_letter_up = 1071
            self.max_letter_low = 1103
        elif lang == "eng":
            self.alph = 26
            self.most_letter = 'e'
            self.lang = "eng"
            self.min_letter_up = 65
            self.min_letter_low = 97
            self.max_letter_up = 90
            self.max_letter_low = 122

    def caesar(self, shift):
        shift = int(shift)
        if self.operation == "decoding":
            shift *= -1
        text = list(self.original_text)
        for elem in range(len(text)):
            letter = text[elem]
            new_ord = ord(letter)
            if self.max_letter_up >= new_ord >= self.min_letter_up:
                new_ord += shift
                if new_ord > self.max_letter_up:
                    new_ord -= self.alph
                elif new_ord < self.min_letter_up:
                    new_ord += self.alph
            elif self.max_letter_low >= new_ord >= self.min_letter_low:
                new_ord += shift
                if new_ord > self.max_letter_low:
                    new_ord -= self.alph
                elif new_ord < self.min_letter_low:
                    new_ord += self.alph
            text[elem] = chr(new_ord)
        text = ''.join(i for i in text)
        return text

    def vigenere(self, cw):
        text = self.original_text.upper()
        text = list(text)
        cw = cw.upper()
        code_word = list(cw)
        cw_index = 0
        if self.operation == "encoding":
            for i in range(len(text)):
                if (self.min_letter_up > ord(text[i])) or (ord(text[i]) > self.max_letter_up):
                    continue
                old_letter = ord(text[i]) - self.min_letter_up
                cw_code = ord(code_word[cw_index]) - self.min_letter_up
                new_letter = (old_letter + cw_code) % self.alph + self.min_letter_up
                text[i] = chr(new_letter)
                cw_index = (cw_index + 1) % len(code_word)
        else:
            for i in range(len(text)):
                if (self.min_letter_up > ord(text[i])) or (ord(text[i]) > self.max_letter_up):
                    continue
                old_letter = ord(text[i]) - self.min_letter_up
                cw_code = ord(code_word[cw_index]) - self.min_letter_up
                new_letter = (old_letter + self.alph - cw_code) % self.alph + self.min_letter_up
                text[i] = chr(new_letter)
                cw_index = (cw_index + 1) % len(code_word)
        text = ''.join(i for i in text)
        return text

    def vernam(self, ck, tp):
        text = list(self.original_text)
        cipher_key = []
        if tp == "word_type":
            cipher_key = list(ord(i) for i in ck)
        else:
            i = 0
            while i != len(ck):
                tmp = int(ck[i:i + 8], 2)
                cipher_key.append(tmp)
                i += 8
        if self.operation == "encoding":
            for i in range(len(text)):
                number_text = ord(text[i])
                number_ans = number_text ^ cipher_key[i]
                text[i] = str(number_ans) + ' '
        else:
            for i in range(len(text)):
                number_text = bin(ord(text[i]))[2:]
                key_text = bin(cipher_key[i])[2:]
                if len(number_text) < 8:
                    number_text = "0" * (8 - len(number_text)) + number_text
                if len(key_text) < 8:
                    key_text = "0" * (8 - len(key_text)) + key_text
                ans = ''
                for j in range(8):
                    if key_text[j] == "0":
                        ans += number_text[j]
                    else:
                        ans += str((int(number_text[j]) + 1) % 2)
                text[i] = chr(int(ans, 2))
        text = ''.join(i for i in text)
        return text

    def auto_caesar(self):
        most_match = [0] * self.alph
        text = self.original_text
        for letter in text:
            new_ord = ord(letter)
            if self.max_letter_up >= new_ord >= self.min_letter_up:
                most_match[new_ord - self.min_letter_up] += 1
            elif self.max_letter_low >= new_ord >= self.min_letter_low:
                most_match[new_ord - self.min_letter_low] += 1
        index_letter = []
        maximum = max(most_match)
        for i in range(self.alph):
            if most_match[i] == maximum:
                index_letter.append(i)
        ans = []
        #print(index_letter)
        for i in range(len(index_letter)):
            shift1 = index_letter[i] - (ord(self.most_letter) - self.min_letter_up)
            shift2 = index_letter[i] - (ord(self.most_letter) - self.min_letter_low)
            ans.append(self.caesar(shift1))
            ans.append(self.caesar(shift2))
        return ans




def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", nargs='?', default="Caesar")
    parser.add_argument("-s", "--shift", nargs='?', default=0)
    parser.add_argument("-w", "--word", nargs='?', default="not given")
    parser.add_argument("-b", "--bit", nargs='?', default="not given")
    parser.add_argument("-o", "--operation", nargs='?', default="encoding")
    parser.add_argument("-t", "--tutorial", action='store_const', const=True, default=False)
    parser.add_argument("-f", "--file", nargs='?', type=argparse.FileType('r'))
    parser.add_argument("-a", "--answer", nargs='?', type=argparse.FileType('w'), default='answer.txt')
    parser.add_argument("-l", "--language", nargs='?', default="eng")
    return parser


if __name__ == "__main__":
    print("start")
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    file_answer = namespace.answer
    #print(namespace)
    if namespace.tutorial:
        tutorial_file = open('tutorial.txt', 'r')
        for line in tutorial_file.readlines():
            print(line)
        sys.exit("End of program")
    file_answer.write("Chosen cipher: {}\n".format(namespace.name))
    text = namespace.file.read()
    parameters = ''
    k_type = ''
    if namespace.name.lower() == "caesar":
        parameters = "namespace.shift"
        file_answer.write("Caesar cipher shift: {}\n".format(namespace.shift))
    elif namespace.name.lower() == "vigenere":
        parameters = "namespace.word"
        file_answer.write("Vigenere cipher code word: {}\n".format(namespace.word))
    elif namespace.name.lower() == "vernam":
        if namespace.bit == "not given":
            k_type = "word_type"
            if text[-1] == "\n":
                text = text[:-1]
            if len(namespace.word) != len(text):
                sys.exit("Error: key and text sizes are not equal")
            file_answer.write("Vernam cipher use word {}\n".format(namespace.word))
        else:
            k_type = "bit_type"
            if (len(namespace.bit) // 8) != len(text):
                sys.exit("Error: binary key and text sizes are not equal")
            file_answer.write("Vernam cipher use set of bits\n")
        parameters = "namespace.word, k_type"
    elif namespace.name.lower() == "auto_caesar":
        if namespace.operation == "encoding":
            sys.exit("No operation 'encoding' for automatic caesar")
    file_answer.write("Operating mode: {}\n".format(namespace.operation))
    file_answer.write("Text language: {}\n".format(namespace.language))
    work_object = Decoding(text, namespace.language, namespace.operation)
    x = ''
    str_tmp = "x = work_object.{}({})".format(namespace.name.lower(), parameters)
    exec(str_tmp)
    file_answer.write("_________________\n")
    if namespace.name.lower() == "auto_caesar":
        for i in range(len(x)):
            file_answer.write("Answer " + str(i + 1) + " is: " + str(x[i]) + '\n')
        sys.exit("End of program")
    file_answer.write("Answer:\n")
    file_answer.write(x + "\n")
    if namespace.name.lower() == "vernam" and namespace.operation == "encoding":
        file_answer.write("in letters:\n")
        for i in x.split():
            file_answer.write(chr(int(i)))
        file_answer.write('\n')
    print("End of program")



