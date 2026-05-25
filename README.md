# Blackjack em Python (OOP)

Um jogo clássico de Blackjack (21) jogável no terminal, construído passo a passo utilizando os princípios de Programação Orientada a Objetos (OOP) em Python.

---

## Estrutura do Projeto (Classes e Objetos)

Até o momento, o jogo conta com a seguinte arquitetura de classes:

* **`Card` (Carta):** Representa uma carta individual do baralho, guardando seu naipe, nome e valor em pontos.
* **`Deck` (Baralho):** Representa um baralho de 52 cartas. Responsável por instanciar as cartas, embaralhar (`shuffle`) e distribuir (`deal`).
* **`Hand` (Mão):** Representa as cartas que o Jogador ou o Dealer seguram. Calcula a pontuação dinamicamente e contém a **lógica de ajuste do Ás** (muda de 11 para 1 automaticamente caso a pontuação passe de 21).
* **`Chips` (Fichas):** Funciona como a carteira do jogador. Inicia com um saldo padrão, registra o valor da aposta da rodada e atualiza o total em caso de vitória ou derrota.
* **`Game` (Juiz/Controlador):** A classe principal que gerencia o fluxo da partida. Atualmente já executa:
    * Instanciação da "mesa" (baralho, fichas e mãos).
    * Recebimento e validação de apostas seguras (`take_bet`).
    * Distribuição das cartas iniciais (`deal_initial_cards`).
    * Checagem imediata de "Blackjack Natural" antes de o jogo seguir (`check_natural_blackjack`).
    * Estrutura global do Game Loop, resetando a mesa a cada rodada e checando se o jogador faliu ou deseja continuar.

---

## Próximos Passos (To-Do)

O esqueleto do jogo está pronto, mas ainda faltam as dinâmicas de turnos. A seguir estão as próximas implementações:

- [ ] **Lógica Visual de Mostrar/Esconder Cartas:** Criar métodos de `print` para exibir a mesa. **Regra importante:** A primeira carta do Dealer deve ficar virada para baixo (oculta) e só deve ser revelada após o turno do jogador terminar.
- [ ] **Turno do Jogador (`hit_or_stand`):** Implementar o loop interativo onde o jogador decide se compra mais cartas para chegar perto de 21 ou se para.
- [ ] **Turno do Dealer:** Implementar o loop automático onde o computador é obrigado a comprar cartas até atingir pelo menos 17 pontos.
- [ ] **Verificação de Vitória:** Lógica final para comparar as mãos, verificar quem deu *Bust* (estourou) e pagar as apostas.