import openai
# from openai import OpenAI
import time
import random




class AI_Analyst:
    def __init__(self):
        self.model="gpt-3.5-turbo"


    def get_completion(self, prompt):

        openai.api_key = "<your key>"
        # messages = prompts


        # messages = [
        #     {
        #         "role": "system", 
        #         "content":"You are a cybersecurity and information security expert."
        #      },
        #     # {
        #     #     "role": "user", 
        #     #     "content": f"You will analyze the scenario based on {model_component}, which you will briefly break down step by step and straight to the point. "
        #     # },
        #     {
        #         "role": "user", 
        #         "content": f"Consider this attack goal: {attack_goal}. what is the attack goal of this scenaria: {prompt} \n Only focus on the attack goal"
        #     },

        #     {
        #         "role": "user", 
        #         "content": f"Consider this attack assets: {target_assets}. Which of them is the target of the attacker based on fact that the goal is: {prompt} \n Only produce the verifiable contents"
        #     }
            
        # ]
        # i = args[0]
        # msg = {
        #     0: f"""Consider this attack goal: {attack_goal}. what is the attack goal of this scenaria: {prompt} \n Only focus on the attack goal """,
        #     1: f"""Consider this attack assets: {target_assets}. {prompt}""",
        #     2: f"""Consider this cybersecurity solution: {prompt}. {comp}"""
        # }

        messages = [
            {
                "role": "system", 
                "content":"You are a cybersecurity and information security expert. \
                    Note: only produce the quality, professional and verifiable contents"
            },
            {
                "role": "user", 
                "content": f"{prompt}"
            },
        ]
        # ]
        #     {
        #         "role": "system", 
        #         "content":"What do you know about the incident. Also, provide solutions about the incident"
        #     },  
        # print("KKKKKKKKKKKKKK: ", prompts)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            seed=352024,
            temperature=1,
            max_tokens=1000,
            top_p=0.8,
            # logit_bias = {
            #     674: -20,  # " #"
            #     5062:-20,  # "#"
            #     9: -20,  # "*"
            #     353:-20,  # " *"
            #     334: -20,  # "**"
            #     3146:-20,  # " **"
            #     12488: -20,  # "***"
            #     17601:-20,  # " ***"
            #     74694:-40, # ```
            # },
        )
        return response.choices[0].message["content"]


    def analyse(self, prompts):
        while True:
            try:
                #print(question)
                result = self.get_completion(prompts)
                #print(result,'\n')
                # predictions.append(result)
                #print(predictions, resp_word_len)
                break
            except (openai.error.RateLimitError, openai.error.APIError, openai.error.Timeout,
                    openai.error.OpenAIError, openai.error.ServiceUnavailableError):
                delay = random.randint(2, 6)
                time.sleep(delay)
        
        return result
    

def main():
    analyst = AI_Analyst()
    input_ = input(": > ")
    response = analyst.analyse(input_)
    print("\n\nResponse: ")
    print(response)

# Entry point of the script
if __name__ == "__main__":    
    from rich.console import Console
    from rich.markdown import Markdown
    # draw_cube()
    main()