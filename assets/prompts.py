SYSTEM_PLANER_PROMPT = """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps."""


AGENT_EXECUTOR_PROMPT = "You are a helpful assistant."


SYSTEM_REPLANER_PROMPT = """**Objective**:
{input}

**Original Plan**:
{plan}

**Completed Steps**:
{past_steps}

**Instructions**:
- If there are more steps needed to achieve the objective, return a **Plan** with the remaining steps.
- If all necessary steps have been completed, return a **Response** to the user based on the information gathered.
- Do **not** include any steps that have already been completed in the new plan.
- Do **not** return an empty plan; if no further steps are needed, you **must** return a **Response**.
- Ensure your output is in the correct structured format as per the `Act` model.

**Remember**:
- The `Act` can be either a `Plan` or a `Response`.
- A `Plan` contains a list of steps that still need to be done.
- A `Response` contains the final answer to the user.

**Provide your output below:**"""
