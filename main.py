from player import Player
from menu import Menu
from game import Game

g = Game()

def main():
    print "Teste"
    while True:
        print(chr(27) + "[2J")
        printaChamp()
        print ("\n1. Novo Jogo\n2. Sair\n")
        ans = input("Opcao: ")
        if ans == 1:
            print "Novo Jogo"
            newGame()
            break
        elif ans == 2:
            print "Flw!"
            break
        else:
            print "Essa opcao nao existe!"

def adicionandoP():
    global g
    print (chr(27) + "[2J")
    printaChamp()
    print "\n\n\n\n"
    nome = raw_input("Nome Jogador: ")
    g.addPlayer(nome)

def adicionandoI():
    global g
    print (chr(27) + "[2J")
    printaChamp()
    print "\n\n\n\n"
    nome = raw_input("Nome Bebida: ")
    g.addItem(nome)

def jogando():
    print (chr(27) + "[2J")
    printaChamp()
    g.getPlayers()
    cod = input("\nDigite o codigo do Jogador que vai beber: ")
    print (chr(27) + "[2J")
    printaChamp()
    g.play(cod)

def newGame():
    global g
    while True:
        print (chr(27) + "[2J")
        printaChamp()
        print ("""
1. Adicionar Item
2. Adicionar Jogador
3. Ver Jogadores
4. Ver Cardapio
5. Jogar
6. Sair""")
        ans = input("Opcao: ")

        if ans == 1:
            adicionandoI()
        elif ans == 2:
            adicionandoP()
        elif ans == 3:
            print (chr(27) + "[2J")
            printaChamp()
            g.getPlayers()
            raw_input("\nPressione ENTER para continuar...")
        elif ans == 4:
            print (chr(27) + "[2J")
            printaChamp()
            g.getCardapio()
            raw_input("\nPressione ENTER para continuar...")
        elif ans == 5:
            jogando()
            raw_input("\nPressione ENTER para continuar...")
        elif ans == 6:
            print (chr(27) + "[2J")
            break
        else:
            print "Essa opcao nao existe!"

def printaChamp():
    print("""
                      .+@+                                                                  ``.``
             @+;,` ,@@@@;                                                              `;#@+';:;'+#@'.
             ,@@@@@@@@@,                                                             ;@'.           `:@+`
              @@@@@@@@@'`          `                                               +@.     ;     ;:    `+@`
       ;      @@@@@@@@@@@@,       .+                                             :@`    :##,     #+##     +#
      +#     @@@@@@@@;.     @#,`  #@`                                           @;       @`::    @,`       `@.
     +@`    @@@@@@@@.       `@@@@:@@+                                         `@`  '     @#:`   `@'#.     `  +;
    :@@    #+.  #@@#         `@@@@@@@                                        .@   `@,    #'.;   ,@       '@#  ;+
   `@@@+++      `@@`           @@@@@@,                                       ,  `  ,@    '@+,    ,    ``@@;+   ,
   @@@@@#        '@             @@@@@@+                                        .@`  +@                +@@`#:
  :@@@@,         `'            `@@@@@@@@                                        +@  +#    `:#@@@#;.    ` #@.
  @@@@`           #            #@@@@@@@@@                                        #@#@   :@'.     `:@'     @
 ,@@@@`           @;          #@@@#@@@@@@@`                                       :, `.@,           `@'   +
 #@@@@            @@`        :.    :@@+                                              '#               ,@
 @@ ;@            @@@     ;@:       #@#                                            `+:                 `@
.@   #           `@@#:,#@@@@         @@                                             `
:    ``          ,@@@@@@@@@          `@
     #`         `#@@@@@@@@.          `;         `.#@@@@`                                                                    `
    .@`       :@@@@@@@@@@;                      #@@:`;@`  :@@`  ,@@     `@@`     @@@    ,@@, ` +@@@@@;   `@@     #@@@@'    .@@'   '@    @@@@@@`
    @@,    `'@@@@@@@@@@@#             .        '@@    `.  `@@    @@     .@@#     @@@`   #@@,   :@#`.@@+  `@@    @@. `@@+    @@@`  :#   @@.   +`
   .@@@@@@@` ,#@@@@@@@@@@:            @`       @@`     `   @@    @@     #+@@     @'@#   @#@:   :@+   @@   @@   +@,    @@`   @:@@  :#   @@     .
`;@@@@@@@#      :@@@@@@@@@,          `@,      .@@          @@    @@    `@.#@.    @,@@  :@+@;   :@#   @@  `@@   @@     +@+   @ #@' :#   @@@+.
,@@@@@@@#`        @@@@@@@@@.         @@'   `  ,@@`         @@@@@@@@    '@ ,@#    @.+@: #::@'   :@+  ,@#   @@   @@     :@@   @ `@@`:#   `@@@@@+
 :@@@@@@          @@@@.'@@@@        :@@+ ;@.  `@@         `@@    @@    @#';@@    @. @@`@ ,@+   :@+#@@#    @@   @@`    ,@#  `@  ,@@:#      +@@@#
  @@@@@#          @@@,     :#       @@@@@@@    @@+         @@    @@   ,@;:;@@,   @` @@+# `@#   :@+        @@   #@;    +@:   @   #@@#   :    :@@
  @@@@@@          @@@         #@@@@@@@@@@@     :@@:    '  `@@    @@   @#   :@#   @` .@@, `@@   :@#        @@   `@@`  `@@    @    @@@   @    .@@
  @@@#@@.         #@`          #@@@@@@@#@;      ;@@@#@@@  `@@    @@   @,   `@@` `@` `@@   @@   :@#        @@    ,@@++@@     @    .@#   @@;:;@@.
  @@# `@#         :+            @@@@@@@@'         +@@#.`  ::::  ;:,, ,.:  `:,,: :,:` ::  :,,,  :,:,      ```      '@#.     .``    .,   `;###,
  @@   `.`        `              +@@@@@@
  @.     ,,      `#             `@@@@@@@
  :       @'    ,@'             `@@@@@@@`
          '@@``+@@,             @@@:  '@.                                                                     `
           @@@@@@@             '+`                                     '@`    ,@@@@@`   +@`    `@@+@#   @;  `@.  #@@@@:
         ` #@@@@@@            .`                                       '@     `@,       @@#    @:` `#   @;  `@`  @@`  :
        .@@@@@@@@@`           @.                                       '@     `@, `    ,@#@   @@ `      @;  `@   #@  .
      ,@@@@@@@@@@@@+         #@`                                       '@     `@@@@    #..@.  @#   `    @:  `@   #@@@.
        `:+@@@@@@@@@@;      +@@. `.:'                                  '@     `@. `   `@##@+  @@   '@   @:  `@   @@  .
             .@@@@`   `@@@##@@@@@@@+                                   '@   ; `@.   , +'  #@  :@,  '@   @;  .@   @@   ;`
              ,@@@      @@@@@@@@@@.                                    +@@@@+``@@@@@` @`  .@,  '@#+@#   :@::@@   @@#@@@
               +@@       @@@@@@@'                                             `````` .``  .    ` .`     ` .,`    ``````
                #@      ;@@@@@;
                 #     +@@@'.
    """)
    # g = Game()
    # g.play(0)
    # g.addItem("51")
    # g.addItem("Domus")
    # g.addItem("Campari")
    # g.addItem("Pinga")
    #
    # g.addPlayer("Matheus")
    # g.addPlayer("Guedes")
    # g.addPlayer("Guga")
    # g.addPlayer("JP")
    #
    # g.play(0)
    # g.play(0)
    # g.play(0)
    # g.play(1)
    # g.play(2)
    # g.play(3)

    # c = Menu()
    # c.addItem("51")
    # c.addItem("Domus")
    # c.addItem("Campari")
    # c.addItem("51")
    # c.addItem("Pinga")
    #
    # print "%s\n" %(c)
    #
    # print c.getItem(0)
    #
    # j = Player("Matheus")
    # j.addShot(0)
    # j.addShot(0)
    # j.addShot(0)
    # j.addShot(0)
    # j.addShot(1)
    #
    # print j

#Roda o programa
if __name__ == "__main__":
    main()
