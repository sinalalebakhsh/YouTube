#!/bin/bash
git add .
git commit -m " GO فارسی
======================================================
    
    
        127- Using Content Blocks and Partials

        
======================================================

1- in Terminal ➤➤➤➤ hugo new site portfolio
Then ➤➤➤➤ cd portfolio
2- Create index.html in layouts directory ➤➤➤➤ index.html
3- copy/paste these code inside layouts/index.html
4- Create _index.md in Content directory
5- content in _index.md
6- in current directory write this  ➤➤➤➤ hugo server
7- in Terminal  ➤➤➤➤ hugo new about.md
8- in Terminal  ➤➤➤➤ mkdir layouts/_default/
9- in Terminal  ➤➤➤➤ cp layouts/index.html layouts/_default/single.html
10- modify this line in content/about.md like this  ➤➤➤➤ draft = false
11- in Terminal ➤➤➤➤ hugo server
12- go in this link in browser  ➤➤➤➤ http://localhost:1313/about
13- Open the layouts/_default/single.html file in your editor and add the title like this:
14- go in this link in browser ➤➤➤➤ http://localhost:1313/about
15- in Terminal
16- Building and Exploring Hugo's Output ➤➤➤➤ in Terminal
17- delete the entire public folder ➤➤➤➤ in Terminal  ➤➤➤➤  rm -r public && hugo
OR:



use Hugo's --cleanDestinationDir argument ➤➤➤➤ in Terminal
hugo --cleanDestinationDir
18- minify the files it generates ➤➤➤➤ in Terminal  ➤➤➤➤ hugo --cleanDestinationDir --minify
19- Create a 'Résumé' page
20- in Terminal ➤➤➤➤ hugo new theme basic
21- Move your existing layout files into this new theme ➤➤➤➤ in Terminal 
➤➤➤➤ mv layouts/index.html themes/basic/layouts/index.html
➤➤➤➤ mv layouts/_default/single.html themes/basic/layouts/_default/single.html
22- Open config.toml and add the following line to the end: 
23- in Terminal --> hugo server
24- Open themes/basic/layouts/partials/head.html and Replace this codes
25- in Terminal
26- open the file themes/basic/layouts/partials/header.html and Replace these
27- create the footer of the site by opening themes/basic/layouts/_default/partials/footer.html
28- Open themes/basic/layouts/index.html and replace the contents with this code basic_theme/portfolio/themes/basic/layouts/index.html
29- modify the code in themes/basic/layouts/_default/single.html so the single page layout works the same way: basic_theme/portfolio/themes/basic/layouts/_default/single.html
30-  in Terminal


➤➤➤➤
"
git push -u origin main 
