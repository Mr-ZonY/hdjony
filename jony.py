o
     �b  �                   @   sp  d dl Z e �d� d dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZd dlmZ e �d� dZdZ	dZ
dZd	Zd
ZdZdZdd� Zeed � e�d�Zee
d � ee
d � eed e
 d e d � e�d� ee
de�� d � eed � eed � d dlZd dlZd dlmZ d dl Z 	 e �d� d dl Z d dl Z e �d� d dl Z d dl Z d dlZd dlmZmZmZmZ dZeed � ejd ejd  ejd! ejd" ej d# gZ!d Z"	 ee!e"e#e!�  d$d%� e�d&� e"d'7 Z"e"d(k�r	nq�d dl Z ed)� eed* e d+ e d, e d- e � e�d.� e �d� e �d� eed/ � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ e
d0 Z$e$D ]Z%ej&�'e%� ej&�(�  e�d1� �q_e)e*e	d2 e ��Z+e+d3k�r�e �d4� e �d� n�e+d5k�r�e �d6� e �d� n�e+d7k�r�e �d8� e �d� n�e+d9k�r�e �d:� e �d� nze+d;k�r�e �d<� e �d� nje+d=k�r�e �d>� e �d� nZe+d?k�r�e �d@� e �d� nJe+dAk�r�e �dB� e �d� n:e+dCk�re �dD� e �d� n*e+dEk�re �dF� e �d� nedGk�r-e �dH� e �d� n
e+dIk�r7e �dJ� q�)K�    N�clear)�sleepzlolcat ban.pyz[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�t� t j��  t�d� qd S )N�
�{�G�z�?)�sys�stdout�writeZwor6d�flush�timer   )ZJonYZword� r   �main.py�	logoprint   s
   
�r   z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	 BLACK HOUNTER�   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictT)�init�Fore�Back�Style�	z 
	      Updating Tools.........
z		   [      ]z		   [.     ]z		   [...   ]z		   [....  ]z		   [......]�)�endg�������?�   �   r   z
	[u   √�]z%	Keep allow termux setup storage.....�   u   
[√] Show Your Option/nz�
[01]	SMS BOMBER
[02]	CIRCLE PIN
[03]	ID TO NUMBER
[04]	NUMBER TO ID
[05]	ROBI
[06]	AIRTEL
[07]	API KEY GENARETOR
[08]	FOLLOWER CLEAN
[09]	FOLLOWING CLEAN
[10]	JOIN-XJOIN
[11]	ADMIN CONNECT
[12]	EXIT
r   z

[>] Select Your Option: �1zpython 01.py�2zpython 02.py�3zpython 04.py�4zpython 05.py�5zpython robi.py�6zpython air.py�7zpython api.py�8zpython flr.py�9zpython flg.pyZ10zpython jx.pyZ11z+xdg-open https://www.facebook.com/iTzJonYhdZ12�exit),�os�systemZasyncior   Zrequestsr
   Zcoloramar   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �print�getZresponseZjsonZrequests.structuresr   r   r   r   r   �aZREDZGREENZBLUEZYELLOWZCYANZ	animation�i�lenZwords�charr   r   r	   �str�input�opr   r   r   r   �<module>   s�   

	



,

�(



























�