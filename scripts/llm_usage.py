from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# Initialize the model and tokenizer (this will run only once)
class LLM:
    def __init__(self, model_name="gpt2"):
        # Load model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()  # Set the model to evaluation mode for inference

        # Move to GPU if available
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")

    def generate_response(self, input_string: str, prompt: str):
        # Concatenate input and prompt for generation
        input_text = f"{prompt} {input_string}"

        # Tokenize input text
        inputs = self.tokenizer(input_text, return_tensors="pt")

        # Move to GPU if available
        if torch.cuda.is_available():
            inputs = inputs.to("cuda")

        # Generate response using the model
        with torch.no_grad():  # Disable gradient calculation for faster inference
            output = self.model.generate(
                inputs["input_ids"],
                max_length=100,  # Adjust max_length as needed
                do_sample=True,  # Sampling for diversity in output
                top_k=50,  # Top-k sampling for efficiency
                top_p=0.95,  # Nucleus sampling (top-p) for better results
                temperature=0.7,  # Adjust temperature for response creativity
            )

        # Decode generated tokens into text
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return response


# Initialize LLM instance only once
llm_instance = LLM()


def run_llm(input_string: str, prompt: str) -> str:
    # Call the generate_response method for the given input
    return llm_instance.generate_response(input_string, prompt)


if __name__ == "__main__":
    input_string = f"""
    Context: 
    What I want you to do: 
    """
    prompt = "Sealu:"
    response = run_llm(input_string, prompt)
    print(response)
