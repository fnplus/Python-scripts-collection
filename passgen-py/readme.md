[![MasterHead](https://raw.githubusercontent.com/kunal-mahatha/passgen-py/main/KUNAL/cli-banner.gif)](https://username.github.io)

# This repository is a combination of two directories
 - CLI tool **(cli-tool)**
 - Custom Library or Module **(lib)**

#

# CLI tool **(cli-tool)**

[![MasterHead](https://raw.githubusercontent.com/kunal-mahatha/passgen-py/main/KUNAL/cli-tool/cli-banner.png)](https://username.github.io)

### Installing Dependencies

```python
pip install argparse
```
```python
pip install pyperclip
```

### About the Tool
This generates a password for your services like **Facebook, Instagram, etc.**, copy it to the **clipboard**, and stores them in a **text file** named `passwords.txt` .

To view the saved passwords [Click Here](https://github.com/kunal-mahatha/passgen-py/blob/main/KUNAL/cli-tool/passwords.txt)

### Features
 - This tool generates an user **customized** password. User can enter the Length, number of lower and upper cases characters, number of numerals and special characters.
 - After password generation it **copies** it to the clipboard, from where it can pe easily pasted anywhere.
 - It uses the **Fisher-Yates shuffle** which runs in O(n) time and also proven to be a perfect shuffle, so it takes less time with high randomness.

### Usage
 To use this :
  - Clone the Repository
  ```python3
  git clone https://github.com/kunal-mahatha/passgen-py.git
  ```
  - locate the `passgen.py`
  ```python3
  cd passgen-py/KUNAL/cli-tool
  ```
  - make a executable file of `passgen.py`
  ```python
  pyinstaller --onefile passgen.py
  ```
  - locate the `passgen` exe file
  ```python
  cd dist/passgen
  ```
  - copy the `passgen` exe file to the path variable
  ```python
  cp passgen-py/KUNAL/cli-tool/dist/passgen
  ```
  - run the `passgen` file
  ```python
passgen -s "facebook" -l 12 -sm 2 -bg 3 -nm 3 -sc 2
```
# 

| Arguments            |       Description                                                                                  |
| ---------------------|----------------------------------------------------------------------------------------------------| 
|`-s ` or `--service ` | is about the service that user want to use the password for, example **Facebook, Instagram, etc.** |
|`-l` or `--length` | is for the length of the password |
|`-sm ` or `--small `  | is for number of lowercase characters.|
|`-bg ` or `--big `    | is for number of uppercase characters.|
|`-nm ` or `--number ` | is for number of numerals.|
|`-sc ` or `--special `| is for number of special characters.|

# 


### Default values of the flags
If the user uses it without using of any flags `-s` `-l` `-sm` `-bg` `-nm` `-sc `, then it will generate a password of **8 Characters** with **2 lowercase, 2 uppercase, 2 numerals, and 2 special characters.**

| Arguments | Default Values |
|-----------|:-------:|
|`-s ` or `--service ` | Facebook |
|`-sm ` or `--small `  | 2 |
|`-bg ` or `--big `    | 2 |
|`-nm ` or `--number ` | 2 |
|`-sc ` or `--special `| 2 |

#

# Custom Library or Module **(lib)**

[![MasterHead](https://raw.githubusercontent.com/kunal-mahatha/passgen-py/main/KUNAL/lib/cli.png)](https://username.github.io)

### About the Library
This is a custom library for the random password generation.

### Locate the module
```python3
cd passgen-py/KUNAL/lib/passgen/dist
```

### Installing the module
```python
pip install passgen-1.0.0-py3-none-any.whl
```
### Importing the module
```pythom
import passgen
```

### Using the module
To use this : 
 - import the module as desribed above.
 - use it as a function by : 
 ```python3
 passgen.passgen(s, l, sm, bg, nm, sc)
 ```
 
 # 
 
| Arguments            |       Description                                                                                  |
| ---------------------|----------------------------------------------------------------------------------------------------| 
|`-s ` or `--service ` | is about the service that user want to use the password for, example **Facebook, Instagram, etc.** |  
|`-l` or `--length` | is for the length of the password |
|`-sm ` or `--small `  | is for number of lowercase characters.|
|`-bg ` or `--big `    | is for number of uppercase characters.|
|`-nm ` or `--number ` | is for number of numerals.|
|`-sc ` or `--special `| is for number of special characters.|


#

### To prevent your passwords from being hacked by social engineering, brute force or dictionary attack method, and keep your online accounts safe, you should notice that:
1. Do not use the same password, security question and answer for multiple important accounts.
2. Use a password that has at least 16 characters, use at least one number, one uppercase letter, one lowercase letter and one special symbol.
3. Do not use the names of your families, friends or pets in your passwords.
4. Do not use postcodes, house numbers, phone numbers, birthdates, ID card numbers, social security numbers, and so on in your passwords.
5. Do not use any dictionary word in your passwords. Examples of strong passwords: ePYHc~dS*)8$+V-' , qzRtC{6rXN3N\RgL , zbfUMZPE6`FC%)sZ. Examples of weak passwords: qwert12345, Gbt3fC79ZmMEFUFJ, 1234567890, 987654321, nortonpassword. 
6. Do not use two or more similar passwords which most of their characters are same, for example, ilovefreshflowersMac, ilovefreshflowersDropBox, since if one of these passwords is stolen, then it means that all of these passwords are stolen.
7. Do not use something that can be cloned( but you can't change ) as your passwords, such as your fingerprints.

# 


# 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### AUTHOR
**NAME - Kunal Mahatha**

**GitHub Profile - [Click Here](https://github.com/kunal-mahatha)**
