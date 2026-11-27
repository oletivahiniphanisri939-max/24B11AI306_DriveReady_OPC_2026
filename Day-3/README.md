# Day 3 – ReCraft AI | Prompt Engineering & Evaluation

## 📌 Overview

ReCraft AI is an AI-powered recycling and upcycling assistant that helps users discover creative ways to reuse everyday waste materials.

The Day 3 task focuses on prompt engineering, chatbot testing, prompt improvement, temperature experimentation, business task classification, and Python functions.

## Learning Objectives

- Customize a SYSTEM prompt for ReCraft AI.
- Create and execute 10 customer test cases.
- Evaluate chatbot responses using expected keywords.
- Improve prompts and compare testing results.
- Experiment with LLM temperature set to 1.0.
- Understand Plain Code, One LLM Call, and Agent.
- Write Python functions using type hints and docstrings.

## Technologies Used

- Python
- Google Colab
- LangChain
- Groq API
- CSV

## Task 1 – SYSTEM Prompt Customization

Created a customized SYSTEM prompt for ReCraft AI to provide:
- Creative waste reuse ideas.
- Simple and practical instructions.
- Relevant suggestions based on waste materials.
- Safety warnings whenever necessary.

##  Task 2 – Customer Testing

Created `tests.csv` containing 10 customer questions and their expected keywords.

The chatbot responses were evaluated using keyword matching.

##  Task 3 – Prompt Improvement

Improved the SYSTEM prompt with additional instructions:

1. Start with the most useful reuse idea.
2. Explain the idea in 2–3 simple steps.
3. Clearly mention the useful product.
4. Include safety warnings whenever necessary.
5. Keep suggestions relevant to the material.

### Test Results

| Prompt Version | Passed | Pass Rate |
|---|---:|---:|
| Original SYSTEM Prompt | 8/10 | 80% |
| Improved SYSTEM Prompt | 7/10 | 70% |

**Observation:** The improved prompt produced relevant and detailed responses, but the keyword-based pass rate decreased by 10 percentage points.

##  Task 4 – Temperature Experiment

Set the LLM temperature to `1.0` and executed the same 10 test cases twice.

| Experiment | Passed | Pass Rate |
|---|---:|---:|
| Run 1 | 8/10 | 80% |
| Run 2 | 8/10 | 80% |

**Observation:** Both runs achieved the same pass rate, although the generated responses varied.

## Task 5 – Business Task Classification

| Business Task | Classification |
|---|---|
| Classify waste materials as plastic, paper, metal, or glass | One LLM Call |
| Look up predefined reuse ideas for a material | Plain Code |
| Understand user goals, choose suitable tools, and guide a recycling task | Agent |

## Python Functions

Created two Python functions using type hints and docstrings:

- `get_reuse_ideas(waste_material: str) -> list[str]`
- `is_safe_for_diy(waste_material: str) -> bool`

These functions demonstrate reusable Python code and basic safety checking.

##  Project Files

| File | Description |
|---|---|
| `task.py` | Day 3 Python implementation |
| `tests.csv` | Customer test questions and expected keywords |
| `README.md` | Day 3 project documentation |

##  Conclusion

Successfully completed Day 3 activities by customizing and improving prompts, evaluating chatbot responses, experimenting with LLM temperature, classifying business tasks, and implementing Python functions.


**Focus:** Prompt Engineering, Testing & Evaluation</Writing
