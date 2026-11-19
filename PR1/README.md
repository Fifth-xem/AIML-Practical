# AIML Practical No. 1: Intelligent Agents and PEAS Representation

## 1. Aim

To design and implement a simple intelligent agent for a real-world application (Smart Home Controller) and demonstrate its PEAS representation and agent behavior.

## 2. Practical Overview

In this practical, we implement a Smart Home Agent that controls room temperature based on temperature and motion detection inputs.

The agent takes the desired room temperature and current sensor readings as input. Based on these readings, it decides whether to turn ON the AC, turn ON the heater, or switch to energy-saving mode.

It also maintains a history of the last three temperature readings.

## 3. PEAS Representation

PEAS stands for Performance Measure, Environment, Actuators and Sensors. It describes the working environment of an intelligent agent.

| Component | Description |
|---|---|
| Performance Measure | Maintain comfortable room temperature and save electricity. |
| Environment | Room or smart home. |
| Actuators | Air Conditioner (AC), Heater and Fan. |
| Sensors | Temperature Sensor and Motion Sensor. |

### Working of PEAS

- **Performance Measure:** The agent tries to maintain the desired temperature while saving energy when nobody is present.
- **Environment:** The room in which the temperature and human presence are monitored.
- **Actuators:** The agent selects an action such as cooling, heating or switching off the AC/heater.
- **Sensors:** The temperature sensor provides current temperature, while the motion sensor detects whether someone is present in the room.

## 4. Code Explanation

### A. Creating the Smart Home Agent Class

`class SmartHomeAgent:`

This defines a class named `SmartHomeAgent` that contains the agent's data and decision-making functions.

### B. Constructor (`__init__`)

`def __init__(self, target_temp=21.0):`

- Initializes the agent.
- `target_temp` stores the desired room temperature.
- Its default value is 21°C.
- `self.history = []` creates an empty list to store recent temperature readings.

The `self` keyword refers to the current object of the class.

### C. Perceive Function

`def perceive(self, current_temp, motion_detected):`

This function receives information from the sensors.

- `current_temp` represents the current room temperature.
- `motion_detected` indicates whether someone is present in the room.
- `self.history.append(current_temp)` adds the current temperature to the history list.

The following condition maintains only the last three readings:

```python
if len(self.history) > 3:
    self.history.pop(0)
```

If the list contains more than three readings, `pop(0)` removes the oldest reading.

Finally, the function calls `decide_action()` to determine the appropriate action.

### D. Decide Action Function

`def decide_action(self, current_temp, motion_detected):`

This is the main decision-making function of the agent.

It uses conditional statements to select an action based on sensor inputs.

**Decision rules:**

| Condition | Action |
|---|---|
| No motion detected | Turn OFF AC/Heater (Energy Saving Mode) |
| Temperature > Target + 1°C | Turn ON AC (Cooling) |
| Temperature < Target - 1°C | Turn ON Heater (Heating) |
| Otherwise | Temperature is Optimal. Fan Only. |

The `if-elif-else` statements allow the agent to select one appropriate action.

The `return action` statement sends the selected action back to the calling function.

### E. Taking User Input

```python
print("========= SMART HOME AGENT =========")

target = float(input("Enter Target Temperature (°C): "))
agent = SmartHomeAgent(target_temp=target)

n = int(input("How many sensor readings do you want to enter? "))
```

- `input()` accepts information from the user.
- `float()` converts the target temperature into a decimal number.
- An object of the SmartHomeAgent class is created using the entered target temperature.
- `n` stores the number of sensor readings.

### F. Processing Sensor Readings

```python
for i in range(n):
```

This loop executes according to the number of sensor readings entered by the user.

For every reading:

```python
current_temp = float(input("Enter Current Temperature (°C): "))
motion = input("Is Motion Detected? (yes/no): ").strip().lower()
```

- The current temperature is entered by the user.
- `strip()` removes unnecessary spaces.
- `lower()` converts the input into lowercase.

The following condition converts the motion input into a Boolean value:

```python
if motion == "yes":
    motion_detected = True
else:
    motion_detected = False
```

Here, `True` means motion is detected, and `False` means no motion is detected.

### G. Agent Decision and Output

```python
action = agent.perceive(current_temp, motion_detected)
```

This sends the sensor readings to the agent. The agent processes the inputs and returns the appropriate action.

The output is displayed using:

```python
print(f"Sensors -> Temperature : {current_temp}°C")
print(f"Sensors -> Motion     : {motion_detected}")
print(f"Actuator -> {action}")
```

The `f` before the string is called an f-string. It allows variables to be displayed directly inside a string.

### H. Displaying Internal History

```python
print(f"Internal Model (Last 3 Temps): {agent.history}")
```

This displays the last three temperature readings stored by the agent.

It demonstrates how the agent maintains a limited internal record of previous sensor readings.

**Note:** The temperature history is stored for demonstration purposes. The current decision-making function uses the current temperature and motion status, not the stored history.

## 5. Agent Behavior

The agent follows these rules:

1. If nobody is present in the room, it switches to energy-saving mode.
2. If the room temperature is more than 1°C above the target temperature, it turns ON the AC.
3. If the room temperature is more than 1°C below the target temperature, it turns ON the heater.
4. If the temperature is within the acceptable range, it selects the fan-only action.

For example, if the target temperature is 24°C:

| Current Temperature | Motion | Agent Action |
|---|---|---|
| 33°C | Yes | Turn ON AC |
| 27°C | Yes | Turn ON AC |
| 24.7°C | Yes | Fan Only |
| 21°C | Yes | Turn ON Heater |
| 23.5°C | No | Energy Saving Mode |

## 6. Important Concepts Used

| Concept | Meaning |
|---|---|
| Intelligent Agent | An entity that observes its environment and takes actions. |
| Percept | Information received by an agent through sensors. |
| Sensors | Devices or inputs used to collect environmental information. |
| Actuators | Components through which an agent performs actions. |
| Agent Function | Maps percepts to appropriate actions. |
| Internal State | Information maintained from previous observations. |
| Rule-Based Agent | An agent that selects actions using predefined rules. |
| Boolean Values | `True` and `False` values representing motion status. |

## 7. Execution Requirements

### Software Requirements

- Python 3
- Any Python editor or terminal (VS Code, IDLE or Ubuntu Terminal)

### Python Libraries

This practical uses only Python's built-in functionality:

- `input()`
- `print()`
- `float()`
- `int()`
- `len()`
- Lists
- Conditional statements
- Loops
- Classes and objects

No external Python libraries are required.

## 8. Running the Practical on Ubuntu

First, check whether Python 3 is installed:

```bash
python3 --version
```

If Python 3 is not installed, install it using:

```bash
sudo apt update
sudo apt install python3
```

No additional Python packages or dependencies need to be downloaded.

Navigate to the folder containing the practical:

```bash
cd ~/Desktop
```

If your Python file is named `smart_home.py`, execute:

```bash
python3 smart_home.py
```

Alternatively, if the file is in another directory, navigate to that directory before executing the command.

## 9. Internet and Offline Requirements

This practical does not require an internet connection.

- It does not use any online APIs.
- It does not download datasets.
- It does not use external libraries.
- It does not require a database.
- All inputs are entered manually by the user.
- All decisions are performed locally using Python conditional statements.

Therefore, the complete program can run without internet access, provided Python 3 is installed on the system.

**Hardware Note:** This implementation is a software simulation. It accepts simulated sensor readings through keyboard input and displays simulated actuator actions through the console. It does not physically control an AC, heater, fan or actual sensors.

## 10. Result

The Smart Home Intelligent Agent was successfully implemented using Python. It receives temperature and motion inputs, makes decisions using predefined rules, performs simulated actuator actions and maintains the history of the last three temperature readings. The PEAS representation of the intelligent agent was also demonstrated successfully.



# AIML Practical No. 1: Intelligent Agents and PEAS Representation – AI Chatbot

## 1. Aim

To design and implement a simple intelligent agent using an AI Chatbot and demonstrate its PEAS representation and agent behavior.

## 2. Practical Overview

In this practical, we implement a simple menu-driven AI chatbot using Python.

The chatbot interacts with users and provides predefined responses related to greetings, student information and college information.

It accepts user choices, processes them using conditional statements and displays appropriate responses.

## 3. PEAS Representation

| Component | Description |
|---|---|
| Performance Measure | Provide correct responses to user selections and maintain smooth interaction. |
| Environment | User interacting with the chatbot through a terminal. |
| Actuators | Displaying chatbot responses using the console. |
| Sensors | Keyboard input received from the user. |

### Working of PEAS

- **Performance Measure:** The chatbot should respond correctly to the selected options.
- **Environment:** The environment consists of the user and the terminal interface.
- **Actuators:** The chatbot displays messages and information using `print()`.
- **Sensors:** The chatbot receives user choices through `input()`.

## 4. Code Explanation

### A. Defining the Chatbot Function

```python
def chatbot():
```

This defines a function named `chatbot()` that contains the complete chatbot program.

### B. Displaying the Welcome Message

```python
print("=== Welcome to AI Chatbot ===")
```

Displays a welcome message when the chatbot starts.

### C. Creating the Main Menu

```python
while True:
    print("\nMain Menu")
    print("1. Greetings")
    print("2. Student Information")
    print("3. College Information")
    print("4. Exit")
```

- `while True` creates an infinite loop.
- The menu is repeatedly displayed until the user selects Exit.
- The user can choose between greetings, student information, college information and exit.

### D. Accepting User Input

```python
choice = input("Enter your choice: ")
```

The `input()` function accepts the user's selection as a string.

### E. Greetings Section

```python
if choice == "1":
```

If the user selects option 1, the greetings submenu is displayed.

It provides three predefined responses:

- Hello – Displays a greeting.
- How are you? – Displays the chatbot's status.
- Your Name – Displays the chatbot's name.

A nested `while True` loop keeps the greetings submenu active.

If the user selects option 4, the `break` statement exits the submenu and returns to the main menu.

### F. Student Information Section

```python
elif choice == "2":
```

If the user selects option 2, the student information submenu is displayed.

It provides three options:

| Option | Chatbot Response |
|---|---|
| Attendance | Your attendance is 92%. |
| Marks | Your marks are 85%. |
| Fees | Your fees are paid. |

The chatbot uses `if-elif-else` statements to identify the selected option and display the corresponding response.

Option 4 takes the user back to the main menu.

### G. College Information Section

```python
elif choice == "3":
```

If the user selects option 3, the college information submenu is displayed.

It provides information about:

- Courses: B.Tech, BCA, MBA and MCA.
- Faculty: Information about experienced faculty.
- Library: Library timings from 9 AM to 6 PM.

The chatbot displays the appropriate information based on the user's selection.

### H. Exit and Invalid Choices

```python
elif choice == "4":
    print("Thank you!")
    break
```

If the user selects option 4, the chatbot displays a thank-you message and terminates the main loop.

The `else` statement handles invalid main menu choices and displays an error message.

Similar invalid-choice handling is provided inside the submenus.

### I. Calling the Function

```python
chatbot()
```

This calls the chatbot function and starts program execution.

## 5. Agent Behavior

The chatbot follows predefined rules:

1. It displays the main menu.
2. It receives the user's selection.
3. It identifies the selected category.
4. It displays the corresponding submenu.
5. It accepts another selection and generates a predefined response.
6. It returns to the main menu or exits when requested.

## 6. Important Concepts Used

| Concept | Meaning |
|---|---|
| Intelligent Agent | A system that receives inputs and produces appropriate actions. |
| Rule-Based Agent | An agent that follows predefined rules to select responses. |
| Sensors | Keyboard inputs received from the user. |
| Actuators | Console messages displayed by the chatbot. |
| `input()` | Accepts user input. |
| `print()` | Displays messages. |
| `if-elif-else` | Performs decision-making. |
| `while True` | Repeats menu execution. |
| `break` | Terminates a loop. |
| Nested Loops | Loops placed inside another loop, used for submenus. |
| Function | A reusable block of code that performs a task. |

## 7. Execution Requirements

### Software Requirements

- Python 3
- Ubuntu Terminal or any Python editor.

### Python Libraries

This program uses only built-in Python functionality.

No external libraries or packages are required.

## 8. Running the Practical on Ubuntu

Check Python installation:

```bash
python3 --version
```

Install Python 3 if it is missing:

```bash
sudo apt update
sudo apt install python3
```

Navigate to the practical directory:

```bash
cd ~/Desktop
```

Run the program (assuming the filename is `chatbot.py`):

```bash
python3 chatbot.py
```

## 9. Internet and Offline Requirements

This chatbot works completely offline.

- It does not use online APIs.
- It does not require an internet connection.
- It does not require datasets.
- It does not use external Python libraries.
- All responses are predefined inside the program.

Therefore, the program can run on college Ubuntu systems without internet access, provided Python 3 is installed.

## 10. Result

The AI Chatbot was successfully implemented using Python. It accepts user selections, processes them using conditional statements and provides predefined responses related to greetings, student information and college information. Its PEAS representation and rule-based agent behavior were demonstrated successfully.
