import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

mybot = ChatBot('Sci-Bot')
training = ChatterBotCorpusTrainer(mybot)
training.train("chatterbot.corpus.english.science")  #training using Science corpus

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    #config
    pass

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        while True:
            ques = input('-> ')
            if ques == "done" or "stop" or "thank you":
                print("Let me know if you need anything else")
                break

        response = mybot.get_response(ques)
        output.append(response)
        
    return SimpleText(dict(text=output))

