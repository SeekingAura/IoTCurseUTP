# IoTCurseUTP
IoT Course Material, from The Universidad Tecnológica de Pereira, Research Group GRANDE, Internal Call 2019-1


# Standar code
[PEP-8](https://www.python.org/dev/peps/pep-0008/)
[Naming conventions PEP-8](https://realpython.com/python-pep8/#naming-conventions)

## Vs code editor rulers
[Reference stackoverflow](https://stackoverflow.com/questions/29968499/vertical-rulers-in-visual-studio-code)
File > Preferences > Settings
```json
"[python]": {
        "editor.rulers": [
            79,
            72
        ]
    },
```


|Type|Naming Convention|Examples|
|:----:|:----|:----|
|Function|Use a lowercase word or words. Separate words by underscores to improve readability, if name have only 1 word to improve diferentiation with "Variables" should use _ at end|function_, my_function|
|Variable|Use a CamelCase but initial letter with lowercase (see about PEP8 about recomendations)|x, var, myVariable|
|Class|Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.|Model, MyClass|
|Method|Use a lowercase word or words. Separate words with underscores to improve readability, if name have only 1 word to improve diferentiation with "Variables" should use _ at end.|class_method, method_|
|Atribute|Use a lowercase single letter, word, or words. Separate words with underscores to improve readability (same as Variable). Remember inside a class should use self.attributename|x, atribute, my_atribute|
|Constant|Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.|CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT|
|Module|Use a short, lowercase word or words. Separate words with underscores to improve readability.|module.py, my_module.py|
|Package|Use a short, lowercase word or words. Do not separate words with underscores.|package, mypackage|