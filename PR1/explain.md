## 11. Concepts and Evaluation

### A. Intelligent Agent

An intelligent agent is a system that observes its environment through sensors, processes the information and performs suitable actions through actuators.

In this practical, the Smart Home Agent observes room temperature and human presence and decides whether cooling, heating or energy-saving mode is required.

### B. Type of Intelligent Agent

This implementation is a **Simple Rule-Based Agent with a limited internal history**.

It uses predefined conditions to decide its actions rather than learning from data.

Its decision-making process is:

1. Receive temperature and motion inputs.
2. Store the current temperature in the history list.
3. Check whether motion is detected.
4. Compare the current temperature with the target temperature.
5. Select the appropriate action.

### C. Perception and Action

- **Perception:** The agent receives current temperature and motion status.
- **Decision:** It checks predefined conditions using `if-elif-else`.
- **Action:** It displays whether the AC, heater or energy-saving mode should be activated.

### D. Internal State

The agent maintains a list called `history` that stores the last three temperature readings.

The `append()` function adds new readings, while `pop(0)` removes the oldest reading when the list exceeds three elements.

This demonstrates maintaining limited information from previous observations. However, the stored history is not currently used in decision-making.

### E. Decision-Making Logic

The agent uses the following rules:

| Condition | Decision |
|---|---|
| Motion is False | AC/Heater OFF |
| Temperature > Target + 1°C | AC ON |
| Temperature < Target - 1°C | Heater ON |
| Otherwise | Fan Only |

For example, if the target temperature is 24°C, the acceptable temperature range is 23°C to 25°C.

### F. Evaluation and Testing

Since this is a rule-based agent and does not use a trained ML model or labeled dataset, traditional ML evaluation metrics are not applicable.

Instead, we evaluate the agent by checking whether it produces the correct action for different sensor inputs.

**Test Case Evaluation Matrix:**

| Test Case | Target Temp | Current Temp | Motion | Expected Action |
|---|---:|---:|---|---|
| 1 | 24°C | 33°C | Yes | AC ON |
| 2 | 24°C | 27°C | Yes | AC ON |
| 3 | 24°C | 24.7°C | Yes | Fan Only |
| 4 | 24°C | 21°C | Yes | Heater ON |
| 5 | 24°C | 23.5°C | No | Energy Saving Mode |

**Evaluation Criteria:**

1. Correct identification of temperature conditions.
2. Correct detection of room occupancy based on motion input.
3. Correct selection of actuator actions.
4. Proper maintenance of the last three temperature readings.
5. Successful execution for multiple sensor readings.

### G. Evaluation Metrics

The following criteria can be used to evaluate the program:

- **Decision Accuracy:** Percentage of test cases in which the agent selects the expected action.
- **Response Correctness:** Whether the output matches the decision rules.
- **Energy-Saving Behavior:** Whether the agent switches off the AC/heater when no motion is detected.

Decision accuracy can be calculated as:

Decision Accuracy = (Correct Decisions / Total Test Cases) × 100

This is a simple test-case-based measure, not a trained model's classification accuracy.

### H. What Are We Actually Doing in This Practical?

We are simulating a smart home temperature controller using an intelligent agent.

We manually provide temperature and motion sensor readings. The agent processes these readings, applies predefined rules and selects an appropriate action.

The practical demonstrates how an intelligent agent perceives its environment, makes decisions and performs actions using the PEAS framework.

No physical sensors or actuators are connected; their behavior is simulated through keyboard inputs and console outputs.




## 11. Concepts and Evaluation

### A. Intelligent Agent

An intelligent agent is a system that receives information from its environment and performs suitable actions based on that information.

In this practical, the chatbot receives user selections through the keyboard and responds with predefined messages.

### B. Type of Intelligent Agent

This implementation is a **Simple Rule-Based Conversational Agent**.

It uses predefined rules and conditional statements to generate responses.

It does not use Natural Language Processing (NLP), machine learning or deep learning.

### C. Perception and Action

- **Perception:** The chatbot receives user choices using the `input()` function.
- **Decision:** It checks the selected option using `if-elif-else` statements.
- **Action:** It displays the corresponding response using the `print()` function.

For example:

1. User selects Student Information.
2. The chatbot displays the Student Menu.
3. User selects Marks.
4. The chatbot responds with "Your marks are 85%."

### D. Rule-Based Decision-Making

The chatbot follows predefined rules for different user selections.

| User Selection | Agent Response |
|---|---|
| Greetings → Hello | Hello! Nice to meet you. |
| Greetings → How are you? | I am doing great! |
| Student → Attendance | Your attendance is 92%. |
| Student → Marks | Your marks are 85%. |
| Student → Fees | Your fees are paid. |
| College → Courses | Displays available courses. |
| College → Faculty | Displays faculty information. |
| College → Library | Displays library timings. |

### E. Use of Loops and Conditional Statements

- **while True:** Repeatedly displays menus until the user exits.
- **Nested Loops:** Maintain separate submenu operations.
- **if-elif-else:** Identify the user's selection and generate responses.
- **break:** Exits a submenu or terminates the chatbot.
- **input():** Accepts user selections.
- **print():** Displays chatbot responses.

### F. Evaluation and Testing

Since the chatbot uses predefined responses and does not contain a trained ML model, traditional ML metrics such as precision, recall and F1-score are not applicable.

The chatbot is evaluated by testing different user selections and checking whether it generates the correct responses.

**Test Case Evaluation Matrix:**

| Test Case | User Input | Expected Output |
|---|---|---|
| 1 | Main Menu → Greetings → Hello | Greeting message |
| 2 | Main Menu → Greetings → Your Name | AI Chatbot response |
| 3 | Main Menu → Student → Attendance | Attendance is 92% |
| 4 | Main Menu → Student → Marks | Marks are 85% |
| 5 | Main Menu → Student → Fees | Fees are paid |
| 6 | Main Menu → College → Courses | Available courses |
| 7 | Main Menu → College → Library | Library timings |
| 8 | Main Menu → Exit | Thank you message |

**Evaluation Criteria:**

1. Correct recognition of user menu selections.
2. Correct generation of predefined responses.
3. Proper navigation between main menu and submenus.
4. Correct handling of invalid choices.
5. Successful termination when the user selects Exit.

### G. Evaluation Metrics

The following criteria can be used:

- **Response Accuracy:** Percentage of tested valid selections that produce the expected response.
- **Navigation Correctness:** Whether the chatbot correctly moves between menus.
- **Error Handling:** Whether invalid inputs are handled appropriately.
- **Task Completion:** Whether the chatbot successfully completes the selected interaction.

Response Accuracy can be calculated as:

Response Accuracy = (Correct Responses / Total Test Cases) × 100

This is a test-case-based evaluation measure, not an ML classification accuracy score.

### H. Limitations

1. The chatbot understands only predefined menu options.
2. It cannot understand natural-language questions.
3. It does not learn from previous conversations.
4. Responses are fixed and stored in the program.
5. Student information is sample data rather than dynamically retrieved information.

### I. What Are We Actually Doing in This Practical?

We are implementing a basic conversational intelligent agent.

The user interacts with the chatbot through a terminal. The chatbot receives selections, processes them using predefined rules and displays appropriate responses.

This practical demonstrates how an intelligent agent uses sensors, decision-making rules and actuators to interact with its environment through the PEAS framework.

It is a basic rule-based chatbot rather than an advanced NLP-based AI chatbot.



## 11. Concepts and Evaluation

### A. Intelligent Agent

An intelligent agent observes user preferences, processes the available information and performs suitable actions.

In this practical, the Recommendation Assistant receives the user's interests and provides recommendations for movies, books and music.

### B. Type of Intelligent Agent

This implementation is intended to demonstrate a **Rule-Based Recommendation Agent**.

It uses predefined categories and recommendations to suggest items based on user selections.

It does not demonstrate a trained machine-learning recommendation algorithm.

### C. User Preferences and Decision-Making

The assistant receives the user's interests through keyboard input.

The recommendation process consists of:

1. Displaying available categories.
2. Receiving the user's preferred category.
3. Displaying the corresponding subcategories.
4. Receiving the user's specific selection.
5. Providing recommendations based on the selected category.

### D. Recommendation Categories

The assistant provides three main categories:

| Main Category | Subcategories |
|---|---|
| Movies | Action, Comedy, Drama |
| Books | Mythology, Fiction, Motivation |
| Music | Motivational, Devotional, Party |

### E. Recommendation Examples

The demonstrated output contains the following recommendations:

| Category | Selected Interest | Recommendations |
|---|---|---|
| Books | Fiction | The Guide, Life of Pi, The Alchemist |
| Movies | Action | RRR, Pushpa: The Rise, K.G.F: Chapter 2 |
| Music | Motivational | Chak De India, Hall of Fame, Believer |

The assistant displays suggestions based on the user's selected interest.

### F. Evaluation and Testing

Since this is intended as a basic rule-based recommendation system, it does not require a trained ML model or labeled dataset.

Its behavior can be evaluated by checking whether the recommendations correspond to the selected category and subcategory.

**Test Case Evaluation Matrix:**

| Test Case | User Selection | Expected Output |
|---|---|---|
| 1 | Book → Fiction | Fiction book recommendations |
| 2 | Book → Mythology | Mythology book recommendations |
| 3 | Movie → Action | Action movie recommendations |
| 4 | Movie → Comedy | Comedy movie recommendations |
| 5 | Music → Motivational | Motivational song recommendations |
| 6 | Music → Devotional | Devotional song recommendations |

Note: The uploaded output demonstrates only Book → Fiction, Movie → Action and Music → Motivational. The remaining cases are suggested tests and require verification against the actual source code.

**Evaluation Criteria:**

1. Correct identification of the selected interest.
2. Correct selection of the corresponding subcategory.
3. Relevance of recommendations to the selected category.
4. Successful display of recommended items.
5. Proper handling of user selections.

### G. Evaluation Metrics

The following criteria can be used to evaluate the recommendation assistant:

- **Recommendation Match Rate:** Percentage of tested selections for which the system displays recommendations from the correct category.
- **Category Accuracy:** Whether the selected category is correctly identified.
- **Recommendation Relevance:** Whether the suggested items match the user's selected interest.
- **Response Correctness:** Whether the expected recommendations are displayed.

Recommendation Match Rate can be calculated as:

Recommendation Match Rate = (Correct Recommendation Outputs / Total Test Cases) × 100

This measures rule-matching behavior. It is not a standard recommendation-system ranking metric such as Precision@K or Recall@K.

### H. Difference Between Rule-Based and ML-Based Recommendation Systems

| Rule-Based System | ML-Based System |
|---|---|
| Uses predefined rules. | Learns patterns from data. |
| Recommendations are manually specified. | Recommendations are generated using learned patterns. |
| Does not require training data. | Usually requires user-item or preference data. |
| Simple to implement. | More complex to implement. |

### I. Limitations

1. Recommendations depend on predefined categories.
2. The system does not learn from user behavior.
3. It does not maintain user preference history.
4. It cannot personalize recommendations using past interactions.
5. Its recommendation quality depends on the manually specified suggestions.

### J. What Are We Actually Doing in This Practical?

We are demonstrating a simple recommendation assistant that receives user interests and provides relevant movie, book and music suggestions.

The system processes the user's selections and displays predefined recommendations.

This practical demonstrates how an intelligent agent can observe user preferences, make rule-based decisions and generate suitable outputs using the PEAS framework.

It is a basic rule-based recommendation system, not a collaborative-filtering or content-based machine-learning model.
