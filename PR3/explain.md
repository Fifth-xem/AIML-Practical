---

# 8. Conceptual Understanding and Working of the Expert System

## 8.1 Knowledge Representation

Knowledge Representation is the process of storing real-world information in a structured format that an AI system can understand and use.

In this practical, knowledge is represented using:
- **Facts:** Information already known to be true.
- **Rules:** Logical conditions used to derive new information.
- **Conclusions:** New facts generated after applying the rules.

For example:

- Fact 1: Patient has Fever.
- Fact 2: Patient has Cough.
- Rule: IF Fever AND Cough, THEN Flu.
- Conclusion: Flu.

Thus, the system represents knowledge using facts and IF-THEN rules.

## 8.2 Expert System

An Expert System is an AI-based computer program that imitates the decision-making ability of a human expert in a particular domain.

Our practical implements a simple medical expert system that uses predefined symptoms and logical rules to derive conclusions.

An expert system generally consists of:

1. **Knowledge Base:** Stores facts and rules.
2. **Inference Engine:** Applies logical rules to available facts.
3. **User Interface:** Allows users to interact with the system.

In our implementation:
- The `rules` list acts as the Knowledge Base.
- The `forward_chaining()` and `backward_chaining()` functions act as the Inference Engine.
- The initial facts and goal are predefined in the Main Program.

## 8.3 Propositional Logic

Propositional Logic is a branch of logic in which statements are represented as propositions that can have either True or False values.

In this practical, the following propositions are used:

| Symbol | Proposition |
|---|---|
| F | Fever |
| C | Cough |
| B | BodyPain |
| FL | Flu |
| V | ViralInfection |
| M | Medicine |
| S | Sneezing |
| CL | Cold |
| R | Rest |

The logical operators used are:

| Operator | Meaning | Example |
|---|---|---|
| AND (∧) | Both conditions must be true | Fever AND Cough |
| IMPLIES (→) | If the condition is true, the conclusion follows | Fever AND Cough → Flu |
| NOT (¬) | Negation of a proposition | NOT Fever |

Our program mainly uses AND and IMPLIES.

### Logical Rules Used

The knowledge base contains five rules:

1. F ∧ C → FL
2. FL ∧ B → V
3. V → M
4. S → CL
5. CL → R

For example, the first rule means that if Fever and Cough are both true, Flu can be concluded.

## 8.4 Knowledge Base and Initial Facts

The knowledge base contains all the predefined logical rules.

**Initial Facts:**

```python
facts = {"Fever", "Cough", "BodyPain"}
```

These are the facts initially provided to the expert system.

**Rules:**

| Rule No. | Conditions (Premises) | Conclusion |
|---|---|---|
| R1 | Fever AND Cough | Flu |
| R2 | Flu AND BodyPain | ViralInfection |
| R3 | ViralInfection | Medicine |
| R4 | Sneezing | Cold |
| R5 | Cold | Rest |

The system checks these rules to generate additional facts.

## 8.5 Forward Chaining Mechanism

Forward Chaining is a data-driven inference technique.

It starts with the available facts and applies rules to derive new conclusions.

### Working in Our Practical

Initial Facts:

Fever, Cough, BodyPain

| Step | Rule Applied | Conditions Satisfied | New Conclusion |
|---|---|---|---|
| 1 | R1 | Fever AND Cough | Flu |
| 2 | R2 | Flu AND BodyPain | ViralInfection |
| 3 | R3 | ViralInfection | Medicine |
| 4 | R4 | Sneezing is absent | Not executed |
| 5 | R5 | Cold is not established | Not executed |

**Final Inferred Facts:**

Fever, Cough, BodyPain, Flu, ViralInfection, Medicine.

The process continues until no new facts can be generated.

### Flow of Forward Chaining

```text
       Initial Facts
             |
             v
    Check Available Rules
             |
             v
    Are All Premises True?
             |
       +-----+-----+
       |           |
      Yes          No
       |           |
       v           |
 Add Conclusion    |
 to Facts          |
       |           |
       +-----+-----+
             |
             v
     Any New Facts?
             |
       +-----+-----+
       |           |
      Yes          No
       |           |
       v           v
   Repeat       Stop
```

## 8.6 Backward Chaining Mechanism

Backward Chaining is a goal-driven inference technique.

It starts with a specific goal and searches for rules that can prove that goal using the available facts.

### Working in Our Practical

Our predefined goal is:

```python
goal = "Medicine"
```

The system works backward through the rules.

| Step | Goal to Prove | Rule Used | Required Premises |
|---|---|---|---|
| 1 | Medicine | R3 | ViralInfection |
| 2 | ViralInfection | R2 | Flu AND BodyPain |
| 3 | Flu | R1 | Fever AND Cough |
| 4 | Fever | Known Fact | Already available |
| 5 | Cough | Known Fact | Already available |
| 6 | BodyPain | Known Fact | Already available |

Since all the required premises are available or successfully proved, the system concludes that Medicine can be proved.

### Flow of Backward Chaining

```text
        Start with Goal
               |
               v
       Is Goal a Known Fact?
               |
          +----+----+
          |         |
         Yes        No
          |         |
          v         v
       Success   Find Matching Rule
                    |
                    v
             Check All Premises
                    |
                    v
            Can All Be Proved?
                    |
               +----+----+
               |         |
              Yes        No
               |         |
               v         v
          Goal Proved  Goal Failed
```

## 8.7 Evaluation Matrices and Logical Analysis

Evaluation matrices help us understand how logical conditions affect the conclusions generated by the expert system.

### A. Truth Table for AND Operator

The AND operator returns True only when both conditions are True.

| Fever (F) | Cough (C) | F AND C | Flu |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Here:
- 1 represents True.
- 0 represents False.

According to Rule R1, Flu is concluded only when both Fever and Cough are true.

### B. Rule Evaluation Matrix

This matrix shows how each rule behaves with the initial facts and the newly inferred facts.

| Rule | Premises | Initial Status | Final Status |
|---|---|---|---|
| R1 | Fever, Cough | True | Executed |
| R2 | Flu, BodyPain | False | Executed after R1 |
| R3 | ViralInfection | False | Executed after R2 |
| R4 | Sneezing | False | Not executed |
| R5 | Cold | False | Not executed |

This demonstrates how the execution of one rule can generate facts required by another rule.

### C. Forward Chaining Evaluation Matrix

| Iteration | Available Facts | New Fact Generated |
|---|---|---|
| 0 | Fever, Cough, BodyPain | Flu |
| 1 | Fever, Cough, BodyPain, Flu | ViralInfection |
| 2 | Fever, Cough, BodyPain, Flu, ViralInfection | Medicine |
| 3 | All previous facts | No new fact |

The algorithm stops when no additional conclusions can be generated.

### D. Backward Chaining Evaluation Matrix

| Goal | Verification | Result |
|---|---|---|
| Medicine | Check ViralInfection | Proved |
| ViralInfection | Check Flu and BodyPain | Proved |
| Flu | Check Fever and Cough | Proved |
| Fever | Check initial facts | True |
| Cough | Check initial facts | True |
| BodyPain | Check initial facts | True |

Since every required condition is satisfied, the final goal Medicine is successfully proved.

**Note:** These matrices demonstrate logical rule evaluation and inference. They are not statistical performance evaluation metrics such as accuracy, precision, recall or F1-score, because this practical does not use a labelled dataset or perform predictive model training.

## 8.8 What Are We Actually Doing in This Practical?

In this practical, we are developing a simplified rule-based medical expert system.

The system is given three initial facts:

- Fever
- Cough
- BodyPain

It contains five predefined logical rules.

First, Forward Chaining uses the initial facts to derive new conclusions:

Fever + Cough → Flu

Flu + BodyPain → ViralInfection

ViralInfection → Medicine

Next, Backward Chaining starts with the goal Medicine and checks whether the required conditions can be proved from the available facts.

Both methods successfully reach the same conclusion using different reasoning approaches.

Therefore, this practical demonstrates how Artificial Intelligence can represent knowledge, apply logical rules and perform automated reasoning.

## 8.9 Important Characteristics of the Implementation

- Uses propositional logic to represent facts and rules.
- Uses a rule-based knowledge base.
- Implements both data-driven and goal-driven reasoning.
- Uses Python sets to maintain unique facts.
- Uses loops for repeated rule evaluation.
- Uses recursion in Backward Chaining.
- Uses a visited set to prevent repeated exploration of goals.
- Does not require machine learning model training or an external dataset.
- Works completely offline using Python's built-in features.

## 8.10 Final Outcome

The practical successfully demonstrates Knowledge Representation and Expert System implementation using propositional logic.

Forward Chaining derives new facts from existing information, whereas Backward Chaining verifies whether a particular goal can be established.

Both mechanisms successfully prove the goal **Medicine** using the predefined facts and rules.
