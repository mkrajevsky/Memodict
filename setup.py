from openai import OpenAI
import json


class Prompter(object):
    def __init__(self):
        self.client = OpenAI(api_key='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')
        
        

    def query_gpt(self, prompt):
        response = self.client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are a interactive wikipedia designed to output JSON. For a given input describe it in terms of 5 categories for each category match 5 descriptions. Each description not longer than 8 words  The output should be formated the following way :{ categories: [{category: name of category, Descriptions : [description1, description2 ...]},  ]}"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                }
            ]
            },
           
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={"type":"json_object"}
            )
        print(response)
        response = json.loads(response.choices[0].message.content)
        print(response)
        """{'categories': [{'category': 'Definition', 'descriptions': ['The state of being alive or having life.', 'To exist or be present in a specific place or environment.', 'Engaging in various activities or experiences.', 'The condition of being functional and active.', 'Participating in ongoing events or activities.']}, {'category': 'Aspects', 'descriptions': ['Breathing and heartbeat as signs of life.', 'Cognitive functions and consciousness.', 'Biological and physiological processes.', 'Emotional and social interactions.', 'Growth and development over time.']}, {'category': 'Activities', 'descriptions': ['Daily routines such as eating and sleeping.', 'Work or professional engagements.', 'Social events and gatherings.', 'Hobbies and recreational activities.', 'Learning and educational pursuits.']}, {'category': 'Environments', 'descriptions': ['Urban and rural settings where people reside.', 'Natural environments like forests and oceans.', 'Workplaces such as offices and factories.', 'Social spaces like parks and cafes.', 'Technological environments like the internet.']}, {'category': 'Expressions', 'descriptions': ['Facial expressions and body language.', 'Spoken and written communication.', 'Artistic expressions like music and painting.', 'Physical activities like dancing and sports.', 'Virtual interactions on social media.']}]}
        """
        result =""
        i = 1
        for category in response['categories']:
            result += f"category {i} {category['category']}: \n"
            for description in category['Descriptions']:
                result += f"\t\t--{description}\n"
            result += "\n"
            i+=1
        return result