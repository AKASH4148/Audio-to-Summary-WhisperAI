from langchain.prompts import PromptTemplate


prompt_template_summary= """
You are a management assistant with a specialization in note taking. You are taking notes for a meetoing.

Write a detailed summary of the following transcript of a meeting

{text}
make sure you don't loose important information. Be a detailed as possible in your summary

also ends with a list of:

-Main takeways
-Action items
-Decisions
-Open Questions
-next Steps

If there are any follow-up meetings, make sure to include them in the summary and mention it specifically.


Detailed summary in English
"""

PROMPT_SUMMARY= PromptTemplate(template=prompt_template_summary, input_variables=["text"])

refine_template_summary=(
    """
You are a management assistant with a specialization in note taking. You are takoing note for a meeting.
Your job is to provide detailed summary of the following transcrpit of a meeting:
We have provided an existing summary up to a certain point: {existing_answer}.
We have the opportunity to refine the existing summary(only if needed) with some more context below.

--------------
{text}
--------------
 Given the new context, refine the original summmary in English.
 If the context isn't useful, return the original summary. Make sure you are detailed in your summary.
 Make sure you don't lose any important information. Be as detailed as possible.

 Also end with a list of 

 -Main takaways
 -Action Items
 -Decisions
 -Open questions
 -Next steps

 If there are any follow up meeting, make sure  to include them in the summmary and mentioned it specifically.
"""   
)

REFINE_PROMPT_SUMMARY=PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=refine_template_summary,
)