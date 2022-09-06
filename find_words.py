# Поиск имён собственных и чисел в тексте введённом пользователем, их количество повторов, 
# и вывод результата на генрерирующуюся страницу.

import sys
from collections import Counter
from jinja2 import Template

import spacy

nlp = spacy.load("en_core_web_sm")

txt_file_url = sys.argv[1]
name_of_html = sys.argv[2]

with open(txt_file_url, 'r') as f:
    text = f.readlines()

print(text)
result_text = ''
for i in text:
        result_text += i.replace('/n','')
        
doc = nlp(result_text)

persons = Counter([token.text for token in doc if token.pos_ == "PROPN"])
nums = Counter([token for token in doc if token.like_num])

result = [[persons[i], i] for i in persons] + [[nums[i], i] for i in nums]

template = Template(
        """
        <html>
                <head>
                 <style>
                
                        .container {
                                width: 600px;
                                margin-left: auto;
                                border-width: 2;
                                border-color: black;
                                }
                        .flexTableValues {
                                display: flex;
                                background-color:#E9F3FF;
                                border-width: 2;
                                border-color: black;
                                width: 200px;
                                height: 30px;
                                font-size: 1.5vw;
                                margin-left: auto;
                        }
                        .flex1 {
                                flex: 2;
                                width: 200px;
                                border-width: 2;
                                border-color: black;
                                text-align: center;
                        }

                        #flex2 {
                                flex: 2;
                                width: 200px;
                                border-width: 2;
                                border-color: black;
                                text-align: center;
                        }
                </style>
                </head>
                <body>
                        <div class="container">
                                <div class="flexTableValues">
                                        <div class="flex1">element</div><div class="flex2">quantity</div>
                                </div>
                                {% for item in result %}
                                <div class="flexTableValues">
                                        <div class="flex1">{{ item[1] }}</div><div class="flex2">{{ item[0] }}</div>
                                </div>
                                {% endfor %}
                        </div>
                </body>
        </html>
        """
        )

with open(name_of_html, 'w') as f:
        f.writelines(template.render(result=result))