from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import transformers
import torch
import re


# Change this file however you need to use whatever model you're using, just 
# make sure the generate function is present


# Optional: 4 bit integer quantization
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # Use NF4 for better precision than standard FP4
    bnb_4bit_use_double_quant=True,      # Quantize the quantization constants for extra VRAM savings
    bnb_4bit_compute_dtype=torch.bfloat16 # Use bfloat16 for faster computation if your GPU supports it
)

# Model ID
model_id = "google/gemma-2-9b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    quantization_config=quant_config,
    low_cpu_mem_usage=True
)

def generate(chat, max_new):
    done = False
    while not done:
        try:
            os.system("clear")
            prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
            inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
            outputs = model.generate(input_ids=inputs.to(model.device), max_new_tokens=max_new)
            done = True
        except:
            del(chat[0])
            del(chat[0])
    text = tokenizer.decode(outputs[0])
    match = re.search(r"<start_of_turn>model(.*?)<end_of_turn>", text, re.S) # This may need to change if you use a different model
    response = match.group(1).strip() if match else text
    return response
