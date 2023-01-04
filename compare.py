from difflib import SequenceMatcher
import argparse

# функция для сравнения строк
def compare_programs(program1, program2):
    matcher = SequenceMatcher(None, program1, program2)
    return matcher.ratio()


# парсинг аргументов с путями до файлов input.txt и scores.txt
parser = argparse.ArgumentParser()
parser.add_argument('inputFile', type=str)
parser.add_argument('scoresFile', type=str)
args = parser.parse_args()

# открытие файлов
inputFile = open(args.inputFile, mode='r', encoding='utf8')
scoresFile = open(args.scoresFile, mode='w', encoding='utf8')

# считывание строк с путями для сравниваемых файлов
filesToCompare = inputFile.readlines()
for line in filesToCompare:
    filename1, filename2 = line.split()
    file1 = open(filename1, mode='r', encoding='utf8')
    file2 = open(filename2, mode='r', encoding='utf8')
    scoresFile.write(str(compare_programs(file1.read(), file2.read()))+'\n') # запись результатов

