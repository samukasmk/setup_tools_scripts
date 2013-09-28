# setup_tools_scripts

> My way to install things with virtualenv, building your virtualenv sandbox to development and production environment. ~ @SamukaSMk

## 1. Apply in your code

#### 1.1. Put ./install in your repo folder

```bash
$ cd /tmp
$ git clone git@github.com:samukasmk/setup_tools_scripts.git

$ cp -r setup_tools_scripts/install /my/repo/folder/project
```

#### 1.2. Set in (setup.py) your app information, author:

> Note: Don't change 'install_requires' attributes

```python
setup(name='MyAppExampleWithSetupToolsScripts',
      version='1.8',
      description='Example of to build your Virtualenv with Setup Tools Scripts.',
      author='Samuel Maciel Sampaio',
      author_email='samukasmk@gmail.com',
      url='https://github.com/samukasmk/setup_tools_scripts',
      install_requires=['pip', 'virtualenv'],
     )
```

#### 1.3. Set in (setup-env.py) the packages dependencies, to install with pip: 

```python
setup(name='MyAppExampleWithSetupToolsScripts_VirtualEnv',
      version='1.0',
      description='Example of to build your Virtualenv with Setup Tools Scripts.',
      author='Samuel Maciel Sampaio',
      author_email='samukasmk@gmail.com',
      url='https://github.com/samukasmk/setup_tools_scripts',
      install_requires=['my_package_dependency_1==1.0',
                        'my_package_dependency_2==1.2',
                        #...
                        # Real Example:
                        'requests==1.2.3',
                        'boto==2.10.0']
     )
```

#### 1.4. Set in (setup-env.py) the links for the executable files of your application:

```python
my_app_example_1_src = os.path.join(orig_folder, '../', 'my_app_example1.py')
my_app_example_1_dst = '/usr/bin/my_app_example1.py'


my_app_example_2_src = os.path.join(orig_folder, '../', 'my_app_example2.py')
my_app_example_2_dst = '/usr/bin/my_app_example2'

apps_list = [
                [my_app_example_1_src, my_app_example_1_dst],
                [my_app_example_2_src, my_app_example_2_dst]
            ]
```

## 2. Build your virtualenv sandbox
```bash
$ cd /my/repo/folder/project/

$ cd ./install

$ python2.7 setup.py install
```

## 3. Check if your virtualenv sandbox was Created:
```bash
$ cd /my/repo/folder/project/

# See the differences with your python library machine


# The virtualenv specific library:

$ venv/bin/pip freeze
# ... The specific python packages, defined in (setup-env.py) dependencies, of the virtualenv specific library
my_package_dependency_1==1.0
my_package_dependency_2==1.2
requests==1.2.3
boto==2.10.0


# The machine library:

$ pip freeze
# ... Your python packages, of the your machine library
```

## 4. (Additional) Add in your (.gitignore) the garbage-build
```bash
$ cd /my/repo/folder/project/

$ vim .gitignore
```

Insert in .gitignore file the content:
```
install/garbage-build
```

## 5. (Additional) Add in executable files the interpreter path
```bash
$ cd /my/repo/folder/project/

$ vim my_executable_app.py
```

Insert in the first line of your "my_executable_app.py" file, the content:

```
#!/my/repo/folder/project/venv/bin/python
```