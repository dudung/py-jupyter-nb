# student.py
# Store students data (id, name, github)
# Sparisoma Viridi | https://github.com/dudung
# 20220425 Create this module.


# define dictionary for students data
Students = {
  10200999: { 'name': "Bot Koum", 'github': 'botkoum' },
  10201945: { 'name': "Fees Kuom", 'github': 'feeskoum' }, 
  10215075: { 'name': "Ahmad Nawwaaf", 'github': 'anawwaaf' },
  10218009: { 'name': "Akram Akbar Amin", 'github': 'AkramAkbarAmin' },
  10218010: { 'name': "Dhika Arya R.B.", 'github': 'realdhikaarya' },
  10218023: { 'name': "Amanda Lathifah", 'github': 'amanda248la' },
  10218062: { 'name': "Salma Aqilah Zahroh", 'github': 'salmaaqilahzahroh' },
  10218100: { 'name': "Nabila As Syifa", 'github': 'nabilaassyf' },
  10219001: { 'name': "Fernanda Adekeu Alif", 'github': 'dekeu1' },
  10219012: { 'name': "Faiz Aulia Rahman", 'github': 'rahmanfaiz' },
  10219017: { 'name': "Lasma Evita Helena", 'github': 'lasmaevitahelena' },
  10219019: { 'name': "Abdu Rafie", 'github': 'rajaabdurafie' },
  10219020: { 'name': "Jonathan Adriel", 'github': 'JonathanAdriel' },
  10219021: { 'name': "Hartanto Wijaya", 'github': 'HartantoWijaya' },
  10219025: { 'name': "Asla Roudhatu Rohmah", 'github': 'AslaRoudhatuRohmah' },
  10219029: { 'name': "Isnaini Mufidhatul Mughni", 'github': 'isnainimufidhatulmughni' },
  10219031: { 'name': "Yoda Taruna Hidayah", 'github': 'YodaTaruna' },
  10219033: { 'name': "Aniesah Akhyar", 'github': 'Aniesah' },
  10219034: { 'name': "Clarisa Andrienny Natasya", 'github': 'Clarisa00' },
  10219035: { 'name': "Dinda Fahrila Suci Ramadhani", 'github': 'dindafahrila' },
  10219036: { 'name': "Jeremy David Dipahotma", 'github': 'jeredav24' },
  10219039: { 'name': "Elen Mengtan Kwandou", 'github': 'elenkwan' },
  10219040: { 'name': "Ridwan Muhammad Syahrul", 'github': 'RidwanMSyahrul' },
  10219043: { 'name': "Alya Ismia Rusdiana", 'github': 'alyarusdiana10' },
  10219044: { 'name': "Tommy Arisandiko", 'github': 'Blitzmaestro' },
  10219048: { 'name': "Said Husain", 'github': 'Supermieisidua' },
  10219051: { 'name': "Clarissa Ivana Yuwono", 'github': 'clarissaivana' },
  10219052: { 'name': "Tiara Novis Saputri", 'github': 'tiaranovis' },
  10219058: { 'name': "Isep Robi Awaludin", 'github': 'iseprobi' },
  10219066: { 'name': "Marshanda Tiana Sarjito", 'github': 'MarshandaTiana' },
  10219069: { 'name': "R R Zahra Auliya S", 'github': 'RRZahra' },
  10219070: { 'name': "Shabrina Adha Indraswari", 'github': 'shabrinaadhai' },
  10219074: { 'name': "Muhammad Farhan", 'github': 'chromaaxion' },
  10219079: { 'name': "Adam Raihan Ramadhani", 'github': '4damrr' },
  10219082: { 'name': "Rahmalia Nur Azizah", 'github': 'RahmaliaNur' },
  10219084: { 'name': "Avima Haamesha", 'github': 'mahaamesha' },
  10219085: { 'name': "Meyke Putri Dalla", 'github': 'Meykeputri' },
  10219086: { 'name': "Rossa Bella Adhina", 'github': 'belladhinars' },
  10219088: { 'name': "Dimas Fasdhia Daniswara", 'github': 'dimasdaniswara' },
  10219091: { 'name': "Qoid Abrori Syakuro", 'github': 'Abrorisya' },
  10219093: { 'name': "Dian Retno Anggraini Ekawati", 'github': 'dianrae' },
  10219095: { 'name': "Nungky Andriani Dinar W.", 'github': 'nungkyadw' },
  10219098: { 'name': "Aldian Nur Azmar", 'github': 'AldianNurAzmar' },
  10219099: { 'name': "Annisa Kemala Sari", 'github': 'annisakss' },
  10219100: { 'name': "Ryan Dwigiantara", 'github': 'Ryandwigiantara' },
  10219101: { 'name': "Muhammad Ervandy Rachmat", 'github': 'ErvandyR' },
  10219112: { 'name': "Hanz Hamzah Kusumah", 'github': 'HanzHamzahK' },
}


# import sleep function
from time import sleep


# check whether a student id valid
def check(anim):
  print("Check students ", end='')
  valid = False
  for nim in Students:
    sleep(0.1)
    print('-', end='')
    if nim == anim:
      valid = True
  print(' ok')
  return valid
