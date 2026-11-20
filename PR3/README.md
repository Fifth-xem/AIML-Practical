# Practical No. 3: Knowledge Representation and Expert System

## 1. Aim

To develop a rule-based expert system using propositional logic and implement Forward Chaining and Backward Chaining mechanisms for intelligent decision making.

## 2. Code Explanation

### A. Rule Class

```python
class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises
        self.conclusion = conclusion
```

- A `Rule` class is created to represent logical rules.
- `premises` contains the conditions that must be satisfied.
- `conclusion` contains the result obtained when all conditions are true.
- `__init__()` initializes these values whenever a rule object is created.

### B. Knowledge Base

```python
rules = [
    Rule(["Fever", "Cough"], "Flu"),
    Rule(["Flu", "BodyPain"], "ViralInfection"),
    Rule(["ViralInfection"], "Medicine"),
    Rule(["Sneezing"], "Cold"),
    Rule(["Cold"], "Rest")
]
```

- The knowledge base stores all the rules of the expert system.
- Each rule follows IF-THEN logic.
- For example, IF Fever AND Cough are true, THEN Flu is concluded.
- These rules represent knowledge using propositional logic.

### C. Forward Chaining

```python
def forward_chaining(facts, rules):
    inferred = set(facts)

    print("\nInitial Facts:", inferred)

    changed = True

    while changed:
        changed = False

        for rule in rules:
            if all(p in inferred for p in rule.premises):
                if rule.conclusion not in inferred:
                    inferred.add(rule.conclusion)
                    print("\nRule Fired:", rule.premises, "->", rule.conclusion)
                    print("Updated Facts:", inferred)
                    changed = True

    return inferred
```

- Forward Chaining is a data-driven reasoning technique.
- It starts with the known facts and derives new conclusions using rules.
- `inferred` stores all the initial and newly derived facts.
- `while changed` repeatedly checks the rules until no new facts are generated.
- `all()` checks whether all the premises of a rule are satisfied.
- If the conditions are satisfied, the conclusion is added to the inferred facts.
- Finally, the function returns all the derived facts.

**Example:** Fever + Cough → Flu → ViralInfection → Medicine.

### D. Backward Chaining

```python
def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    if goal in facts:
        print(goal, "is a known fact.")
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for rule in rules:
        if rule.conclusion == goal:
            print("\nTrying Rule:", rule.premises, "->", rule.conclusion)

            success = True

            for premise in rule.premises:
                if not backward_chaining(premise, facts, rules, visited):
                    success = False
                    break

            if success:
                print("Goal", goal, "proved.\n")
                return True

    return False
```

- Backward Chaining is a goal-driven reasoning technique.
- It starts with a goal and checks whether it can be proved using the available facts and rules.
- `goal` represents the conclusion we want to prove.
- First, it checks whether the goal is already a known fact.
- `visited` keeps track of previously explored goals to prevent repeated exploration.
- The program searches for a rule whose conclusion matches the goal.
- It then recursively checks whether all the premises of that rule can be proved.
- If all premises are satisfied, it returns `True`; otherwise, it returns `False`.

**Example:** To prove Medicine, the system checks ViralInfection, then Flu and BodyPain, and finally Fever and Cough.

### E. Main Program

```python
facts = {"Fever", "Cough", "BodyPain"}
```

- Defines the initial facts available to the expert system.
- These facts are used by both chaining mechanisms.

```python
result = forward_chaining(facts, rules)
```

- Calls Forward Chaining and stores all the inferred facts in `result`.

```python
for fact in sorted(result):
    print(fact)
```

- Displays all the final facts in alphabetical order.

```python
goal = "Medicine"
```

- Defines Medicine as the goal that the system needs to prove.

```python
if backward_chaining(goal, facts, rules):
    print("\nGoal Achieved:", goal)
else:
    print("\nGoal Cannot be Proved")
```

- Calls Backward Chaining to check whether the goal can be achieved.
- Displays whether the goal is successfully proved.

## 3. Concepts Used

| Concept | Explanation |
|---|---|
| Knowledge Representation | Storing knowledge in the form of facts and rules. |
| Expert System | An AI system that uses stored knowledge to make decisions. |
| Propositional Logic | Represents statements that can be either True or False. |
| Rule-Based System | Uses IF-THEN rules to derive conclusions. |
| Knowledge Base | Collection of facts and logical rules. |
| Inference Engine | Applies rules to derive new conclusions. |
| Forward Chaining | Starts with facts and derives conclusions. |
| Backward Chaining | Starts with a goal and checks whether it can be proved. |
| Premises | Conditions required for a rule to execute. |
| Conclusion | Result obtained when the premises are satisfied. |
| Recursion | A function calling itself to solve a smaller subproblem. |

## 4. Difference Between Forward and Backward Chaining

| Forward Chaining | Backward Chaining |
|---|---|
| Data-driven approach. | Goal-driven approach. |
| Starts with known facts. | Starts with a goal. |
| Derives new facts using rules. | Checks rules to prove the goal. |
| Continues until no new facts are generated. | Continues until the goal is proved or cannot be proved. |
| Used to discover possible conclusions. | Used to verify a particular conclusion. |

## 5. Expected Output

The program initially takes Fever, Cough and BodyPain as facts.

**Forward Chaining derives:**
1. Flu
2. ViralInfection
3. Medicine

**Backward Chaining verifies:**
1. Flu can be proved using Fever and Cough.
2. ViralInfection can be proved using Flu and BodyPain.
3. Medicine can be proved using ViralInfection.

Final result:

```text
Goal Achieved: Medicine
```

## 6. Conclusion

The practical successfully demonstrates a rule-based expert system using propositional logic. Forward Chaining derives new facts from existing facts, whereas Backward Chaining verifies a specified goal using logical rules. Both techniques demonstrate how an expert system performs intelligent reasoning and decision making.

## 7. Dependencies and Execution

This practical uses only Python's built-in features and does not require any external Python libraries.

**Required software:**
- Python 3
- Any Python code editor or terminal

**Execution command:**

```bash
python3 Chaining.py
```

No additional Python packages are required.


facts = {"Fever", "Cough", "BodyPain"}
Rule(["Fever", "Cough"], "Flu")
