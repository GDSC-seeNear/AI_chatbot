# SeeNear AI Chatbot

Our model was developed using Huggingface and Pytorch.  
We fine-tuned the Ko-Dialog(GPT-2) model by classifying datasets that can relate to emotions in the dataset.  


## Test Chatbot Converstaion (5 Times)

Our application provides answers for one conversation, but using the code below, we generate the appropriate answers by reflecting the previous conversation.  

If you want to use it, you can use the [model](https://huggingface.co/keonju/chat_bot) as follows.  

```python

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("keonju/chat_bot")
model = AutoModelForCausalLM.from_pretrained("keonju/chat_bot")

# Let's chat for 5 lines
for step in range(5):
     message = input("MESSAGE: ")

        if message in ["", "q"]:  # if the user doesn't wanna talk
            break

        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        
       
        # generated a response while limiting the total chat history to 1000 tokens, 
        if (trained):
            chat_history_ids = model.generate(
                bot_input_ids, 
                max_length=1000,
                pad_token_id=tokenizer.eos_token_id,  
                no_repeat_ngram_size=3,       
                do_sample=True, 
                top_k=100, 
                top_p=0.7,
                temperature = 0.8, 
            )
        else:
            chat_history_ids = model.generate(
                bot_input_ids, 
                max_length=1000, 
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3
            )

        # pretty print last ouput tokens from bot
        print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
```

- - -
</br>

# Start Guide

**Requirments**

What you need to build and run this application:   
- Python 3.10
- MySQL 8.0.26

**Installation**
```
$ git clone https://github.com/GDSC-seeNear/AI_chatbot.git
```
If Linux
```
$ sudo apt-get install git-lfs
$ git lfs install
```

If Mac Os
```
$ brew install git-lfs
$ git lfs install
```

```
$ pip install -r requirements.txt
$ git clone https://huggingface.co/keonju/chat_bot
```

**.env File**
```
SQLALCHEMY_DATABASE_URL=mysql+pymysql://{user}}:{user_password}@{Host}:{Port}/{Database}
```
**Run**
```
$ uvicorn main:app —host 0.0.0.0 --port 8080
```
</br>

- - -
### Tensorflow lite
This is a Tensorflowlite model made with Transformer structure. I only checked that it works on Python.
```python
from tensorflow.lite.python import interpreter
interpreter = tf.lite.Interpreter(model_content=tflite_model)

signatures = interpreter.get_signature_list()
interpreter.get_signature_list() # {'serving_default': {'inputs': ['sentence'], 'outputs': ['output_0']}}
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
input_details 
'''
[{'name': 'serving_default_sentence:0',
  'index': 0,
  'shape': array([], dtype=int32),
  'shape_signature': array([], dtype=int32),
  'dtype': numpy.bytes_,
  'quantization': (0.0, 0),
  'quantization_parameters': {'scales': array([], dtype=float32),
   'zero_points': array([], dtype=int32),
   'quantized_dimension': 0},
  'sparsity_parameters': {}}]
'''
output_details
'''
[{'name': 'StatefulPartitionedCall:0',
  'index': 69,
  'shape': array([], dtype=int32),
  'shape_signature': array([], dtype=int32),
  'dtype': numpy.bytes_,
  'quantization': (0.0, 0),
  'quantization_parameters': {'scales': array([], dtype=float32),
   'zero_points': array([], dtype=int32),
   'quantized_dimension': 0},
  'sparsity_parameters': {}}]
'''

# Input
input_data = "나 오늘 우울해".encode("utf-8")
input_array = np.array(input_data, dtype=np.bytes_)

# Run
interpreter.allocate_tensors()
interpreter.set_tensor(input_details[0]['index'], input_array)
interpreter.invoke()

# Ouptput
output_tensor = interpreter.get_tensor(output_details[0]['index'])
print(output_tensor.item().decode('utf-8')) # 오늘 우울한 일이 있었나봐요 .

- - -
### Reference
1. Fine-Tuned Model  
AI chatbot model fine-tuned [Ko-Dialo GPT](https://huggingface.co/byeongal/Ko-DialoGPT) for empathetic answers.  

2. Dataset    
[Korean Chatbot Dataset](https://github.com/songys/Chatbot_data)  
[Continuous Conversation Dataset with Korean Sentiment Information](https://aihub.or.kr/aihubdata/data/view.do?currMenu=120&topMenu=100&dataSetSn=271&aihubDataSe=extrldata)  
[A one-shot conversation dataset with Korean emotion information](https://aihub.or.kr/aihubdata/data/view.do?currMenu=120&topMenu=100&dataSetSn=270&aihubDataSe=extrldata)  
[Wellness Conversation Script Dataset](https://aihub.or.kr/aihubdata/data/view.do?currMenu=120&topMenu=100&dataSetSn=267&aihubDataSe=extrldata)  
