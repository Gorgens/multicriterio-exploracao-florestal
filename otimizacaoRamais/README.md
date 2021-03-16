# Otimização multicritério da exploração florestal. 

Coordenador: Eric Bastos Gorgens (UFVJM)

Este projeto visa implementar uma abordagem multicritério para otimizar a extração madeireira em floresta Amazônica, baseado em camadas de informações extraídas de sensor LiDAR (Light Detection and Ranging) aerotransportado. A partir de camadas que descrevem a topografia, a hidrografia, as restrições legais, as restrições operacionais, a vegetação  entre outras, pretende-se avaliar diferentes composições da superfície de custo a ser usada como referência para a otimização. Cada camada de informação será gerada a partir de uma metodologia específica de processamento. Um algoritmo para determinar o trajeto de menor custo ligará o ponto de origem aos pontos que representam as árvores a serem extraídas. Espera-se ao final do projeto apresentar uma análise das informações capturadas pelas camadas criadas, propor quais as melhores camadas e seus respectivos pesos para a construção da superfície de custo e propor uma metodologia replicável para implementação da otimização aqui proposta em futuros planos de manejo. Os resultados serão publicados através de trabalhos de conclusão de curso, relatórios de iniciação científica, dissertações, teses, anais e artigos, além de participação de eventos científicos nacionais e internacionais.

![Fluxograma multicriterio](img/fluxo.png)

## Apoios recebidos

- Research Stay DAAD
- CNPq Pesquisador Produtividade

## Resumo dos resultados

- Propor uma otimização multicritério para auxiliar o planejamento florestal

![Composição 1](img/rotas.png)

Barbosa, Rauff Pereira et al. Multi-criteria optimization for log extraction in Amazon based on airborne laser scanning data. Scientia Forestalis, v. 45, n. 115, p. 541-550, 2017.

![Alternativas](img/alternativas.png)

Gorgens, Eric Bastos et al. Automated operational logging plan considering multi-criteria optimization. Computers and Electronics in Agriculture, v. 170, p. 105253, 2020.

- Analisar a relevância das diferentes camadas de informação durante o processo de otimização.  

![Impactos dos cenários](img/impactos.png)

Barbosa, Rauff Pereira et al. Multi-criteria optimization for log extraction in Amazon based on airborne laser scanning data. Scientia Forestalis, v. 45, n. 115, p. 541-550, 2017.

![Diferentes camadas](img/camadas.png)

![Relevância das camadas](img/relevancia.png)

Gorgens, Eric Bastos et al. Automated operational logging plan considering multi-criteria optimization. Computers and Electronics in Agriculture, v. 170, p. 105253, 2020.

- Analisar as diferentes composições e pesos para a criação da superfície de custo a ser otimizada. 

![Composição 1](img/custos.png)

Barbosa, Rauff Pereira et al. Multi-criteria optimization for log extraction in Amazon based on airborne laser scanning data. Scientia Forestalis, v. 45, n. 115, p. 541-550, 2017.

![Composição 2](img/composicao.png)

Gorgens, Eric Bastos et al. Automated operational logging plan considering multi-criteria optimization. Computers and Electronics in Agriculture, v. 170, p. 105253, 2020.

- Desenvolver uma rotina de processamento baseado em software livre para implementação da otimização.  

Scripts em python para QGIS 2.x: [coleção dos scripts](https://github.com/Gorgens/multicriterio-exploracao-florestal/tree/master/python)

Gorgens, Eric Bastos et al. Automated operational logging plan considering multi-criteria optimization. Computers and Electronics in Agriculture, v. 170, p. 105253, 2020.

- Analisar as oportunidades da metodologia baseada em sensoriamento remoto frente à metodologia atualmente estabelecida pela legislação florestal brasileira. 
