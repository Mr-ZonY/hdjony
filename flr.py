o
    ???bS  ?                   @   s~  d dl Z e ?d? d dl Z e ?d? ed? d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd? Zeeed e
 ??Ze ?d? eed ? e?d?Zeed ? ee	d ? eed e	 d e d ? e?d? ee
de?? d ? eed ? ee
d ? d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed ? d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ d dlZd dlmZ d dlZd dlZd dlZd dlmZ e?d? d Zed! Ze? Z d"e d#< d$e d%< ee d&< ej!ee d'?Z"ej!ee d'?Z"e"?? d( d)k?r6eed* e	 e"?? d+ d,  d ? e"?? d+ d- Z#e?d? g Z$ee	d. e d/ e
 d ?Z%d0Z&ej!e&e d'?Z'e%?r?e#D ]Z(eed1 e	 d2 e e(d3  ? e$?)e(d3 ? ?qYz!e$D ]Z*ed4 e* Ze?d? ej!ee d'?Z"eee"j+ ? ?qwW n   ed5? e?d? Y eee	d6 e
 d7 e	 d8 ??Z,e ?d? e?d? dS )9?    N?clearzlolcat ban.py?
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )Nr   ?{?G?z??)?sys?stdout?write?flush?time?sleep)ZJoNyZword? r   ?flr.py?	logoprint   s
   
?r   z[>] Enter Api Key: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 1.1.2u   	 ♥♥z	 BLACK HOUNTERr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)?CaseInsensitiveDictz 
)r
   )?init?Fore?Back?Style?   z5https://circle.robi.com.bd/mylife/appapi/appcall.php?zop=getFollowerInfoList?gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-key)?headersZrdescZOKz[>] Total Follower:?data?totalZfollowerz

	[!]z+ If You Wonna To Clear Follower List Type Yz?https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=Your Circle  Follower List Is Cleaning By Using JonY's SysTem....!! &retry=falsez[>]z CIRCLE ID	:	 ?nicknamezop=blockUser&nickname=zError!z	 

	Pressz Enterz To Exit)-?os?system?printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   ?str?input?x?getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   ?baseZurlr   ZpostZresp?yZfolNicks?boolZurlxZresp5?user?appendr   ?textZxnr   r   r   r   ?<module>   s?   




	
$
 
?
 
