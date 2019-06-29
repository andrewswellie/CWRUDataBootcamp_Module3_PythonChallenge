# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:08:11 2019

@author: andre
"""

#import os
#import re
#
#resource_files = os.listdir('Resources')
#
#for f in resource_files:
#    with open(os.path.join('Resources',f),'r') as data:
#        paragraph=data.read()
#    words=re.split('[^\w\']+',paragraph)
#    words=words[:-1:]
#    sentences=re.split('[.!?]\W+',paragraph)
#    num_words=len(words)
#    num_sentences=len(sentences)
#    num_letters_per_word = list()
#    for word in words:
#        num_letters_per_word.append(len(word))
#    avg_letter_count=round(sum(num_letters_per_word)/len(num_letters_per_word),2)
#    avg_sentence_length=round(num_words/num_sentences,2)
#    output_lines = list()
#    output_lines.append('Paragraph Analysis for file: '+f+'\n')
#    output_lines.append('---------------------------------------\n')
#    output_lines.append('Word Count: '+str(num_words)+'\n')
#    output_lines.append('Sentence Count: '+str(num_sentences)+'\n')
#    output_lines.append('Average Number of Letters per Word: '+str(avg_letter_count)+'\n')
#    output_lines.append('Average Sentence Length: '+str(avg_sentence_length)+'\n\n')
#    for line in output_lines:
#        print(line,end='')
#    with open('output_'+f.split('.')[0]+'.txt','w') as output_file:
#        output_file.writelines(output_lines)