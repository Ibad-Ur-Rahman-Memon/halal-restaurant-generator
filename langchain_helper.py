# langchain_helper.py
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openapi_key = os.getenv("OPENAI_API_KEY")

# Set the API key for OpenAI
os.environ["OPENAI_API_KEY"] = openapi_key

# Initialize the LLM with a moderate creativity level
llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(country):
    """
    Generates a unique Halal restaurant name and its menu items based on a selected Islamic country.
    """

    # Prompt 1: Generate restaurant name based on Islamic country theme
    prompt_template_name = PromptTemplate(
        input_variables=['country'],
        template="Imagine a new Halal restaurant inspired by {country}'s culinary heritage. Suggest a creative and elegant name for this restaurant."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Prompt 2: Generate menu items based on the generated restaurant name
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest a list of traditional halal menu items served at a restaurant named {restaurant_name}. Return the items in a comma-separated string."
    )
    menu_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine chains in a sequence
    combined_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=['country'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Run the chain with user input (Islamic country)
    response = combined_chain({'country': country})

    return response

# For local testing
if __name__ == "__main__":
    result = generate_restaurant_name_and_items("Morocco")
    print(result)
