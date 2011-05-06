#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import string
import os 

class Writer:
	"A simple class who is able to write SQL INSERT command into a file"
	insert_into = "INSERT INTO "
	values = "VALUES "

	def __init__(self, f, t):
		self.file = f
		self.table_name = t.upper()

	def formatCommand(self, keys, vals):
		cmd = self.insert_into
		cmd += self.table_name 
		cmd +=  " (" + ", ".join(keys) + ") " 
		cmd += "\n" + self.values
		cmd +=  " (" + ", ".join(vals) + ") " 
		cmd += ";\n\n"
		return cmd
		
	def write(self, dico):
		keys = []
		vals = []
		for k,v in dico.iteritems():
			keys.append(k)
			vals.append(v)
		cmd = self.formatCommand(keys, vals)
		self.file.write(cmd)

class DBInsert:
	"A class linked with a DB, which is able to read data from a folder and create insertion script for each tables"
	def __init__(self, d, p):
		self.tables = d
		self.path = p
	


def makeDico(ks, vs):
	z = zip(ks,vs)
	d = {}
	for (k,v) in z:
		d[k] = v
	return d

#Recoller les morceaux 'Saint, Maurice' -> 'Saint Maurice'
def reformat(l):
	l_ret = []
	ok = True
	for e in l:
		if not ok:
			tmp += ' ' + e
			if e.endswith("'"):
				l_ret.append(tmp)
				ok=True
		elif (e.startswith("'")) and (not e.endswith("'")):
			ok = False
			tmp = e
		else:
			l_ret.append(e)
	return l_ret

def useFile(file_name, writer):
	f = open(file_name)
	s = f.readline()
	#on enleve le \n et on découpe en liste
	s = string.strip(s)
	l_key = string.split(s)
	for s in f:
		s = string.strip(s)
		l_val = string.split(s)
		#gestion des espaces:
		if (len(l_key) < len(l_val)):
			l_val = reformat(l_val)
		d = makeDico(l_key, l_val)
		writer.write(d)
	f.close()
	return

def processTable(nom_table):
	f = open('../Insertion_Gesico/Insert/Insert_' + t + '.sql', 'w')
	w = Writer(f, t)
	useFile('../Insertion_Gesico/Data/' + t + '.txt', w)
	f.close()

def concatFile(t):
	f_tmp = open('../Insertion_Gesico/Insert/Insert_' + t + '.sql')
	s = f_tmp.read()
	f_tmp.close()
	return s


print u"Début du processus de création de script d'insertion d'un jeu de test." 

tables_listes = ['Classement_Demande', 'Etat_Demande', 'Type_Demande', 'Type_Evenement', 'Nature_Sillon', 'Type_PR', 'Point_Remarquable']
tables_valeurs = ['Demande', 'Demande_Reference', 'Historique_Evenement', 'Sillon', 'Jalonnement']

#Création de chaque fichier SQL d'insert
for t in tables_listes:
	processTable(t)

for t in tables_valeurs:
	processTable(t)

#Création d'un script global
s = ""
for t in tables_listes:
	s += concatFile(t)
for t in tables_valeurs:
	s += concatFile(t)

s2 = ""
tables_valeurs.reverse()
for t in tables_valeurs:
	s2 += "DELETE FROM " + t.upper() + ";\n"
tables_listes.reverse()
for t in tables_listes:
	s2 += "DELETE FROM " + t.upper() + ";\n"

f = open('../Insertion_Gesico/Insert/Insert_GLOBAL.sql', 'w')
f.write(s2)
f.write(s)
f.close()


print u"Fin du traitement"
