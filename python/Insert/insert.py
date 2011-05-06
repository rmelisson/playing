#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import string
import os 

class Writer:
	"A simple class who is able to write SQL INSERT command into a file"
	insert_into = "INSERT INTO "
	values = "VALUES "
	delete = "DELETE FROM "

	def __init__(self, f, t):
		self.file = f
		self.table_name = t.upper()

	def formatInsert(self, keys, vals):
		cmd = self.insert_into
		cmd += self.table_name 
		cmd +=  " (" + ", ".join(keys) + ") " 
		cmd += "\n" + self.values
		cmd +=  " (" + ", ".join(vals) + ") " 
		cmd += ";\n\n"
		return cmd

	def formatDelete(self):
		cmd = self.delete
		cmd += self.table_name 
		cmd += ";\n\n"
		self.file.write(cmd)
		
	def write(self, dico):
		keys = []
		vals = []
		#INSERT
		for k,v in dico.iteritems():
			keys.append(k)
			vals.append(v)
		cmd = self.formatInsert(keys, vals)
		self.file.write(cmd)
		return cmd

class DBInsert:
	"A class linked with a DB description, which is able to read data from a folder and create insertion script for each tables and a GLOBAL script."
	def __init__(self, d, p):
		self.tables = d
		self.path = p
	
	def makeDico(self, ks, vs):
		z = zip(ks,vs)
		d = {}
		for (k,v) in z:
			d[k] = v
		return d

	#Recoller les morceaux 'Saint, Maurice' -> 'Saint Maurice'
	def reformat(self, l):
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

	#Utilise un fichier de données pour ecrire un fichier sql
	def useFile(self, file_name, writer):
		b = ""
		#DELETE
		writer.formatDelete()
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
				l_val = self.reformat(l_val)
			d = self.makeDico(l_key, l_val)
			b += writer.write(d)
		f.close()
		return b

	#Lance le traitement sur une table
	def processTable(self, t):
		f = open(self.path + '/Insert/Insert_' + t + '.sql', 'w')
		w = Writer(f, t)
		s = self.useFile(self.path + 'Data/' + t + '.txt', w)
		f.close()
		return s
	
	#Retourne le contenu d'un script pour le GLOBAL
	def concatFile(self, t):
		f_tmp = open(self.path + 'Insert/Insert_' + t + '.sql')
		s = f_tmp.read()
		f_tmp.close()
		return s

	#Retourne les commandes de vidage des tables
	def deleteCmd(self):
		s = ""
		#On retourne l'ordre pour les delete dans le bon sens
		tables.reverse()
		#Ecriture du fichier GLOBAL regroupant l'ensemble des insert
		for t in self.tables:
			s += "DELETE FROM " + t.upper() + ";\n"
		s += "\n"
		return s


	def goScript(self):
		#s récupère l'ensemble des commandes pour le GLOBAL
		s=""
		#Lance le traitement de chaque table
		for t in self.tables:
			s += self.processTable(t)
		s = self.deleteCmd() + s
		f = open(self.path + 'Insert/Insert_GLOBAL.sql', 'w')
		f.write(s)
		f.close()


print u"Début du processus de création de script d'insertion d'un jeu de test." 

#Les tables doivent être indiquées dans l'ordre de dépendance.
tables = ['Classement_Demande', 'Etat_Demande', 'Type_Demande', 'Type_Evenement', 'Nature_Sillon', 'Type_PR', 'Point_Remarquable', 'Demande', 'Demande_Reference', 'Historique_Evenement', 'Sillon', 'Jalonnement']

db = DBInsert(tables, '../Insertion_Gesico/')
db.goScript()

print u"Fin du traitement"
