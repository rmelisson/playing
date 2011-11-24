#!/usr/bin/python
# -*- coding: iso-8859-1 -*
import random
import copy
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from datetime import date

class Person:
    "A person is a friend who can be designed as a gift receiver or a gift sender :)"
    def __init__(self, p, n, s, e):
        self.prenom = p
        self.nom = n
        self.surnom = s
        self.email = e

class GiftMixer:
    "GiftMixer is a simple class which can associate friends for exchange gifts and is also able to send email to those guys "

    def __init__(self, l, c):
        self.friends = l
        self.couples = c

    def mix(self):
        self.associations = []
        random.seed()
        temp_l = copy.copy(self.friends);
        # Mix it!
        # Iterate randomly until we get a correct mix
        while (1):
            random.shuffle(temp_l)
            self.associations = list(zip(self.friends, temp_l))
            try:
                self.assert_associations(self.friends, self.associations,
                        self.couples)
                break
            except AssertionError:
                pass
        return

    def report(self):
        f = open(date.today().__str__() + '.mix', 'w')
        for (s, r) in self.associations:
            f.write(s.prenom + " -> " + r.prenom + "\n")
        f.close()
        return

    def mail_start(self):
        name_tmpl = Template('* $prenom $nom \"$surnom\"\n')
        names = ''
        for f in self.friends:
            names += name_tmpl.substitute(prenom = f.prenom, nom = f.nom, surnom = f.surnom)

        txt_tmpl = Template("Yo yo $prenom $nom\nTu as l'immense chance de t'être selectionné(e) pour le gift mix 2010, une expérience bouleversante qui renversera ce noël.\nVoici la liste des amigos:\n\n$liste \nUn second mail te dévoilera l'identité de l'heureux élu à qui destiner ton cadeau!\ncya cya.\nGiftMixer Robot 1.10")
        s = smtplib.SMTP('smtp.sfr.fr')
        s.set_debuglevel(1)
        for f in self.friends:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Vous avez dit noyël? -step one-"
            msg['From'] = "pere-noel@gmail.com"
            msg['To'] = f.email
            part_plain = txt_tmpl.substitute(prenom = f.prenom, nom = f.nom, liste = names)
            msg.attach(MIMEText(part_plain, 'plain'))
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit
        return


    def mail_gifter(self):
        txt_tmpl = Template("Yo, \nTon cadeau, c'est à $prenom $nom \"$surnom\" que tu dois l'envoyer! No rules, c'est toi qui vois.\ncya.\nGiftMixer Robot 1.10")
        s = smtplib.SMTP('smtp.sfr.fr')
        s.set_debuglevel(1)
        for (f, r) in self.associations:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Vous avez dit noyël? -step two-"
            msg['From'] = "pere-noel@gmail.com"
            msg['To'] = f.email
            part_plain = txt_tmpl.substitute(prenom = r.prenom, nom = r.nom, surnom= r.surnom)
            msg.attach(MIMEText(part_plain, 'plain'))
            s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit
        return

    def assert_associations(self, l, a, c):
        if (a == []):
            return False
        # Assert that there is as many people as associations.
        assert len(l) == len(a)
        # Assert that everyone send a gift, receive another and don't have to autosend gift :/
        senders = []
        receivers = []
        for (s,r) in a:
            # Assert this association is not a couple
            assert (s,r) not in c
            assert (r,s) not in c
            # Autosend is not for christmas, but for the rest of the year :)
            assert s != r
            senders.append(s)
            receivers.append(r)
        for p in l:
            assert p in senders
            assert p in receivers  
        return True

####### SEQUENCE

def step_one(l):
    "at first we send an announcement in order to verify adresses"
    giftMixer = GiftMixer(l)
    giftMixer.mail_start()

def step_two(l):
    "then we mix the list, save a report and send the second mail with the name of the receiver"
    giftMixer = GiftMixer(l)
    giftMixer.mix()
    giftMixer.report()
    giftMixer.mail_gifter()

######## TEST

def start_test():
    jean = Person("jean", "J", "jannot", "rmelisson@gmail.com")
    paul = Person("paul", "p", "polo", "p@p.p")
    marc = Person("marc", "m", "marco", "m@m.m")
    marie = Person("marie", "ma", "marie", "ma@ma.m")

    l = [jean, paul, marc, marie]
    c = [ (marc, marie) ]
    a_ok = [ (jean, marc), (marc, jean), (paul, marie), (marie, paul) ]
    a_nok1 = [ (jean, paul), (marc, jean), (jean, paul), (paul, marie) ]
    a_nok2 = [ (jean, paul), (marc, jean), (paul, paul), (paul, marc) ]
    a_nok3 = [ (jean, paul), (marc, jean), (paul, paul) ]
    a_nok4 = [ (paul, jean), (marc, paul), (jean, marie), (marie, marc) ]

    giftMixer = GiftMixer(l, c)
    giftMixer.assert_associations(l, a_ok, c)
    try:
        giftMixer.assert_associations(l, a_nok1, c)
        raise BaseException("1")
    except AssertionError:
        pass
    try:
        giftMixer.assert_associations(l, a_nok2, c)
        raise BaseException("2")
    except AssertionError:
        pass
    try:
        giftMixer.assert_associations(l, a_nok3, c)
        raise BaseException("3")
    except AssertionError:
        pass
    try:
        giftMixer.assert_associations(l, a_nok4, c)
        raise BaseException("4")
    except AssertionError:
        pass

    giftMixer.mix()
    giftMixer.report()
    #giftMixer.mail()

start_test()

####### END TEST


####### OUR lIST 

def create_list():
    ben = Person('Benou', 'Donov', 'superman', 'benoit.dalinval@gmail.com')
    adri = Person('Adri', 'Robi', 'Foxy', 'adrienheele@gmail.com')
    agathe = Person('Agathe', 'Ioubaby', 'oushka', 'agathe_gerard@hotmail.com' )
    nath = Person('Nathalie', 'Dek', 'Acrob', 'nathaliedec@hotmail.fr')
    franz = Person('Franz', 'Kafkaz', 'babyBoss', 'franzuze@gmail.com')
    dum = Person('Justin', 'Dooky', 'rPichon59', 'justin.dumont@hotmail.com')
    ge = Person('Germain', 'Dble', 'hipster', 'dbleg.adamski@gmail.com' )
    verv = Person('Romu', 'Verherf', 'skieur2province', 'romu83@gmail.com')
    mkton = Person('Remi', 'Mich***', 'mkton', 'rmelisson@gmail.com')
    edouard = Person('Edouard', 'Mutsch', 'la scie', 'edouard.mutschler@gmail.com')
    sarah = Person('Sarah', 'Françoise', 'bisha59', 'bisha002@hotmail.com')
    quentin = Person('Quentin', 'III', 'napoleon', 'quentinlabre@hotmail.fr')
    lucie = Person('Lucie', '', '', '?????????@hotmail.fr')
    morgane = Person('Morgane', '', '', '?????@?.fr')
    perrine = Person('Perrine', '', '', '?????@?.fr')
    momo = Person('Momo', '', '', '?????@?.fr')
    #cedric = Person('Cedric', 'ho yé', 'cmdt', 'cedric.ogez@gmail.com')
    #elodie = Person('Elodie', 'Maze', 'eltof', 'dodiem2@hotmail.com')
    #xav = Person('Xav', 'Lavigne', 'hornet rulz', 'lavigne.xavier@gmail.com')

    l = [ben, adri, agathe, nath, franz, dum, ge, verv, mkton, edouard, sarah,
            quentin, perrine, morgane, momo]
    c = [ (adri, sarah), (dum, agathe), (franz, nath), (verv, lucie)]
    return [l, c]

remim = Person('Remi', 'Melisson', 'remi', 'rmelisson@gmail.com')
mkton = Person('mk', 'Tom', 'mkton', '0.mkton.0@gmail.com')
robot = Person("Rob", "Ho", "we're the robots", "remi.melisson@hotmail.fr")

#l = [robot, mkton, remim]
lc = create_list()

giftMixer = GiftMixer(lc[0], lc[1])
giftMixer.mix()
giftMixer.report()

#step_one(l)
#step_two(l)

