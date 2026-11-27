# Day 3 – ReCraft AI

## Prompt Engineering and Evaluation

### Objective
To customize the SYSTEM prompt for ReCraft AI, test customer questions, improve the prompt, and evaluate the chatbot's responses.

### Tasks Completed

**1. SYSTEM Prompt Customization**
- Created a SYSTEM prompt for ReCraft AI.
- Defined the chatbot's role as a recycling and upcycling assistant.
- Added instructions to provide simple, safe, and useful recycling ideas.

**2. Customer Question Testing**
- Created `tests.csv` containing 10 customer questions.
- Added expected keywords (`must_include`) for each question.
- Tested chatbot responses and calculated the pass rate.

**3. Prompt Improvement**
- Improved the SYSTEM prompt to provide practical ideas and clear steps.
- Original prompt pass rate: **80%**
- Improved prompt pass rate: **70%**

**4. Temperature Experiment**
- Set the model temperature to `1.0`.
- Executed the tests twice.

| Run | Pass Rate |
|---|---:|
| Run 1 | 80% |
| Run 2 | 80% |

**Observation:** Both runs produced the same pass rate.

**5. Business Task Classification**

| Business Task | Classification |
|---|---|
| Classify waste materials | One LLM Call |
| Look up predefined reuse ideas | Plain Code |
| Understand user goals and guide recycling tasks | Agent |

**6. Python Functions**
Created two Python functions with type hints and docstrings:
- `get_reuse_ideas(waste_material: str) -> list[str]`
- `is_safe_for_diy(waste_material: str) -> bool`

### Files Included
- `task.py` – Day 3 Python implementation.
- `tests.csv` – Customer questions and expected keywords.
- `README.md` – Day 3 task documentation.

### Conclusion
Completed the Day 3 activities, including prompt customization, chatbot testing, prompt improvement, temperature experimentation, task classification, and Python functions.
