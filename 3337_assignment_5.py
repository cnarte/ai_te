#%%
!pip install chatterbot
!pip install chatterbot_cohhrpus
#%%
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#%%
chatbot=ChatBot('assignment bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
exit_words = ["Goodbye",
"bye",
"bye-bye",
"quit",
"stop",
"end",
"adios",
"au revoir",
"bbye",
"talk to you later",
]
#%%
while True:
  query  = input()
  response = chatbot.get_response(query)
  for i in exit_words:
    if query.find(i) != -1:
      print("have a good day")
      break
  else:
    print(response)
# %%
