# Conversa com Marcos sobre primeiros passos no RStudio



# Importar a base
crv = read.csv('crv.csv')

# Analises base importada
str(crv)
summary(crv)
head(crv)
tail(crv)

# Testar hipóteses por meio de gráfico

# 1 Pergunta direcionadora: Qual a distribuição da variável de interesse (crv numérico)?
# H0: crv tem distribuição normal.

# 2 Pergunta direcionadora: Existe diferença entre o CRV (numeríca) dos municípios (categórico) estudados?
# H0: que os coeficientes de crv = f(municipio) são igual a 0.

# 3 Pergunta direcionadora: Existe relação entre dbase médio (numérica) da tora com o crv (numérico)?
# H0: que os coeficienbtes de crv = f(dbase) são igual a 0.

# Criar gráficos básicos
# Histograma
# 1 Pergunta direcionadora: Qual a distribuição da variável de interesse (crv numérico)?
# H0: crv tem distribuição normal.
hist(x = crv$crv)

# Boxplot
# 2 Pergunta direcionadora: Existe diferença entre o CRV (numeríca) dos municípios (categórico) estudados?
# H0: que os coeficientes de crv = f(municipio) são igual a 0.
boxplot(crv$crv ~ crv$municipio)


# Dispersão
# 3 Pergunta direcionadora: Existe relação entre dbase médio (numérica) da tora com o crv (numérico)?
# H0: que os coeficienbtes de crv = f(dbase) são igual a 0.
crv$dbase = (crv$dbase1 + crv$dbase2)/2
plot(crv$crv ~crv$dbase)

