## Aula 12

### Exercício 43

Este exercício consiste na implementação de uma aplicação para gestão de torneios.
Comece por definir um jogo de equipas que lhe interesse (e.g., futebol, andebol, CS Go,
padel, etc.) e que se possa encaixar nas seguintes características:

- Pretende-se guardar numa base de dados as entidades:
  - Torneios – cada torneio tem os atributos id_torneio, nome, datas (início-fim) e
local.
  - Equipa – cada equipa é constituída para um torneio e tem os atributos id_equipa,
sigla, nome e id_torneio (chave estrangeira).
  - Jogador – cada jogador tem id_jogador, nome, data_de_nascimento (dia-mês-ano).
  - Jogo: cada jogo tem 2 equipas, uma data de realização e é guardado o resultado
final (e.g., números de golos das 2 equipas).
  - Ao longo do tempo cada jogador pode participar em várias equipas e cada equipa
tem vários jogadores.
- Para gerir as entidades deve ter um interface GUI implementado usando kivy.
 - Um web service intermedia as comunicações entre a base de dados e o interface GUI,
i.e., o interface não comunica diretamente com a base de dados mas sim com este
serviço.
- Algumas funcionalidades extra serão (até 30% da classificação):
  - (a) no sistema deve
ser fácil encontrar os jogadores por nome;
  - (b) no sistema será fácil filtrar a lista de
torneios (p.e., por nome ou por datas);
  - (c) o sistema permite a gestão de um torneio,
incluindo a definição manual ou aleatória das partidas num sistema de eliminação;
  - (d)
As equipas têm um logo que é apresentado no interface;
  - (e) o sistema tem um módulo
estatístico que apresente número de vitórias por jogador, jogador com mais vitórias
num determinado torneio, tornei com mais "golos", jogo com mais "golos", etc.

*Observação final*: as classificações finais são de 0 a 5... Não tem de fazer tudo o que
é enunciado para poderem apresentar o trabalho! O fundamental é ter um sistema
“funcional”!