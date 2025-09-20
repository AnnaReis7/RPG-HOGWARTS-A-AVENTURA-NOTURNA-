#codigo_fonte

inicio = input("Deseja iniciar o jogo?(sim ou não):")

if inicio.lower() == "sim":

  print("\nO relógio da torre de Hogwarts anuncia uma nova era.")

  print("Nos corredores e nas florestas proibidas, segredos esquecidos voltam a despertar.")

  print("Cada feitiço pode ser a chave para a glória ou para a ruína, cabe a vocês, jovens bruxos e bruxas, escreverem a próxima página da história mágica.")

  print("Preparem suas varinhas, pois a aventura começa agora!")

elif inicio.lower() == "não" or inicio.lower() == "nao":

  print("Fim de jogo!")

else:
  print("Resposta inválida, tente novamente.")
  exit()

print("Você acaba de desembarcar em Hogwarts, é seu primeiro ano.")

print("Ao chegar no castelo, é conduzido por corredores sombrios até o salão principal.")

print("Lá, encontra longas mesas retangulares, cercadas por alunos curiosos, e um imenso tapete vermelho que corta o centro do salão.")

print("É ali, naquele momento, que o Chapéu Seletor começará a anunciar a casa de cada novato — incluindo você.")

print("\nResponda as questões e descubra sua casa em Hogwarts...")

pontos = {
      "Grifinória": 0,
      "Sonserina": 0,
      "Corvinal": 0,
      "Lufa-Lufa": 0
 }
def quiz_hogwarts():
 perguntas = [

   ("O que você mais valoriza?",
    {"a": ("Coragem", "Grifinória"),
    "b": ("Ambição", "Sonserina"),
    "c": ("Inteligência", "Corvinal"),
    "d": ("Lealdade", "Lufa-Lufa")}),

   ("Qual animal você prefere?",
    {"a": ("Leão", "Grifinória"),
    "b": ("Cobra", "Sonserina"),
    "c": ("Águia", "Corvinal"),
    "d": ("Texugo", "Lufa-Lufa")}),

   ("Qual feitiço você usaria primeiro?",
    {"a": ("Expelliarmus (desarmar o inimigo)", "Grifinória"),
     "b": ("Avada Kedavra (proibido, mas poderoso)", "Sonserina"),
     "c": ("Expecto Patronum (invocar um patrono)", "Corvinal"),
     "d": ("Reparo (consertar coisas)", "Lufa-Lufa")}),

   ("Qual destas aulas você mais gostaria de assistir?",
    {"a": ("Defesa Contra as Artes das Trevas", "Grifinória"),
     "b": ("Poções", "Sonserina"),
     "c": ("Adivinhação", "Corvinal"),
     "d": ("Herbologia", "Lufa-Lufa")}),

   ("Seus amigos diriam que você é...",
    {"a": ("Corajoso(a)", "Grifinória"),
    "b": ("Ambicioso(a)", "Sonserina"),
    "c": ("Sábio(a)", "Corvinal"),
    "d": ("Amigável", "Lufa-Lufa")}),

   ("Qual dessas cores você prefere?",
    {"a": ("Vermelho e Dourado", "Grifinória"),
    "b": ("Verde e Prata", "Sonserina"),
    "c": ("Azul e Bronze", "Corvinal"),
    "d": ("Amarelo e Preto", "Lufa-Lufa")}),

   ("Se tivesse que escolher um objeto mágico, qual seria?",
    {"a": ("Espada de Grifinória", "Grifinória"),
    "b": ("Medalhão de Sonserina", "Sonserina"),
    "c": ("Diadema de Corvinal", "Corvinal"),
    "d": ("Taça de Lufa-Lufa", "Lufa-Lufa")}),
]

# Loop pelas perguntas
for i, (pergunta, alternativas) in enumerate(perguntas, start=1):
  print(f"\n{i}) {pergunta}")
  for letra, (texto, _) in alternativas.items():
    print(f"{letra}) {texto}")
  resp = input("Resposta: ").lower()

  match resp:
    case "a" | "b" | "c" | "d":
      casa = alternativas[resp][1]
      pontos[casa] += 1

    case _:
      print("Resposta inválida! O Chapéu vai ignorar essa...")

# Determinar as casas com mais pontos
maior_pontuacao = max(pontos.values())
casas_vencedoras = [casa for casa, score in pontos.items() if score == maior_pontuacao]

print("\nO Chapéu Seletor pensou, refletiu... e decidiu!")

if len(casas_vencedoras) == 1:
  print(f"\nSua casa é: {casas_vencedoras[0]}")
else:
  print(f"Estou em dúvida... Você poderia se encaixar em: {', '.join(casas_vencedoras)}")
  escolha = input("Qual delas você prefere? ").capitalize()
  if escolha in casas_vencedoras:
    print(f"\nMuito bem! Então será... {escolha}!")
  else:
    print(f"\nNão entendi sua escolha... Então o Chapéu decide: {casas_vencedoras[0]}")

# Executar o quiz
quiz_hogwarts()


print("\nApós o jantar de boas-vindas, os novatos foram levados aos dormitórios de suas respectivas casas.")

print("Ao andar pelos corredores de Hogwarts, é possível perceber que a escola possui grandes mistérios e segredos sombrios. Sabendo disso, você precisa tomar uma decisão:")

print("\n1 - Explorar Hogwarts sozinho durante a madrugada.")
print("\n2 - Ignorar os pensamentos intrusivos e imprudentes de explorar Hogwarts.")

opcao = input("\nEscolha 1 ou 2: ")
if opcao == "1":
  print("\nVocê é pego por um dos professores, mas ele acoberta seus atos na esperança de que isso não ocorra novamente.")
  print("Caso contrário, você pode gerar graves consequências para sua casa.")

elif opcao == "2":
  print("\nVocê apenas dorme tranquilamente durante as madrugadas, mas sente que está perdendo algo por obedecer fielmente às regras da escola.")

else:
  print("Opção inválida.")

print("\nNo dia seguinte você acorda sentindo uma leve ventania em seu rosto.")
print("As janelas de seu dormitório estavam escancaradas e, em cima de sua cômoda, havia um envelope com seu nome.Você tem a opção de:")

print("\n1 - Abrir o envelope imediatamente para ver o que tem dentro.")
print("\n2 - Deixar para ler mais tarde.")

escolha = input("\nEscolha 1 ou 2: ")
if escolha == "1":
  print("\nVocê encontra uma carta que diz: 'Você possui grande potencial para ser livre sem precisar obedecer a essas regras inúteis.'")
elif escolha == "2":
  print("\nVocê deixa o envelope lá mesmo e vai se arrumar para o café da manhã, quando de repente, seu companheiro de dormitório abre o envelope e lê em voz alta:")
  print("'Você possui grande potencial para ser livre sem precisar obedecer a essas regras inúteis.'")

print("\nLogo após o café da manhã, seu companheiro de quarto se apresenta como Liandrux Pastanar.")
print("Ele pergunta o que significava aquele envelope e quem havia deixado lá.")
print("Claramente, você não sabia o que estava acontecendo, então não respondia nada e seguia para a aula de feitiços.")
print("Chegando lá, o professor seleciona alguns alunos para mostrarem suas habilidades com a varinha.")
print("Você e Pastanar foram uns dos escolhidos, então você decide:")

print("\n1 - Ser o primeiro a se apresentar, mesmo estando nervoso.")
print("\n2 - Se apresentar por último, a fim de observar como os outros alunos agem.")

decisao = input("\nEscolha 1 ou 2: ")
if decisao == "1":
  print("\nVocê erra o feitiço por estar nervoso demais, mas Pastanar acerta um feitiço não tão comum e surpreende a todos por ser apenas um novato.")
elif decisao == "2":
  print("\nMesmo tentando observar os outros alunos, você erra o feitiço, mas Pastanar acerta um feitiço não tão comum e surpreende a todos por ser apenas um novato.")

print("\nVocê fica intrigado com a mensagem da carta e resolve ir explorar a escola durante a madrugada. Você pensa em chamar Pastanar para ir com você.")

print("\n1 - Chamar Pastanar.")
print("\n2 - Não chamar Pastanar.")

convite = input("\nEscolha 1 ou 2: ")
if convite == "1":
  print("\nPastanar aceita seu convite e vocês vão juntos explorar a biblioteca durante a madrugada.")
elif convite == "2":
  print("\nVocê decide sair sozinho na madrugada para explorar a biblioteca.")

print("\nNo meio do caminho, encontra Pastanar, que, surpreso, pergunta o que você está fazendo indo para lá a essa hora.")
print("Antes que consiga explicar, ele se convida para te acompanhar. Juntos, seguem em direção à biblioteca.")
print("Você e Pastanar entram na Biblioteca Noturna de Hogwarts.")
print("As estantes parecem sussurrar segredos antigos...")


# Lista com descrições que será mostrada com for
cenas = [
    "O silêncio é tão denso que parece mágico.",
    "Uma chama bruxuleante ilumina livros encadernados em couro.",
    "Pastanar olha para você, inquieto, como se escondesse algo."
    ]
for cena in cenas:
  print(cena)

print("\nO que você deseja fazer?")
print("1 - Abrir uma estante trancada por feitiços.")
print("2 - Pesquisar nos catálogos antigos.")
print("3 - Escutar os sussurros da biblioteca.")

escolha = input("\n Escolha 1, 2 ou 3: ")

# Usando match case
match escolha:
  case "1":
    print("\nVocê toca a estante e um compartimento secreto se abre.")
    print("Dentro, há um livro em correntes mágicas.")

  case "2":
    print("\nNos catálogos, você encontra menções a uma criatura aprisionada nos porões.")
    print("Pastanar tenta disfarçar, mas você percebe que ele sabe mais do que aparenta.")

  case "3":
    print("\nVocê ouve uma voz sussurrando o nome de um livro proibido.")
    print("Pastanar recua, assustado, como se temesse algo invisível.")

  case _:
    print("\nOpção inválida, então você apenas observa o silêncio da biblioteca.")

print("\nDiante disso, você precisa decidir como agir com Pastanar.")

print("1 - Confiar nele e pedir ajuda.")
print("2 - Ignorar e tentar abrir o livro sozinho.")
print("3 - Sugerir voltar outro dia.")

decisao = input("\nEscolha 1, 2 ou 3: ")

match decisao:
  case "1":
    print("\nVocê decide confiar em Pastanar.")
    print("Ele aceita seguir com você até os porões da escola.")

  case "2":
    print("\nVocê toca o livro e sente uma energia sombria percorrer seu corpo.")
    print("Pastanar observa em silêncio, os olhos brilhando de forma estranha.")

  case "3":
    print("\nVocês recuam por enquanto, mas o mistério da biblioteca continua vivo.")

  case _:
    print("\nVocê hesita e não toma decisão... Pastanar decide por você: seguir até os porões.")

print("\nVocês descem até os porões da escola.")
print("Lá, uma criatura sombria desperta diante de vocês, oferecendo poder ilimitado...")

print("\nO que você fará diante da entidade?")
print("1 - Aceitar o pacto sombrio.")
print("2 - Usar um ritual para tentar selar a criatura.")
print("3 - Rejeitar o pacto e conjurar um feitiço de luz.")
final = input("\nEscolha 1, 2 ou 3: ")

# Usando match case para finais com histórias elaboradas
match final:
  case "1":
    print("\nFINAL TRÁGICO")
    historia_tragico = [
        "A voz da criatura invade sua mente, doce como mel e amarga como veneno.",
        "Você aceita o pacto, e as correntes do livro se quebram em chamas negras.",
        "Seu corpo se curva à sombra, seus olhos brilham em vermelho.",
        "Pastanar grita, mas é tarde demais: você se torna o novo guardião da escuridão.",
        "Hogwarts nunca mais será a mesma — e seu nome é apagado dos registros oficiais.",
        "Tudo o que resta é uma lenda sussurrada: o estudante que trocou sua alma por poder."
    ]
    for linha in historia_tragico:
      print(linha)

  case "2":
    print("\nFINAL NEUTRO")
    historia_neutro = [
          "Você segura o livro pesado e recita palavras antigas em voz trêmula.",
          "Runas brilham no ar, formando correntes de luz em torno da criatura.",
          "A sombra grita, mas se enrosca como fumaça sendo sugada para dentro do feitiço.",
          "Quando tudo acaba, o livro cai em suas mãos, agora marcado por cicatrizes de fogo.",
          "Você conseguiu selar a criatura... mas uma parte da escuridão ficou dentro de você.",
          "Hogwarts está a salvo, mas seus sonhos jamais serão tranquilos novamente."
          ]

    for linha in historia_neutro:
      print(linha)

  case "3":
    print("\nFINAL HERÓICO")
    historia_heroico = [
        "Você ergue a varinha e, com toda a força de sua alma, conjura um feitiço de luz.",
        "Uma explosão dourada ilumina o porão, afastando a sombra que recua em agonia.",
        "Pastanar cobre os olhos, incapaz de suportar o brilho intenso.",
        "A criatura uiva até se despedaçar em poeira escura que desaparece no ar.",
        "O silêncio retorna, mas desta vez carregado de vitória.",
        "Hogwarts jamais esquecerá o estudante que derrotou as trevas sozinho.",
        "Você se torna uma lenda, um símbolo de esperança para as próximas gerações."
        ]

    for linha in historia_heroico:
      print(linha)

  case _:
    print("\nComo você não escolheu nada, a criatura aproveita sua hesitação...")
    print("Em um instante, a sombra envolve seu corpo e apaga sua existência.")
    print("FINAL TRÁGICO")


print("\nFIM DA AVENTURA")
