# Contributions File
I have taken help from pritom saha akash about python syntax.
I also saw answers in https://github.com/P7h/IntroToHadoopAndMR__Udacity_Course link but i did not follow it.
Although i took idea  from muna, sajid, toufiq vaiya( means why their answers differ from mine however finally i remained fixed on my idea an submitting final submission honestly) but at last i made my code unique and i think it is different from others.

In 1 and 2 the result matched with all others.

However in 3 the result differed because, some of the students gave idea of using len(data)==10 and some other gave len(data)>1
but i took split at "GET ", and obtained url where GET method was applied. It is where the file is hit or obtained by requesting the website. I applied urlparse.netloc to obtain web address like www.a.com and urlparse.path for path to file like /displaytitle.php. So the file address considered was urlparse.netloc+urlparse.path. It was done because http://www.a.com/displaytitle.php?s=19 http://www.a.com/displaytitle.php?s=20 (seen in log files) as urlparse.netloc+urlparse.path=www.a.com/displaytitle.php will not be considered different. It will be considered same file.

In unique files also i considered urlparse.netloc+urlparse.path as unique.
