from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template='''
Please summarize the research paper titled "{paper_input}"with the following specification:
Explanation style : "{style_input}"
Explanation lenght : "{length_input}"
1.Mathematical Details :
    - Include relevant mathematical equation if present in paper
    - Explain the mathematical concept using simple, concise intuitive code snippets.
2. Analogies :
    - Use relatable analogy to simplify topics
If certain information is not available of paper, respond with insufficient information. Don't guess. Ensure the summary is clear , accurate and aligned with given inputs.
''' , input_variables=['paper_input','style_input','length_input'],
validate_template=True
)

template.save('template.json')