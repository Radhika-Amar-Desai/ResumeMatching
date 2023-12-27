import os
from langchain.document_loaders import PyPDFLoader

os.environ["OPENAI_API_KEY"] = "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"

pdf_loader = PyPDFLoader('./docs/RachelGreenCV.pdf')
documents = pdf_loader.load()

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# we are specifying that OpenAI is the LLM that we want to use in our chain
chain = load_qa_chain(llm=OpenAI())
query = """
Rate this person's compatability for a job with the following job description : 
Rate from 0 to 10
**Position:** Creative Content Developer

**Location:** Anywhere

**Job Type:** Full-time

**Company:** InnovateTech Solutions

**About Us:**
At InnovateTech Solutions, we are on a mission to redefine the way people experience technology. We believe in pushing boundaries, embracing creativity, and fostering a collaborative environment where ideas come to life. If you're passionate about technology, innovation, and love turning ideas into compelling content, we want you on our team!

**Job Description:**

As a Creative Content Developer, you will be a key player in shaping the narrative of our brand and products. You'll work closely with cross-functional teams to create engaging and impactful content that resonates with our audience. Your creativity will be instrumental in developing a strong online presence and driving brand awareness.

**Responsibilities:**

- Develop creative and compelling content for various platforms, including website, social media, blogs, and marketing materials.
- Collaborate with marketing, design, and product teams to ensure consistent messaging and brand voice.
- Conduct research to stay updated on industry trends and incorporate relevant insights into content creation.
- Craft clear and concise copy that communicates complex ideas in an easy-to-understand manner.
- Edit and proofread content to ensure accuracy, consistency, and adherence to brand guidelines.
- Stay informed about the competitive landscape and suggest strategies to differentiate our content.

**Requirements:**

- Proven experience as a content developer or similar role.
- Strong portfolio showcasing a variety of creative content (written, visual, multimedia).
- Excellent written and verbal communication skills.
- Ability to work in a fast-paced environment and meet tight deadlines.
- Familiarity with technology and a keen interest in staying updated on industry trends.
- Attention to detail and a passion for storytelling.

**How to Apply:**
If you're excited about the prospect of contributing to a dynamic and innovative team, please submit your resume, portfolio, and a cover letter explaining why you're the perfect fit for this role to careers@innovatetech.com. Use the subject line "Creative Content Developer Application - [Your Name]".

InnovateTech Solutions is an equal opportunity employer. We encourage candidates from all backgrounds to apply. We can't wait to see your creativity in action!
"""
response = chain.run(input_documents=documents, question=query)
print(response) 