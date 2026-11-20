
# AIML Practicals – Python Setup and Execution Guide

This repository contains Artificial Intelligence and Machine Learning laboratory practicals implemented using Python.

This guide explains how to install the required dependencies and execute the practicals using:

1. Ubuntu Terminal
2. Visual Studio Code (VS Code)
3. Spyder IDE

It also includes GitHub setup, dataset preparation and troubleshooting instructions.

---

# 1. System Requirements

Recommended environment:

- Operating System: Ubuntu Linux (64-bit)
- Python: 3.8
- Package Manager: Conda
- Code Editor: VS Code
- Python IDE: Spyder 5.5.1
- Version Control: Git

IMPORTANT:
Some college computers may use older Ubuntu versions such as Ubuntu 14.04 with Python 3.4.3.

Do not replace or modify the system Python installation. Use a separate Conda environment for AIML practicals.

# 2. Required Python Libraries

| Library | Purpose |
|---|---|
| NumPy | Numerical calculations and array operations |
| Pandas | Dataset loading and data manipulation |
| Matplotlib | Data visualization and graphs |
| Seaborn | Statistical data visualization |
| SciPy | Scientific computing and hierarchical clustering |
| Scikit-learn | Machine learning algorithms and evaluation |
| Spyder | Python development environment |

# 3. Installation on Ubuntu

## Step 1: Open Terminal

Press:

Ctrl + Alt + T

Check the system configuration:

```bash
lsb_release -a
python3 --version
uname -m
```

## Step 2: Install Basic Utilities

```bash
sudo apt-get update

sudo apt-get install -y wget curl git bzip2 ca-certificates
```

If Ubuntu 14.04 repositories are unavailable, resolve the archived repository issue before proceeding. Do not replace the system Python.

## Step 3: Download Miniconda

```bash
cd ~

wget https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh
```

Run the installer:

```bash
bash Miniconda3-py38_23.3.1-0-Linux-x86_64.sh
```

Installation instructions:

1. Press Enter to read the license.
2. Press Q to finish reading.
3. Type yes to accept.
4. Press Enter to accept the default installation directory.
5. Type yes when asked to initialize Conda.

Close and reopen Terminal.

Activate Conda:

```bash
source ~/miniconda3/bin/activate
```

Check installation:

```bash
conda --version
```

## Step 4: Create AIML Environment

```bash
conda create -n aiml python=3.8 -y
```

Activate the environment:

```bash
conda activate aiml
```

Check Python:

```bash
python --version
```

Expected version:

Python 3.8.x

IMPORTANT:

Activate this environment whenever you start working on AIML practicals.

```bash
conda activate aiml
```

## Step 5: Install Required Dependencies

Install a compatible pip version:

```bash
python -m pip install "pip==24.3.1"
```

Install NumPy:

```bash
python -m pip install numpy==1.24.4
```

Install Pandas:

```bash
python -m pip install pandas==2.0.3
```

Install Matplotlib:

```bash
python -m pip install matplotlib==3.7.5
```

Install Seaborn:

```bash
python -m pip install seaborn==0.13.2
```

Install SciPy:

```bash
python -m pip install scipy==1.10.1
```

Install Scikit-learn:

```bash
python -m pip install scikit-learn==1.3.2
```

Install Spyder:

```bash
python -m pip install spyder==5.5.1
```

Install Jupyter and IPython kernel support:

```bash
python -m pip install jupyter ipykernel
```

## Step 6: Verify Dependencies

Run:

```bash
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import matplotlib; print('Matplotlib:', matplotlib.__version__)"
python -c "import seaborn; print('Seaborn:', seaborn.__version__)"
python -c "import scipy; print('SciPy:', scipy.__version__)"
python -c "import sklearn; print('Scikit-learn:', sklearn.__version__)"
```

Check Spyder:

```bash
spyder --version
```

If all commands execute without errors, the required dependencies are installed.

---

# 4. Method 1 – Running Practicals Using Ubuntu Terminal

## Step 1: Open Terminal

Press:

Ctrl + Alt + T

## Step 2: Activate AIML Environment

```bash
conda activate aiml
```

## Step 3: Navigate to the Practical Folder

Example:

```bash
cd ~/AIML-Practicals/PR4
```

## Step 4: View Available Files

```bash
ls
```

Example:

```text
AIML_PR4.py
heart.csv
README.md
```

## Step 5: Execute Python Program

```bash
python AIML_PR4.py
```

Replace the filename with the required practical's Python filename.

Examples:

```bash
python AIML_PR4.py
python AIML_PR5.py
python AIML_PR6.py
python AIML_PR7.py
python AIML_PR8.py
python AIML_PR9.py
```

## Useful Terminal Commands

| Command | Description |
|---|---|
| pwd | Display current directory |
| ls | List files |
| cd foldername | Open a folder |
| cd .. | Move one directory back |
| clear | Clear terminal |
| python filename.py | Execute Python program |
| conda activate aiml | Activate environment |
| conda deactivate | Deactivate environment |

---

# 5. Method 2 – Running Practicals Using VS Code

## Step 1: Open VS Code

If VS Code is installed:

```bash
code
```

Alternatively, open it from the Applications menu.

NOTE: Modern VS Code releases may not support Ubuntu 14.04. Use an already working compatible installation.

## Step 2: Open Practical Folder

1. Open VS Code.
2. Click File.
3. Select Open Folder.
4. Navigate to AIML-Practicals.
5. Select the required practical folder or main repository folder.

## Step 3: Install Python Extension

1. Open Extensions.
2. Search for Python.
3. Install the Microsoft Python extension if compatible with your VS Code version.

## Step 4: Select Python Interpreter

Press:

Ctrl + Shift + P

Search for:

Python: Select Interpreter

Select the Conda environment.

If it is not listed, select Enter Interpreter Path and provide:

```text
/home/USERNAME/miniconda3/envs/aiml/bin/python
```

Replace USERNAME with your Ubuntu username.

## Step 5: Open Python File

Example:

```text
PR4/AIML_PR4.py
```

## Step 6: Execute Program

Option 1:

Click the Run Python File button in the upper-right corner.

Option 2:

Open Terminal inside VS Code:

Terminal -> New Terminal

Execute:

```bash
conda activate aiml
cd ~/AIML-Practicals/PR4
python AIML_PR4.py
```

The output and errors will appear in the integrated terminal.

---

# 6. Method 3 – Running Practicals Using Spyder IDE

Spyder is an Integrated Development Environment designed for Python programming, scientific computing and machine learning.

It provides an editor, IPython Console, Variable Explorer and Plots panel.

## Step 1: Activate AIML Environment

Open Ubuntu Terminal:

```bash
conda activate aiml
```

## Step 2: Launch Spyder

```bash
spyder
```

Spyder should open in a separate window.

## Step 3: Understand Spyder Interface

The main sections are:

1. Editor:
   Used to write and edit Python programs.

2. IPython Console:
   Displays program output, errors and execution results.

3. Variable Explorer:
   Displays variables, NumPy arrays and Pandas DataFrames.

4. Plots:
   Displays graphs generated using Matplotlib and other visualization libraries.

## Step 4: Open Practical File

1. Click File.
2. Select Open.
3. Navigate to the practical folder.
4. Select the Python file.
5. Click Open.

Example:

```text
AIML-Practicals/PR7/AIML_PR7.py
```

## Step 5: Set Working Directory

This step is very important when your program loads CSV datasets.

Example:

If the program contains:

```python
data = pd.read_csv("heart.csv")
```

Spyder must use the directory containing heart.csv as its working directory.

Method 1:

1. Find the Working Directory bar.
2. Click its folder icon.
3. Select the folder containing your practical and dataset.

Method 2:

Enter the following command in IPython Console:

```python
import os
os.chdir("/home/USERNAME/AIML-Practicals/PR4")
```

Replace USERNAME with your Ubuntu username.

## Step 6: Run Python Program

There are three ways:

Method 1: Click the green Run button.

Method 2: Press F5.

Method 3: Select Run -> Run.

Recommended method: Press F5.

## Step 7: View Output

After execution:

- Printed results appear in IPython Console.
- Variables appear in Variable Explorer.
- Graphs appear in the Plots panel or separate plot windows, depending on settings.

## Step 8: Execute Another Practical

To execute another practical:

1. Click File -> Open.
2. Select the next practical's Python file.
3. Change the working directory to its folder.
4. Press F5.

## Useful Spyder Shortcuts

| Shortcut | Function |
|---|---|
| F5 | Run complete Python file |
| Ctrl + S | Save Python file |
| Ctrl + L | Clear IPython Console display |
| Ctrl + Shift + P | Command palette, where supported |

To clear previous variables:

```python
%reset -f
```

Restart Spyder after changing its Python environment.

---

# 7. Dataset Preparation

Some practicals require external CSV datasets.

Keep the required CSV files inside the corresponding practical folders.

Example:

```text
PR4/
    AIML_PR4.py
    heart.csv
    README.md

PR6/
    AIML_PR6.py
    heart.csv
    README.md

PR7/
    AIML_PR7.py
    Mall_Customers.csv
    README.md
```

Use relative paths in Python programs.

Recommended:

```python
pd.read_csv("heart.csv")
```

Avoid absolute Windows paths such as:

```python
pd.read_csv("D:/AIML/PR4/heart.csv")
```

## Dataset Notes

- Practical 4: heart.csv
- Practical 6: heart.csv
- Practical 7: Mall_Customers.csv
- Practical 5: California Housing dataset fetched through Scikit-learn.
- Practical 9: Breast Cancer Wisconsin dataset provided through Scikit-learn.

IMPORTANT:

Practical 5 may require an internet connection for its first dataset download. Run it once beforehand and verify the local dataset cache.

Practical 9 does not require an external CSV for load_breast_cancer().

Always verify the actual CSV filenames and paths used in each Python program.

---

# 8. requirements.txt

Create a file named requirements.txt in the main repository folder.

Paste:

```text
numpy==1.24.4
pandas==2.0.3
matplotlib==3.7.5
seaborn==0.13.2
scipy==1.10.1
scikit-learn==1.3.2
```

To install all dependencies together:

```bash
python -m pip install -r requirements.txt
```

Spyder is installed separately:

```bash
python -m pip install spyder==5.5.1
```

---

# 9. GitHub Setup and Upload Instructions

## Step 1: Install Git

```bash
sudo apt-get install git -y
```

Verify:

```bash
git --version
```

## Step 2: Create GitHub Repository

1. Open https://github.com/
2. Sign in.
3. Click the + icon.
4. Select New repository.
5. Repository name: AIML-Practicals
6. Add description.
7. Select Public or Private.
8. Do not initialize with another README if one already exists locally.
9. Click Create repository.

## Step 3: Navigate to Repository Folder

```bash
cd ~/AIML-Practicals
```

## Step 4: Initialize Git

```bash
git init
```

## Step 5: Configure Git Identity

Replace the example details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## Step 6: Add Files

```bash
git add .
```

## Step 7: Commit Files

```bash
git commit -m "Add AIML practicals"
```

## Step 8: Set Main Branch

```bash
git branch -M main
```

## Step 9: Connect GitHub Repository

Replace the URL with your actual repository URL:

```bash
git remote add origin https://github.com/YOUR_USERNAME/AIML-Practicals.git
```

## Step 10: Push Files to GitHub

```bash
git push -u origin main
```

Authenticate when requested using an authorized GitHub authentication method.

## Updating Repository in Future

Whenever you modify practical code:

```bash
git add .
git commit -m "Update practical codes"
git push
```

---

# 10. .gitignore

Create a file named .gitignore in the main repository folder.

Paste:

```text
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
venv/
env/
aiml_env/
.spyproject/
.DS_Store
```

Do not ignore the CSV datasets required by your programs.

Do not upload large Conda environment folders.

---

# 11. Troubleshooting

## Problem 1: Conda command not found

Run:

```bash
source ~/miniconda3/bin/activate
```

Then:

```bash
conda activate aiml
```

## Problem 2: ModuleNotFoundError

Example:

```text
ModuleNotFoundError: No module named 'pandas'
```

Solution:

```bash
conda activate aiml
python -m pip install pandas
```

Replace pandas with the missing module.

## Problem 3: CSV File Not Found

Example:

```text
FileNotFoundError: heart.csv
```

Solution:

1. Check that the CSV file exists.
2. Check its exact filename.
3. Set the working directory to the correct practical folder.
4. Use relative file paths.

Check files:

```bash
ls
```

## Problem 4: Spyder Does Not Open

Activate the environment:

```bash
conda activate aiml
```

Try:

```bash
spyder
```

Check any error displayed in Terminal.

## Problem 5: Wrong Python Interpreter in VS Code

Select:

Python: Select Interpreter

Choose:

```text
/home/USERNAME/miniconda3/envs/aiml/bin/python
```

## Problem 6: Dataset Download Error

Some Scikit-learn datasets require internet access for the first download.

Download and cache the required dataset before the practical examination.

## Problem 7: Matplotlib Graph Not Appearing

Check that the program includes:

```python
import matplotlib.pyplot as plt

plt.show()
```

In Spyder, also check the Plots pane and graphics backend settings.

---

# 12. Practical Day Quick Commands

## Terminal

```bash
conda activate aiml
cd ~/AIML-Practicals/PR4
python AIML_PR4.py
```

## VS Code

```bash
conda activate aiml
cd ~/AIML-Practicals
code .
```

Select the AIML interpreter and execute the required Python file.

## Spyder

```bash
conda activate aiml
spyder
```

Open the Python file, set the working directory and press F5.

---

# 13. Final Practical Examination Checklist

Before attending the examination, verify:

- [ ] Python environment is installed.
- [ ] Conda environment is activated successfully.
- [ ] NumPy is installed.
- [ ] Pandas is installed.
- [ ] Matplotlib is installed.
- [ ] Seaborn is installed.
- [ ] SciPy is installed.
- [ ] Scikit-learn is installed.
- [ ] Spyder opens successfully.
- [ ] VS Code opens successfully, if available.
- [ ] All practical Python files are available.
- [ ] Required CSV datasets are available.
- [ ] Practical 5 dataset is cached.
- [ ] All programs have been tested.
- [ ] GitHub repository contains the latest code.
- [ ] requirements.txt is available.

---

# 14. Important Notes

1. Always activate the AIML Conda environment before executing programs.
2. Do not modify Ubuntu's system Python.
3. Use Python 3.8 for the specified dependency versions.
4. Ensure that datasets are in the correct practical folders.
5. Check working directories when using Spyder.
6. Test programs before the final examination.
7. Keep a backup of the repository and datasets.
8. Ubuntu 14.04 is outdated. Miniconda, Spyder and other application compatibility must be tested on the actual college machine before relying on this setup.

---

# Conclusion

This setup provides a common Python environment for executing Artificial Intelligence and Machine Learning practicals through Ubuntu Terminal, Visual Studio Code and Spyder IDE.

Using a dedicated Conda environment ensures that the required Python libraries are available without modifying the system Python installation.

