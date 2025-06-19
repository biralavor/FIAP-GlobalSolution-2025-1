# FIAP GlobalSolution 2025-1 Plataforma S.I.R.E.N.A.

![GlobalSolution 2025 01 - Computacional Thinking using Python(1)](https://github.com/user-attachments/assets/d09e2c97-870c-4650-913c-89b7a65fcb65)

# Nota Geral: 94,83
Nota máxima: 100 pontos
| Matéria | Nota |
|---------|------|
| Artificial Intelligence | 100 |
| Building Relational Database| 100 |
| Computational Thinking using Python | 100 |
| Domain Driven Design using Java | 95 |
| Front-end Design Engineering | 84 |
| Software Engineering and Business Model| 90 |

[Check S.I.R.E.N.A.'s website here](https://biralavor.github.io/FIAP-GlobalSolution-2025-1/Front-end/)


> [!TIP]
> ## SUMÁRIO
> 1. [Integrantes](https://github.com/biralavor/FIAP-Challenge-2025-1#1-integrantes)
> 2. [Cliente](https://github.com/biralavor/FIAP-Challenge-2025-1#2-cliente)
> 3. [Metas](https://github.com/biralavor/FIAP-Challenge-2025-1#3-metas)
> 4. [Hipóteses](https://github.com/biralavor/FIAP-Challenge-2025-1#4-hipoteses)
> 5. [Segmentos de Cliente](https://github.com/biralavor/FIAP-Challenge-2025-1#5-segmentos-de-cliente)
> 6. [Solução](https://github.com/biralavor/FIAP-Challenge-2025-1#6-solucao)
>    
> - 6.1 [Fase 1 - Treinamento da Operação - curto prazo](https://github.com/biralavor/FIAP-GlobalSolution-2025-1#61-fase-1---treinamento-da-opera%C3%A7%C3%A3o---curto-prazo)
> - 6.2 [Fase 2 - Aprimoramento da Predição - médio prazo](https://github.com/biralavor/FIAP-GlobalSolution-2025-1#62-fase-2---aprimoramento-da-predi%C3%A7%C3%A3o---m%C3%A9dio-prazo)
> - 6.3 [Fase 3 - Coleta Refinada do Microclima - longo prazo](https://github.com/biralavor/FIAP-GlobalSolution-2025-1#63-fase-3---coleta-refinada-do-microclima---longo-prazo)
> 7. [Milestones](https://github.com/biralavor/FIAP-Challenge-2025-1#7-milestones)
> 8. [Tecnologias Utilizadas](https://github.com/biralavor/FIAP-Challenge-2025-1#8-tecnologias-utilizadas)

## 1. Integrantes
[RM 565463 - Bira Lavor](https://github.com/biralavor)

[RM 565355 - Lucas Hideki](https://github.com/HidekiLucas0701)

## 2. Cliente
- Governos Estaduais
- Governos Municipais

## 3. Metas
> [!IMPORTANT]
> - **Técnica:**
>     - Redução de 70% dos falsos positivos em alertas de enxurradas e alagamentos
>     - Acurácia mínima de 95% na previsão do volume de chuva
> - **Operacional:**
>     - Redução de 40% no tempo de elaboração do plano de ação
>     - Execução da ação em até 15 min
> - **Social:**
>     - Redução de 60% em vítimas fatais nas áreas mapeadas
>     - Aumento em 3x na adesão das evacuações


## 4. Hipóteses
| Descrição |   |
|-----------|---|
| **Aumento da eficácia operacional** <br><br>Agentes públicos reduzirão o tempo de resposta em 40% usando o dashboard do S.I.R.E.N.A., que integra dados meteorológicos, recursos humanos e planos de ação pré-aprovados; | ![image](https://github.com/user-attachments/assets/17db8a8d-21f8-415e-bace-749ff6aed03d) |
| **Adoção de agentes públicos** <br><br>Times priorizarão alertas da S.I.R.E.N.A. com score de confiabilidade acima de 90%, reduzindo trotes; | ![image](https://github.com/user-attachments/assets/d23a9922-9c78-43f0-a682-7a0808a6e58d) |
| **Engajamento da população** <br><br>Cidadãos de áreas de risco seguirão alertas da S.I.R.E.N.A. 3x mais rápido, quando receberem instruções específicas e geolocalizadas; | ![image](https://github.com/user-attachments/assets/536d965e-bead-4e3f-b965-1b25bae993f0) |



## 5. Segmentos de Cliente
- Agentes Públicos: Defesa Civil, Corpor de Bombeiros, C.E.T.
- Cidadãos

## 6. Solução
### Plataforma S.I.R.E.N.A
Sistema Integrado de Resposta às Emergências e Notificações Ambientais, que gera alertas antecipados e coordenação integrada de recursos públicos.

Nosso objetivo é prever chuvas extremas e fazer a ponte entre agentes públicos e cidadãos, reduzindo mortes e danos econômicos em eventos climáticos.
![Sirena-white-horizontal](https://github.com/user-attachments/assets/acd3c561-ceab-40e4-be35-680c61a0c251)

### 6.1 Fase 1 - Treinamento da Operação - curto prazo
Chatbot L.U.C.A.S. - Localizador Urbano de Chamados e Alertas de Segurança para WhatsApp

O Chatbot L.U.C.A.S. atua como canal de comunicação direta entre a população e o sistema de monitoramento urbano. Sem exigir login, ele permite que qualquer cidadão envie relatos sobre ocorrências como alagamentos, quedas de árvores ou falta de energia. Além disso, orienta o usuário com informações de segurança em situações de risco e encaminha automaticamente os dados para análise pelo sistema.

Aqui, o Cidadão poderá reportar um incidente e conferir se está ou não em local de perigo.

Já o Agente poderá acessar um relatório das ocorrências dos bairros e verificar qual bairro com maior ocorrência é o mais perto de sua localização atual.

[Chatbot_LUCAS.webm](https://github.com/user-attachments/assets/c541b471-22ed-4776-af0e-7f2282b0ece1)


### 6.2 Fase 2 - Aprimoramento da Predição - médio prazo
Combinação de múltiplos modelos de Machine Learning tendo como variável resposta: dados topográficos; dados das estações meteorológicas atuais; histórico de alagamentos; dados de trânsito em tempo real e dados das novas estações meteorológicas.

A partir daí, os Agentes Públicos vão acelerar o processo de tomada de decisão e execução com SIRENA;
Os Cidadãos poderão encontrar uma rota de fuga mais rápida para locais protegidos, já que ambos terão acesso a um plano de ação integrado, geolocalizado e distribuído pelo chatbot L.U.C.A.S.

![image](https://github.com/user-attachments/assets/4a3943ee-c825-4c6f-9862-8a146b2cef50)

### 6.3 Fase 3 - Coleta Refinada do Microclima - longo prazo
Queremos engajar a população ao transformá-los em mini estações meteorológicas portáteis com o aplicativo SIRENA.

Atualmente os dispositivos móveis premium têm sensores climáticos de alta precisão embarcados.

O compartilhamento desses dados aumentará e muito a acurácia das predições do microclima e o tempo de resposta dos modelos, beneficiando a todos que estiverem conectados ao LUCAS.

![image](https://github.com/user-attachments/assets/e15fdf7e-4fc6-4770-a877-89e986887269)


## 7. Milestones
| Milestone | Descrição |
|-----------|-----------|
| **#1** | Chatbot já será apresentado à população e aos agentes públicos.<br>Modo Cidadão: O Cidadão poderá indicar ocorrências climáticas e receber alertas, baseadas em sua geolocalização.<br>Modo Agente: Agentes deverão confirmar ocorrências in loco, daquelas já filtradas por alta confiabilidade. |
| **#2** | Desenvolvimento de cada modelo de Machine Learning: topografia, histórico de alagamento, estações meteorológicas antigas, estações meteorológicas novas e trânsito em tempo real |
| **#3** | Combinação dos múltiplos modelos de Machine Learning para o desenvolvimento de um plano de ação geolocalizado |
| **#4** | Modo Cidadão vai indicar locais mais seguros, durante eventos climáticos, baseados em sua localização, topografia, risco e dados climáticos.<br>Modo Agente vai receber o plano de ação elaborado pelo S.I.R.E.N.A., indicando melhor rota de como chegar ao local |


## 8. Tecnologias Utilizadas
<ol>
  <li>IBM WATSONX - Chatbot do tipo assistente conversasional -> https://cloud.ibm.com/catalog/services/watsonx-assistant</li>
  <li>Node-Red - Ferramenta low-code para conexão de fluxos entre APIs -> https://nodered.org/</li>
  <li>Telegram - Rede social e servico de mensageria -> https://www.telegram.org</li>
  <li>Java - Linguagem de alto nível orientada a objetos -> https://www.java.com</li>
  <li>Python - Linguagem de alto nível de múltiplo propósito -> https://www.python.org</li>
  <li>Oracle Data Modeler - Ferramenta de definicão de modelos lógicos, relacionais e físicos para o banco de dados -> https://www.oracle.com/databse</li>
  <li>HTML - HyperText Markup Language é o esqueleto das páginas e sites do projeto -> https://developer.mozilla.org/en-US/docs/Web/HTML</li>
  <li>CSS - Cascading Style Sheets é a linguagem que controla a apresentacão visual dos sites do projeto -> https://developer.mozilla.org/en-US/docs/Web/CSS</li>
  <li>JS - JavaScript é a linguagem que controla o compoprtamento e funcionalidades dos sites do projeto -> https://developer.mozilla.org/en-US/docs/Web/JavaScript</li>
  <li>Agile - Conjunto de práticas e princípios que aceleram o desenvolvimento de software -> https://agilemanifesto.org/</li>
  <li>Scrum - Método de trabalho que facilita a execucão dos princípios ágeis (Agile) -> https://www.scrum.org/</li>
</ol>

## Watch the promo video of S.I.R.E.N.A:
Mussum Ipsum, cacilds vidis litro abertis. 

[Acesso ao repositório SIRENA GlobalSolution no Github](https://github.com/biralavor/FIAP-GlobalSolution-2025-1)
