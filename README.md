# Scraping

Web Scraping, HTML, Chrome Development tools, Splinter, BeautifulSoup, MongoDB, Python3, Flask to the end of a working webSite that scrapes new data at the push of a button. 

### Final working code: 

As direction by the flask documentation: the file structure is set up as follows: 
<ul><li>my-flask-app ----> templates -----> index.html </li>
<li>        ----> app.py</li>
<li>        ----> scraping.py</li>
<li>        ----> static ----> .css (these files don't exist but I'm putting them here as a place holder for future reference).</li>
</ul>
learnings:
There were four relatively simple steps that held me back over a week on this project. I kept receiving 'connection refused' and/or 'file not found' errors. In fact, when I originally submitted the files, they were all correct. I was just running them wrong. Frustrating but the kind of lesson you only have to learn once. The following steps will prevent those errors in the future: 


1) Run app.py first, then click the index file, then look at localhost 5000. 
  I was running index first without looking at local host. THEN I was looking at localhost without runnin the .py file
  
2) to make changes to the index file and have them show up on the local host front end, you have to make sure the flask python file is in debug mode. Then, for production, turn off debug mode

I worked with a number of guides to figure these steps out, but the steps were so simple that I didn't realize what exactly was fixing the problem until now. (each session I'd learn a little bit more... 'ah, you have to look at localhost: 5000' 'oh, refreshing the index file is not enough, you need the debuger in the flask file'. (I actually discovered this one through documentation.) 

The harder pieces of the challenge were setting up the flask file to save the mongo database. With some clear print statements set throughout the code, with the help of a tutor, I was able to find out why the hemisphere images were not being collected and fix that error in the scrape.py code. The problem was that we were rushing the code and needed to add a time.sleep(2) element to the function. 

### Conclusion:

The code is now responsive and has been changed in three ways, the button color, the stacking of the images and the typography.
It is not beautiful, nor is is portfolio ready. If I have time after catching up on Module 11 and 12, I'll come back and make it beautiful. 





<img width="1216" alt="Screen Shot 2021-07-02 at 2 17 00 PM" src="https://user-images.githubusercontent.com/14239715/124314471-727b3880-db40-11eb-9ca9-f80a92623581.png">
<img width="483" alt="Screen Shot 2021-07-02 at 2 17 15 PM" src="https://user-images.githubusercontent.com/14239715/124314473-73ac6580-db40-11eb-842c-2780e3afc637.png">
<img width="486" alt="Screen Shot 2021-07-02 at 2 17 26 PM" src="https://user-images.githubusercontent.com/14239715/124314479-74dd9280-db40-11eb-83d6-02e194c5def9.png">
<img width="618" alt="Screen Shot 2021-07-02 at 2 17 43 PM" src="https://user-images.githubusercontent.com/14239715/124314483-760ebf80-db40-11eb-98df-79eb1501d1b4.png">


