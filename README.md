# ReAct Agent Implementation



Where is None coming from?




Ok should probably add weather API call




Hmm ok in loop won't answer age raised 4th power question, breaking

- Add sorry had trouble answering
- Run in loop get working
- Change tools
- That's it
- Share notes

"""
What else could I add?
- Something relating to me
- Something with local file uploaded
- Code interpreter
- General LLM chat

Questions
- Can this handle something requring two steps?

Other things
- Needs default behavior for hitting max (how old is US hit max first time, second got right away)



Good example: how old is the united states and whats its age in days?
If you ask chat gpt, knows age, uses code interpreter math part
Simliar thing here, successful agent looks up age wikipedia and then does math

Interesting API gets that right too 

Now let's change it to age raised to 4th power - agent gets that
~ 3.5 billion - well actually only kind of. The answer returned is correct but LLM formats wrong to 354,453,529,6

Answer: The United States is approximately 244 years old, and its age raised to the 4th power is 354,453,529,6.

Now LLM completely lies
The United States is 245 years old as of 2021. 

Raising its age to the 4th power would give us:
245^4 = 282,853,250,000
245^4 is actually ~3.6 billion


Refactor this so can keep rifling off questions


Exactly the type of thing going through above would be great for notes on my website


Good linkedin header would be "whats happening when chat gpt shows little code symbol?"

Would want to change this to implement a code interpreter but same idea

And this would be great example of LLM vs LLM with tools

"""


"""
Sunday: polish this up, add notes to website, maybe add code interpreter
Angle good linkedin post

Do something on summarization too soon while fresh
Maybe autoeval tool
Maybe quick note on website
"""