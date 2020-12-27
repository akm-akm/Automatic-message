import time,os,keyboard  



def bmsg():
    os.system("cls")     
    print('''
 -----------------------------------------------
 |                                             |
 |                CUSTOM MESSAGE               |
 |                                             |
 |   Description# -  Input a message x which   |
 |   u  have  to  send for y number of  time   |
 |   with  some  time  gap z . Works  on any   |
 |   text  field. increase  the time gap  if   |
 |   incomplete    messages     are    sent.   |
 |                                             |
 -----------------------------------------------    
    ''')

def babs():
    os.system("cls")    
    print('''
 -----------------------------------------------
 |                                             |
 |                 AUTO ABUSE                  |
 |                                             |
 |   Description  -  Auto send  abuses  from   |
 |   from built in list of 1000 abuses  with   |
 |   english translation. Works  on any text   |
 |   field.  increase   the   time   gap  if   |
 |   incomplete    messages     are    sent.   |
 |                                             |
 -----------------------------------------------
    ''')

def banner():
    os.system("cls") 
    print("""
 ---------------------------------------------------------------------------------------
 |                                         |*|                                         |
 |        ENTER 1 FOR CUSTOM MESSAGE       |*|         ENTER 2 FOR AUTO ABUSE          |
 |                                         |*|                                         |
 | Description  -  Input a message x which |*| Description  - Auto  send  abuses  from |
 | u  have  to  send for y number of  time |*| from built in list of 1000 abuses  with |
 | with  some  time  gap z . Works  on any |*| english translation. Works  on any text |
 | text  field. increase  the time gap  if |*| field.  increase   the   time   gap  if |
 | incomplete    messages     are    sent. |*| incomplete    messages     are    sent. |
 |                                         |*|                                         |
 ---------------------------------------------------------------------------------------
                                                                                  By AKM
                            ENTER ANY OTHER NUMBER FOR INSTANT

                                     "jai shree ram" 

                                       [0]  -  EXIT                                        
 """)

def bjai():
    os.system("cls")     
    print('''
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%::::*%%%%%%%%%%%%%::::*%%%%%%%%*::::*%%%%%!::::*%%%%%%%%%%%%!::::*%%%%%%
 %%%%%%%%%%%%%%%!....:%%%%%%%%%%%%%....*%%%%%%*:...:*%%%%%%:....:*%%%%%%%%%%!.....!%%%%%%
 %%%%%%%%%%%%%%*......:%%%%%%%%%%%%:...*%%%%%!...:!%%%%%%%%:.....:%%%%%%%%%!......!%%%%%%
 %%%%%%%%%%%%%*:..:!...!%%%%%%%%%%%:...*%%%*:...!%%%%%%%%%%:......:%%%%%%%!.......!%%%%%%
 %%%%%%%%%%%%%:..:*%:..:*%%%%%%%%%%:...*%%!...:*%%%%%%%%%%%:...:...:%%%%%!...::...!%%%%%%
 %%%%%%%%%%%%!...!%%*...:%%%%%%%%%%:...*!:...!%%%%%%%%%%%%%:...!!...:%%%!...:*:...!%%%%%%
 %%%%%%%%%%%*...:%%%%!...!%%%%%%%%%:...:.....:*%%%%%%%%%%%%:...!%!...:%*...:%%:...!%%%%%%
 %%%%%%%%%%%:...*%%%%%:...*%%%%%%%%:.....:!...:*%%%%%%%%%%%:...!%%!...:...:*%%:...!%%%%%%
 %%%%%%%%%%!....::::::....:%%%%%%%%:...:!%%*:...!%%%%%%%%%%:...!%%%!.....:*%%%:...!%%%%%%
 %%%%%%%%%*....:::::::::...!%%%%%%%:...*%%%%%:...:*%%%%%%%%:...!%%%%!...:*%%%%:...!%%%%%%
 %%%%%%%%%:...!%%%%%%%%*....*%%%%%%:...*%%%%%%!...:*%%%%%%%:...!%%%%%!::*%%%%%:...!%%%%%%
 %%%%%%%%!...:%%%%%%%%%%!...:%%%%%%....*%%%%%%%*:...!%%%%%%:...!%%%%%%%%%%%%%%:...!%%%%%%
 %%%%%%%*::::*%%%%%%%%%%%::::!%%%%%::::*%%%%%%%%%::::!%%%%%::::!%%%%%%%%%%%%%%::::!%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ''')





def jai():
    bjai()
    print(" Enter b in any input to go back\n")
    x=input(" PRESS ENTER TO START  >> ")
    if str(x).lower()=='b':
        return
    print("\n CLICK ON A TEXT FIELD IN 3 SECOND")
    print(" Press b to stop\n")
    time.sleep(3)
    x="jai shree ram"
    while True :
         keyboard.write(x)
         time.sleep(0.03)
         keyboard.write("\n")
         try: 
             if keyboard.is_pressed('b'): 
                 print(' Stopping')
                 time.sleep(2)
                 break               
         except:
             pass  

def msg():
     bmsg()
     print(" Enter b in any input to go back\n")
     x=str(input(" Enter text >> "))
     if x.lower()=='b':
        return
     a=input(" No of msg >> ")
     if str(a).lower()=='b':
        return
     sl=input(" gap in sec >> ")
     if int(sl)==0:
         sl=0.03
     if str(sl).lower()=='b':
        return
     print("\n CLICK ON A TEXT FIELD IN 5 SECOND")
     print(" Press b to stop\n")
     n=0
     time.sleep(5)
     for i in range(int(a) ) :
           n=n+1
           keyboard.write(x)
           time.sleep(int(sl))
           keyboard.write("\n")
           try: 
             if keyboard.is_pressed('b'): 
                 bmsg()      
                 print(' Stopping')
                 print( " MESSAGE SENT = "+str(n))
                 time.sleep(2)
                 break               
           except:
                 pass
     bmsg()      
     print( " MESSAGE SENT = "+str(n))
     time.sleep(2)

def abs():
    a=["Bhosadike-BORN FROM A ROTTEN PUSSY " ,"Beti chod-Daughter fucker " ,"Bhadhava- Pimp " ,"Chodu- Fucker " ,"Chutiya- Fucker, bastard " ,"Gaand- ASS " ,"Gaandu-Asshole " ,"Gadha, Bakland- Idiot " ,"Lauda, Lund- Penis, dick, cock " ,"Hijra- Gay, Transsexual " ,"Kuttiya- Bitch " ,"Paad- FART " ,"Paad- FART " ,"Saala kutta- Bloody dog " ,"Saali kutti- Bloody bitch " ,"Tatti- Shit " ,"Tatti- Shit " ,"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat " ,"Chut ke dhakkan- Pussy lid " ,"Chut ke gulam- Pussy whipped " ,"Choot marani ka- Pussy whipped " ,"Choot marani ka- Pussy whipped " ,"Chipkali ke jhaat ke baal- Lizardâ€™s cunt hairs " ,"Chipkali ke jhaat ke paseene- Sweat of Lizardâ€™s pubic hair " ,"Chipkali ke gaand ke pasine-  Sweat of a lizardâ€™s ass " ,"Chipkali ke gaand ke pasine-  Sweat of a lizardâ€™s ass " ,"Chipkali ki bhigi chut- Wet pussy of a wall lizard " ,"Chinaal ke gadde ke nipple ke baal ke joon- Prostituteâ€™s breastâ€™s nippleâ€™s hairâ€™s lice " ,"Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen " ,"Cuntmama- Vaginal uncle " ,"Chhed- Vagina,Hole " ,"Apni gaand mein muthi daal- Put your fist up your ass " ,"Apni lund choos- Go and suck your own dick " ,"Apni ma ko ja choos- Go suck your mom " ,"Bhen ke laude- Sisterâ€™s dick " ,"Abla naari tera buble bhaari-  woman, your tits are huge " ,"Buddha Khoosat- Old fart " ,"Bol teri gand kaise maru- let me know how to fuck you in the ass " ,"Bur ki chatani- Ketchup of cunt " ,"Chunni- Clit " ,"Chinaal- Whore " ,"Chudai khana- Whore house " ,"Chudan chuda- Fucking games " ,"Chudan chuda- Fucking games " ,"Chut ka bhoot- Vaginal Ghost " ,"Gaand ka makhan- Butter from the ass " ,"Gaand main lassan- Garlic in ass " ,"Gaand mein bambu- A bambooup your ass " ,"Gaandfat- Busted ass " ,"Gaandfat- Busted ass " ,"Hazaar lund teri gaand main-Thousand dicks in your ass " ,"Jhaant ke pissu- Bug of pubic hai " ,"Jhaant ke pissu- Bug of pubic hai " ,"Kutte ki jat- Breed of dog " ,"Kutte ke tatte- Dogâ€™s balls " ,"Kutte ke poot, teri maa ki choot-  Son of a dog, your motherâ€™s pussy " ,"Lavde ke bal- Hair on your penis " ,"Lavde ke bal- Hair on your penis " ,"Lund Ke Pasine- Sweat of dick " ,"Meri Gand Ka Khatmal: Bug of my Ass " ,"Moot, Mootna- Piss off " ,"Rundi khana- whore house " ,"Rundi khana- whore house " ,"Teri gaand main kute ka lund- A dogâ€™s dick in your ass " ,"Teri maa ka bhosda- Your motherâ€™s breasts " ,"Teri maa ki chut- Your motherâ€™s pussy " ,"Tere gaand mein keede paday- May worms infest your ass-hole " ,"Ullu ke pathe- Idiot " ,"Ullu ke pathe- Idiot " ,"Idiot " ,"Bakland " ,"Idiot " ,"Bhandava " ,"Pimp " ,"Bhoot-nee ka " ,"Chinaal " ,"Whore " ,"Chup Kar " ,"Shut Up " ,"Chutia / Chutiya / choo-tia / Chutan " ,"Fucker / Bastard " ,"Fucker / Bastard " ,"Hooker " ,"Bastard " ,"Haraam Zaada " ,"Bastard " ,"Hijda / Hijra " ,"Transsexual / Gay " ,"Animal " ,"Dog " ,"Bitch " ,"Khota " ,"Donkey " ,"Son of donkey " ,"Kutte ki jat " ,"Breed of dog " ,"Najayaz " ,"Illegitimate " ,"Najayaz paidaish " ,"Illegitimately born " ,"Saala kutta " ,"Bloody bitch " ,"Soover " ,"Pig (Very offensive to Muslims) " ,"Tatti " ,"Shit " ,"Bahen Chod " ,"Sister-fucker " ,"Sister's dick " ,"Bahen ke takke " ,"Sister's balls " ,"Beti Chod " ,"Daughter fucker " ,"Bhai Chod " ,"Brother-fucker " ,"Brother-fucker " ,"Son of a buffalo " ,"Jhalla, Faggot " ,"gay, fairy " ,"Jhant ke baal " ,"Jhaant ke pissu " ,"Bug of pubic hair " ,"Kutte ka aulad " ,"Son of a dog " ,"Kutte ke tatte " ,"Dog's balls " ,"Maadher chod " ,"Mother-fucker " ,"Padma " ,"Fat Bitch " ,"Raand ka jamai " ,"Son-in-law of a whore " ,"Son-in-law of a whore " ,"Male prostitute " ,"Rundi " ,"Hooker " ,"Rundi ka bacha " ,"Son of a whore " ,"Son of a whore " ,"Soower ke bachche " ,"Ullu ke pathe " ,"Idiot (lit. son of an owl) " ,"Bandaa " ,"Semi-dick " ,"BhonsRi-Waalaa " ,"You fucker " ,"Carrom board " ,"Flat-chested " ,"Vagina (lit. 'hole') " ,"Pussy " ,"Chut marike " ,"Idiot " ,"Chodu " ,"Fucker " ,"Chodra " ,"Fucker " ,"Choochii " ,"Gaandu " ,"Asshole " ,"Gaand " ,"Ass " ,"Ing ge pan di kut teh " ,"You are a pig " ,"LavDa " ,"Penis, dick, cock " ,"Lavde " ,"Penis, dick, cock " ,"Penis, dick, cock " ,"Lavde ke bal " ,"Hair on your penis " ,"Lavander " ,"Dick head " ,"Mangachinamun " ,"Idiot " ,"Muth mar " ,"Masturbate (lit. use your fist) " ,"Nimbu sharbat " ,"Flat-chested " ,"Maa ke bable " ,"Mother's breasts " ,"Mammey mumm-aye " ,"Breasts " ,"Tatte Masalna " ,"Ball smashing/crushing " ,"Ball smashing/crushing " ,"Penis " ,"Toota hua lund " ,"Broken dick " ,"Goat-fucker " ,"One who takes commission from a " ,"prostitute " ,"Bhandwe ki aulad " ,"Son of a pimp " ,"Bhosad Chod " ,"Ass fucker " ,"Bumchod " ,"Ketchup of cunt " ,"Cuntmama " ,"Sweat of lizard's cunt " ,"Chipkali ke gaand ke pasine " ,"Sweat of a lizard's ass " ,"Chipkali ke jhaat ke baal " ,"Lizard's cunt hairs " ,"Chippkali ke jhaant ke paseene " ,"Sweat of Lizard's pubic hair " ,"Chodela " ,"Fucked up " ,"Chodu bhagat " ,"Fucking asshole " ,"Chhola Phudakna " ,"Chudan chudai " ,"Chudai khana " ,"Whore house " ,"Chunni " ,"Choot ka baal " ,"Hair of vagina " ,"Choot ke bhoot " ,"Choot ke bhoot " ,"Chut ke dhakkan " ,"Pussy lid " ,"Chut mari ke " ,"Fucked up " ,"Choot marani ka " ,"Pussy whipped " ,"Chut ke pasine mein talay huye " ,"bhajiye " ,"Snack fried in pussy sweat " ,"Chup Ke Chut Hai " ,"Shut the Fuck up " ,"Fatey condom kay natije " ,"Result of ruptured condom " ,"Fatay huay lundtopi ka result " ,"Result of a torn condom " ,"Gaandu " ,"Born from an ass " ,"Busted ass " ,"Extra playfulness (rude term) " ,"Gaand ka makhan " ,"Butter from the ass " ,"Gaand marau " ,"Person who gets fucked up the ass " ,"Faggot " ,"Jhant chaatu " ,"Pubic hair licker " ,"Jhaat ka bhaaji " ,"Pubic hair fried with vegetables " ,"Kutte ka beej " ,"Semen of a dog " ,"Cock sucker " ,"Lundoos " ,"Born into this world from a dick " ,"Lund ka shorba " ,"Semen of dick " ,"Brain of penis " ,"Lund pe chad ja " ,"Go ride a dick " ,"Lund pe thand hai " ,"Even my dicks absolutely cool! (I " ,"don't care) " ,"Lund Ke Pasine " ,"Sweat of dick " ,"Lavde ke baal " ,"Dick hair " ,"Mother's pimp " ,"Muth maar " ,"Go piss " ,"Parichod " ,"Phatele Nirodh ke Natije " ,"Your are the result of a torn condom. " ,"Pucchi " ,"Pussy " ,"Raandi baajer " ,"Raandi baajer " ,"Rundi ko choud " ,"Screw a hooker " ,"Rubber bhosda " ,"Rubber pussy " ,"Sadi hui gand " ,"Stinking ass " ,"Tera adha Nirodh mein rah gaya " ,"The rest of you was left in the condom " ,"Apna land choos " ,"Go and suck your own dick " ,"Apni gaand mein muthi daal " ,"Put your fist up your ass " ,"Apni ma ko ja choos " ,"Go suck your mom " ,"Chinaal ke gadde ke nipple ke baal ke " ,"joon " ,"Prostitute's breast's nipple's hair's " ,"lice " ,"Chullu bhar muth mein doob mar " ,"Drown yourself in a handful of semen " ,"Gand Ka Khatmal " ,"Bug of Ass " ,"Gandkate Kutte " ,"A dog with his ass scooped out " ,"Gaand mein bambu " ,"A bamboo up your ass " ,"Gaand main danda " ,"Bug up your ass " ,"Hazaar lund teri gaand main " ,"Hazaar lund teri gaand main " ,"Jaa Apni Bajaa " ,"Go fuck yourself " ,"Jab tu paida hua tow aagey se ya " ,"Jab tu paida hua tow aagey se ya " ,"peechey se nikla tha chutiya? " ,"out from the front or the back? " ,"Kahe ko kha raha hai chut ki chapati " ,"Why are boring me with all this " ,"aur lund ka beja? " ,"useless narrative? " ,"Kali Choot Ke Safaid Jhaat " ,"White hair of a black pussy " ,"Kutte ke poot, teri maa ki choot " ,"Son of a dog, your mother's pussy " ,"Lo, mera lund anpi behen ko de do, " ,"Take my dick and give it to your sister " ,"agar khud na chod paya " ,"if you can't fuck her yourself " ,"Suck dick " ,"Ma chudi " ,"Mother's fucked " ,"mein chodoonga aur tera baap laltern " ,"cunt and your dad will bring a " ,"lantern. " ,"Mein teri maa ko liya tha uski suhaag " ,"I had your mother on her wedding " ,"Mera chunni choos " ,"Mera chunni choos " ,"Meri lund choos " ,"Suck my dick " ,"Mere Chuus Maro " ,"Suck my dick " ,"Na choot, na chooche, nakhre noor " ,"No pussy, no boobs, and still behaves " ,"jahan ke! " ,"like a princess! " ,"Raand ka pati " ,"Husband of a whore " ,"Rundi ki tatti pe baithnewaali makkhi " ,"The fly that sits on the ass of a whore " ,"Rundi ke tatti pe biathne wala makhi " ,"Terey baad di gaand wich danda " ,"I am going to put a stick in your damn " ,"ghussa ker rakh dhungi. " ,"ass. " ,"Teri behen ka launda rubber ka " ,"Theri " ,"Theri " ,"I will fuck your wife in front of you " ,"ko " ,"Tere " ,"Saamne " ,"Elephant's dick in your ass " ,"A dog's dick in your ass " ,"Tere gaand mein keede paday " ,"May worms infest your ass-hole " ,"Teri Jhanten Kaat kar tere mooh par " ,"laga kar unki french beard bana " ,"them on your face and make a goatee " ,"on your face. " ,"Teri ma gandi rundi " ,"Your mother is a filthy whore " ,"Teri ma gadha ka lund choosay " ,"Your mother sucks donkey dick " ,"Teri maa ki bimaar badboodar choot " ,"Your mom's diseased smelly cunt " ,"Teri ma ki choot me hathi ka dum " ,"An elephant's trunk in you mother's " ,"An elephant's trunk in you mother's " ,"Teri ma ki chut mai sabka lund " ,"Everyone's dick in your mom's pussy " ,"Teri maa ki phudi guy ki hai " ,"Your mother has a cow's pussy " ,"Teri maa ka bhosda " ,"Your mother's breasts " ,"Teri maa ki chute " ,"Tere mai ki chut tere baap ka land " ,"Your father's penis in your mother's " ,"vagina " ,"khandan ko ghussa ker rakh doonga. " ,"I'm going to put your whole family in " ,"your mom's ass. " ,"hue, maarey hue chipkili ki unday. " ,"There are burnt, dead lizard eggs in " ,"Teri ma ki budh mein chaarpai " ,"bichhake teri bahen ko chodun. " ,"Teri maa ki chut mein chatri leke " ,"ghus jaunga aur khol dunga. " ,"I will enter your mother's pussy with " ,"tera baap! " ,"tera baap! " ,"Tor mai ke chodho " ,"Get back in your mother's womb " ]
    b=["5h1t"," a$$"," a$$hole"," bitch"," bitch tit"," bitch tit"," bitchass"," bitched"," bitcher"," bitchers"," bitches"," bitchin"," bitching"," bitchtits"," bitchy"," black cock"," blonde action"," blonde on blonde action"," bloodclaat"," bloody"," bloody hell"," blow job"," blow me"," blow mud"," blow your load"," blowjob"," blowjobs"," blue waffle"," blue waffle"," blumpkin"," blumpkin"," bod"," bodily"," boink"," boiolas"," bollock"," bollocks"," bollok"," bollox"," bondage"," boned"," boner"," boners"," bong"," boob"," boobies"," boobs"," booby"," booger"," bookie"," boong"," booobs"," boooobs"," booooobs"," booooooobs"," bootee"," bootie"," booty"," booty call"," booze"," boozer"," boozy"," bosom"," bosomy"," breasts"," Breeder"," brotherfucker"," brown showers"," brunette action"," buceta"," bugger"," bukkake"," bull shit"," bulldyke"," bullet vibe"," bullshit"," bullshits"," bullshitted"," bullturds"," bum"," bum boy"," bumblefuck"," bumclat"," bummer"," buncombe"," bung"," bung hole"," bunghole"," bunny fucker"," bust a load"," bust a load"," busty"," butt"," butt fuck"," butt fuck"," butt plug"," buttcheeks"," buttfuck"," buttfucka"," buttfucker"," butthole"," buttmuch"," buttmunch"," butt-pirate"," buttplug"," c.0.c.k"," c.o.c.k."," c.u.n.t"," c0ck"," c-0-c-k"," c0cksucker"," caca"," cacafuego"," cahone"," camel toe"," cameltoe"," camgirl"," camslut"," camwhore"," carpet muncher"," carpetmuncher"," cawk"," cervix"," chesticle"," chi-chi man"," chick with a dick"," child-fucker"," chinc"," chincs"," chink"," chinky"," choad"," choade"," choade"," choc ice"," chocolate rosebuds"," chode"," chodes"," chota bags"," chota bags"," cipa"," circlejerk"," cl1t"," cleveland steamer"," climax"," clit"," clit licker"," clit licker"," clitface"," clitfuck"," clitoris"," clitorus"," clits"," clitty"," clitty litter"," clitty litter"," clover clamps"," clunge"," clusterfuck"," cnut"," cocain"," cocaine"," coccydynia"," cock"," c-o-c-k"," cock pocket"," cock pocket"," cock snot"," cock snot"," cock sucker"," cockass"," cockbite"," cockblock"," cockburger"," cockeye"," cockface"," cockfucker"," cockhead"," cockholster"," cockjockey"," cockknocker"," cockknoker"," Cocklump"," cockmaster"," cockmongler"," cockmongruel"," cockmonkey"," cockmunch"," cockmuncher"," cocknose"," cocknugget"," cocks"," cockshit"," cocksmith"," cocksmoke"," cocksmoker"," cocksniffer"," cocksuck"," cocksuck"," cocksucked"," cocksucked"," cocksucker"," cock-sucker"," cocksuckers"," cocksucking"," cocksucks"," cocksucks"," cocksuka"," cocksukka"," cockwaffle"," coffin dodger"," coital"," cok"," cokmuncher"," coksucka"," commie"," condom"," coochie"," coochy"," coon"," coonnass"," coons"," cooter"," cop some wood"," cop some wood"," coprolagnia"," coprophilia"," corksucker"," cornhole"," cornhole"," corp whore"," corp whore"," corpulent"," cox"," crabs"," crack"," cracker"," crackwhore"," crap"," crappy"," creampie"," cretin"," crikey"," cripple"," crotte"," cum"," cum chugger"," cum chugger"," cum dumpster"," cum dumpster"," cum freak"," cum freak"," cum guzzler"," cum guzzler"," cumbubble"," cumdump"," cumdump"," cumdumpster"," cumguzzler"," cumjockey"," cummer"," cummin"," cumming"," cums"," cumshot"," cumshots"," cumslut"," cumstain"," cumtart"," cunilingus"," cunillingus"," cunnie"," cunnilingus"," cunny"," cunt"," c-u-n-t"," cunt hair"," cunt hair"," cuntass"," cuntbag"," cuntbag"," cuntface"," cunthole"," cunthunter"," cuntlick"," cuntlick"," cuntlicker"," cuntlicker"," cuntlicking"," cuntlicking"," cuntrag"," cunts"," cuntsicle"," cuntsicle"," cuntslut"," cunt-struck"," cunt-struck"," cus"," cut rope"," cut rope"," cyalis"," cyberfuc"," cyberfuck"," cyberfuck"," cyberfucked"," cyberfucked"," cyberfucker"," cyberfuckers"," cyberfucking"," cyberfucking"," d0ng"," d0uch3"," d0uche"," d1ck"," d1ld0"," d1ldo"," dago"," dagos"," dammit"," damn"," damned"," damnit"," darkie"," darn"," date rape"," daterape"," dawgie-style"," deep throat"," deepthroat"," deggo"," dendrophilia"," dick"," dick head"," dick hole"," dick hole"," dick shy"," dick shy"," dickbag"," dickbeaters"," dickdipper"," dickface"," dickflipper"," dickfuck"," dickfucker"," dickhead"," dickheads"," dickhole"," dickish"," dick-ish"," dickjuice"," dickmilk"," dickmonger"," dickripper"," dicks"," dicksipper"," dickslap"," dick-sneeze"," dicksucker"," dicksucking"," dicktickler"," dickwad"," dickweasel"," dickweed"," dickwhipper"," dickwod"," dickzipper"," diddle"," dike"," dildo"," dildos"," diligaf"," dillweed"," dimwit"," dingle"," dingleberries"," dingleberry"," dink"," dinks"," dipship"," dipshit"," dirsa"," dirty"," dirty pillows"," dirty sanchez"," dirty Sanchez"," div"," dlck"," dog style"," dog-fucker"," doggie style"," doggiestyle"," doggie-style"," doggin"," dogging"," doggy style"," doggystyle"," doggy-style"," dolcett"," domination"," dominatrix"," dommes"," dong"," donkey punch"," donkeypunch"," donkeyribber"," doochbag"," doofus"," dookie"," doosh"," dopey"," double dong"," double penetration"," Doublelift"," douch3"," douche"," douchebag"," douchebags"," douche-fag"," douchewaffle"," douchey"," dp action"," drunk"," dry hump"," duche"," dumass"," dumb ass"," dumbass"," dumbasses"," Dumbcunt"," dumbfuck"," dumbshit"," dummy"," dumshit"," dvda"," dyke"," dykes"," eat a dick"," eat a dick"," eat hair pie"," eat hair pie"," eat my ass"," ecchi"," ejaculate"," ejaculated"," ejaculates"," ejaculates"," ejaculating"," ejaculating"," ejaculatings"," ejaculation"," ejakulate"," erect"," erection"," erotic"," erotism"," escort"," essohbee"," eunuch"," extacy"," extasy"," f u c k"," f u c k e r"," f.u.c.k"," f_u_c_k"," f4nny"," facial"," fack"," fag"," fagbag"," fagfucker"," fagg"," fagged"," fagging"," faggit"," faggitt"," faggot"," faggotcock"," faggots"," faggs"," fagot"," fagots"," fags"," fagtard"," faig"," faigt"," fanny"," fannybandit"," fannyflaps"," fannyfucker"," fanyy"," fart"," fartknocker"," fatass"," fcuk"," fcuker"," fcuking"," fecal"," feck"," fecker"," feist"," felch"," felcher"," felching"," fellate"," fellatio"," feltch"," feltcher"," female squirting"," femdom"," fenian"," fice"," figging"," fingerbang"," fingerfuck"," fingerfuck"," fingerfucked"," fingerfucked"," fingerfucker"," fingerfucker"," fingerfuckers"," fingerfucking"," fingerfucking"," fingerfucks"," fingerfucks"," fingering"," fist fuck"," fist fuck"," fisted"," fistfuck"," fistfucked"," fistfucked"," fistfucker"," fistfucker"," fistfuckers"," fistfuckers"," fistfucking"," fistfucking"," fistfuckings"," fistfuckings"," fistfucks"," fistfucks"," fisting"," fisty"," flamer"," flange"," flaps"," fleshflute"," flog the log"," flog the log"," floozy"," foad"," foah"," fondle"," foobar"," fook"," fooker"," foot fetish"," footjob"," foreskin"," freex"," frenchify"," frigg"," frigga"," frotting"," fubar"," fuc"," fuck"," fuck"," f-u-c-k"," fuck buttons"," fuck hole"," fuck hole"," Fuck off"," fuck puppet"," fuck puppet"," fuck trophy"," fuck trophy"," fuck yo mama"," fuck yo mama"," fuck you"," fucka"," fuckass"," fuck-ass"," fuck-ass"," fuckbag"," fuck-bitch"," fuck-bitch"," fuckboy"," fuckbrain"," fuckbutt"," fuckbutter"," fucked"," fuckedup"," fucker"," fuckers"," fuckersucker"," fuckface"," fuckhead"," fuckheads"," fuckhole"," fuckin"," fucking"," fuckings"," fuckingshitmotherfucker"," fuckme"," fuckme"," fuckmeat"," fuckmeat"," fucknugget"," fucknut"," fucknutt"," fuckoff"," fucks"," fuckstick"," fucktard"," fuck-tard"," fucktards"," fucktart"," fucktoy"," fucktoy"," fucktwat"," fuckup"," fuckwad"," fuckwhit"," fuckwit"," fuckwitt"," fudge packer"," fudgepacker"," fudge-packer"," fuk"," fuker"," fukker"," fukkers"," fukkin"," fuks"," fukwhit"," fukwit"," fuq"," futanari"," fux"," fux0r"," fvck"," fxck"," gae"," gai"," gang bang"," gangbang"," gang-bang"," gang-bang"," gangbanged"," gangbangs"," ganja"," gash"," gassy ass"," gassy ass"," gay"," gay sex"," gayass"," gaybob"," gaydo"," gayfuck"," gayfuckist"," gaylord"," gays"," gaysex"," gaytard"," gaywad"," gender bender"," genitals"," gey"," gfy"," ghay"," ghey"," giant cock"," gigolo"," ginger"," gippo"," girl on"," girl on top"," girls gone wild"," git"," glans"," goatcx"," goatse"," god"," god damn"," godamn"," godamnit"," goddam"," god-dam"," goddammit"," goddamn"," goddamned"," god-damned"," goddamnit"," godsdamn"," gokkun"," golden shower"," goldenshower"," golliwog"," gonad"," gonads"," goo girl"," gooch"," goodpoop"," gook"," gooks"," goregasm"," gringo"," grope"," group sex"," gspot"," g-spot"," gtfo"," guido"," guro"," h0m0"," h0mo"," ham flap"," ham flap"," hand job"," handjob"," hard core"," hard on"," hardcore"," hardcoresex"," he11"," hebe"," heeb"," hell"," hemp"," hentai"," heroin"," herp"," herpes"," herpy"," heshe"," he-she"," hircismus"," hitler"," hiv"," ho"," hoar"," hoare"," hobag"," hoe"," hoer"," holy shit"," hom0"," homey"," homo"," homodumbshit"," homoerotic"," homoey"," honkey"," honky"," hooch"," hookah"," hooker"," hoor"," hootch"," hooter"," hooters"," hore"," horniest"," horny"," hot carl"," hot chick"," hotsex"," how to kill"," how to murdep"," how to murder"," huge fat"," hump"," humped"," humping"," hun"," hussy"," hymen"," iap"," iberian slap"," inbred"," incest"," injun"," intercourse"," jack off"," jackass"," jackasses"," jackhole"," jackoff"," jack-off"," jaggi"," jagoff"," jail bait"," jailbait"," jap"," japs"," jelly donut"," jerk"," jerk off"," jerk0ff"," jerkass"," jerked"," jerkoff"," jerk-off"," jigaboo"," jiggaboo"," jiggerboo"," jism"," jiz"," jiz"," jizm"," jizm"," jizz"," jizzed"," jock"," juggs"," jungle bunny"," junglebunny"," junkie"," junky"," kafir"," kawk"," kike"," kikes"," kill"," kinbaku"," kinkster"," kinky"," klan"," knob"," knob end"," knobbing"," knobead"," knobed"," knobend"," knobhead"," knobjocky"," knobjokey"," kock"," kondum"," kondums"," kooch"," kooches"," kootch"," kraut"," kum"," kummer"," kumming"," kums"," kunilingus"," kunja"," kunt"," kwif"," kwif"," kyke"," l3i+ch"," l3itch"," labia"," lameass"," lardass"," leather restraint"," leather straight jacket"," lech"," lemon party"," LEN"," leper"," lesbian"," lesbians"," lesbo"," lesbos"," lez"," lezza/lesbo"," lezzie"," lmao"," lmfao"," loin"," loins"," lolita"," looney"," lovemaking"," lube"," lust"," lusting"," lusty"," m0f0"," m0fo"," m45terbate"," ma5terb8"," ma5terbate"," mafugly"," mafugly"," make me come"," male squirting"," mams"," masochist"," massa"," masterb8"," masterbat*"," masterbat3"," masterbate"," master-bate"," master-bate"," masterbating"," masterbation"," masterbations"," masturbate"," masturbating"," masturbation"," maxi"," mcfagget"," menage a trois"," menses"," menstruate"," menstruation"," meth"," m-fucking"," mick"," microphallus"," middle finger"," midget"," milf"," minge"," minger"," missionary position"," mof0"," mofo"," mo-fo"," molest"," mong"," moo moo foo foo"," moolie"," moron"," mothafuck"," mothafucka"," mothafuckas"," mothafuckaz"," mothafucked"," mothafucked"," mothafucker"," mothafuckers"," mothafuckin"," mothafucking"," mothafucking"," mothafuckings"," mothafucks"," mother fucker"," mother fucker"," motherfuck"," motherfucka"," motherfucked"," motherfucker"," motherfuckers"," motherfuckin"," motherfucking"," motherfuckings"," motherfuckka"," motherfucks"," mound of venus"," mr hands"," muff"," muff diver"," muff puff"," muff puff"," muffdiver"," muffdiving"," munging"," munter"," murder"," mutha"," muthafecker"," muthafuckker"," muther"," mutherfucker"," n1gga"," n1gger"," naked"," nambla"," napalm"," nappy"," nawashi"," nazi"," nazism"," need the dick"," need the dick"," negro"," neonazi"," nig nog"," nigaboo"," nigg3r"," nigg4h"," nigga"," niggah"," niggas"," niggaz"," nigger"," niggers"," niggle"," niglet"," nig-nog"," nimphomania"," nimrod"," ninny"," ninnyhammer"," nipple"," nipples"," nob"," nob jokey"," nobhead"," nobjocky"," nobjokey"," nonce"," nsfw images"," nude"," nudity"," numbnuts"," nut butter"," nut butter"," nut sack"," nutsack"," nutter"," nympho"," nymphomania"," octopussy"," old bag"," omg"," omorashi"," one cup two girls"," one guy one jar"," opiate"," opium"," orally"," organ"," orgasim"," orgasims"," orgasm"," orgasmic"," orgasms"," orgies"," orgy"," ovary"," ovum"," ovums"," p.u.s.s.y."," p0rn"," paedophile"," paki"," panooch"," pansy"," pantie"," panties"," panty"," pawn"," pcp"," pecker"," peckerhead"," pedo"," pedobear"," pedophile"," pedophilia"," pedophiliac"," pee"," peepee"," pegging"," penetrate"," penetration"," penial"," penile"," penis"," penisbanger"," penisfucker"," penispuffer"," perversion"," phallic"," phone sex"," phonesex"," phuck"," phuk"," phuked"," phuking"," phukked"," phukking"," phuks"," phuq"," piece of shit"," pigfucker"," pikey"," pillowbiter"," pimp"," pimpis"," pinko"," piss"," piss off"," piss pig"," pissed"," pissed off"," pisser"," pissers"," pisses"," pisses"," pissflaps"," pissin"," pissin"," pissing"," pissoff"," pissoff"," piss-off"," pisspig"," playboy"," pleasure chest"," pms"," polack"," pole smoker"," polesmoker"," pollock"," ponyplay"," poof"," poon"," poonani"," poonany"," poontang"," poop"," poop chute"," poopchute"," Poopuncher"," porch monkey"," porchmonkey"," porn"," porno"," pornography"," pornos"," pot"," potty"," prick"," pricks"," prickteaser"," prig"," prince albert piercing"," prod"," pron"," prostitute"," prude"," psycho"," pthc"," pube"," pubes"," pubic"," pubis"," punani"," punanny"," punany"," punkass"," punky"," punta"," puss"," pusse"," pussi"," pussies"," pussy"," pussy fart"," pussy fart"," pussy palace"," pussy palace"," pussylicking"," pussypounder"," pussys"," pust"," puto"," queaf"," queaf"," queef"," queer"," queerbait"," queerhole"," queero"," queers"," quicky"," quim"," racy"," raghead"," raging boner"," rape"," raped"," raper"," rapey"," raping"," rapist"," raunch"," rectal"," rectum"," rectus"," reefer"," reetard"," reich"," renob"," retard"," retarded"," reverse cowgirl"," revue"," rimjaw"," rimjob"," rimming"," ritard"," rosy palm"," rosy palm and her 5 sisters"," rtard"," r-tard"," rubbish"," rum"," rump"," rumprammer"," ruski"," rusty trombone"," s hit"," s&m"," s.h.i.t."," s.o.b."," s_h_i_t"," s0b"," sadism"," sadist"," sambo"," sand nigger"," sandbar"," sandbar"," Sandler"," sandnigger"," sanger"," santorum"," sausage queen"," sausage queen"," scag"," scantily"," scat"," schizo"," schlong"," scissoring"," screw"," screwed"," screwing"," scroat"," scrog"," scrot"," scrote"," scrotum"," scrud"," scum"," seaman"," seamen"," seduce"," seks"," semen"," sex"," sexo"," sexual"," sexy"," sh!+"," sh!t"," sh1t"," s-h-1-t"," shag"," shagger"," shaggin"," shagging"," shamedame"," shaved beaver"," shaved pussy"," shemale"," shi+"," shibari"," shirt lifter"," shit"," s-h-i-t"," shit ass"," shit fucker"," shit fucker"," shitass"," shitbag"," shitbagger"," shitblimp"," shitbrains"," shitbreath"," shitcanned"," shitcunt"," shitdick"," shite"," shiteater"," shited"," shitey"," shitface"," shitfaced"," shitfuck"," shitfull"," shithead"," shitheads"," shithole"," shithouse"," shiting"," shitings"," shits"," shitspitter"," shitstain"," shitt"," shitted"," shitter"," shitters"," shitters"," shittier"," shittiest"," shitting"," shittings"," shitty"," shiz"," shiznit"," shota"," shrimping"," sissy"," skag"," skank"," skeet"," skullfuck"," slag"," slanteye"," slave"," sleaze"," sleazy"," slope"," slope"," slut"," slut bucket"," slut bucket"," slutbag"," slutdumper"," slutkiss"," sluts"," smartass"," smartasses"," smeg"," smegma"," smut"," smutty"," snatch"," sniper"," snowballing"," snuff"," s-o-b"," sod off"," sodom"," sodomize"," sodomy"," son of a bitch"," son of a motherless goat"," son of a whore"," son-of-a-bitch"," souse"," soused"," spac"," spade"," sperm"," spic"," spick"," spik"," spiks"," splooge"," splooge moose"," spooge"," spook"," spread legs"," spunk"," stfu"," stiffy"," stoned"," strap on"," strapon"," strappado"," strip"," strip club"," stroke"," stupid"," style doggy"," suck"," suckass"," sucked"," sucking"," sucks"," suicide girls"," sultry women"," sumofabiatch"," swastika"," swinger"," t1t"," t1tt1e5"," t1tties"," taff"," taig"," tainted love"," taking the piss"," tampon"," tard"," tart"," taste my"," tawdry"," tea bagging"," teabagging"," teat"," teets"," teez"," teste"," testee"," testes"," testical"," testicle"," testis"," threesome"," throating"," thrust"," thug"," thundercunt"," tied up"," tight white"," tinkle"," tit"," tit wank"," tit wank"," titfuck"," titi"," tities"," tits"," titt"," tittie5"," tittiefucker"," titties"," titty"," tittyfuck"," tittyfucker"," tittywank"," titwank"," toke"," tongue in a"," toots"," topless"," tosser"," towelhead"," tramp"," tranny"," transsexual"," trashy"," tribadism"," trumped"," tub girl"," tubgirl"," turd"," tush"," tushy"," tw4t"," twat"," twathead"," twatlips"," twats"," twatty"," twatwaffle"," twink"," twinkie"," two fingers"," two fingers with tongue"," two girls one cup"," twunt"," twunter"," ugly"," unclefucker"," undies"," undressing"," unwed"," upskirt"," urethra play"," urinal"," urine"," urophilia"," uterus"," uzi"," v14gra"," v1gra"," vag"," vagina"," vajayjay"," va-j-j"," valium"," venus mound"," veqtable"," viagra"," vibrator"," violet wand"," virgin"," vixen"," vjayjay"," vodka"," vomit"," vorarephilia"," voyeur"," vulgar"," vulva"," w00se"," wad"," wang"," wank"," wanker"," wankjob"," wanky"," wazoo"," wedgie"," weed"," weenie"," weewee"," weiner"," weirdo"," wench"," wet dream"," wetback"," wh0re"," wh0reface"," white power"," whiz"," whoar"," whoralicious"," whore"," whorealicious"," whorebag"," whored"," whoreface"," whorehopper"," whorehouse"," whores"," whoring"," wigger"," willies"," willy"," window licker"," wiseass"," wiseasses"," wog"," womb"," wop"," wrapping men"," wrinkled starfish"," wtf"," xrated"," x-rated"," xx"," xxx"," yaoi"," yeasty"," yellow showers"," yid"," yiffy"," yobbo"," zibbi"," zoophilia"," zubb","anal","anus","arse","ass","ass fuck","ass hole","assfucker","asshole","assshole","bastard","bitch","black cock","bloody hell","boong","cock","cockfucker","cocksuck","cocksucker","coon","coonnass","crap","cunt","cyberfuck","damn","darn","dick","dirty","douche","dummy","erect","erection","erotic","escort","fag","faggot","fuck","Fuck off","fuck you","fuckass","fuckhole","god damn","gook","hard core","hardcore","homoerotic","hore","lesbian","lesbians","mother fucker","motherfuck","motherfucker","negro","nigger","orgasim","orgasm","penis","penisfucker","piss","piss off","porn","porno","pornography","pussy","retard","sadist","sex","sexy","shit","slut","son of a bitch","suck","tits","viagra","whore","xxx"] 
    babs()
    print(" Enter b in any input to go back\n")
    aa=input(" No of abuses >> ")
    if str(aa).lower()=='b':
        return

    sl=input(" Time gap in sec >> ")
    if int(sl)==0:
         sl=0.03
    if str(sl).lower()=='b':
        return
    x=input(" PRESS 1 FOR HINDI AND 2 FOR ENGLISH >> ")
    if str(x).lower()=='b':
        return
    elif int(x)==1:
        c=a
    elif int(x)==2:
        c=b  
    x=input("  ENTER TO START  >> ")
    if str(x).lower()=='b':
        return
    print("\n CLICK ON A TEXT FIELD IN 5 SECOND")
    print(" Press b to stop\n")
    time.sleep(5)
    n=0
    for i in c :
         keyboard.write(i)
         time.sleep(int(sl))
         keyboard.write("\n")
         n=n+1
         if n>int(aa):
             break
         try: 
             if keyboard.is_pressed('b'): 
                 babs()      
                 print(' Stopping')
                 print( "MESSAGE SENT = "+str(n))
                 time.sleep(2)
                 break               
         except:
                 pass   

while True:
    banner()
    
    try:
        c=int(input(" ENTER CHOICE >> "))
        if c==1:
            msg()
        elif c==2:
            abs()
        elif c==0:
            os._exit(0)
        elif c!=1 & c!=2 & c!=0:
            jai()
    except Exception  as e:
        banner()
        print(" ENTER CHOICE >> INVALID CHOICE!")
        time.sleep(1)   