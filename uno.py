
Languages
Tags
Authors
Sets
NOTE: Recipes have moved! Please visit GitHub.com/activestate/code for the current versions.
Uno (Text-Based) (Python recipe)

A text based recreation of the classic card game featuring functional AIs to play with. Some rules have been modified. User interface is text based, non-curses, using only simple python commands to draw it.
Python, 1534 lines Download

   1
   2
   3
   4
   5
   6
   7
   8
   9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  29
  30
  31
  32
  33
  34
  35
  36
  37
  38
  39
  40
  41
  42
  43
  44
  45
  46
  47
  48
  49
  50
  51
  52
  53
  54
  55
  56
  57
  58
  59
  60
  61
  62
  63
  64
  65
  66
  67
  68
  69
  70
  71
  72
  73
  74
  75
  76
  77
  78
  79
  80
  81
  82
  83
  84
  85
  86
  87
  88
  89
  90
  91
  92
  93
  94
  95
  96
  97
  98
  99
 100
 101
 102
 103
 104
 105
 106
 107
 108
 109
 110
 111
 112
 113
 114
 115
 116
 117
 118
 119
 120
 121
 122
 123
 124
 125
 126
 127
 128
 129
 130
 131
 132
 133
 134
 135
 136
 137
 138
 139
 140
 141
 142
 143
 144
 145
 146
 147
 148
 149
 150
 151
 152
 153
 154
 155
 156
 157
 158
 159
 160
 161
 162
 163
 164
 165
 166
 167
 168
 169
 170
 171
 172
 173
 174
 175
 176
 177
 178
 179
 180
 181
 182
 183
 184
 185
 186
 187
 188
 189
 190
 191
 192
 193
 194
 195
 196
 197
 198
 199
 200
 201
 202
 203
 204
 205
 206
 207
 208
 209
 210
 211
 212
 213
 214
 215
 216
 217
 218
 219
 220
 221
 222
 223
 224
 225
 226
 227
 228
 229
 230
 231
 232
 233
 234
 235
 236
 237
 238
 239
 240
 241
 242
 243
 244
 245
 246
 247
 248
 249
 250
 251
 252
 253
 254
 255
 256
 257
 258
 259
 260
 261
 262
 263
 264
 265
 266
 267
 268
 269
 270
 271
 272
 273
 274
 275
 276
 277
 278
 279
 280
 281
 282
 283
 284
 285
 286
 287
 288
 289
 290
 291
 292
 293
 294
 295
 296
 297
 298
 299
 300
 301
 302
 303
 304
 305
 306
 307
 308
 309
 310
 311
 312
 313
 314
 315
 316
 317
 318
 319
 320
 321
 322
 323
 324
 325
 326
 327
 328
 329
 330
 331
 332
 333
 334
 335
 336
 337
 338
 339
 340
 341
 342
 343
 344
 345
 346
 347
 348
 349
 350
 351
 352
 353
 354
 355
 356
 357
 358
 359
 360
 361
 362
 363
 364
 365
 366
 367
 368
 369
 370
 371
 372
 373
 374
 375
 376
 377
 378
 379
 380
 381
 382
 383
 384
 385
 386
 387
 388
 389
 390
 391
 392
 393
 394
 395
 396
 397
 398
 399
 400
 401
 402
 403
 404
 405
 406
 407
 408
 409
 410
 411
 412
 413
 414
 415
 416
 417
 418
 419
 420
 421
 422
 423
 424
 425
 426
 427
 428
 429
 430
 431
 432
 433
 434
 435
 436
 437
 438
 439
 440
 441
 442
 443
 444
 445
 446
 447
 448
 449
 450
 451
 452
 453
 454
 455
 456
 457
 458
 459
 460
 461
 462
 463
 464
 465
 466
 467
 468
 469
 470
 471
 472
 473
 474
 475
 476
 477
 478
 479
 480
 481
 482
 483
 484
 485
 486
 487
 488
 489
 490
 491
 492
 493
 494
 495
 496
 497
 498
 499
 500
 501
 502
 503
 504
 505
 506
 507
 508
 509
 510
 511
 512
 513
 514
 515
 516
 517
 518
 519
 520
 521
 522
 523
 524
 525
 526
 527
 528
 529
 530
 531
 532
 533
 534
 535
 536
 537
 538
 539
 540
 541
 542
 543
 544
 545
 546
 547
 548
 549
 550
 551
 552
 553
 554
 555
 556
 557
 558
 559
 560
 561
 562
 563
 564
 565
 566
 567
 568
 569
 570
 571
 572
 573
 574
 575
 576
 577
 578
 579
 580
 581
 582
 583
 584
 585
 586
 587
 588
 589
 590
 591
 592
 593
 594
 595
 596
 597
 598
 599
 600
 601
 602
 603
 604
 605
 606
 607
 608
 609
 610
 611
 612
 613
 614
 615
 616
 617
 618
 619
 620
 621
 622
 623
 624
 625
 626
 627
 628
 629
 630
 631
 632
 633
 634
 635
 636
 637
 638
 639
 640
 641
 642
 643
 644
 645
 646
 647
 648
 649
 650
 651
 652
 653
 654
 655
 656
 657
 658
 659
 660
 661
 662
 663
 664
 665
 666
 667
 668
 669
 670
 671
 672
 673
 674
 675
 676
 677
 678
 679
 680
 681
 682
 683
 684
 685
 686
 687
 688
 689
 690
 691
 692
 693
 694
 695
 696
 697
 698
 699
 700
 701
 702
 703
 704
 705
 706
 707
 708
 709
 710
 711
 712
 713
 714
 715
 716
 717
 718
 719
 720
 721
 722
 723
 724
 725
 726
 727
 728
 729
 730
 731
 732
 733
 734
 735
 736
 737
 738
 739
 740
 741
 742
 743
 744
 745
 746
 747
 748
 749
 750
 751
 752
 753
 754
 755
 756
 757
 758
 759
 760
 761
 762
 763
 764
 765
 766
 767
 768
 769
 770
 771
 772
 773
 774
 775
 776
 777
 778
 779
 780
 781
 782
 783
 784
 785
 786
 787
 788
 789
 790
 791
 792
 793
 794
 795
 796
 797
 798
 799
 800
 801
 802
 803
 804
 805
 806
 807
 808
 809
 810
 811
 812
 813
 814
 815
 816
 817
 818
 819
 820
 821
 822
 823
 824
 825
 826
 827
 828
 829
 830
 831
 832
 833
 834
 835
 836
 837
 838
 839
 840
 841
 842
 843
 844
 845
 846
 847
 848
 849
 850
 851
 852
 853
 854
 855
 856
 857
 858
 859
 860
 861
 862
 863
 864
 865
 866
 867
 868
 869
 870
 871
 872
 873
 874
 875
 876
 877
 878
 879
 880
 881
 882
 883
 884
 885
 886
 887
 888
 889
 890
 891
 892
 893
 894
 895
 896
 897
 898
 899
 900
 901
 902
 903
 904
 905
 906
 907
 908
 909
 910
 911
 912
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535

	

import os
import sys
import random
import math
import time

class BadInputError(Exception):
    pass

class Player():

    def __init__(self, name):
        self.id = None
        self.name = name
        self.type = 'Human'
        self.hand = Hand()
        self.legalCards = []
        self.wildCards = []
        self.valueChangeCards = []
        self.zeroCards = []
        self.canSkip = False
        self.canReverse = False
        self.canDrawTwo = False
        self.canDrawFour = False
        self.canValueChange = False
        self.drew = False
        self.scrollMax = 0
        self.points = 0
        self.forceDraw = 0

    def addCard(self, card):
        self.drew = True
        if self.forceDraw > 0:
            self.forceDraw -= 1
            self.drew = False
        self.hand.addCard(card)
        
    def beginTurn(self):
        self.drew = False
        
    def didDraw(self):
        return self.drew
        
    def getLegalCards(self, color, value, zeroChange=False):
        self.canSkip = False
        self.canReverse = False
        self.canDrawTwo = False
        self.canDrawFour = False
        self.canValueChange = False
        self.canZeroChange = False
        self.legalCards = []
        self.wildCards = []
        self.valueChangeCards = []
        self.zeroCards = []
        plusFours = []
        for card in self.hand:
            if card.isWild():
                if card.getValue() == '+4':
                    plusFours.append(card)
                else:
                    self.wildCards.append(card)
            elif zeroChange and card.isZero():
                self.canZero = True
                self.zeroCards.append(card)
            elif card.getColor() == color or card.getValue() == value:
                if card.getColor() != color:
                    self.canValueChange = True
                    self.valueChangeCards.append(card)
                if card.getValue() == "+2":
                    self.canDrawTwo = True
                elif card.getValue() == 'R':
                    self.canReverse = True
                elif card.getValue() == 'X':
                    self.canSkip = True
                self.legalCards.append(card)
        if len(self.legalCards) == 0 and len(plusFours) > 0:
            self.canDrawFour = True
            self.wildCards += plusFours
                
    def getValidCards(self):
        return self.legalCards
    
    def getAllValidCards(self):
        return self.legalCards + self.wildCards + self.zeroCards
                
    def hasLegalCard(self):
        return len(self.legalCards) > 0
        
    def addPoints(self, amount):
        if (self.points + amount) <= 999999999999999999999:
            self.points += amount
        
    def removeCard(self, index):
        return self.hand.removeCard(index)
    
    def assignID(self, identity):
        self.id = identity

    def getName(self):
        return self.name

    def getID(self):
        return self.id
    
    def getPoints(self):
        return self.points

    def getType(self):
        return self.type

    def getCardNum(self):
        return len(self.hand)

    def getHand(self, scrollNum=0, hide=False):
        return self.hand.show(scrollNum, hide)
    
    def getForceDraws(self):
        return self.forceDraw
    
    def addForceDraw(self, num):
        self.forceDraw += num
    
    def decreaseForceDraw(self):
        self.forceDraw -= 1
        
    def removeForceDraw(self):
        self.forceDraw = 0

    def checkCard(self, index):
        return self.hand.getCard(int(index))
    
    def discardHand(self):
        self.hand.discard()
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '({},{})'.format(self.name, self.points)

class Hand():
    ''''deck' (Deck) : Card's Color (rgby)
       'numberOfCards' (int) : Card's Value (0-9, R, X, W, +2, +4)'''

    def __init__(self, deck=None,numberOfCards=0):
        self.hand = []
        if deck != None:
            self.draw(deck,numberOfCards)

    def __iter__(self):
        return iter(self.hand)

    def __len__(self):
        return len(self.hand)

    def __getitem__(self, item):
        try:
            return self.hand[item]
        except:
            return ''

    def addCard(self, card):
        self.hand.append(card) 
        
    def removeCard(self, index):
        index = int(index)
        if (0 <= index < len(self)):
            return self.hand.pop(index)      

    def discard(self):
        self.hand = []

    def show(self, scrollNum=0, hide=False):
        if scrollNum == -1:
            scrollNum = 0
        output = ''
        num = 0
        header, footer, upper, lower = '', '', '', ''
        header +=   ('\033[97m\u2666--\u2666\033[0m ')
        upper +=    ('\033[97m|<-|\033[0m ')
        lower +=    ('\033[97m|<-|\033[0m ')
        footer +=   ('\033[97m\u2666--\u2666\033[0m ')
        for i in range(10):
            indexNum = i+(10*scrollNum)
            if indexNum < len(self):
                header += (self[indexNum].getRow(0,hide)+' ')
                upper += (self[indexNum].getRow(1,hide)+' ')
                lower += (self[indexNum].getRow(2,hide)+' ')
                footer += (self[indexNum].getRow(3,hide)+' ')
                num += 1
        for j in range(10-num):
            j #unused
            header += ('     ')
            footer += ('     ')
            upper += ('     ')
            lower += ('     ')
        header +=   ('\033[97m\u2666--\u2666\033[0m ')
        upper +=    ('\033[97m|->|\033[0m ')
        lower +=    ('\033[97m|->|\033[0m ')
        footer +=   ('\033[97m\u2666--\u2666\033[0m ')
        output += ('  '+header+'\n  '+upper+'\n  '+lower+'\n  '+footer+'\n\033[97m|-(<)--')
        for k in range(num):
            output += '({})'.format(k)
            output += '--'
        for l in range(10-num):
            l #unused
            output += '-----'
        output += '(>)--|\033[0m\n'
        return output

    def getCard(self, index):
        return self.hand[index]
    
    def indexCard(self, card):
        return self.hand.index(card)

class GameSettings():
    
    playerIdentities = ('play1','play2','play3','play4')
    computerNames = ('Watson','SkyNet','Hal','Metal Gear')
    
    def __init__(self):
        self.playerStaging = []                  #    Where Player Objs Are Stored Before Game Starts
        self.players = {}                        #    ID : Player Obj
        self.numPlayers = 0
        self.useColor = True 
        self.displayEffects = True
        self.hideComputerHands = True
        self.zeroChange = False
        self.computerSimulation = False
        self.mainMenuError = ''
        self.computerSpeed = 'normal'
        
    def canAddPlayer(self):
        return (self.numPlayers < 4)
    
    def canRemovePlayer(self):
        return (self.numPlayers > 0)
    
    def canBegin(self):
        return (self.numPlayers > 1)
        
    def addPlayer(self, player):
        self.playerStaging.append(player)
        self.numPlayers += 1
        
    def removePlayer(self, number):
        number -= 1
        del self.playerStaging[number]
        self.numPlayers -= 1
        
    def clearStaging(self):
        self.numPlayers = 0
        self.playerStaging = []
        
    def finalizePlayers(self):
        self.players.clear()
        identity = 0
        for player in self.playerStaging:
            playerID = self.playerIdentities[identity]
            player.assignID(playerID)
            self.players[playerID] = player
            identity += 1
        
    def getPlayerNum(self):
        return self.numPlayers
    
    def getComputerName(self):
        complete = False
        index = self.numPlayers
        while not complete:
            name = self.computerNames[index]
            complete = True
            for player in self.playerStaging:
                if player.getName() == name:
                    index += 1
                    if index >= len(self.computerNames):
                        index = 0
                        complete = False
            
        return self.computerNames[index]
    
    def getRandomIdentity(self):
        '''For Getting a Random Player for First Turn.'''
        return random.choice(self.players.keys())
    
    def compileMainMenuElements(self):
        def getBlankSpace(word, total):
            return " "*(total-len(word))
        
        def getPlayerBox(playerNum, rowNum):
            if rowNum == 1:
                name = self.playerStaging[playerNum-1].getName()
                return '{}{}'.format(name, getBlankSpace(name, 29))
            elif rowNum == 2:
                points = self.playerStaging[playerNum-1].getPoints()
                return 'Points: {}{}'.format(points, getBlankSpace(str(points), 21))
                
        self.mainMenuElements= {'play1row1':'No Player                    ','play1row2':'                             ',
                                'play2row1':'No Player                    ',
                                'play2row2':'                             ',
                                'play3row1':'No Player                    ','play3row2':'                             ',
                                'play4row1':'No Player                    ',
                                'play4row2':'                             ', 
                                'play1box':'\033[90m','play2box':'\033[90m','play3box':'\033[90m','play4box':'\033[90m',
                                'beginBox':'\033[90m','addBox':'\033[97m','removeBox':'\033[90m'
                                }
        playerBoxKey = 'play{}box'
        playerRowKey = 'play{}row{}'
        i = 1
        for j in self.playerStaging:
            j
            colorCode = ['\033[91m','\033[94m','\033[92m','\033[93m']
            key = playerBoxKey.format(i)
            self.mainMenuElements[key] = colorCode[i-1]
            self.mainMenuElements[playerRowKey.format(i,1)] = getPlayerBox(i, 1)
            self.mainMenuElements[playerRowKey.format(i,2)] = getPlayerBox(i, 2)
            i+=1
        if self.canBegin():
            self.mainMenuElements['beginBox'] = '\033[95m'
        if not self.canAddPlayer():
            self.mainMenuElements['addBox'] = '\033[90m'
        if self.canRemovePlayer():
            self.mainMenuElements['removeBox'] = '\033[97m'
            
    def changeComputerSpeed(self):
        if self.computerSpeed == 'slow':
            self.computerSpeed = 'normal'
        elif self.computerSpeed == 'normal':
            self.computerSpeed = 'fast'
        elif self.computerSpeed == 'fast':
            self.computerSpeed = 'slow'
    
    def getMainMenuElements(self):
        return self.mainMenuElements

class Deck():
    ''''shuffle' (bool) : shuffle deck.'''

    colors =     ('red','yellow','green','blue')
    values =     ('0','1','2','3','4','5','6','7','8','9','X','R','+2')
    
    def __init__(self, populate):
        '''Initializes proper deck of 108 Uno Cards.'''
        self.deck = []
        if populate:
            self.populate(True)
            
    def __getitem__(self, index):
        return self.deck[index]
            
    def populate(self, shuffle=True):
        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(color, value))
                if value != '0':
                    self.deck.append(Card(color, value))
        for i in range(4):
            i #unused
            self.deck.append(Card('wild', '+4'))
            self.deck.append(Card('wild', 'W'))
        if shuffle:
            self.shuffle()

    def __iter__(self):
        return iter(self.deck)

    def __len__(self):
        return len(self.deck)

    def draw(self):
        return self.deck.pop()
    
    def place(self, card):
        return self.deck.append(card)
    
    def insert(self, card):
        self.deck.insert(0, card)

    def shuffle(self):
        random.shuffle(self.deck)

class ComputerPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Computer'
        self.begun = False
        self.colorsInHand = {'red':0, 'blue':0, 'green':0, 'yellow':0, 'wild':0}
        self.colorsOutHand = {}
        self.currentColor = ""
        
    def addCard(self, card):
        Player.addCard(self, card)
        color = card.getColor()
        self.colorsInHand[color] += 1
        
    def indexCard(self, cardColor, cardValue):
        for card in self.hand:
            if card.getValue() == cardValue:
                if cardValue in ('+4', 'W'):
                    return self.hand.indexCard(card)
                else:
                    if card.getColor() == cardColor:
                        return self.hand.indexCard(card)
        raise ValueError("Card Cannot Be Found")
        
    def think(self, match):
        card = None
        self.currentColor = match.currentColor
        currentValue = match.currentValue
        zeroChangeRule = match.zeroChange
        twoPlayers = False
        previousTurnID = match.getNextTurn(True)
        nextTurnID = match.getNextTurn(False)
        previousPlayer = match.getPlayer(previousTurnID)
        #nextPlayer = match.getPlayer(nextTurnID)
        if previousTurnID == nextTurnID:
            twoPlayers = True
            if self.canSkip == False and self.canReverse == True:
                self.canSkip = True
            self.canReverse = False
        
        self.getLegalCards(self.currentColor, currentValue, zeroChangeRule)

        ### DRAW CASE ###
        
        if len(self.legalCards) == 0 and len(self.wildCards) == 0:
            return "d"
        
        else:
            
            ### NO LEGAL CARD, USE WILD CARD ###
            
            if len(self.legalCards) == 0:
                
                if zeroChangeRule and self.canZeroChange:
                    bestZeroColor = self.getBestColor(self.zeroCards)
                    card = self.getCardByColor(self.zeroCards, bestZeroColor)
                    
                else:
                    
                    if self.canDrawFour:
                        card = self.getCardByValue(self.wildCards, "+4")
                        print(card)
                        
                    else:
                        card = random.choice(self.wildCards)
                
            else:
                
                ### HAS LEGAL CARD ###
                
                if twoPlayers and self.canSkip: #Always play a skip card in a two player game
                    #print("Shed Skip Strategy")
                    card = self.getCardByValue(self.legalCards,"R", "X")
                    
                if self.canReverse and previousPlayer.didDraw():
                    #print("Reverse Strategy")
                    reverseCards = self.getAllCardsByValue(self.legalCards, "R")
                    for reverseCard in reverseCards:
                        if reverseCard.getColor() == self.currentColor:
                            card = reverseCard
                    
                if self.canValueChange:
                    # Computer Can Value Change, However, Should it?
                    # Computer Checks to See if Value Change Color is Better Than Current
                    currentColorNum = self.colorsInHand[self.currentColor]
                    bestValueChangeColor = self.getBestColor(self.valueChangeCards)
                    if self.colorsInHand[bestValueChangeColor] > currentColorNum or len(self.valueChangeCards) == len(self.legalCards):
                        card = self.getCardByColor(self.valueChangeCards, bestValueChangeColor)
                    
                    
                if card == None:
                    #print("Random Strategy")
                    card = random.choice(list(set(self.legalCards) - set(self.valueChangeCards)))
            
        color = card.getColor()
        self.colorsInHand[color] -= 1
        return str(self.indexCard(card.getColor(), card.getValue()))
    
    def getWildColor(self):
        maxKey = max(self.colorsInHand, key=self.colorsInHand.get)
        if maxKey == 'wild':
            return random.choice(('r','g','b','y'))
        else:
            return maxKey
        
    def getCardByValue(self, cardList, *values):
        for card in cardList:
            if card.getValue() in values:
                return card
            
    def getAllCardsByValue(self, cardList, *values):
        cards = []
        for card in cardList:
            if card.getValue() in values:
                cards.append(card)
        return cards
    
    def getCardByColor(self, cardList, *colors):
        for card in cardList:
            if card.getColor() in colors:
                return card
    
    def getBestColor(self, cardList):
        bestColor = None
        bestColorNum = 0
        for card in cardList:
            color = card.getColor()
            if self.colorsInHand[color] > bestColorNum:
                bestColor = color
                bestColorNum = self.colorsInHand[color]
        return bestColor

class Card():
    '''
    'suit' (string) : Card's Color (rgby)
    'rank' (string) : Card's Value (0-9, R, X, W, +2, +4)
    '''

    colors = {
        'red'       :   '\033[91m',
        'green'     :   '\033[92m',
        'yellow'    :   '\033[93m',
        'blue'      :   '\033[94m',
        'purple'    :   '\033[95m',
        'cyan'      :   '\033[96m',
        'white'     :   '\033[97m',
        'wild'      :   '',
        'dwild'     :   '',
        'dred'       :   '\033[31m',
        'dgreen'     :   '\033[32m',
        'dyellow'    :   '\033[33m',
        'dblue'      :   '\033[34m',
        'dpurple'    :   '\033[35m',
        'dcyan'      :   '\033[36m',
        'dwhite'     :   '\033[37m',
    }
    
    idMap = {
        'red':'R','blue':'B','green':'G','yellow':'Y','wild':'W',
        '0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9',
        '+2':'+','R':'R','W':'W','+4':'$','X':'X'
    }

    bigNums = {
        "0" : [" .d888b. ","d88P Y88b","888   888","888   888","888   888","888   888","d88P Y88b"," \"Y888P\" "],
        "1" : ["  d888   "," d8888   ","   888   ","   888   ","   888   ","   888   ","   888   "," 8888888 "],
        "2" : [".d8888b. ","d88P  Y88","d8    888","    .d88P",".od888P\" ","d88P\"    ","888\"     ","888888888"],
        "3" : [" .d8888b.","d88P  Y88","     .d88","   8888\" ","     \"Y8b","888    88","Y88b  d88"," \"Y8888P\""],
        "4" : ["    d88b ","   d8P88 ","  d8  88 "," d8   88 ","d8    88 ","888888888","      88 ","      88 "],
        "5" : ["888888888","888      ","888      ","8888888b ","   \"Y88b ","      888","Y88b d88P","\"Y8888P\" "],
        "6" : [" .d888b. ","d88P Y88b","888      ","888d888b ","888P \"Y8b","888   888","Y88b d88b"," \"Y888P\" "],
        "7" : ["888888888","      d8P","     d8P ","    d8P  "," 8888888 ","  d8P    "," d8P     ","d8P      "],
        "8" : [" .d888b. ","d8P   Y8b","Y8b.  d8P"," \"Y8888\" "," .dP\"Yb. ","888   888","Y88b d88P"," \"Y888P\" "],
        "9" : [" .d888b. ","d8P   Y8b","88     88","Y8b.  d88"," \"Y88P888","      888","Y88b d88P"," \"Y888P\" "],
        "X" : ["Y8b   d8P"," Y8b d8P ","  Y8o8P  ","   Y8P   ","   d8b   ","  d888b  "," d8P Y8b ","d8P   Y8b"],
        "W" : ["88     88","88     88","88  o  88","88 d8b 88","88d888b88","88P   Y88","8P     Y8","P       Y"],
        "+2" : ["  db     ","  88     ","C8888D   ","  88 8888","  VP    8","     8888","     8   ","     8888"],
        "+4" : ["  db     ","  88     ","C8888D   ","  88   d ","  VP  d8 ","     d 8 ","    d8888","       8 "],
        "R9" : ["    d88P ","   d88P  ","  d88P   "," d88P    "," Y88b    ","  Y88b   ","   Y88b  ","    Y88b "],
        "R8" : ["   d88P  ","  d88P   "," d88P    ","d88P     ","Y88b     "," Y88b    ","  Y88b   ","   Y88b  "],
        "R7" : ["  d88P  Y"," d88P    ","d88P     ","88P      ","88b      ","Y88b     "," Y88b    ","  Y88b  d"],
        "R6" : [" d88P  Y8","d88P    Y","88P      ","8P       ","8b       ","88b      ","Y88b    d"," Y88b  d8"],
        "R5" : ["d88P  Y88","88P    Y8","8P      Y","P        ","b        ","8b      d","88b    d8","Y88b  d88"],
        "R4" : ["88P  Y88b","8P    Y88","P      Y8","        Y","        d","b      d8","8b    d88","88b  d88P"],
        "R3" : ["8P  Y88b ","P    Y88b","      Y88","       Y8","       d8","      d88","b    d88P","8b  d88P "],
        "R2" : ["P  Y88b  ","    Y88b ","     Y88b","      Y88","      d88","     d88P","    d88P ","b  d88P  "],
        "R1" : ["  Y88b   ","   Y88b  ","    Y88b ","     Y88b","     d88P","    d88P ","   d88P  ","  d88P   "],
        "R0" : [" Y88b    ","  Y88b   ","   Y88b  ","    Y88b ","    d88P ","   d88P  ","  d88P   "," d88P    "],
    }
        

    def __init__(self, color, value):
        '''Initializes Uno Card w/ Color and Value.'''
        self.wild = False       #Is wild card?
        self.zero = False
        self.cardID = '{}{}'.format(self.idMap[color],self.idMap[value])
        self.setColor(color)
        self.setValue(value)
        self.setPoints(value)


    #############################################

    ### -\/-  Retrieve Card Information  -\/- ### 
    
    def __repr__(self):
        return "{},{}".format(self.color, self.value)

    def getBigNum(self, reverse, reverseSeed=0):
        '''Returns list of strings to draw card's value on the pile.'''
        bigNums = []
        colorCode = self.colorCode
        colorCodeDark = self.colorCodeDark
        value = self.value
        if value == 'R':
            if not reverse:
                value += str(reverseSeed)
            else:
                value += str(9-reverseSeed)
        for mid in self.bigNums[value]:
            bigNums += ['{}| |{}'.format(colorCode,colorCodeDark)+mid+'{}| |\033[0m\t'.format(colorCode)]
            
        return bigNums

    def getColor(self):
        '''Returns card's color.'''
        return self.color
    
    def getColorCode(self):
        '''Returns card's color code.'''
        return self.colorCode

    def getValue(self):
        '''Returns card's value.'''
        return self.value
    
    def getPoints(self):
        '''Returns card's point value.'''
        return self.points
    
    def getRow(self,rowNum,hide=False):
        value = self.value
        displaySpace = self.displaySpace
        if hide:
            colorCode = '\033[97m'
            value = '?'
            displaySpace = ' '
        else:
            colorCode = self.colorCode
            if self.isWild():
                if rowNum == 0:  
                    colorCode = '\033[91m'
                elif rowNum == 1:
                    colorCode = '\033[93m'
                elif rowNum == 2:
                    colorCode = '\033[92m'
                elif rowNum == 3:
                    colorCode = '\033[94m'
        
        if rowNum == 0:
            return      '{}\u2666--\u2666\033[0m'.format(colorCode)
        elif rowNum == 1:
            return      '{}|{}{}|\033[0m'.format(colorCode, displaySpace, value)
        elif rowNum == 2:
            if hide:
                return   '{}|? |\033[0m'.format(colorCode)
            else:
                return   '{}|  |\033[0m'.format(colorCode)
        elif rowNum == 3:
            return      '{}\u2666--\u2666\033[0m'.format(colorCode)

    #############################################

    ### -\/-  Set Card Information  -\/- ### 
    
    def setColor(self, color):
        '''Sets Card's color and escape code.'''
        if color == 'blue':
            self.color = 'blue'
            self.colorCode = self.colors['blue']
            self.colorCodeDark = self.colors['dblue']
        elif color == 'red':
            self.color = 'red'
            self.colorCode = self.colors['red']
            self.colorCodeDark = self.colors['dred']
        elif color == 'yellow':
            self.color = 'yellow'
            self.colorCode = self.colors['yellow']
            self.colorCodeDark = self.colors['dyellow']
        elif color == 'green':
            self.color = 'green'
            self.colorCode = self.colors['green']
            self.colorCodeDark = self.colors['dgreen']
        elif color == 'wild':         #No color modification
            self.wild = True
            self.color = 'wild'
            self.colorCodeDark = self.colors['dwild']
            self.colorCode = self.colors['wild']

    def setValue(self, value):
        if value in ('0','1','2','3','4','5','6','7','8','9','X','R','+2','+4','W'):
            self.value = value
            self.displaySpace = ' '
            if len(value) == 2:
                self.displaySpace = ''
            if value == '0':
                self.zero = True
                
    def setPoints(self, value):
        if value in ('0','1','2','3','4','5','6','7','8','9'):
            self.points = int(value)
        elif value in ("W", "+4"):
            self.points = 50
        else:
            self.points = 20


    #############################################

    ### -\/-  Wild Card Methods  -\/- ### 

    def changeColor(self, color):
        '''Changes Card's Color, Intended for Wild Cards.'''
        self.setColor(color)

    def isWild(self):
        '''Returns if card is a wild card.'''
        return self.wild
    
    def isZero(self):
        return self.zero
    
class Match():

    elementsInit = {
        ### Names (final) ###
        'P1Name':'           ', 'P2Name':'           ', 'P3Name':'           ', 'P4Name':'           ',
        ### Card Values ### 
        'P1Cards':'           ', 'P2Cards':'           ', 'P3Cards':'           ', 'P4Cards':'           ',
        ### Turn Colors / Hand###
        'P1Turn':'', 'P2Turn':'', 'P3Turn':'', 'P4Turn':'',
        'HName':'\t\t', 'HVisual':'' ,'Hand':'',
        ### Deck ###
        'DNum':'', 'Deck':['','','','','','','','',''],
        'PostDNum':'',
        ### Pile ###
        'uHeader':'\t\t\t\t', 'uMiddle':'   ', 'uLower':'   ',
        'oHeader':'\t\t\t', 'oMiddle':['\t\t\t','\t\t\t','\t\t\t','\t\t\t','\t\t\t','\t\t\t','\t\t\t','\t\t\t'],
        ### Messages ###
        'Console':'', 'Error':''
        }
    
    speeds = {'slow':2,'normal':1,'fast':0}
        

    def __init__(self, gs):
        ### Decks ###
        self.deck = Deck(True)
        self.pile = Deck(False)
        
        ### Player Information ###
        self.players = gs.players
        self.turnList = []
        self.handTitles =  {'play1':'','play2':'','play3':'','play4':''}
        
        ### Carry Information ###
        self.displayEffects = gs.displayEffects
        self.hideComputerHands = gs.hideComputerHands
        self.zeroChange = gs.zeroChange
        self.computerSpeed = self.speeds[gs.computerSpeed]
        self.simulation = gs.computerSimulation

        ### Data ###
        self.handPosition = 0               # For hand displays
        self.drawAmount = 0                 # Used for force draws
        self.passes = 0                     # Keep track of consecutive passes for emergency color change
        self.passMax = 0                    # Max passes before color change
        self.turn = ''                      # Current turn
        self.event = ''                     # Wild, Reverse, Skip, etc
        self.wildColorChange = ''           # Specifies color to change wild card to
        self.currentColor = ''              # Current color
        self.currentValue = ''              # Current value
        self.winnerID = ''                  # ID of Player who Won
        self.reverse = False                # Is turn order reversed
        self.turnComplete = False           # Is turn complete
        self.matchComplete = False          # Is the Game over?
        self.matchAbort = False             # Did the match conclude without a winner?
        self.forcedWild = False             # Force change wild

        ### Initialize Names / Cards / Deck (Assuming New Game) ###
        self.elements = dict(self.elementsInit)
        
        keyStringName = 'P{}Name'
        keyStringCards = 'P{}Cards'
        
        for i in self.players:
            self.elements[keyStringName.format(i[-1])] = self.players[i].getName()+(' '*(11-len(self.players[i].getName())))
            self.elements[keyStringCards.format(i[-1])] = '  '+(' '*(3-len(str(self.players[i].getCardNum()))))+str(self.players[i].getCardNum())+' Cards'
            
        self.elements['DNum'] = len(self.deck)
        
        if len(str(len(self.deck))) < 2:
            self.elements['PostDNum'] = '\t'
            
        j = 8
        for i in range(int(math.ceil(len(self.deck)/12))):
            self.elements['Deck'][j] = '='
            j -= 1
                    
        for key in GameSettings.playerIdentities:
            try:
                self.buildHandString(key)
                self.turnList += [key]
            except KeyError:
                pass
            
        self.passMax = len(self.turnList)
            
    def clearShell(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def begin(self):
        self.elements['Console'] = 'Beginning Game, Press Enter.'
        print(self.drawScreen())
        self.enterBreak()
        self.eventDealCards()
        self.turn = random.choice(self.turnList)
        self.elements['Console'] = 'First turn will be {}. Press Enter.'.format(self.players[self.turn].getName())
        print(self.drawScreen(True))
        self.enterBreak()
        self.placeCard()
        self.elements['P{}Turn'.format(self.turn[-1])] = '\033[93m'
        if self.event == 'wild':
            self.eventWildCard()
        elif self.event == 'reverse':
            self.eventReverse()
            
    def end(self, gs):
        if not self.matchAbort:
            points = 0
            self.elements['P{}Turn'.format(self.turn[-1])] = ''
            self.elements['Console'] = '{} Wins! Press Enter to Begin Point Tally'.format(self.players[self.winnerID].getName())
            print(self.drawScreen())
            self.enterBreak()
            
            for identity in self.turnList:
                if identity != self.winnerID:
                    self.turn = identity
                    self.elements['HName'] = self.handTitles[self.turn]
                    self.elements['P{}Turn'.format(self.turn[-1])] = '\033[93m'
                    while self.players[identity].getCardNum() > 0:
                        card = self.players[identity].removeCard(0)
                        points += card.getPoints()
                        self.elements['Console'] = '{} Won {} Points!'.format(self.players[self.winnerID].getName(),points)
                        
                        keyStringCards = 'P{}Cards'
                        self.elements[keyStringCards.format(identity[-1])] = '  '+(' '*(3-len(str(self.players[identity].getCardNum()))))+str(self.players[identity].getCardNum())+' Cards'
                        self.players[identity].maxScroll = math.ceil((self.players[identity].getCardNum() / 10)-1)
                        if self.handPosition > self.players[identity].maxScroll:
                            self.handPosition -= 1
                        self.buildHandVisual(identity)
                        
                        if self.displayEffects and not self.simulation:
                            print(self.drawScreen())
                            time.sleep(.1)
                    self.elements['P{}Turn'.format(self.turn[-1])] = ''
                        
            self.players[self.winnerID].addPoints(points)
            self.elements['Console'] = '{} Won {} Points! Press Enter'.format(self.players[self.winnerID].getName(),points)
            print(self.drawScreen())
            self.enterBreak()
        
        gs.clearStaging()
        for identity in self.turnList:
            self.players[identity].discardHand()
            gs.addPlayer(self.players[identity])
        return gs
        
    def adjustCardAmount(self, playerID):
        keyStringCards = 'P{}Cards'
        self.elements[keyStringCards.format(playerID[-1])] = '  '+(' '*(3-len(str(self.players[playerID].getCardNum()))))+str(self.players[playerID].getCardNum())+' Cards'
        self.players[playerID].maxScroll = math.ceil((self.players[playerID].getCardNum() / 10)-1)
        if self.handPosition > self.players[playerID].maxScroll:
            self.handPosition -= 1
        self.buildHandVisual(playerID)

    def buildHandString(self, playerID):
        playerName = self.players[playerID].getName()
        if len(playerName) < 9:
            self.handTitles[playerID] = "{}'s Hand\t".format(self.players[playerID].getName())
        else:
            self.handTitles[playerID] = "{}'s Hand".format(self.players[playerID].getName())

    def buildHandVisual(self, playerID):
        string = '['
        for i in range(self.players[playerID].maxScroll+1):
            if i == self.handPosition:
                string += '|'
            else:
                string += '-'
        string += ']'
        self.elements['HVisual'] = string

    def checkInput(self, playerInput):
        if playerInput == '':
            return {'valid':False,'entry':playerInput}
        if playerInput.isnumeric():
            if int(playerInput)+(10*self.handPosition) < self.players[self.turn].getCardNum():
                return {'valid':True,'entry':str(int(playerInput)+(10*self.handPosition)),'type':'card'}
            else:
                self.elements['Error'] = '{} is not a card.'.format(playerInput)
                return {'valid':False,'entry':playerInput}
        else:
            playerInput = playerInput.lower()[0]
            if playerInput in ['<','>','u','d','p','q','s']:
                return {'valid':True,'entry':playerInput}
            else:
                self.elements['Error'] = '{} is not a valid selection.'.format(playerInput)
                return {'valid':False,'entry':playerInput}

    def checkColorInput(self, playerInput):
        if playerInput == '':
            return {'valid':False,'entry':playerInput}
        playerInput = str(playerInput).lower()[0]
        if playerInput[0] == 'b':
            return {'valid':True,'entry':'blue'}
        elif playerInput[0] == 'r':
            return {'valid':True,'entry':'red'}
        elif playerInput[0] == 'g':
            return {'valid':True,'entry':'green'}
        elif playerInput[0] == 'y':
            return {'valid':True,'entry':'yellow'}
        return {'valid':False,'entry':playerInput}

    def eventDealCards(self):
        if self.displayEffects and not self.simulation:
            self.elements['Console'] = 'Dealing Cards...'
        for i in ('play1','play2','play3','play4'):
            if i in self.players:
                for j in range(7):
                    j #unused
                    self.dealCard(i)
                    if self.displayEffects and not self.simulation:
                        print(self.drawScreen(True))
                        time.sleep(.1)

    def eventReverse(self):
        if self.displayEffects and not self.simulation:
            hide = False
            if self.players[self.turn].getType() == "Computer":
                hide = self.hideComputerHands
            self.elements['Console'] = "Reverse Card Played! Reversing Turn Order.".format(self.players[self.turn].getName())
            print(self.drawScreen(hide))
            time.sleep(1)
            for i in range(10):
                cardBigNums = self.pile[0].getBigNum(self.reverse,i)
                self.elements['oMiddle'] = cardBigNums
                print(self.drawScreen(hide))
                if self.displayEffects and not self.simulation:
                    time.sleep(.1)
        cardBigNums = self.pile[0].getBigNum(self.reverse,9)
        self.elements['oMiddle'] = cardBigNums
        self.reverse = not self.reverse
        self.event = ''
            
    def eventSkip(self):
        if self.displayEffects and not self.simulation:
            hide = False
            if self.players[self.turn].getType() == "Computer":
                hide = self.hideComputerHands
            self.elements['Console'] = "Skip Card Placed! Skipping {}'s Turn.".format(self.players[self.turn].getName())
            print(self.drawScreen(hide))
            time.sleep(1)
            for i in range(2):
                i #unused
                self.elements['P{}Turn'.format(self.turn[-1])] = '\033[91m'
                print(self.drawScreen(hide))
                time.sleep(.3)
                self.elements['P{}Turn'.format(self.turn[-1])] = ''
                print(self.drawScreen(hide))
                time.sleep(.3)
        self.turnComplete = True
        self.event = ''

    def eventWildCard(self):
        hide = False
        if not self.forcedWild:
            if self.players[self.turn].getType() == 'Human':
                self.elements['Console'] = 'Wild Card! Specifiy a Color: (B)lue, (R)ed, (G)reen, (Y)ellow'
                self.elements['Error'] = 'Specifiy A Color'
                print(self.drawScreen())
                playerInput = str(input("Color Change: "))
                checked = self.checkColorInput(playerInput)
                while not checked['valid']:
                    if checked['entry'] == '<':
                        self.handPosition -= 1
                        if self.handPosition == -1:
                            self.handPosition = self.players[self.turn].maxScroll
                        self.buildHandVisual(self.turn)
                    elif checked['entry'] == '>':
                        self.handPosition += 1
                        if self.handPosition > self.players[self.turn].maxScroll:
                            self.handPosition = 0
                        self.buildHandVisual(self.turn)
                    print(self.drawScreen())
                    playerInput = str(input("Color Change: "))
                    checked = self.checkColorInput(playerInput)
            else:
                hide = self.hideComputerHands
                checked = self.checkColorInput(self.players[self.turn].getWildColor())
            self.wildColorChange = checked['entry']
        else:
            self.wildColorChange = self.checkColorInput(random.choice(('r','b','g','y')))['entry']
            self.forcedWild = False
        self.currentColor = self.wildColorChange
        self.elements['Error'] = ""
        if self.displayEffects and not self.simulation:
            self.elements['Console'] = 'Wild Card! Changing Color.'
            seed = 1
            for i in range(10):
                i #unused
                if seed > 4:
                    seed = 1
                print(self.drawScreen(hide,wildSeed=seed))
                time.sleep(.1)
                seed += 1
        self.pile[0].changeColor(self.wildColorChange)
        self.wildColorChange = ''
        cardBigNums = self.pile[0].getBigNum(self.reverse)
        self.elements['oHeader'] = '{}\u2666\u2666\u2666=========\u2666\u2666\u2666\033[0m\t'.format(self.pile[0].getColorCode())
        self.elements['oMiddle'] = cardBigNums
        self.event = ''
        
    def eventDraw(self):
        self.players[self.turn].addForceDraw(self.drawAmount)
        self.drawAmount = 0
        self.event = ''

    def dealCard(self, playerID):
        
        card = self.deck.draw()
        self.players[playerID].addCard(card)
        
        ### Adjust Hand Visual ###
        self.players[playerID].maxScroll = math.ceil((self.players[playerID].getCardNum() / 10)-1)
        self.handPosition = self.players[playerID].maxScroll
        self.buildHandVisual(playerID)
        
        ### Adjust Player Tile ###
        keyStringCards = 'P{}Cards'
        self.elements[keyStringCards.format(playerID[-1])] = '  '+(' '*(3-len(str(self.players[playerID].getCardNum()))))+str(self.players[playerID].getCardNum())+' Cards'
        
        ### Adjust Deck ###
        self.elements['DNum'] = len(self.deck)
        if len(str(len(self.deck))) < 2:
            self.elements['PostDNum'] = '\t'
        j = 8
        self.elements['Deck'] = [' ',' ',' ',' ',' ',' ',' ',' ', ' ']
        for i in range(math.ceil(len(self.deck)/12)):
            i #unused
            self.elements['Deck'][j] = '='
            j -= 1

    def placeCard(self, card=None):
        if card == None:
            ### Used At Beginning For First Card ###
            card = self.deck.draw()
            self.elements['DNum'] = len(self.deck)
            
        cardColor = card.getColorCode()
        cardBigNums = card.getBigNum(self.reverse)
        
        self.currentColor = card.getColor()
        self.currentValue = card.getValue()
        
        self.pile.insert(card)
        self.elements['oHeader'] = '{}\u2666\u2666\u2666=========\u2666\u2666\u2666\033[0m\t'.format(cardColor)
        self.elements['oMiddle'] = cardBigNums
        
        if len(self.pile) > 1:
            previousCard = self.pile[1]
            previousCardColor = previousCard.getColorCode()
            self.elements['uHeader'] = '{}      \u2666\u2666\u2666=========\u2666\u2666\u2666\033[0m\t\t'.format(previousCardColor)
            self.elements['uMiddle'] = '{}| |\033[0m'.format(previousCardColor)
            self.elements['uLower'] = '{}\u2666\u2666\u2666\033[0m'.format(previousCardColor)
            
        if self.currentColor == 'wild':
            self.event = 'wild'
        
        if self.currentValue == 'X':
            self.event = 'skip'
        elif self.currentValue == 'R':
            if len(self.players) > 2:
                self.event = 'reverse'
            else:
                self.event = 'skip'
        elif self.currentValue == '+4':
                self.drawAmount = 4
        elif self.currentValue == '+2':
                self.drawAmount = 2
        self.passes = 0
                
    def extractCard(self, playerID, index):
        card = self.players[playerID].removeCard(index)
        if self.players[playerID].getCardNum() == 0:
            self.matchComplete = True
            self.winnerID = self.turn
        self.adjustCardAmount(playerID)
        return card
    
    def enterBreak(self):
        if not self.simulation:
            str(input())
        return
            
    def nextTurn(self):
        self.turnComplete = False
        self.handPosition = 0
        turnType = self.players[self.turn].getType()
        self.players[self.turn].beginTurn()
        ### Prepare Hand Visuals ###
        
        self.elements['HName'] = self.handTitles[self.turn]
        self.buildHandVisual(self.turn)
        
        if self.event == 'skip':
            self.eventSkip()
        elif self.drawAmount > 0:
            self.eventDraw()
        
        while not self.turnComplete:
            if turnType == 'Human':
                self.players[self.turn].getLegalCards(self.currentColor, self.currentValue, self.zeroChange)
                if len(self.deck) > 0:
                    self.elements['Console'] = 'Select a card, (D)raw, or (P)ause.'
                else:
                    self.players[self.turn].removeForceDraw()
                    self.elements['Console'] = 'Select a card, (D)raw, (P)ause, or Pas(s).'
                if self.players[self.turn].getForceDraws() > 0:
                    self.elements['Error'] = 'Draw Card Played! Draw {} cards.'.format(self.players[self.turn].getForceDraws())
                print(self.drawScreen())
                playerInput = str(input("\033[97mSelection: \033[92m"))
                checked = self.checkInput(playerInput)
                while not checked['valid']:
                    print(self.drawScreen())
                    playerInput = str(input("\033[97mSelection: \033[92m"))
                    checked = self.checkInput(playerInput)
    
                playerInput = checked['entry']
                
                if playerInput == '<':
                    self.handPosition -= 1
                    if self.handPosition == -1:
                        self.handPosition = self.players[self.turn].maxScroll
                    self.buildHandVisual(self.turn)
                elif playerInput == '>':
                    self.handPosition += 1
                    if self.handPosition > self.players[self.turn].maxScroll:
                        self.handPosition = 0
                    self.buildHandVisual(self.turn)
                elif playerInput == 'd':
                    if len(self.deck) > 0:
                        self.elements['Error'] = ''
                        self.dealCard(self.turn)
                    else:
                        self.elements['Error'] = "Cannot Draw. Deck is Empty"
                elif playerInput == 'p':
                    pauseOutput = self.pauseScreen()
                    if pauseOutput == 'quit':
                        self.matchComplete = True
                        self.turnComplete = True
                        self.winnerID = 'play1'
                        self.matchAbort = True
                elif playerInput == 's':
                    if len(self.deck) > 0:
                        self.elements['Error'] = "Cannot pass until Deck is empty."
                    elif len(self.players[self.turn].getAllValidCards()) > 0:
                        self.elements['Error'] = "Cannot pass while having playable cards."
                    else:
                        self.turnComplete = True
                        self.passes += 1
                        if self.passes == self.passMax:
                            self.forcedWild = True
                            self.event = 'wild'
                            self.passes = 0
                elif playerInput.isnumeric():
                    if self.players[self.turn].getForceDraws() == 0:
                        cardCheck = self.players[self.turn].checkCard(playerInput)
                        if cardCheck in self.players[self.turn].getAllValidCards():
                            card = self.extractCard(self.turn, playerInput)
                            self.placeCard(card)
                            self.elements['Error'] = ""
                            self.turnComplete = True
                        else:
                            self.elements['Error'] = "Card Doesn't Match The Color {} or Value {}!".format(self.currentColor, self.currentValue)
                    else:
                        pass
                    
            elif turnType == 'Computer':
                self.elements['Console'] = '{}\'s Turn'.format(self.players[self.turn].getName())
                print(self.drawScreen(self.hideComputerHands))
                if not self.simulation:
                    time.sleep(self.computerSpeed)
                #str(input())
                while (True):
                    if self.displayEffects and not self.simulation:
                        time.sleep(.2)
                    if self.players[self.turn].getForceDraws() > 0 and len(self.deck) > 0:
                        cardIndex = 'd'
                    else:
                        cardIndex = self.players[self.turn].think(self)
                    if cardIndex.isnumeric():
                        card = self.extractCard(self.turn, int(cardIndex))
                        if card.getColor() != self.currentColor:
                            self.resetDrawBool()
                        self.placeCard(card)
                        self.turnComplete = True
                        break
                    else:
                        if cardIndex == 'd':
                            if len(self.deck) > 0:
                                self.dealCard(self.turn)
                                print(self.drawScreen(self.hideComputerHands))
                            else:
                                self.turnComplete = True
                                self.players[self.turn].removeForceDraw()
                                self.passes += 1
                                if self.passes == self.passMax:
                                    self.forcedWild = True
                                    self.event = 'wild'
                                    self.passes = 0
                                break
                
            ### DECODE INPUT ###
                
        if self.event == 'reverse':
            self.eventReverse()
        elif self.event == 'wild':
            self.eventWildCard()
            
        # Clear Current Turn
        self.elements['P{}Turn'.format(self.turn[-1])] = ''
        # Prepare Next Turn
        self.turn = self.getNextTurn()
        self.elements['P{}Turn'.format(self.turn[-1])] = '\033[93m'

    def drawScreen(self, hide=False, wildSeed=0):
        if self.simulation:
            return ''
        colorCombos = {
            1 : ['\033[91m','\033[93m','\033[92m','\033[94m'],
            2 : ['\033[94m','\033[91m','\033[93m','\033[92m'],
            3 : ['\033[92m','\033[94m','\033[91m','\033[93m'],
            4 : ['\033[93m','\033[92m','\033[94m','\033[91m'] }
        currentTurn = self.turn
        if currentTurn == '':
            currentTurn = self.turnList[-1]
            hide = True
        if wildSeed != 0:
            colorMod = colorCombos[wildSeed]
        else:
            colorMod = ['','','','']

        self.clearShell()
        screenout = ''
        screenout += '\t\t\033[94m      || ||\033[92m ||\ ||  \033[91m// \\\\\n\033[0m'
        screenout += '\t\t\033[94m      || ||\033[92m ||\\\|| \033[91m((   ))\n\033[0m'
        screenout += '\t\t\033[94m      \\\ //\033[92m || \|| \033[91m \\\ //\n\033[0m'
        screenout += '\033[97m===============================================================\n'
        screenout += '\033[93m{}\033[0m\n'.format(self.elements['Console'])
        screenout += '\033[97m===============================================================\n'
        screenout += '\t\t\t\t\t\t'     +        ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P1Turn'])
        screenout += '\033[97mDeck:\t\t'        +       '{}'.format(self.elements['uHeader'])       +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P1Turn'],self.elements['P1Name'])
        screenout += '\033[97m{} Cards'.format(self.elements['DNum'])       +       '{}'.format(self.elements['PostDNum'])+'\t'     +       '{}'.format(self.elements['uHeader'])       +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P1Turn'],self.elements['P1Cards'])
        screenout += '\t\t      '       +      '{}'.format(self.elements['uMiddle'])        +       '\033[97m{}{}'.format(colorMod[0],self.elements['oHeader'])     +      ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P1Turn'])
        screenout += '\033[97m  _+_ \t\t      '     +       '{}'.format(self.elements['uMiddle'])                                                                                                   +       '\033[97m{}{}'.format(colorMod[1],self.elements['oHeader'])         +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P2Turn'])                                                                                  
        screenout += '\033[97m | '      +       '\033[92m{}\033[0m'.format(self.elements['Deck'][0])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[2],self.elements['oMiddle'][0])      +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P2Turn'],self.elements['P2Name'])
        screenout += '\033[97m | '      +       '\033[92m{}\033[0m'.format(self.elements['Deck'][1])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[3],self.elements['oMiddle'][1])      +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P2Turn'],self.elements['P2Cards'])
        screenout += '\033[97m | '      +       '\033[92m{}\033[0m'.format(self.elements['Deck'][2])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[0],self.elements['oMiddle'][2])      +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P2Turn'])
        screenout += '\033[97m | '      +       '\033[93m{}\033[0m'.format(self.elements['Deck'][3])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[1],self.elements['oMiddle'][3])      +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P3Turn'])
        screenout += '\033[97m | '      +       '\033[93m{}\033[0m'.format(self.elements['Deck'][4])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[2],self.elements['oMiddle'][4])      +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P3Turn'],self.elements['P3Name'])
        screenout += '\033[97m | '      +       '\033[93m{}\033[0m'.format(self.elements['Deck'][5])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uMiddle'])       +       '\033[97m{}{}'.format(colorMod[3],self.elements['oMiddle'][5])      +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P3Turn'],self.elements['P3Cards'])
        screenout += '\033[97m | '      +       '\033[91m{}\033[0m'.format(self.elements['Deck'][6])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uLower'])        +       '\033[97m{}{}'.format(colorMod[0],self.elements['oMiddle'][6])      +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P3Turn'])
        screenout += '\033[97m | '      +       '\033[91m{}\033[0m'.format(self.elements['Deck'][7])        +       '\033[97m |\t\t      '      +       '{}'.format(self.elements['uLower'])        +       '\033[97m{}{}'.format(colorMod[1],self.elements['oMiddle'][7])      +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P4Turn'])
        screenout += '\033[97m |_'      +     '\033[91m{}\033[0m'.format(self.elements['Deck'][8])          +        '\033[97m_|\t\t         '                                                      +      '\033[97m{}{}'.format(colorMod[2],self.elements['oHeader'])          +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P4Turn'],self.elements['P4Name'])
        screenout += '\033[97m\t\t         '    +                                                                                                                                                                   '\033[97m{}{}'.format(colorMod[3],self.elements['oHeader'])         +       ' \033[97m{}|{}|\033[0m\n'.format(self.elements['P4Turn'],self.elements['P4Cards'])
        screenout += '\t\t\t\t\t\t'     +       ' \033[97m{}\u2666-----------\u2666\033[0m\n'.format(self.elements['P4Turn'])
        screenout += "\033[97m{}".format(self.elements['HName'])        +       "\t\t\t\t {}\n".format(self.elements['HVisual'])
        screenout += '\033[97m===============================================================\n'
        screenout += self.players[currentTurn].getHand(self.handPosition,hide)
        screenout += '\033[91m{}\033[0m'.format(self.elements['Error'])
        return screenout
    
    def pauseScreen(self):
        while True:
            self.clearShell()
            print('\n\t\t\tPause')
            print('\n\t\t1. Resume')
            print('\t\t2. Quit')
            
            selection = str(input('\nSelection: ')).upper()
            while selection not in ['1', '2']:
                print('\nSelection Invalid')
                selection = str(input('\nSelection: ')).upper()
                
            if selection == '1' or "":
                return ""
                
            elif selection == '2':
                return "quit"
                
    
    def isComplete(self):
        return self.matchComplete
    
    def next(self):
        self.turn = self.getNextTurn()
    
    def getNextTurn(self, forceReverse=False):
        if forceReverse:
            reverse = not self.reverse
        else:
            reverse = self.reverse
        currentIndex = self.turnList.index(self.turn)
        if not reverse:
            if (currentIndex + 1) == len(self.turnList):
                return self.turnList[0]
            else:
                return self.turnList[currentIndex+1]
        else:
            if currentIndex == 0:
                return self.turnList[len(self.turnList) - 1]
            else:
                return self.turnList[currentIndex-1]
            
    def getPlayer(self, playerID):
        return self.players[playerID]
    
    def resetDrawBool(self):
        for identity in self.players:
            self.players[identity].drew = False

def Uno(debugging=False):

    ###MENUS###
    
    def clearShell():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainMenu():
        sys.stdout.write("\x1b[8;32;63t")
        sys.stdout.flush()
        gs = GameSettings()
        
        while True:
 
            print(drawMainMenu(gs))
            
            selection = str(input('\033[97mSelection: \033[92m'))
            while selection not in ['1', '2', '3', '4', '5']:
                gs.mainMenuError = "Invalid Selection"
                print(drawMainMenu(gs))
                selection = str(input('\033[97mSelection: \033[92m'))
                
            if selection == '1':
                if gs.canBegin():
                    gs.mainMenuError = ""
                    gs.finalizePlayers()
                    gs = playMatch(gs)
                else:
                    gs.mainMenuError = "Two Players Required to Begin"

            elif selection == '2':
                if gs.canAddPlayer():
                    gs.mainMenuError = ""
                    gs = addPlayer(gs)
                else:
                    gs.mainMenuError = "Max Number of Players Reached"
                    
            elif selection == '3':
                if gs.canAddPlayer():
                    gs.mainMenuError = ""
                    gs = addComputer(gs)
                else:
                    gs.mainMenuError = "Max Number of Players Reached"

            elif selection == '4':
                if gs.canRemovePlayer():
                    gs.mainMenuError = ""
                    gs = removePlayer(gs)
                else:
                    gs.mainMenuError = "No Players to Remove"

            elif selection == '5':
                gs.mainMenuError = ""
                gs = settingsMenu(gs)

            else:
                raise BadInputError('Data Provided Has No Function')
            
    def playMatch(gs):
        for i in range(1):
            i
            m = Match(gs)
            m.begin()
            while (not m.isComplete()):
                m.nextTurn()
            gs = m.end(gs)
        return gs
            
    def addPlayer(gs):
        colors = ['\033[91m','\033[94m', '\033[92m', '\033[93m']
        nameOkay = False
        playerNum = gs.getPlayerNum() + 1
        colorIndex = playerNum - 1
        message = "\033[97mPlease Enter Player {}'s Name: {}".format(playerNum, colors[colorIndex])
        
        while not nameOkay:
            print(drawMainMenu(gs))
            name = str(input(message)).title()
            if len(name) > 11:
                gs.mainMenuError = "Name Must Be 11 Characters or Less!"
            elif len(name) == 0:
                gs.mainMenuError = ""
                return gs
            else:
                nameOkay = True
                for player in gs.playerStaging:
                    if player.getName() == name:
                        nameOkay = False
                if nameOkay == False or name in GameSettings.computerNames:
                    gs.mainMenuError = "Name Cannot Match Another Player's Name!"
                        
        p = Player(name)
        gs.addPlayer(p)
        gs.mainMenuError = ""
        
        return gs
    
    def addComputer(gs):
        name = gs.getComputerName()
        c = ComputerPlayer(name)
        gs.addPlayer(c)
        
        return gs
    
    def removePlayer(gs):
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=63))
        sys.stdout.flush()
        clearShell()
        
        complete = False
        playerNum = gs.getPlayerNum()
        message = "\033[97mPlease Enter Player Number to Remove: \033[91m".format(playerNum)
        
        while (not complete):
            print(drawMainMenu(gs))
            number = str(input(message)) 
            if len(number) == 0:
                gs.mainMenuError = ""
                return gs
            try:
                number = int(number)
                if 0 < number <= playerNum:
                    complete = True
                else:
                    gs.mainMenuError = "Invalid Player Number!"
            except:
                gs.mainMenuError = "Please Enter the Player Number, not Name!"
        
        gs.mainMenuError = ""
        gs.removePlayer(number)
        return gs
    
    def settingsMenu(gs):
        while True:
            sys.stdout.write("\x1b[8;32;63t")
            sys.stdout.flush()
            clearShell()
            print('\n\t\tSettings')
            print('\n\t1. Draw Effects\t\t\t{}'.format(gs.displayEffects))
            print('\t2. Hide Computer Hands\t\t{}'.format(gs.hideComputerHands))
            print('\t3. Computer Speed\t\t{}'.format(gs.computerSpeed.title()))
            #print('\t4. Zero Card Changes Color\t{}'.format(gs.zeroChange))
            #print('\t5. Run Simulations\t\t{}'.format(gs.computerSimulation))
            print('\n\tA. Exit')
            
            selection = str(input('\nSelection: ')).upper()
            while selection not in ('1', '2', '3', '4', '5', 'A', ''):
                print('\nSelection Invalid')
                selection = str(input('\nSelection: ')).upper()
                
            if selection == '1':
                gs.displayEffects = not gs.displayEffects
                
            elif selection == '2':
                gs.hideComputerHands = not gs.hideComputerHands
                
            elif selection == '3':
                gs.changeComputerSpeed()
                '''
            elif selection == '4':
                gs.zeroChange = not gs.zeroChange
                
            elif selection == '5':
                gs.computerSimulation = not gs.computerSimulation
                '''
            elif selection == 'A' or selection == '' or selection in ('4','5'):
                return gs
    
    def drawMainMenu(gs):
        clearShell()
        gs.compileMainMenuElements()
        menuElements = gs.getMainMenuElements()
        screenout = ''
        screenout += '\t\t\033[94m      || ||\033[92m ||\ ||  \033[91m// \\\\\n\033[0m'
        screenout += '\t\t\033[94m      || ||\033[92m ||\\\|| \033[91m((   ))\n\033[0m'
        screenout += '\t\t\033[94m      \\\ //\033[92m || \|| \033[91m \\\ //\n\033[0m'
        screenout += '\033[97m===============================================================\033[0m\n'
        screenout += "{}1-----------------------------1\033[0m {}2-----------------------------2\033[0m\n".format(menuElements['play1box'],menuElements['play2box'])
        screenout += "{}|{}|\033[0m {}|{}|\033[0m\n".format(menuElements['play1box'],menuElements['play1row1'],menuElements['play2box'],menuElements['play2row1'])
        screenout += "{}|{}|\033[0m {}|{}|\033[0m\n".format(menuElements['play1box'],menuElements['play1row2'],menuElements['play2box'],menuElements['play2row2'])
        screenout += "{}1-----------------------------1\033[0m {}2-----------------------------2\033[0m\n".format(menuElements['play1box'],menuElements['play2box'])
        screenout += "{}3-----------------------------3\033[0m {}4-----------------------------4\033[0m\n".format(menuElements['play3box'],menuElements['play4box'])
        screenout += "{}|{}|\033[0m {}|{}|\033[0m\n".format(menuElements['play3box'],menuElements['play3row1'],menuElements['play4box'],menuElements['play4row1'])
        screenout += "{}|{}|\033[0m {}|{}|\033[0m\n".format(menuElements['play3box'],menuElements['play3row2'],menuElements['play4box'],menuElements['play4row2'])
        screenout += "{}3-----------------------------3\033[0m {}4-----------------------------4\033[0m\n".format(menuElements['play3box'],menuElements['play4box'])
        screenout += "\033[97m===============================================================\033[0m\n"
        screenout += "  {}\u2666---------------------------\u2666\033[0m \u2666===========================\u2666\n".format(menuElements['beginBox'])
        screenout += "  {}|1.       Begin Match       |\033[0m |        High Scores        |\n".format(menuElements['beginBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m \u2666---------------------------\u2666\n".format(menuElements['beginBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}|2.       Add Player        |\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}|3.      Add Computer       |\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['addBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['removeBox'])
        screenout += "  {}|4.      Remove Player      |\033[0m |                           |\n".format(menuElements['removeBox'])
        screenout += "  {}\u2666---------------------------\u2666\033[0m |                           |\n".format(menuElements['removeBox'])
        screenout += "  \033[97m\u2666---------------------------\u2666\033[0m |                           |\n"
        screenout += "  \033[97m|5.        Settings         |\033[0m |                           |\n"
        screenout += "  \033[97m\u2666---------------------------\u2666\033[0m \u2666===========================\u2666\n"
        screenout += "\033[97m===============================================================\033[0m\n"
        screenout += '\033[91m{}\033[0m'.format(gs.mainMenuError)
        return screenout
    
    mainMenu()
            
if __name__ == "__main__":
    Uno()
        

Share
	Created by Brandon Martin on Sat, 15 Jul 2017 (MIT)
◄ 	Python recipes (4591) 	►
◄ 	Brandon Martin's recipes (4) 	►
Tags

    artificial_intelligence
    cards
    game
    text_game
    uno

▶ Show machine tags (10)
Required Modules

    math
    os
    random
    sys
    time

Other Information and Tasks

    Licensed under the MIT License
    Viewed 7759 times
    Revision 1

 
