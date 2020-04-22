# Google page rank algorithm and HITS algorithm

**<br>Google page rank:</br>**
<br>reference: https://en.wikipedia.org/zh-hant/PageRank</br>
<br>PageRank (PR) is an algorithm used by Google Search to rank web pages in their
 search engine results. PageRank was named after Larry Page, one of the founders
  of Google. PageRank is a way of measuring the importance of website pages.</br>

**<br>HITS algorithm</br>**
<br>reference: https://en.wikipedia.org/wiki/HITS_algorithm</br> 
<br>Hyperlink-Induced Topic Search (HITS; also known as hubs and authorities) is a link 
analysis algorithm that rates Web pages, developed by Jon Kleinberg. The idea behind
 Hubs and Authorities stemmed from a particular insight into the creation of web pages
  when the Internet was originally forming; that is, certain web pages, known as hubs, 
  served as large directories that were not actually authoritative in the information 
  that they held, but were used as compilations of a broad catalog of information that
   led users direct to other authoritative pages.</br>
   
**<br>How to use the program </br>**
<br>in the input.json file, there are several variable to initialize according to the following web graph</br>
<br>![alt text](web%20graph.PNG)</br>
```
G: the link matrix, where G[i][j] = 1 means there is a link pointing from page i to page j
PR: the initial page rank vector, usually is all 1
Hub: the initial hub vector, usually is all 1
Aut: the initial authority vector, usually is all 1
```
calculate page rank by
```
in pageRank.py, call:
calPageRank(PR, G, damping factor, # of iteration, mode)

where mode = 0, 1, 2
0: no normalization at all
1: normalize all PR values in every iteration with L1 norm
2: normalize all PR values with L1 norm only at the end of final iteration
```
calculate Hub and Authority by
```
in HubandAuthority.py, call:
calHubAndAuthority(G, # of iteration, Hub, Aut)
```
