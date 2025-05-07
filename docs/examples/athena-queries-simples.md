# Exemplos de Queries no Athena

## Contar clientes por status

```sql
SELECT status, COUNT(*) 
FROM vendas 
GROUP BY status;

```sql
SELECT produto, preco 
FROM datalake
WHERE estado = 'SC' AND nome = 'Godo Capiperibe'

#Pode adicionar outras aqui, sua preferência