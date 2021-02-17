# AirBnB - clone

<div align="center"><img src="images/AirBnBConsole.gif" width="500" height="500"/>

---
<div align="left">

## Resources:books:
Read or watch:
* [cmd - module](https://docs.python.org/3.4/library/cmd.html)
* [uuid - module](https://docs.python.org/3.4/library/uuid.html)
* [Datatime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args / kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

---
<div align="left">

## Learning Objectives:bulb:
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---
<div align="center">

### [1. BaseModel](./models.base_model.py)
* Class BaseModel that defines all common attributes/methods for other classes.

### [2. Store first object](./models.file_storage.py)
* FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.

### [3. Console 0.0.1](./console.py)
* Contains the entry point of the command interpreter:
---
<div align="left">

## **How it works our console?**

```python3
Interactive mode:

$ ./console.py

  (hbnb)
```
```python3
Non-Interactive mode:

$ echo "command" | ./console.py

  (hbnb)
```
---
## **Commands**
```
-> quit - command for exit the program.

-> EOF - Command for quit the console and exit the program.

-> create - Command for create a new instance of BaseModel.

-> show - Prints the string representation of an instance based on the class name and id

-> all - Prints all string representation of all instances based or not on the class name.

-> destroy - Deletes an instance based on the class name and id.

-> update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
```
---
## **Example**

```python3
$ ./console.py

$ (hbnb) create BaseModel

$ 792b15dd-9f87-41a9-ba31-e27e70404bd7

$ (hbnb) show BaseModel 792b15dd-9f87-41a9-ba31-e27e70404bd7

 [BaseModel] (792b15dd-9f87-41a9-ba31-e27e70404bd7) {'updated_at': datetime.datetime(2021, 2, 17, 15, 51, 6, 950105), 'id': '792b15dd-9f87-41a9-ba31-e27e70404bd7', 'created_at': datetime.datetime(2021, 2, 17, 15, 51, 6, 950075)}

$ (hbnb) update BaseModel 792b15dd-9f87-41a9-ba31-e27e70404bd7 first_name "Testing"

$ (hbnb)

$ (hbnb) show BaseModel 792b15dd-9f87-41a9-ba31-e27e70404bd7

 [BaseModel] (792b15dd-9f87-41a9-ba31-e27e70404bd7) {'updated_at': datetime.datetime(2021, 2, 17, 15, 51, 6, 950105), 'id': '792b15dd-9f87-41a9-ba31-e27e70404bd7', 'created_at': datetime.datetime(2021, 2, 17, 15, 51, 6, 950075), 'first_name': '"Testing"'}

$ (hbnb) quit

$
```
----
## Authors


* **Juliana Monroy Perez** - [julianamonr03](https://github.com/julianamonr03)

<!-- Contact info -->


📫 **How to reach me:**

[<img align="center" alt="contact | Twitter" width="22px" src="https://github.com/deut-erium/deut-erium/blob/master/assets/twitter.svg" />](https://twitter.com/julianamonroy03)
[<img align="center" alt="contact | LinkedIn" width="22px" src="https://github.com/deut-erium/deut-erium/blob/master/assets/linkedin.svg" />](https://www.linkedin.com/in/juliana-monroy-5760b9199/)
[<img align="center" alt="contact | Instagram" width="22px" src="https://github.com/hargun79/hargun79/blob/master/Assets/Instagram.svg" />](https://www.instagram.com/julianamonr03/)
[<img align="center" alt="contact | Instagram" width="27px" src="https://github.com/deut-erium/deut-erium/blob/master/assets/discord.svg" />](https://discord.com/usersdeuterium#0883)


-----
* **Jose Esteban Muñoz** - [jose120918](https://github.com/jose120918)

<!-- Contact info -->

📫 **How to reach me:**


[<img align="center" alt="contact | Twitter" width="22px" src="https://github.com/deut-erium/deut-erium/blob/master/assets/twitter.svg" />](https://twitter.com/sumercealcuadra)
[<img align="center" alt="contact | LinkedIn" width="22px" src="https://github.com/deut-erium/deut-erium/blob/master/assets/linkedin.svg" />](https://www.linkedin.com/in/jose-esteban-mu%C3%B1oz-garzon/)
[<img align="center" alt="contact | Instagram" width="22px" src="https://github.com/hargun79/hargun79/blob/master/Assets/Instagram.svg" />](https://www.instagram.com/joseesteban120918/)

