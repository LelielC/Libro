#!/usr/bin/env python
# coding: utf-8

# # Encuesta

# In[1]:


from metakernel import register_ipython_magics
register_ipython_magics()


# In[2]:



get_ipython().run_cell_magic('activity', '', '\n\n{"activity": "poll",\n "instructors": ["dblank"],\n "items": [\n      {"id": "1", \n       "question":  """Which of the following will print "Hello" 5 times without errors?""", \n       "type": "multiple choice",\n       "options": [\n"""<pre style="width: 600px">\nfor (int i=0; i < 5; i++) {\n    println("Hello");\n}\n</pre>""",\n"""<pre style="width: 600px">\nprintln("Hello");\nprintln("Hello");\nprintln("Hello");\nprintln("Hello");\nprintln("Hello");\n</pre>""",\n"""<pre style="width: 600px">\nint i = 0;\nwhile (i < 5) {\n    println("Hello");\n    i++;\n}\n</pre>""",\n        "All of the above",\n        "None of the above",\n    ]},\n        \n    {"id": "2", \n     "question":    """Which of the following is a function definition?""", \n     "type": "multiple choice",\n     "options":    [\n"""<pre style="width: 600px">\nvoid draw() {\n}\n</pre>""",\n"""<pre style="width: 600px">\nrect(10, 10, 50, 50);\n</pre>""",\n"""<pre style="width: 600px">\ndrawBunny(mouseX, mouseY, 50, 100);\n</pre>""",\n        "All of the above",\n        "None of the above",\n        ]},\n      {"id": "3", \n       "question":     """Which of the following has parameters?""", \n       "type": "multiple choice",\n       "options":     [\n"""<pre style="width: 600px">\nvoid draw() {\n}\n</pre>""",\n"""<pre style="width: 600px">\nvoid drawRect(float x, float y, float w, float h) {\n    rect(x, y, w, h);\n}\n</pre>""",\n"""<pre style="width: 600px">\nvoid drawBunny() {\n    rect(10, 20, 100, 150);\n}\n</pre>""",\n        "All of the above",\n        "None of the above",\n        ]},\n     {"id": "4", \n      "question":  """Which of the following is a function call?""", \n      "type": "multiple choice",\n      "options": [\n"""<pre style="width: 600px">\nvoid draw() {\n}\n</pre>""",\n"""<pre style="width: 600px">\nrect(10, 10, 50, 50);\n</pre>""",\n"""<pre style="width: 600px">\ndrawBunny(mouseX, mouseY, 50, 100);\n</pre>""",\n        "2 and 3",\n        "None of the above",\n        ]},\n    ]\n}')

