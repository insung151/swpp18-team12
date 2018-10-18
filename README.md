<pre>
███████╗███╗   ██╗██╗   ██╗ ██████╗██╗     ██╗   ██╗██████╗  
██╔════╝████╗  ██║██║   ██║██╔════╝██║     ██║   ██║██╔══██╗  
███████╗██╔██╗ ██║██║   ██║██║     ██║     ██║   ██║██████╔╝  
╚════██║██║╚██╗██║██║   ██║██║     ██║     ██║   ██║██╔══██╗  
███████║██║ ╚████║╚██████╔╝╚██████╗███████╗╚██████╔╝██████╔╝  
╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝ ╚═════╝ ╚═════╝  
</pre>
[![Coverage Status](https://coveralls.io/repos/github/swsnu/swpp18-team12/badge.svg?branch=master)](https://coveralls.io/github/swsnu/swpp18-team12?branch=master)
<br>
[![송호준](https://badgen.net/badge/송호준/hojunroks/purple)](https://github.com/hojunroks)
[![이영재](https://badgen.net/badge/이영재/snumath/purple)](https://github.com/snumath)
[![황인성](https://badgen.net/badge/황인성/insung151/purple)](https://github.com/insung151)

We've not implemented yet. Please see [our wiki](https://github.com/swsnu/swpp18-team12/wiki) to see what we will implement.


## Branch Manager
- Sprint1: 이영재
- Sprint2: 황인성
- Sprint3: 이영재
- Sprint4: 황인성
- Sprint5: 송호준
- Sprint6: 송호준


## How to get started

- Clone repository

```
$ git clone https://github.com/swsnu/swpp18-team12.git
$ cd swpp18-team12
```

- Run backend server

```
$ cd backend
$ pip install -r requirements.txt
$ cd snuclub
$ DJANGO_SETTINGS_MODULE=snuclub.settings.local python manage.py runserver
```
- Run frontend server
```
$ yarn
$ yarn start
```



## Code Style

Tab size is 2 spaces in html and typescript

Tab size is 4 spaces in python

Type script code style follows our `tslint.json`  and python code style follows `PEP 8` as possibe as you can



## Git convention

We use rebase and squash instead of merge to ensure the log message is clean.

```
git checkout your_barnch
git fetch origin
git rebase -i origin/master
... confilct resolve ...
git push origin your branch
```

#### commit message

Capitalize the subject line

Use the imperative mood in the subject line

```
Fixed typo(x)
Fix typo(o)
```

#### branch naming

`feature/<featurename>` : Feature branches are used when developing a new feature or enhancement . No matter when the feature branch will be finished, it will always be merged back into the master branch.

`bug/<bug-id>` : Bug branches will be created when there is a bug on the live site that should be fixed and merged into the next deployment. No matter when the bug branch will be finished, it will always be merged back into master.

#### pr

pr description should contain the following

```
#### What does this PR do?
#### Description of Task to be completed?
- something
- something
#### How should this be manually tested?
```

If pr includes migrations, you should label it  `need migrations`

If pr includes a modification of our secret file, you should label it `update secret `

At least 2 reviewers are required for pr to merge!



## open source Angular projects

#### [click](https://medium.mybridge.co/18-amazing-open-source-angular-projects-dd9e81d921ee)

