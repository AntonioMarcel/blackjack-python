# Blackjack em Python no Terminal

Um jogo de Blackjack via linha de comando, totalmente funcional e escrito em Python usando Orientação a Objetos. Este projeto simula uma experiência real de cassino diretamente no seu terminal, completo com sistema de apostas, lógica do dealer e regras estritas de cassino.

## Funcionalidades

* **Design Orientado a Objetos:** Arquitetura limpa e modular usando classes separadas para Cartas (Cards), Baralho (Deck), Mãos (Hands), Fichas (Chips) e a lógica principal do Jogo (Game).
* **Sistema de Apostas:** Os jogadores começam com um saldo de fichas e fazem apostas a cada rodada. Pagamentos e perdas são gerenciados automaticamente.
* **Aplicação das Regras de Cassino:**
  * O Dealer é programado para comprar cartas até atingir 17.
  * Detecção de Blackjack Natural (21 nas duas primeiras cartas).
  * Tratamento de "Push" (Empate), onde a aposta é devolvida com segurança ao jogador.
* **Valor Dinâmico do Ás:** Os Áses ajustam automaticamente seu valor (11 ou 1) para evitar que o jogador ou o dealer estourem (bust).
* **Interface de Terminal Imersiva:** Feedback visual mostrando cartas escondidas (hole cards), revelações dramáticas e registros de ação turno a turno.

## Estrutura do Projeto

O código base é dividido em componentes modulares para fácil manutenção e escalabilidade:

* `Card`: Representa uma única carta de baralho com um naipe e valor específicos.
* `Deck`: Representa um baralho padrão de 52 cartas. Lida com a geração, embaralhamento e distribuição.
* `Hand`: Gerencia as cartas na mão de um jogador/dealer, calcula o valor total da mão e gerencia os ajustes do Ás.
* `Chips`: Gerencia o saldo do jogador, validando fundos e lidando com as transações de apostas.
* `Game`: O motor principal que une todos os objetos, gerenciando o loop do jogo, as entradas do usuário e as condições de vitória/derrota.

## Como Executar

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Clone este repositório:
```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   ```
3. Navegue até o diretório do projeto:
```bash
   cd nome-do-repositorio
   ```
4. Execute o jogo:
```bash
   python main.py
   ```
   *(Nota: Certifique-se de estar executando o arquivo principal onde a classe `Game` é instanciada).*

## Como Jogar

1. **Faça sua aposta:** Digite a quantidade de fichas que deseja apostar no início da rodada.
2. **Analise a mesa:** Você receberá duas cartas viradas para cima. O dealer recebe uma carta virada para cima e uma escondida.
3. **Comprar (Hit) ou Parar (Stand):**
   * Digite `H` para **Hit** (comprar outra carta) e chegar mais perto de 21.
   * Digite `S` para **Stand** (manter sua mão atual) e passar o turno para o dealer.
4. **Condições de Vitória:** Você vence se o total da sua mão for maior que o do dealer sem ultrapassar 21, ou se o dealer estourar (passar de 21). Se a sua mão ultrapassar 21, você estoura e perde sua aposta instantaneamente.