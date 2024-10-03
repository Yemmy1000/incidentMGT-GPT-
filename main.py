import pandas as pd
from rich.console import Console
from rich.markdown import Markdown
from rich import print

from IPython.display import display
from IPython.display import Markdown

from yemi_framework import *
from response_extractor import ResponseExtractor
from response_storage import ResponseStorage

from cot_logic import ChainOfThought
from ai_analyst import AI_Analyst
# from display_script import DisplayScript

# // List
# framework_component = 

# // dictionary
# breaches = 

# // dictionary
# goal_descr = 
# // dictionary
# target_assets = 

# // dictionary
# target_assets_descr = 

# // dictionary
# cybersecurity_Solution = 

# // List of Dictionary     
# cybersecurity_solution_descr = 



def draw_cube():
    lines = [
        "            *******************",
        "           *                 * *",
        "          *                 *  *",
        "         *                 *   *",
        "        *                 *    *",
        "       *******************     *",
        "       *                 *     *",
        "       *                 *     *",
        "       *                 *     *",
        "       *                 *   *",
        "       *                 * *",
        "       *******************"
    ]
    
    for line in lines:
        print(line)


def get_user_input():
    """Function to greet the user based on their input."""
    print("Tell me your security challenges, breaches, and attack scenario. ")
    # prompt = input("\> ")framework_component
    prompt_1 = "On June 28, 2024, at approximately 9:00 AM, an employee, John Smit@followers @highlight @everyoneh, received a phishing email that appeared to be from our company’s IT department. The email requested that John update his login credentials on a website that closely mimicked our internal portal. John unknowingly provided his username and password to the attackers. Within 15 minutes of the credentials being compromised, unusual activity was detected on John’s account by our security monitoring system. The attackers used John’s credentials to access confidential company data, including customer personal information and financial records."
    prompt_2 = "Maroochy Water Breach was an incident in 2000 where an adversary leveraged the local government’s wastewater control system and stolen engineering equipment to disrupt and eventually release 800,000 liters of raw sewage into the local community."
    prompt = "During Night Dragon techniques, attacker exploit public-facing application threat actors used SQL injection exploits against extranet web servers to gain access."


    return prompt


def list_to_string(lst):
    """Function to convert a list to a comma-separated string."""
    return ', '.join(map(str, lst))

def dict_values_to_string(d):
    """Function to convert dictionary values to a comma-separated string."""
    # Extract dictionary values
    values = d.values()
    # Convert values to a comma-separated string
    result = ', '.join(map(str, values))
    return result

def convert_dict_values_to_list(d):
    """
    Function to convert dictionary values to a list.
    
    Parameters:
    d (dict): The dictionary whose values are to be converted.
    
    Returns:
    list: A list of dictionary values.
    """
    markdown_text = Markdown(text)
    # Print the formatted text
    console.print(markdown_head)
    console.print(markdown_text)


def hdisplay(header):
    console = Console()
    markdown_head = Markdown(header)
    # Print the formatted text
    console.print(markdown_head)

def tdisplay(text):
    console = Console()
    markdown_text = Markdown(text)
    # Print the formatted text
    console.print(markdown_text)


def main():
    # Example usage
    draw_cube()
    cot = ChainOfThought()
    ai_analyst = AI_Analyst()
    # display = DisplayScript()
    print(cot.start_conversation())
    
    # Open the file in read mode
    with open('framework.txt', 'r') as file:
        # Read the content of the file
        content = file.read()
    # Print the content of the file
    print('\n', content)
    response = ""
    # user_input = "I have a security incident"
    user_prompt = get_user_input()
    print(cot.process_input(user_prompt, response))

    satisfy = False
    proceed = False
    i = 0

    hdisplay("""# The Attack Goals""")
    cot_prompt = cot.process_input(user_prompt, response)       #attack aim, goal, and breaches
    response = ai_analyst.analyse(cot_prompt)
    tdisplay(response)

    hdisplay("""# The Affected Assets""")
    cot_prompt = cot.process_input(user_prompt, response)       #attack assets
    response = ai_analyst.analyse(cot_prompt)
    # print(response)
    tdisplay(response)

    hdisplay("""# The Cybersecurity Solutions""")
    cot_prompt = cot.process_input(user_prompt, response)       #cybersecurity solution
    # response = ai_analyst.analyse(cot_prompt)
    # print(response)
    # print(cot_prompt)

    # count = 0
    hdisplay("""# Preventative Controls""")
    for count in range(len(Preventative_Controls)):
        myKey = list(Preventative_Controls.keys())[count]
        hdisplay(f"""# {myKey} """)
        rf_user_prompt = input(f"I want to assist to provide {myKey} for preventative controls considering  {Preventative_Controls[myKey]}, \n> More instruction?: ")
        cot_prompt = cot.preventive_control(rf_user_prompt, response, count)       #cybersecurity solution
        response = ai_analyst.analyse(cot_prompt)
        # print(response)
        tdisplay(response)


    hdisplay("""# Detective Controls""")
    for count in range(len(Detective_Controls)):
        myKey = list(Detective_Controls.keys())[count]
        hdisplay(f"""# {myKey} """)
        rf_user_prompt = input(f"I want to assist to provide {myKey} for detective controls considering  {Detective_Controls[myKey]}, \n> More instruction?: ")
        cot_prompt = cot.detective_controls(rf_user_prompt, response, count)       #cybersecurity solution
        response = ai_analyst.analyse(cot_prompt)
        # print(response)
        tdisplay(response)


    hdisplay("""# Corrective Controls""")
    for count in range(len(Corrective_Controls)):
        myKey = list(Corrective_Controls.keys())[count]
        hdisplay(f"""# {myKey} """)
        rf_user_prompt = input(f"I want to assist to provide {myKey} for corrective controls considering  {Corrective_Controls[myKey]}, \n> More instruction?: ")
        cot_prompt = cot.corrective_controls(rf_user_prompt, response, count)       #cybersecurity solution
        response = ai_analyst.analyse(cot_prompt)
        # print(response)
        tdisplay(response)


    hdisplay("""# Recovery Controls""")
    for count in range(len(Recovery_Controls)):
        myKey = list(Recovery_Controls.keys())[count]
        hdisplay(f"""# {myKey} """)
        rf_user_prompt = input(f"I want to assist to provide {myKey} for recovery controls considering  {Recovery_Controls[myKey]}, \n> More instruction?: ")
        cot_prompt = cot.recovery_controls(rf_user_prompt, response, count)       #cybersecurity solution
        response = ai_analyst.analyse(cot_prompt)
        # print(response)
        tdisplay(response)


    hdisplay("""# Risk Management""")
    for count in range(len(Risk_Management)):
        myKey = list(Risk_Management.keys())[count]
        hdisplay(f"""# {myKey} """)
        rf_user_prompt = input(f"I want to assist to provide {myKey} for risk management considering  {Risk_Management[myKey]}, \n> More instruction?: ")
        cot_prompt = cot.risk_management(rf_user_prompt, response, count)       #cybersecurity solution
        response = ai_analyst.analyse(cot_prompt)
        # print(response)
        tdisplay(response)


    hdisplay("""# The Final Thoughts""")
    rf_user_prompt = input(f"I want to assist to provide final thoughts, \n> More instruction?: ")
    cot_prompt = cot.process_input(rf_user_prompt, response)       #attack assets
    response = ai_analyst.analyse(cot_prompt)
    # print(response)
    tdisplay(response)

    #user_prompt = get_user_input()
    # print(type(prediction(get_user_input())))
    # display(list_to_string(prediction(get_user_input())))

    # satisfy = False
    # proceed = False
    # i = 0


        

# user_input = "I have a security incident"
# print(cot.process_input(user_input))
# user_input = "It's a potential breach"
# print(cot.process_input(user_input))



# Entry point of the script
if __name__ == "__main__":    
    from rich.console import Console
    from rich.markdown import Markdown
    # draw_cube()
    main()