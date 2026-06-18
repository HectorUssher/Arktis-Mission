
#region vor dem Spiel

neustart = True

while neustart == True:

#endregion    










#region Einstellungen







#region >Bibliotheken

    import random
    import time
    import shutil

#endregion






#region >Variablen

    size = shutil.get_terminal_size()
    rand_name = False

    Schiffsnamen = ["Barakuda","Alligator","Skylla","Midgardsnake","Wayfarer","Orka","Riptide","Polarstern","Andromeda","Argo","Poseidon"]
    mögl_vornamen = ["Tobias","Hector","Malte","Christoph","Burdock","Gale","Steve","Coriolanus","James","Nelson","Micheal","Alexander","Sebastian"]
    mögl_nachnamen = ["Ussher","Hawthorne","Mellark","Snow","Williams","Wilson","Morgan","Hunter","Logan","Raven","Griffin"]
    monsternamen = ["mutierter Hai", "mutierter Schweinswal","mutierte Robbe"]
    mögliche_andere_gegenstände = ["15x explosive Munition","10x explosive Munition"]

    unmögl_namen = []
    verletzte = 0
    Schaden = 10
    heck = 1000
    bug = 1000
    andere_dinge = []
    brücke = 800
    repeat = True
    spielen = True
    kämpfe = 0
    zerst_brücke = False

    positionen = {
        "mutierter Krake1":random.randint(22,30),
        "mutierter Grauwal1":random.randint(13,20),
        "mutierter Grauwal2":random.randint(7,12),
        "Großes Schiff1":random.randint(20,30),
        "Kleines Schiff1":random.randint(15,27),
        "Fischerboot1":random.randint(7,15),
        "mutierter Schwertwal1":random.randint(3,13),
        "mutierter Schwertwal2":random.randint(6,20),
        "mutierter Schwertwal3":random.randint(3,30),
        "eisscholle1":random.randint(3,27),
        "eisscholle2":random.randint(3,27),
        "eisscholle3":random.randint(3,27),
        "eisscholle4":random.randint(3,27),
        "eisscholle5":random.randint(3,27),
        "eisscholle6":random.randint(3,27),
        "eisscholle7":random.randint(3,27),
        "eisscholle8":random.randint(3,27),
        "hinweis1":random.randint(3,10),
        "hinweis2":random.randint(7,15),
        "hinweis3":random.randint(12,20),
        "hinweis4":random.randint(17,25),
        "hinweis5":random.randint(22,30),
    }

    werte_gegner_haben_muss = []

    werte_gegner = {
        "mutierter Krake":{
            "leben_gegner":520,
            "min_gegn_angriffe":8,
            "max_gegn_angriffe":16,
            "minschaden":10,
            "maxschaden":23,
            "gegner_macht":9,
            "fallenlassende_nahrung":70,
            "fallenlassende_bauteile":0,
            "fallenlassende_andere_dinge":["Saugnäpfe"],
            "typ":"monster",
        },
        "mutierter Grauwal":{
            "leben_gegner":600,
            "min_gegn_angriffe":0,
            "max_gegn_angriffe":2,
            "minschaden":35,
            "maxschaden":80,
            "gegner_macht":7,
            "fallenlassende_nahrung":130,
            "fallenlassende_bauteile":0,
            "fallenlassende_andere_dinge":[],
            "typ":"monster",
        },
        "Großes Schiff":{
            "leben_gegner":1300,
            "min_gegn_angriffe":7,
            "max_gegn_angriffe":10,
            "minschaden":7,
            "maxschaden":15,
            "gegner_macht":10,
            "fallenlassende_nahrung":40,
            "fallenlassende_bauteile":100,
            "fallenlassende_andere_dinge":["50x explosive Munition"],
            "typ":"schiff",
        },
        "Kleines Schiff":{
            "leben_gegner":800,
            "min_gegn_angriffe":3,
            "max_gegn_angriffe":5,
            "minschaden":10,
            "maxschaden":10,
            "gegner_macht":8,
            "fallenlassende_nahrung":20,
            "fallenlassende_bauteile":40,
            "fallenlassende_andere_dinge":["20x explosive Munition"],
            "typ":"schiff",
        },
        "Fischerboot":{
            "leben_gegner":170,
            "min_gegn_angriffe":3,
            "max_gegn_angriffe":5,
            "minschaden":1,
            "maxschaden":2,
            "gegner_macht":5,
            "fallenlassende_nahrung":130,
            "fallenlassende_bauteile":0,
            "fallenlassende_andere_dinge":[],
            "typ":"schiff",
        },
        "mutierter Schwertwal":{
            "leben_gegner":350,
            "min_gegn_angriffe":3,
            "max_gegn_angriffe":7,
            "minschaden":15,
            "maxschaden":25,
            "gegner_macht":6,
            "fallenlassende_nahrung":60,
            "fallenlassende_bauteile":0,
            "fallenlassende_andere_dinge":[],
            "typ":"monster",
        },
    }

    x_pos = {}
    pos_u_boot = [random.randint(0,6),random.randint(1,30)]
    pos_schiff = [3,1]
    auf_pos = len(positionen)
    munition = 100
    spielzug = 1

    welcher_hinweis = 0
    story = random.randint(1,3)
    story1_hinweise = [
        "A1-alpha-57 kann sich nicht melden, weil der Telepermer rausgenommen wurde",
        "Kein Mensch ist dafür verantwortlich, das der Telepermer weg ist.",
        "Das gefährlichste der Wesen hier hat den Telepermer verschwinden lassen.",
        "Du musst die Krake finden und töten um den Telepermer wiederzuerlangen.",
        f"Die Krake befindet sich bei X {positionen.get("mutierter Krake1")}."
    ]
    story2_hinweise = [
        "Auf A1-alpha-57 ist etwas Schreckliches passiert, kein Mensch lebt dort mehr.",
        "Kein Feind ist für die Katastrophe Verantwortlich.",
        "Die Strahlung einer von Amerika getesteten Bombe hat alle Lebewesen mutieren lassen",
        "du musst in den Stützpunkt gehen und dort Amerika funken",
        "der Stützpunkt befindet sich auf dem Festland"
    ]
    story3_hinweise = [
        "Das Problem wurde von Russland ausgelöst",
        "Russland hat ein U-Boot hier",
        "Mit dem U-Boot stören sie das Signal und machen die Tiere Krank sodass keiner rauskommt",
        "Du musst das U-Boot zerstören",
        f"Die Koordinaten für das U-Boot sind: X {pos_u_boot[1]}, Y {pos_u_boot[0]}."
    ]

    über = " __ __ __ __ __ __ __ __ __ __ __ __ __ __ KARTE __ __ __ __ __ __ __ __ __ __ __ __ __ __ F"
    map0 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|e"
    map1 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|s"
    map2 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|t"
    map3 = "|_X|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|l"
    map4 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|a"
    map5 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|n"
    map6 = "|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|d"
    Map = [map0,map1,map2,map3,map4,map5,map6]
    for i in range(len(positionen)):
        x_pos[list(positionen.keys())[i]] = random.randint(0,6)
    for i in range(len(positionen)):
        Map[list(x_pos.values())[i]] = Map [list(x_pos.values())[i]] [:(list(positionen.values())[i]*3)-1] + "#" + Map [list(x_pos.values())[i]] [(list(positionen.values())[i]*3):]

#endregion






#region >Funktionen





#region >>rand_schiffsnamen
    def rand_schiffsnamen():
        if len(Schiffsnamen) == 0:
            print("Keiner der Namen hat euch gefallen. ")
            print("")
        else:
            rand_Zahl = random.randint(1,len(Schiffsnamen))-1
            rand_schiff_name = Schiffsnamen[rand_Zahl]
            Schiffsnamen.pop(rand_Zahl)
            return rand_schiff_name
#endregion





#region >>rand_namen
    def rand_namen():
            anz_vornamen = random.randint(1,6)
            if anz_vornamen < 4:
                rand_voller_name = mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_nachnamen[random.randint(0,len(mögl_nachnamen)-1)]
            elif anz_vornamen < 6:
                rand_voller_name = mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_nachnamen[random.randint(0,len(mögl_nachnamen)-1)]
            else:
                rand_voller_name = mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_vornamen[random.randint(0,len(mögl_vornamen)-1)]+" "+mögl_nachnamen[random.randint(0,len(mögl_nachnamen)-1)]
            return rand_voller_name
#endregion





#region >>schuss
    def schuss():
        global Schaden
        global werte_gegner_haben_muss
        global explosive_mun
        global munition
        if explosive_mun > 0:
            Schaden = 30
            explosive_mun -= 1
        werte_gegner_haben_muss[0] -= Schaden
        munition -= 1
        print(f"{name_gegner} -{Schaden}")
        Schaden = 10
#endregion





#region >>wasserangreifen
    def wasserangreifen():
        print("Dein Angriff")
        print("")
        global werte_gegner_haben_muss
        global Schaden
        global treffer
        global schüsse
        global munition
        global geschütze
        getroffen = skillabfrage(5)
        if munition >= geschütze:
            if getroffen > 28:
                print("Kritischer Schaden")
                getroffen = geschütze
                Schaden += 50
            elif getroffen > 24:
                getroffen = geschütze
            elif getroffen > 18:
                getroffen = geschütze - 1
            elif getroffen > 15:
                getroffen = geschütze - 2
            elif getroffen > 12:
                getroffen = geschütze - 3
            elif getroffen > 9:
                getroffen = geschütze - 4
            elif getroffen <= 9:
                getroffen = geschütze - 5
            for i in range(getroffen):
                schuss()
                if i == 0:
                    Schaden = 10
                time.sleep(0.1)
            treffer += getroffen
        else:
            
            if getroffen > 28:
                print("Kritischer Schaden")
                getroffen = geschütze
                Schaden += 50
            elif getroffen > 24:
                getroffen = munition
            elif getroffen > 18:
                getroffen = munition - 1
            elif getroffen > 15:
                getroffen = munition - 2
            elif getroffen > 12:
                getroffen = munition - 3
            elif getroffen > 9:
                getroffen = munition - 4
            elif getroffen <= 6:
                getroffen = munition - 5
            for i in range(getroffen):
                schuss()
                if i == 0:
                    Schaden = 10
                time.sleep(0.1)
            treffer += getroffen
        schüsse += geschütze
        if werte_gegner_haben_muss[0] <= 0:
            werte_gegner_haben_muss[0] = 0
            print("")
        print(f"Leben {name_gegner}: {werte_gegner_haben_muss[0]}")
        print("")
#endregion





#region >>land_angreifen
    def land_angreifen():
        global werte_gegner_haben_muss
        print("Dein Angriff")
        print("")
        getroffen = skillabfrage(5)
        getroffen = int(getroffen // (30 / eis_leute))
        for i in range(getroffen):
            print(f"{name_gegner} -1")
        werte_gegner_haben_muss[0] -= getroffen
        print(werte_gegner_haben_muss[0])
#endregion





#region >>monster_angriff
    def monster_angriff():
        global crewmitglieder
        global verletzte
        global tote
        global brücke
        global bug
        global heck
        global geschütze
        global schaden_geschütze
        global brücke_schaden
        global bug_schaden
        global heck_schaden
        print(f"{name_gegner} Angriff")
        print("")
        angriffsstelle = random.randint(1,3)
        if angriffsstelle == 1:
            for i in range(random.randint(werte_gegner_haben_muss[1],werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                brücke_schaden += gegn_schaden
                brücke -= gegn_schaden
                print(f"Brücke -{gegn_schaden}")
                time.sleep(0.1)
            if werte_gegner_haben_muss[5] > 5:
                if random.randint(1,17) == 10:
                    schaden_geschütze+=1
                    geschütze-=1
            if werte_gegner_haben_muss[5] > 2:
                if random.randint(1,9) == 6:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
        elif angriffsstelle == 2:
            for i in range(random.randint(werte_gegner_haben_muss[1], werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                bug_schaden += gegn_schaden
                bug -= gegn_schaden
                print(f"Bug -{gegn_schaden}")
                time.sleep(0.1)
            if werte_gegner_haben_muss[5] > 5:
                if random.randint(1,17) == 10:
                    schaden_geschütze+=1
                    geschütze-=1
            if werte_gegner_haben_muss[5] > 2:
                if random.randint(1,9) == 6:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
        else:
            for i in range(random.randint(werte_gegner_haben_muss[1], werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                heck_schaden += gegn_schaden
                heck -= gegn_schaden
                print(f"Heck -{gegn_schaden}")
                time.sleep(0.1)
            if werte_gegner_haben_muss[5] > 5:
                if random.randint(1,6) == 6:
                    tote +=1
                    crewmitglieder -= 1
            if werte_gegner_haben_muss[5] > 2:
                if random.randint(1,3) == 3:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
#endregion





#region >>schiff_angriff
    def schiff_angriff():
        global crewmitglieder
        global verletzte
        global tote
        global brücke
        global bug
        global heck
        global geschütze
        global schaden_geschütze
        global brücke_schaden
        global bug_schaden
        global heck_schaden
        print(f"{name_gegner} Angriff")
        print("")
        angriffsstelle = random.randint(1,3)
        if angriffsstelle == 1:
            for i in range(random.randint(werte_gegner_haben_muss[1],werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                brücke_schaden += gegn_schaden
                brücke -= gegn_schaden
                print(f"Brücke -{gegn_schaden}")
                time.sleep(0.1)
            if werte_gegner_haben_muss[5] > 5:
                if random.randint(1,15) == 10:
                    schaden_geschütze+=1
                    geschütze-=1
            if werte_gegner_haben_muss[5] > 2:
                if random.randint(1,8) == 6:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
        elif angriffsstelle == 2:
            for i in range(random.randint(werte_gegner_haben_muss[1], werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                bug_schaden += gegn_schaden
                bug -= gegn_schaden
                print(f"Bug -{gegn_schaden}")
                time.sleep(0.1)
                if random.randint(1,15) == 10:
                    schaden_geschütze+=1
                    geschütze-=1
                if random.randint(1,6) == 6:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
        else:
            for i in range(random.randint(werte_gegner_haben_muss[1], werte_gegner_haben_muss[2])):
                gegn_schaden = random.randint(werte_gegner_haben_muss[3],werte_gegner_haben_muss[4])
                heck_schaden += gegn_schaden
                heck -= gegn_schaden
                print(f"Heck -{gegn_schaden}")
                time.sleep(0.1)
                if random.randint(1,6) == 6:
                    tote +=1
                    crewmitglieder -= 1
                if random.randint(1,3) == 3:
                    verletzte += 1
                    crewmitglieder -= 1
            print("")
#endregion





#region >>landmonster_angriff
    def landmonster_angriff():
        global verletzte
        global tote
        global auf_eis
        global eis_leute
        global crewmitglieder
        prozent_töten = ((eis_leute+10)/30)*100
        zufallszahl = random.randint(1,100)
        if zufallszahl <= prozent_töten:
            eis_leute -= 1
            crewmitglieder -= 1
            print("Einer deiner Leute wurde getötet.")
            print(f"Einsatzfähige Crewmitglieder auf der Eisscholle: {eis_leute}")
            print(f"Einsatzfähige Crewmitglieder Gesamt: {crewmitglieder}")
        else:
            eis_leute -= 1
            crewmitglieder -= 1
            verletzte += 1
            print("Einer deiner Leute wurde verletzt.")
            print(f"Einsatzfähige Crewmitglieder auf der Eisscholle: {eis_leute}")
            print(f"Einsatzfähige Crewmitglieder Gesamt: {crewmitglieder}")
        if eis_leute == 0:
            auf_eis = False
#endregion





#region >>kampf
    def kampf():

        global zerst_tage
        global zerst_brücke
        global kämpfe
        global andere_dinge
        global bauteile
        global win
        global nahrung
        global treffer
        global schüsse
        global tote
        global verletzte
        global schaden_geschütze
        global brücke_schaden
        global bug_schaden
        global heck_schaden
        global zerstörtes_teil
        kämpfe += 1
        win = None
        treffer = 0
        schüsse = 0
        schaden_geschütze = 0
        brücke_schaden = 0
        bug_schaden = 0
        heck_schaden = 0
        tote = 0
        verletzte = 0
        kämpfen = True
        runde = 2
        zerstörtes_teil = None
        global auf_eis

        print(f"    {schiff_name}  VS  {name_gegner}")
        print("")

        while kämpfen == True:
            if runde % 2 == 0:
                if werte_gegner_haben_muss[9] != "landmonster":
                    aktion = input("Führe eine der folgenden Aktionen durch: 1: Angreifen, 2: Reparieren, 3: Zurückziehen ") 
                    print("")
                    if aktion == "1":
                        wasserangreifen()
                    elif aktion == "2":
                        reparieren()
                    elif aktion == "3":
                        funktioniert = zurückziehen()
                        if funktioniert == 1:
                            kämpfen = False
                            win = None
                    else:
                        print("Keine mögliche Aktion")
                else:
                    land_angreifen()
                    
            else:
                if werte_gegner_haben_muss[9] == "monster":
                    monster_angriff()
                elif werte_gegner_haben_muss[9] == "schiff":
                    schiff_angriff()
                else:
                    landmonster_angriff()
                    if eis_leute == 0:
                        auf_eis = False
                        kämpfen = False
            runde += 1

            if brücke <= 0 or bug <= 0 or heck <= 0:
                win = False
                kämpfen = False
                if brücke <= 0:
                    zerstörtes_teil = "Brücke"
                elif brücke <= 0:
                    zerstörtes_teil = "Bug"
                else:
                    zerstörtes_teil = "Heck"
            elif werte_gegner_haben_muss[0] <= 0:
                werte_gegner_haben_muss[0] = 0
                kämpfen = False
                win = True
            elif geschütze == 0:
                print("Du hast keine funktionierenden Geschütze mehr.")
                print("")
            elif brücke < 100 or bug < 100 or heck < 100:
                if brücke < 100 :
                    print(f"Deine Brücke ist fast zerstört.")
                    print("")
                elif bug < 100:
                    print(f"Dein Bug ist fast zerstört.")
                    print("")
                else:
                    print(f"Dein Heck ist fast zerstört.")
                    print("")

        time.sleep(1)
        print("   Kampfbericht")
        print("")
        time.sleep(0.7)
        if win == True:
            print(f"{name_gegner} wurde besiegt.")
            print("")
        elif win == False:
            print(f"{schiff_name} wurde besiegt.")
            werte_gegner_haben_muss[6] = 0
            werte_gegner_haben_muss[7] = 0
            werte_gegner_haben_muss[8] = []
        else:
            print(f"{schiff_name} hat sich zurückgezogen.")
            print("")
            werte_gegner_haben_muss[6] = 0
            werte_gegner_haben_muss[7] = 0
            werte_gegner_haben_muss[8] = []
        
        nahrung += werte_gegner_haben_muss[6]
        bauteile += werte_gegner_haben_muss[7]
        andere_dinge.append(werte_gegner_haben_muss[8])
        time.sleep(0.7)
        print("Attackierung:")
        time.sleep(0.2)
        print(f"Schüsse {schüsse}")
        time.sleep(0.2)
        print(f"Treffer {treffer}")
        print("")
        time.sleep(0.7)
        print("Verluste:")
        time.sleep(0.2)
        print(f"Tote {tote}")
        time.sleep(0.2)
        print(f"Verletzte {verletzte}")
        print("")
        time.sleep(0.7)
        print("Schaden am Schiff:")
        time.sleep(0.2)
        print(f"Brücke {brücke_schaden}")
        time.sleep(0.2)
        print(f"Bug {bug_schaden}")
        time.sleep(0.2)
        print(f"Heck {heck_schaden}")
        time.sleep(0.2)
        print(f"Geschütze {schaden_geschütze}")
        print("")
        time.sleep(0.7)
        print("Gewonnene Ressoursen:")
        time.sleep(0.2)
        print(f"Nahrung: {werte_gegner_haben_muss[6]}")
        time.sleep(0.2)
        print(f"Bauteile: {werte_gegner_haben_muss[7]}")
        time.sleep(0.2)
        print(f"Anderes: {werte_gegner_haben_muss[8]}")
        time.sleep(2)
        print("")
        if win == False:
            verloren(1)
#endregion





#region >>skillabfrage
    def skillabfrage(anzahl_würfel):
        summe = 0
        runde = 1
        würfel = {}
        sichere_würfel = []
        for i in range(1,anzahl_würfel+1):
            würfel[i]=random.randint(1,6)
        while len(sichere_würfel) < 5 and runde < 4:
            print("Deine Würfel")
            for i in range(anzahl_würfel):
                print(f"Würfel " +str(i+1)+": " +str(würfel[i+1]))
                time.sleep(0.2)
            eingabe = input(f"Welche Würfel wollen sie sichern? Gesicherte Würfel: {sichere_würfel} ")
            print("")
            for i in range(len(eingabe)):
                if not any(y == eingabe[i] for y in sichere_würfel):
                    sichere_würfel.append(eingabe[i])
            for i in range(anzahl_würfel):
                if not any(x == str(i+1) for x in sichere_würfel):
                    würfel[i+1] = random.randint(1,6)
            runde += 1
            sichere_würfel.sort()
            time.sleep(1)
        print("Deine Würfel")
        for i in range(anzahl_würfel):
            print(f"Würfel " +str(i+1)+": " +str(würfel[i+1]))
            time.sleep(0.2)
        for i in range(anzahl_würfel):
            summe += würfel[i+1]
        time.sleep(0.2)
        print(f"Ihre würfelsumme beträgt {summe}.")
        print("")
        return summe
#endregion





#region >>reparieren
    def reparieren():
        global brücke
        global bug
        global heck
        global geschütze
        global bauteile
        reparieren_repeat = True
        while reparieren_repeat == True:
            reparieren_repeat = False
            print(f"Brücke: {brücke}/800   Bug: {bug}/1000   Heck: {heck}/1000   Funktionierende Geschütze: {geschütze}/{MAX_GESCHÜTZE}   Bauteile: {bauteile}")
            print("")
            reparaturstelle = input("Wo am Schiff möchtest du reparien? (1: Brücke, 2: Bug , 3: Heck, 4: Geschütze) ")
            print("")
            if reparaturstelle < "4":
                reparatur_punkte = input(f"Um wie viele Lebenspunkte möchtest du dein Schiff dort reparieren? (1 Bauteil  ->  10 Lebenspunkte) ")
                print("")
                try:
                    reparatur_punkte = int(reparatur_punkte)
                    if reparatur_punkte / 10 <= bauteile:
                        if reparaturstelle == "1":
                            brücke += reparatur_punkte
                            if brücke > 800:
                                brücke = 800
                            print(f"Brücke: {brücke}")
                            print("")
                        if reparaturstelle == "2":
                            bug += reparatur_punkte
                            if bug > 1000:
                                bug = 1000
                            print(f"Bug: {bug}")
                            print("")
                        if reparaturstelle == "3":
                            heck += reparatur_punkte
                            if heck > 1000:
                                heck = 1000
                            print(f"Heck: {heck}")
                            print("")
                        if reparatur_punkte % 10 == 0:
                            bauteile -= reparatur_punkte/10
                        else:
                            bauteile -= reparatur_punkte//10+1
                    else:
                        print("Nicht genügend Bauteile")
                        print("")
                except:
                    print("Keine mögliche Eingabe")
                    print("")
            elif reparaturstelle == "4":
                try:
                    reparatur_punkte = input(f"Wie viele Geschütze willst du Reparieren? (17 Bauteile  ->  1 Geschütz) ")
                    print("")
                    reparatur_punkte = int(reparatur_punkte)
                    if reparatur_punkte * 17 <= bauteile:
                        geschütze += reparatur_punkte
                        bauteile -= reparatur_punkte*17
                        if geschütze > MAX_GESCHÜTZE:
                            geschütze = MAX_GESCHÜTZE
                    else:
                        print("Nicht genügend Bauteile")
                        print("")
                except:
                    print("Keine mögliche Eingabe")
                    print("")
#endregion





#region >>bildschirm
    def bildschirm():
        warten = 0
        bildschirm1 = "Brücke: "+str(brücke)+(70-(8+len(str(brücke))))*" "+schiff_zeichnung1
        bildschirm2 = "Bug: "+str(bug)+(70-(5+len(str(bug))))*" "+schiff_zeichnung2
        bildschirm3 = "Heck: "+str(heck)+(70-(6+len(str(heck))))*" "+schiff_zeichnung3
        bildschirm4 = "funkt. Geschütze: "+str(geschütze)+(70-(18+len(str(geschütze))))*" "+schiff_zeichnung4
        bildschirm5 = über+   "   |   Nahrung: "+str(nahrung)
        bildschirm6 = Map[0]+ "   |   Bauteile: "+str(int((bauteile)))
        bildschirm7 = Map[1]+ "   |   Munition: "+str(munition)
        bildschirm8 = Map[2]+ "   |   davon explos. Mun.: "+str(explosive_mun)
        bildschirm9 = Map[3]+ "   |   Andere Dinge: "+str(andere_dinge)
        bildschirm10 = Map[4]+"   |   Crewmitglieder:"
        bildschirm11 = Map[5]+"   |   verfügbar: "+str(crewmitglieder)
        bildschirm12 = Map[6]+"   |   verletzt: "+str(verletzte) 

        print(bildschirm1)
        time.sleep(warten)
        print(bildschirm2)
        time.sleep(warten)
        print(bildschirm3)
        time.sleep(warten)
        print(bildschirm4)
        time.sleep(warten)
        print(130*"-")
        time.sleep(warten)
        print(bildschirm5)
        time.sleep(warten)
        print(bildschirm6)
        time.sleep(warten)
        print(bildschirm7)
        time.sleep(warten)
        print(bildschirm8)
        time.sleep(warten)
        print(bildschirm9)
        time.sleep(warten)
        print(bildschirm10)
        time.sleep(warten)
        print(bildschirm11)
        time.sleep(warten)
        print(bildschirm12)
        time.sleep(warten)
        print("")
#endregion





#region >>karte aktualisieren
    def karte_aktualisieren(bewegung):
        global Map

        if bewegung == "1":#oben
            Map[pos_schiff[0]+1] = Map[pos_schiff[0]+1] [:pos_schiff[1]*3-1] + "_"+ Map[pos_schiff[0]+1] [pos_schiff[1]*3:]
            Map[pos_schiff[0]] = Map [pos_schiff[0]] [:pos_schiff[1]*3-1] + "X" + Map [pos_schiff[0]] [pos_schiff[1]*3:]
        elif bewegung == "2":#rechts
            Map[pos_schiff[0]] = Map [pos_schiff[0]] [:pos_schiff[1]*3-4] + "_|_"+ "X" + Map [pos_schiff[0]] [pos_schiff[1]*3:]
        elif bewegung == "3":#unten
            Map[pos_schiff[0]-1] = Map[pos_schiff[0]-1] [:pos_schiff[1]*3-1] + "_"+ Map[pos_schiff[0]-1] [pos_schiff[1]*3:]
            Map[pos_schiff[0]] = Map [pos_schiff[0]] [:pos_schiff[1]*3-1] + "X" + Map [pos_schiff[0]] [pos_schiff[1]*3:]
        elif bewegung == "4":#link
            Map[pos_schiff[0]] = Map [pos_schiff[0]] [:pos_schiff[1]*3-1] + "X" + "|__"+ Map [pos_schiff[0]] [pos_schiff[1]*3+3:]
#endregion





#region >>bewegen
    def bewegen():
        global name_gegner
        global pos_schiff
        bewegung = input("Führe eine Bewegung aus. (oben: 1, rechts: 2, unten: 3, links: 4) ")
        print("")
        if bewegung == "1":
            pos_schiff[0] -= 1
        elif bewegung == "2":
            pos_schiff[1] += 1
        elif bewegung == "3":
            pos_schiff[0] += 1
        elif bewegung == "4":
            pos_schiff[1] -= 1

        if pos_schiff[0] < 0:
            pos_schiff[0]+=1
        elif pos_schiff[0] > 6:
            pos_schiff[0]-=1
        elif pos_schiff[1] < 1:
            pos_schiff[1]+=1
        elif pos_schiff[1] > 30:
            print("Ihr habt an das Festland angelegt.")
            festland()
        elif pos_u_boot == pos_schiff and story == 3:
            if spielzug > 12:
                name_gegner = "U-Boot"
                werte_gegner_haben_muss[0] = 1000
                werte_gegner_haben_muss[1] = 2
                werte_gegner_haben_muss[2] = 6
                werte_gegner_haben_muss[3] = 35
                werte_gegner_haben_muss[4] = 70
                werte_gegner_haben_muss[5] = 9
                werte_gegner_haben_muss[6] = 0
                werte_gegner_haben_muss[7] = 0
                werte_gegner_haben_muss[8] = []
                werte_gegner_haben_muss[9] = "schiff"
                kampf()
            print("")
        karte_aktualisieren(bewegung)
        auf_ereignis()
#endregion





#region >>eisscholle
    def eisscholle():
        global andere_dinge
        global munition
        global explosive_mun
        global bauteile
        global nahrung
        global zerst_brücke
        global auf_eis
        global schiff_name
        global eisbär_position
        global truhe_position
        global eis_position
        global Schaden
        global brücke
        global eis_leute
        global geschütze
        print("Ihr seid auf eine Eisscholle getroffen.")
        print("")
        if zerst_brücke == True and bauteile >= 80:
            print("Brücke für 80 Bauteile repariert")
            print("")
            brücke = 800
            zerst_brücke = False
            bauteile -= 80
        elif zerst_brücke == True:
            print("Zu wenig Bauteile um die Brücke zu reparieren.")
            print("Bauteile benötigt : 80")
            print(f"Bauteile in besitz {bauteile}")
        gemerk_schiff_name = schiff_name
        schiff_name = "Kapitän " + nachname
        auf_eis = True
        eis_leute = int(input("Wie viele Crewmitglieder möchtest du auf die Eisscholle mitnehmen? (max 10, min 2) "))
        if eis_leute > 10:
            eis_leute = 10
        elif eis_leute < 2:
            eis_leute = 2
        zufallszahl = random.randint(1,2)
        if zufallszahl == 1:
            eis_position = [3,4]
        else:
            eis_position = [2,4]
        eisbär_position = [random.randint(0,3),random.randint(0,12)]
        truhe_position = [random.randint(0,3),random.randint(0,12)]
        
        if zufallszahl == 1:
            if eisbär_position[0] == -1:
                eisbär_position[0] += 1
            elif eisbär_position[0] == 0:
                if eisbär_position[1] <= 3:
                    eisbär_position[1] = 4
                elif eisbär_position[1] >= 10:
                    eisbär_position[1] = 9
            elif eisbär_position[0] == 1:
                if eisbär_position[1] <= 0:
                    eisbär_position[1] = 1
                elif eisbär_position[1] >= 11:
                    eisbär_position[1] = 10
            elif eisbär_position[0] == 2:
                if eisbär_position[1] <= 1:
                    eisbär_position[1] = 2
                elif eisbär_position[1] >= 11:
                    eisbär_position[1] = 10
            elif eisbär_position[0] == 3:
                if eisbär_position[1] <= 3:
                    eisbär_position[1] = 5
                elif eisbär_position[1] >= 6:
                    eisbär_position[1] = 5
        else:
            if eisbär_position[0] == -1:
                eisbär_position[0] += 1
            elif eisbär_position[0] == 0:
                if eisbär_position[1] <= 1:
                    eisbär_position[1] = 2
                elif eisbär_position[1] >= 9:
                    eisbär_position[1] = 8
            elif eisbär_position[0] == 1:
                if eisbär_position[1] <= 0:
                    eisbär_position[1] = 1
                elif eisbär_position[1] >= 10:
                    eisbär_position[1] = 9
            elif eisbär_position[0] == 2:
                if eisbär_position[1] <= 3:
                    eisbär_position[1] = 6
                elif eisbär_position[1] >= 9:
                    eisbär_position[1] = 8
            elif eisbär_position[0] == 3:
                if eisbär_position[1] <= 3:
                    eisbär_position[1] = 4
                elif eisbär_position[1] >= 8:
                    eisbär_position[1] = 7

        if zufallszahl == 1:
            if truhe_position[0] == -1:
                truhe_position[0] += 1
            elif truhe_position[0] == 0:
                if truhe_position[1] <= 3:
                    truhe_position[1] = 4
                elif truhe_position[1] >= 10:
                    truhe_position[1] = 9
            elif truhe_position[0] == 1:
                if truhe_position[1] <= 0:
                    truhe_position[1] = 1
                elif truhe_position[1] >= 11:
                    truhe_position[1] = 10
            elif truhe_position[0] == 2:
                if truhe_position[1] <= 1:
                    truhe_position[1] = 2
                elif truhe_position[1] >= 11:
                    truhe_position[1] = 10
            elif truhe_position[0] == 3:
                if truhe_position[1] <= 3:
                    truhe_position[1] = 5
                elif truhe_position[1] >= 6:
                    truhe_position[1] = 5
        else:
            if truhe_position[0] == -1:
                truhe_position[0] += 1
            elif truhe_position[0] == 0:
                if truhe_position[1] <= 1:
                    truhe_position[1] = 2
                elif truhe_position[1] >= 9:
                    truhe_position[1] = 8
            elif truhe_position[0] == 1:
                if truhe_position[1] <= 0:
                    truhe_position[1] = 1
                elif truhe_position[1] >= 10:
                    truhe_position[1] = 9
            elif truhe_position[0] == 2:
                if truhe_position[1] <= 3:
                    truhe_position[1] = 6
                elif truhe_position[1] >= 9:
                    truhe_position[1] = 8
            elif truhe_position[0] == 3:
                if truhe_position[1] <= 3:
                    truhe_position[1] = 4
                elif truhe_position[1] >= 8:
                    truhe_position[1] = 7
            else:
                eis_position[0] = 3

        eisscholle_anzeigen(zufallszahl)
        global name_gegner
        global werte_gegner_haben_muss
        print("")
        while auf_eis == True:
            if eis_leute == 0:
                auf_eis == False
            richtung = input("In welche Richtung möchtest du laufen?(1 Oben, 2 Rechts, 3 unten, 4 Links) ")
            print("")
            if richtung == "1":
                eis_position[0] -= 1
            elif richtung == "2":
                eis_position[1] += 1
            elif richtung == "3":
                eis_position[0] += 1
            elif richtung == "4":
                eis_position[1] -= 1
            if eisbär_position == eis_position:
                eisbär_position = [0,0]
                print("du bist auf einen Eisbär gestoßen?")
                name_gegner = "mutierter Eisbär"
                leben_gegner = random.randint(11,15)
                min_gegn_angriffe = 1
                max_gegn_angriffe = 2
                minschaden = 3
                maxschaden = 5
                gegner_macht = 4
                fallenlassende_nahrung = 15
                fallenlassende_bauteile = 0
                fallenlassende_andere_dinge = []
                typ = "landmonster"
                werte_gegner_haben_muss = [leben_gegner,min_gegn_angriffe,max_gegn_angriffe,minschaden,maxschaden,gegner_macht,fallenlassende_nahrung,fallenlassende_bauteile,fallenlassende_andere_dinge,typ]
                kampf()
            elif truhe_position == eis_position:
                truhe_position = [0,0]
                nahrung_truhe = random.randint(40,80)
                bauteile_truhe = random.randint(15,35)
                munition_truhe = random.randint(0,30)
                print("Sie sind auf eine Truhe gestoßen.")
                print("inhalt: ")
                print(f"Nahrung: {nahrung_truhe}")
                print(f"Bauteile: {bauteile_truhe}")
                print(f"Munition: {munition_truhe}")
                nahrung += nahrung_truhe
                bauteile += bauteile_truhe
                munition += munition_truhe
                rand_zahl = random.randint(0,1)
                if rand_zahl == 1:
                    gegenstand = mögliche_andere_gegenstände[random.randint(0,len(mögliche_andere_gegenstände)-1)]
                    print(f"Sonstiges: {gegenstand}")
                    if gegenstand[4:] == "explosive Munition":
                        explosive_mun += int(gegenstand[:2])
                        munition += int(gegenstand[:2])
                    else:
                        andere_dinge.append(gegenstand)
            if zufallszahl == 1:
                if eis_position[0] == -1:
                    eis_position[0] += 1
                elif eis_position[0] == 0:
                    if eis_position[1] <= 3:
                        eis_position[1] = 4
                    elif eis_position[1] >= 10:
                        eis_position[1] = 9
                elif eis_position[0] == 1:
                    if eis_position[1] <= 0:
                        eis_position[1] = 1
                    elif eis_position[1] >= 11:
                        eis_position[1] = 10
                elif eis_position[0] == 2:
                    if eis_position[1] <= 1:
                        eis_position[1] = 2
                    elif eis_position[1] >= 11:
                        eis_position[1] = 10
                elif eis_position[0] == 3:
                    if eis_position[1] <= 3:
                        auf_eis = False
                        schiff_name = gemerk_schiff_name
                    elif eis_position[1] >= 6:
                        eis_position[1] = 5
                else:
                    eis_position[0] = 3
            else:
                if eis_position[0] == -1:
                    eis_position[0] += 1
                elif eis_position[0] == 0:
                    if eis_position[1] <= 1:
                        eis_position[1] = 2
                    elif eis_position[1] >= 9:
                        eis_position[1] = 8
                elif eis_position[0] == 1:
                    if eis_position[1] <= 0:
                        eis_position[1] = 1
                    elif eis_position[1] >= 10:
                        eis_position[1] = 9
                elif eis_position[0] == 2:
                    if eis_position[1] <= 3:
                        auf_eis = False
                        schiff_name = gemerk_schiff_name
                    elif eis_position[1] >= 9:
                        eis_position[1] = 8
                elif eis_position[0] == 3:
                    if eis_position[1] <= 3:
                        eis_position[1] = 4
                    elif eis_position[1] >= 8:
                        eis_position[1] = 7
                else:
                    eis_position[0] = 3

            eisscholle_anzeigen(zufallszahl)
#endregion





#region >>hinweis
    def hinweis():
        print("")
        print("Ihr seid auf einen Hinweis gestoßen")
        print(f"Hinweis:")
        if story == 1:
            print(story1_hinweise[welcher_hinweis])
        elif story == 2:
            print(story2_hinweise[welcher_hinweis])
        else:
            print(story3_hinweise[welcher_hinweis])
        print("")
#endregion





#region >>auf_ereignis
    def auf_ereignis():
        global welcher_hinweis
        global name_gegner
        global auf_pos
        global nahrung
        global bauteile
        global munition
        global explosive_mun
        global andere_dinge
        name_sache = None
        auf_pos = len(positionen)
        for i in range(len(positionen)):
            if pos_schiff[0] == list(x_pos.values())[i] and pos_schiff[1] == list(positionen.values())[i]:
                richtiger_name_sache = list(positionen.keys())[i]
                name_sache = richtiger_name_sache[:len(richtiger_name_sache)-1]
        if name_sache != None:
            if any(x == name_sache for x in werte_gegner):
                name_gegner = name_sache
                for i in range(10):
                    werte_gegner_haben_muss[i] = [list(werte_gegner[name_gegner].values())[i]]
                    werte_gegner_haben_muss[i] = werte_gegner_haben_muss[i][0]
                positionen.pop(richtiger_name_sache)
                kampf()
            if name_sache == "hinweis":
                positionen.pop(richtiger_name_sache)
                name_sache = name_sache[:7]
                hinweis()
                welcher_hinweis += 1
            if name_sache == "eisscholle":
                name_sache = name_sache[:10]
                eisscholle()

        else:
            zufallszahl = random.randint(1,100)
            if zufallszahl <= 15:
                time.sleep(0.2)
                print("Im Wasser sind undeutlich Umrisse erkennbar. Kurz seht ihr etwas aus dem Wasser kommen, dann plötzlich ein Wummern gegen den Rumpf")
                time.sleep(0.2)
                print("'Da ist etwas im Wasser'")
                time.sleep(0.2)
                print("")
                zufallszahl = random.randint(1,len(monsternamen))
                zufallszahl -= 1
                name_gegner = monsternamen[zufallszahl]
                werte_gegner_haben_muss[0] = random.randint(100,240)
                werte_gegner_haben_muss[1] = random.randint(1,2)
                werte_gegner_haben_muss[2] = random.randint(4,5)
                werte_gegner_haben_muss[3] = random.randint(5,12)
                werte_gegner_haben_muss[4] = random.randint(15,28)
                werte_gegner_haben_muss[5] = (werte_gegner_haben_muss[0]//100+werte_gegner_haben_muss[1]+werte_gegner_haben_muss[2]+werte_gegner_haben_muss[3]+werte_gegner_haben_muss[4])//5
                werte_gegner_haben_muss[6] = werte_gegner_haben_muss[0]//8
                werte_gegner_haben_muss[7] = 0
                werte_gegner_haben_muss[8] = []
                werte_gegner_haben_muss[9] = "monster"
                kampf()
            elif zufallszahl <= 20:
                truhe = [random.randint(0,100),random.randint(0,20)]
                print("Ihr habt eine Truhe mit Sachen drin gefunden")
                print("Inhalt:")
                print(f"Essen {truhe[0]}")
                print(f"Bauteile {truhe[1]}")
                print("")
            elif zufallszahl <=32:
                nahrung_truhe = random.randint(40,80)
                bauteile_truhe = random.randint(15,35)
                munition_truhe = random.randint(0,30)
                print("Sie sind auf eine Truhe gestoßen.")
                print("inhalt: ")
                print(f"Nahrung: {nahrung_truhe}")
                print(f"Bauteile: {bauteile_truhe}")
                print(f"Munition: {munition_truhe}")
                nahrung += nahrung_truhe
                bauteile += bauteile_truhe
                munition += munition_truhe
                rand_zahl = random.randint(1,2)
                if rand_zahl == 1:
                    gegenstand = mögliche_andere_gegenstände[random.randint(0,len(mögliche_andere_gegenstände)-1)]
                    print(f"Sonstiges: {gegenstand}")
                    if gegenstand[4:] == "explosive Munition":
                        explosive_mun += int(gegenstand[:2])
                        munition += int(gegenstand[:2])
                    else:
                        andere_dinge.append(gegenstand)
                
                print("")
#endregion





#region >>verloren
    def verloren(grund):
        global spielen
        print("    Missionsbericht")
        print("")
        print("Mission gescheitert")
        if grund == 1:
            print(f"{schiff_name} gesunken nach zu starker Beschädigung.")
        elif grund == 2:
            print("Alle Crewmitglieder verstorben.")
        bericht()

        spielen = False
#endregion





#region >>eisscholle_anzeigen
    def eisscholle_anzeigen(zufallszahl):
        if zufallszahl == 1:
            eis =  r"    ______   "
            eis0 = r" __/      \  "
            eis1 = r"|          | "
            eis2 = r" \_    ____/ "
            eis3 = r"  X\__/      "
        else:
            eis =  r"  _______   "
            eis0 = r"_/       \  "
            eis1 = r"\___      | "
            eis2 = r"  X/     /  "
            eis3 = r"   \____/   "
        Eis = [eis0,eis1,eis2,eis3]
        Eis[eisbär_position[0]] = Eis[eisbär_position[0]] [:eisbär_position[1]] + "#" + Eis[eisbär_position[0]][eisbär_position[1] + 1:]
        Eis[truhe_position[0]] = Eis[truhe_position[0]] [:truhe_position[1]] + "#" + Eis[truhe_position[0]][truhe_position[1] + 1:]

        Eis[eis_position[0]] = Eis[eis_position[0]] [:eis_position[1]] + "*" + Eis[eis_position[0]][eis_position[1] + 1:]
        print(eis)
        for i in range(0,4):
            print(Eis[i])
        print("")
#endregion





#region >>gewinn
    def gewinn():
        global spielen
        print("    Missionsbericht")
        print("")
        print("Mission erfüllt")
        if story == 1:
            print("Die Krake die den Telepermer genommen hat wurde besiegt.")
        elif story == 2:
            print("Du konntest einen Funkspruch aussprechen und dein Land warnen.")
        else:
            print("Das Feindliche U-Boot wurde zerstört.")
        print("")
        print("Du konntest die Mission erfüllen und das Militärische Gleichgewicht wieder herstellen. Kurz danach wurde von beiden Seiten ein Friedensvertrag unterzeichnet.")
        bericht()

        spielen = False
#endregion





#region >>festland
    def festland():
        global pos_schiff
        global munition
        global bauteile
        global zerst_brücke
        global brücke
        vorhand_mun = 60
        übr_rak = 8
        umgeb1  =  "So sieht die Umgebung aus"
        umgeb2  = r"       _________ "
        umgeb3  = r"    __/         \__ "
        umgeb4  = r"  _/   \     * /   \_"
        umgeb5  = r" / *    \     /      \ "
        umgeb6  = r"|   *    \   /        | "
        umgeb7  = r"|--------  #  --------| "
        umgeb8  = r"|        /   \     *  | "
        umgeb9  = r" \_     /   * \     _/ "
        umgeb10 = r"   \__ /   * * \ __/ "
        umgeb11 = r"      \_________/ "
        zielscheibe1  = " __________________________"
        zielscheibe2  = "|   ____________________   |"
        zielscheibe3  = "|  |   ______________   |  |"
        zielscheibe4  = "|  |  |   ________   |  |  |"
        zielscheibe5  = "|  |  |  |   __   |  |  |  |"
        zielscheibe6  = "|  |  |  |  |__|  |  |  |  |"
        zielscheibe7  = "|  |  |  |________|  |  |  |"
        zielscheibe8  = "|  |  |______________|  |  |"
        zielscheibe9  = "|  |____________________|  |"
        zielscheibe10 = "|__________________________|"
        zielscheibe = [zielscheibe1,zielscheibe2,zielscheibe3,zielscheibe4,zielscheibe5,zielscheibe6,zielscheibe7,zielscheibe8,zielscheibe9,zielscheibe10]
        schussfeld0 = r"  1__2__3__4__5__6__7_ "
        schussfeld1 = r"1|__|__|__|__|__|__|__|"
        schussfeld2 = r"2|__|__|__|__|__|__|__|"
        schussfeld3 = r"3|__|__|__|/\|__|__|__|"
        schussfeld4 = r"4|__|__|<[ [] ]>|__|__|"
        schussfeld5 = r"5|__|__|__|\/|__|__|__|"
        schussfeld6 = r"6|__|__|__|__|__|__|__|"
        schussfeld7 = r"7|__|__|__|__|__|__|__|"
        schussfeld = [schussfeld0,schussfeld1,schussfeld2,schussfeld3,schussfeld4,schussfeld5,schussfeld6,schussfeld7]

        print("Du bist in dem Stützpunkt.")
        print("")
        if zerst_brücke == True and bauteile >= 80:
            print("Brücke für 80 Bauteile repariert")
            print("")
            brücke = 800
            zerst_brücke = False
            bauteile -= 80
        elif zerst_brücke == True:
            print("Zu wenig Bauteile um die Brücke zu reparieren.")
            print("Bauteile benötigt : 80")
            print(f"Bauteile in besitz {bauteile}")
        stützpunkt = True
        while stützpunkt == True:
            waff_kam = False
            komm_zen = False
            bew = input("Du kannst zu einen dieser Orte gehen: 1: zurück aufs Wasser, 2: Waffenkammer, 3: Kommando-Zentrale ")
            print("")
            if bew == "1":
                pos_schiff[1] = 30
                stützpunkt = False
            elif bew == "2":
                waff_kam = True
                print("Du bist jetzt in der Waffenkammer.")
                print("")

            elif bew == "3":
                komm_zen = True
                print("Du bist jetzt in der Kommando-Zentrale.")
                print("")

            while waff_kam == True:
                aktion = input("Du kannst nun eine dieser Aktionen durchführen: 1: Zurückgehen, 2: Munition nehmen, 3: Zielschiessen")
                print("")
                if aktion == "1":
                    waff_kam = False
                elif aktion == "2":
                    genommunition = int(input(f"Wie viel Munition möchtest du dir nehmen? ({vorhand_mun} übrig)"))
                    if genommunition > vorhand_mun:
                        genommunition = vorhand_mun
                    if genommunition < 0:
                        genommunition = 0
                    print("")
                    munition+=genommunition
                    vorhand_mun-=genommunition
                    print(f"{genommunition} munition genommen.")
                    print("")
                elif aktion == "3":
                    zielschiessen = True
                    for i in range(10):
                        print(zielscheibe[i])
                    print("")
                    while zielschiessen == True:
                        schuss = input("wo möchtest du hinschiessen? (X-Position un dann mit komma getrennt Y-Position) ")
                        print("")
                        try:
                            trenn = schuss.find(",")
                            x_schuss = schuss[:trenn]
                            y_schuss = schuss[trenn+1:]
                            x_schuss = int(x_schuss)
                            y_schuss = int(y_schuss)
                            zielscheibe[y_schuss] = zielscheibe[y_schuss][:x_schuss]+"+"+zielscheibe[y_schuss][x_schuss+1:]
                            print("Schuss")
                            for i in range(10):
                                print(zielscheibe[i])
                        except:
                            zielschiessen = False
                    
            while komm_zen == True:
                aktion = input("Du kannst eine dieser Aktionen durchführen: 1: Zurückgehen, 2: Aufs Radar Schauen, 3: Funken, 4: Raketen abschießen ")
                print("")
                if aktion == "1":
                    komm_zen = False
                elif aktion == "2":
                    print(umgeb1)
                    print(umgeb2)
                    print(umgeb3)
                    print(umgeb4)
                    print(umgeb5)
                    print(umgeb6)
                    print(umgeb7)
                    print(umgeb8)
                    print(umgeb9)
                    print(umgeb10)
                    print(umgeb11)
                    print("")
                    print("")
                elif aktion == "3":
                    if story == 2 and welcher_hinweis < 2:
                        win()
                elif aktion == "4":
                    raketen_feuern = True
                    print(f"übrige Raketen: {übr_rak}")
                    for i in range(8):
                        print(schussfeld[i])
                    while raketen_feuern == True:
                        print(f"übrige Raketen: {übr_rak}")
                        print("")
                        x_schuss = 0
                        y_schuss = 0
                        gefeu_ort = input("Wo möchtest du hinschießen? (erst X-Position und dann direkt dahinter Y-Position) ")
                        try:
                            x_schuss = int(gefeu_ort[0])
                            y_schuss = int(gefeu_ort[1])
                        except ValueError:
                            print("verfehlt")
                            print("")

                        if y_schuss == 3 and x_schuss == 4:
                            print("Du kannst nicht auf dich selbst schießen")
                            print("")
                        elif y_schuss == 4 and (x_schuss == 3 or x_schuss == 4 or x_schuss == 5):
                            print("Du kannst nicht auf dich selbst schießen")
                            print("")
                        elif y_schuss == 5 and x_schuss == 4:
                            print("Du kannst nicht auf dich selbst schießen")
                            print("")
                        elif übr_rak < 1:
                            print("Keine Raketen übrig")
                            raketen_feuern = False
                        elif x_schuss<8 and x_schuss>0 and y_schuss<8 and y_schuss>0:
                            time.sleep(0.1)
                            print("Rakete vorbereiten...")
                            time.sleep(4)
                            print("FEUER")
                            print("")
                            time.sleep(0.2)
                            x_schuss = x_schuss*3-1
                            schussfeld[y_schuss] = schussfeld[y_schuss][:x_schuss]+"##"+schussfeld[y_schuss][x_schuss+2:]
                            for i in range(8):
                                print(schussfeld[i])
                            time.sleep(2)
                            print("")
                            print("")
                            übr_rak -= 1
                        else:
                            raketen_feuern = False
#endregion
        




#region >>zurückziehen
    def zurückziehen():
        zufallszahl = random.randint(1,5)
        if zufallszahl <= 3:
            print("Zurückziehen Erfolgreich")
            zufallszahl = random.randint(1,10)
            if werte_gegner_haben_muss[5] >= zufallszahl:
                print(f"Allerdings konnte dich {name_gegner} noch einmal angreifen.")
                print("")
                if werte_gegner_haben_muss[9] == "monster":
                    monster_angriff()
                else:
                    schiff_angriff()
            return 1
        else:
            print("Zurückziehen Fehlgeschlagen")
            print("")
            return 0
#endregion





#region >>bericht
    def bericht():
        print("")
        print(f"Züge gesamt : {spielzug}")
        print("")
        print(f"Dein Name : {voller_name}")
        print("")
        print(f"Name deines Schiffes : {schiff_name}")
        print("")
        print(f"Name der Mission : {mission_name}")
        print("")
        print(f"Übrige Besatzung : {crewmitglieder+verletzte}")
        print("")
        print(f"Kämpfe : {kämpfe}")
        print("")
        print("Schiff:")
        print(f"Brücke : {brücke}")
        print(f"Bug : {bug}")
        print(f"Heck : {heck}")
        print(f"übrige Geschütze : {geschütze}")
        print("")
#endregion

#endregion

#endregion










#region Spieleinleitung






#region >Regelwerk

    print("")
    print("")
    print("")
    print("")
    abfrage = input("Brauchen sie ein Regelwerk? (ja oder nein) ")
    print("")

    if abfrage == "ja":
        print("Okay, Drücke einmal auf die enter Taste wenn du einen Abschnitt fertig gelesen hast, um den nächsten anzeigen zu lassen.(NUR IM REGELWERK)")
        print("")
        input("")
        print("Ganz am Anfang wollen wir ein paar grundlegende Sachen von dir abfragen.")
        print("Dies sind dein Name, wie dein Schiff heißen soll, die Schwierigkeit und wie die Mission heißen soll auf der du dich während des Spiels befindest.")
        print("Dabei kannst du, außer bei der Schwierigkeit, entweder selbst etwas eingeben oder dir den Namen zufällig auswählen lassen.")
        print("Dafür drückst du statt etwas einzugeben einfach die enter Taste. Wenn dir der Ausgewählte Name gefällt, kannst du in mit 'okay' bestätigen. Andernfalls kannst du einfach noch einmal die enter Taste drücken oder selbst etwas eingeben.")
        print("")
        input("")
        print("In dem Spiel bewegst du dich über eine Karte.")
        print("Diese geht von X : 1 bis 30, Y : 1 bis 7 und sieht etwa so aus:")
        print("")
        print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ KARTE __ __ __ __ __ __ __ __ __ __ __ __ __ __ F")
        print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|__|__|__|__|#_|__|__|__|__|e")
        print("|__|__|__|_#|__|__|__|_#|__|__|__|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|__|__|__|__|s")
        print("|__|__|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|_#|__|__|_#|__|__|_#|__|__|__|__|_#|__|t")
        print("|_X|__|__|_#|__|__|__|__|_#|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|__|__|__|__|__|__|l")
        print("|__|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|_#|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|a")
        print("|__|_#|__|__|__|__|_#|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|n")
        print("|__|__|__|__|__|__|__|__|__|__|__|__|__|_#|__|__|__|__|__|_#|__|__|__|__|__|__|_#|__|__|__|d")
        print("")
        print("Die # bedeuten das an dieser Stelle Irgendetwas ist. Das kann ein Gegner sein, eine Eisscholle oder ein Hinweis.")
        input("")
        print("In einem Zug musst du immer erst eine Bewegung machen und dann zwischen einer von verschiedenen Aktionen wählen.")
        print("Beim bewegen musst du eine Zahl von 1 bis 4 eingeben um dich nach: 1, : oben, 2 : rechts, 3 : unten, 4 : links zu bewegen.")
        print("Bei der darauffolgenden Aktion kannst du zwischen 1 : reparieren, 2 : einem extra Zug, 3 : Crew heilen wählen. Deine Crew heilt aber auch, ohne das du heilen als Aktion wählst, langsam.")
        print("")
        input("")
        print("Beim Bewegen auf der Karte kann es sein das du auf einen Gegner triffst.")
        print("Dies kann passieren wenn die auf ein # gehst aber schwache Gegner können auch so auftauchen.")
        print("Bei einem Kampf sind immer du und dein Gegner abwechselnd dran.")
        print("Wenn du dran bist, kannst du zwischen 3 Aktionen wählen: angreifen, reparieren, zurückziehen.")
        print("Wenn du reparierst, kannst du entweder deine Brücke, dein Bug, dein Heck oder deine Geschütze reparieren. Dafür werden Bauteile benötigt, von denen man am Anfang schon welche hat, sie aber auch im Spiel erwerben kann.")
        print("Wenn du dich zurückziehst, zum Beispiel weil du nicht mehr so viele Leben hast, verlierst du den kampf, wirst aber nicht zerstört. Doch vorsicht! Zurückziehen funktioniert nicht immer direkt beim ersten mal, und selbst wenn bist du noch nicht direkt sicher.")
        print("")
        input("")
        print("Wenn du angreifst, kriegst du 5 würfel die eine zufällige Zahl von 1 bis 6 zeigen. Von denen kannst du nun beliebige 'sichern'. Die Würfel die du gesichert hast, werden nicht noch einmal gewürfelt, der Rest aber schon. Dies wiederholt sich 3 runden lang, oder bis alle Würfel 'gesichert' sind. Die Summe der Würfel am Ende bestimmt wie häufig du triffst.")
        print("")
        print("Wenn der Gegner dran ist greift er dein Schiff entweder an der Brücke, am Bug oder am Heck an. dabei greift er nicht immer gleich häufig an und macht auch nicht immer gleich viel Schaden, Stärkere Gegner greifen allerdings häufiger an und machen dabei auch mehr Schaden. bei einem Gegnerischen Angriff kann es je nach Typ des Gegners (Monster, Schiff oder Monster an Land) und je nach stärke des Gegners auch Geschütze zerstören oder Menschen verletzten oder ganz Töten.")
        print("")
        input("")
        print("Außer Gegnern kannst du bei den # auch noch Eisschollen und Hinweisen begegnen.")
        print("Wenn du auf eine Eisscholle triffst, kannst du sie Erkunden gehen. Auf jeder Eisscholle befinden sich zwei #. Das eine ist ein Gegner an Land(Landgegner haben andere Attacken, und werden anders angegriffen.), und das Andere ist eine Truhe mit Sachen drin. UM wieder zurück zum Schiff zu gelangen, muss man zurück zu X gehen.")
        print("")
        print("Zuletzt kann man auch auf Hinweise stoßen. Hinweise verraten einem was man genau machen muss um die Mission zu erfüllen. Die Bedingungen zur erfüllung der Mission können unterschiedlich sein und damit auch die Hinweise.")
        print("")
        input("")
        print("Jeden Zug, nachdem du die Aktion ausgeführt hast, müssen deine Crewmitglieder essen. Dabei verbraucht jedes Crewmitglied genau ein Nahrung.")
        print("Aber keine Sorge neue Nahrung Kannst du z.B. Durch besiegen von Gegner, aber auch auf Eisschollen bekommen.")
        print("")
        print("Jedes mal wenn du schießt, verbrauchst du genau eine Munition. Zusätzliche kann man auch auf Eisschollen finden.")
        print("")
        input("WICHTIGER HINWEIS: niemals häufiger als einmal auf die enter Taste drücken. In der Einleitung muss man, außer wenn du gerade etwas eingeben sollst, kurz warten bis es weitergeht. Wenn ihr dort schon etwas eingebt, gilt es schon für den nächsten Schritt!")

        


#endregion







#region >Einleitung
    einleitung = input("Brauchen sie eine Einleitung? (ja oder nein) ")
    print("")

    if einleitung == "ja":
        print("(Einleitung)")
        print("Wir Schreiben das Jahr 2075. Nach immer mehr Spannungen zwischen den Großmächten Russland und Amerika, rüsten beide jetzt so rapide wie möglich auf. " \
        "Während Russland seine Bomben auf abgelegenen Inseln testet, hat Amerika die Arktis als ihren Testort und Hauptstützpunkt eingenommen. " \
        "Seit den fünf Tagen seit denen sich A1-alpha-57 nicht mehr gemeldet hat, herrscht in Amerika Panik. Wenn Russland jetzt angreifen würde, " \
        "hätte Amerika nichts zur Verteidigung. Drohnen die das verstrahlte Gebiet überquert haben konnten den Stützpunkt ganz normal sehen, " \
        "aber nicht hinein. Doch nun soll eine bemannte Mission gestartet werden.")
        time.sleep(20)
        print("...")
        print("")
#endregion






#region >Missionsname auswählen
    time.sleep(1)
    mission_name = input("Wie soll eure Mission heißen? (enter Taste um den Namen zufällig auswählen zu lassen.) ")
    print("")

    if mission_name == "":
        rand_name = True
        rand_mission_name = "Mission "+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"-"+str(random.randint(0,9))+str(random.randint(0,9))
        print(rand_mission_name)
        print("")

    while rand_name == True:
        mission_name = input("Wie soll eure Mission heißen? (enter Taste um den Namen erneut zufällig auswählen zu lassen, 'okay' um den ausgewählten Namen zu benutzen.) ")
        print("")
        if mission_name == "okay":
            mission_name = rand_mission_name
            rand_name = False
        elif mission_name == "":
            rand_mission_name = "Mission "+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"-"+str(random.randint(0,9))+str(random.randint(0,9))
            print("")
            print(rand_mission_name)
            print("")
        else:
            rand_name = False
#endregion






#region >Geschichte nach Missionsname
    time.sleep(0.5)
    print("(Geschichte)")
    time.sleep(0.5)
    print("Stimme1: 'Und? wie weit sind sie mit der Lösung des ... Problems.'")
    time.sleep(2)
    print("Stimme2: 'Nun Ja, bisher habe ich ein paar geeignete Leute und ein Schiff bekommen können.'")
    time.sleep(2.5)
    print(f"Stimme1: 'Gut, das alles muss streng geheim bleiben. Okay? Hier sind alle Unterlagen für {mission_name}")
    time.sleep(4)
    print("(Schritte)")
    time.sleep(0.5)
    print("Um die Ecke kommt ein Großer, Breiter Mann. Er trägt die Uniform des Militärs und unter seiner rechten Schulter sieht man das Symbol, " \
    "das zeigt dass er Verteidigungsminister ist,leuchten. Hinter ihm erscheinen zwei Soldaten und ein kleiner Mann mit Papieren in der Hand.")
    time.sleep(7)
    print("'In drei Tagen wird das Schiff bereit sein zum Aufbruch'")
    print("")
#endregion







#region >Schiffnamen auswählen
    time.sleep(1)
    schiff_name = input("Wie soll euer Schiff heißen? (enter Taste um den Namen zufällig auswählen zu lassen.) ")
    print("")
    if schiff_name == "":
        rand_name = True
        rand_schiff_name = rand_schiffsnamen()
        print(rand_schiff_name)
        print("")
    while rand_name == True:
        schiff_name = input("Wie soll euer Schiff heißen? (enter  um den Namen erneut zufällig auswählen zu lassen, 'okay' um den ausgewählten Namen zu benutzen.) ")
        print("")
        if schiff_name == "okay":
            schiff_name = rand_schiff_name
            rand_name = False
        elif schiff_name == "":
            rand_schiff_name = rand_schiffsnamen()
            print("")
            if rand_schiff_name != None:
                print(rand_schiff_name)
                print("")
        else:
            rand_name = False
#endregion







#region >Gesch. nach schiffname
    time.sleep(0.5)
    print("(Geschichte)")
    print("")
    time.sleep(0.5)
    print(f"Schon seit Tagen seit ihr mit der '{schiff_name}' unterwegs richtung Nordpol, " \
        "doch bisher war weit und breit nur Wasser und in letzter Zeit auch ab und an Eisschollen. " \
        "Du sitzt in deiner Kajüte und prüfst noch mal ob der Kurs auch wirklich stimmt und ob die Route zurück nicht durch " \
        "zu gefährliche Gebiete führt, als plötzlich:")
    time.sleep(8)
    print("RRUMMMMS!")
    time.sleep(0.7)
    print("Ein gewaltiges Beben reißt dich nach hinten, wobei dir der Straktosplan," \
    " und damit die geplante Route und Heimreise, aus der Hand fallen und auf dem Boden zerschellen.")
    print("")#endregion







#region >Namen auswählen
    time.sleep(1)
    voller_name = input(f"Sie sind der Käpten der {schiff_name}, wie soll ihr Name lauten? (Vor- und Nachname, enter Taste um den Namen zufällig auswählen zu lassen.) ")
    print("")
    if voller_name == "":
        rand_name = True
        rand_voller_name = rand_namen()
        print(rand_voller_name)
        print("")
    while rand_name == True:
        voller_name = input("Wie soll ihr Name lauten? (Vor- und Nachname, enter Taste um den Namen erneut zufällig auswählen zu lassen, 'okay' um den ausgewählten Namen zu benutzen.) ")
        print("")
        if voller_name == "okay":
            voller_name = rand_voller_name
            rand_name = False
        elif voller_name == "":
            rand_voller_name = rand_namen()
            print("")
            if rand_voller_name != None:
                print(rand_voller_name)
                print("")
        else:
            rand_name = False

    zwischen = voller_name.rfind(" ")
    vorname = voller_name[0:zwischen]
    nachname = voller_name[zwischen+1:len(voller_name)]
#endregion

#endregion







#region >Gesch. nach name
    time.sleep(0.5)
    print("(Geschichte)")
    print("")
    time.sleep(0.5)
    print(f"'Käpt'n, Käpt'n. Kapitän {nachname} kommen Sie aufs Deck, das müssen Sie sich ansehen!' ")
    print("")
    time.sleep(1)

#endregion







#region >Schwierigkeit
    while repeat == True:
        schwierigkeit = input("Welche Schwierigkeitsstufe wollen sie auswählen? (schwer: 1, mittel: 2, leicht: 3 )")
        print("")
        explosive_mun = 0
        if schwierigkeit == "3":
            print("Schwierigkeitsstufe: leicht")
            print("")
            crewmitglieder = 50
            nahrung = 400
            MAX_GESCHÜTZE = 7
            geschütze = 7
            munition = 280
            bauteile = 60

            schiff_zeichnung1 = r"  Brücke__)n___o=           o=    Doppelgeschütz      "
            schiff_zeichnung2 = r"_=o_=o_/        \__D--__    D--   x2 reichweite Geschütz"
            schiff_zeichnung3 = r"\______________________/    )n    Radar               "
            schiff_zeichnung4 = r"  Heck           Bug         . *  Größerer Schaden    "
            
            repeat = False
        elif schwierigkeit == "2":
            print("Schwierigkeitsstufe: mittel")
            print("")
            crewmitglieder = 38
            nahrung = 266
            geschütze = 6
            MAX_GESCHÜTZE = 6
            munition = 210
            bauteile = 50
            
            schiff_zeichnung1 = r"Brücke_)n_o=            o=    Doppelgeschütz   "
            schiff_zeichnung2 = r"_=o__/     \ __o=__     )n    Radar            "
            schiff_zeichnung3 = r"\_________________/     . *    Größerer Schaden"
            schiff_zeichnung4 = r"  Heck       Bug                               "

            repeat = False
        elif schwierigkeit == "1":
            print("Schwierigkeitsstufe: schwer")
            print("")
            crewmitglieder = 25
            nahrung = 150
            MAX_GESCHÜTZE = 5
            geschütze = 5
            munition = 150
            bauteile = 40

            schiff_zeichnung1 = r" Brücke__o=_         o=    Doppelgeschütz  "
            schiff_zeichnung2 = r" _=o_)/     \_o-_    o-    Einzelgeschütz  "
            schiff_zeichnung3 = r"|_______________/    . *   Größerer Schaden"
            schiff_zeichnung4 = r"  Heck     Bug       )     Radar           "

            repeat = False
        else:
            print("Dies ist keine Mögliche Eingabe")
            print("")
            repeat = True

#endregion







#region >Testkampf
    time.sleep(1)
    print("Direkt vor euch taucht aus dem Wasser ein Großer Hai auf.")
    time.sleep(1.5)
    print("'Was zur Hölle ist das?'")
    time.sleep(0.8)
    print(f"Das Tier rammt sein Kopf gegen die {schiff_name} und beisst einmal kräftig in euren Bug.")
    time.sleep(1)
    print("'Es versucht unser Schiff zu zerstören!'")
    time.sleep(0.4)
    print("'Wir müssen es abschiessen'")
    print("")
    time.sleep(3)


    gegner_macht = 1
    name_gegner = "mutierter Hai"
    leben_gegner = 100
    minschaden = 20
    maxschaden = 30
    min_gegn_angriffe = 1
    max_gegn_angriffe = 3
    fallenlassende_nahrung = 20
    fallenlassende_bauteile = 0
    fallenlassende_andere_dinge = []
    typ = "monster"

    werte_gegner_haben_muss = [leben_gegner,min_gegn_angriffe,max_gegn_angriffe,minschaden,maxschaden,gegner_macht,fallenlassende_nahrung,fallenlassende_bauteile,fallenlassende_andere_dinge,typ]

    kampf()

    while win != True:
        print("Fast, probiere es nochmal!")
        print("")
        kampf()
    time.sleep(1)
    print("Gut, nun weisst du wie man kämpft")
    print("Jetzt must du deinen ersten Zug machen")
    print("")
#endregion

#endregion










#region Im Spiel
    print(f"Zug {spielzug}")
    bildschirm()
    zug = 0
    story = 3
    while spielen == True:
        if zug % 2 == 0:
            bewegen()
        else: 

            aktion = input("Führe eine Aktion durch: Reparieren = 1, Zusätzliche Bewegung = 2, Crew heilen = 3 ")
            print("")

            if aktion == "1":
                if brücke > 0:
                    reparieren()
            elif aktion == "2":
                bewegen()
            elif aktion == "3":
                abfrage = input("Wie viele Crewmitglieder willst du Heilen? 5 Nahrung -> 1 Crewmitglied ")
                print("")
                try:
                    abfrage = int(abfrage)
                    if abfrage*5 > nahrung:
                        abfrage = nahrung//5
                    elif abfrage < 0:
                        abfrage = 0
                    elif abfrage > verletzte:
                        abfrage = verletzte
                    print(f"Nahrung -{abfrage*5}")
                    print(f"{abfrage} Crewmitglieder geheilt.")
                    print("")
                    nahrung -= abfrage*5
                    verletzte -= abfrage
                    crewmitglieder += abfrage
                except:
                    print("Keine mögliche Eingabe")

            else:
                print("Keine mögliche Eingabe")

            if nahrung < crewmitglieder + verletzte:
                print("Deine Nahrung ist knapp.")
                print("")
                nahrung = 0
                crewmitglieder -= (crewmitglieder-nahrung) //8 +5
            else:
                nahrung -= (crewmitglieder + verletzte)//2

            if crewmitglieder < 1:
                verloren(2)

            if verletzte > 0:
                crewmitglieder += 1
                verletzte -= 1
            spielzug += 1

        if zerst_brücke == True:
            if zerst_tage == 0:
                zerst_tage += 1
                brücke = 0
                print("Deine Brücke wurde vollkommen zerstört.")
                print("Du hast nun noch eine begrenzte zeit um auf einer Eisscholle oder dem Festland deine brücke zu reparieren")
                print(f"übrige Züge: {10-zerst_tage}")
                print(zerst_tage)
                print("")
            elif zerst_tage <= 9:
                zerst_tage += 1
                print(f"übrige Züge: {10-zerst_tage}")
            elif zerst_tage > 9:
                verloren(1)
            if brücke < 0:
                verloren(1)
        if story == 1 and name_gegner == "mutierter Krake":
            gewinn()
        elif story == 3 and name_gegner == "U-Boot":
            gewinn()
        else:
            print(f"Zug {spielzug}")
            print("")
            bildschirm()
            print("")
        
        zug += 1
    
#endregion










#region nach dem Spiel
    nochmal = 3
    while nochmal != 1 and nochmal != 2:
        nochmal = input("Möchtest du nochmal Spielen? (1:Ja, 2:Nein)")
        if nochmal == 1:
            neustart = True
        elif nochmal == 2:
            neustart = False
print("Schade, ein andernmal")
#endregion
