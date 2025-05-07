import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node produtos
produtos_node1746173838554 = glueContext.create_dynamic_frame.from_catalog(database="vendas", table_name="produtos_csv", transformation_ctx="produtos_node1746173838554")

# Script generated for node vendedores
vendedores_node1746173969450 = glueContext.create_dynamic_frame.from_catalog(database="vendas", table_name="vendedores_csv", transformation_ctx="vendedores_node1746173969450")

# Script generated for node Vendas
Vendas_node1746173207075 = glueContext.create_dynamic_frame.from_catalog(database="vendas", table_name="vendas_csv", transformation_ctx="Vendas_node1746173207075")

# Script generated for node itensvenda
itensvenda_node1746173452234 = glueContext.create_dynamic_frame.from_catalog(database="vendas", table_name="itensvenda_csv", transformation_ctx="itensvenda_node1746173452234")

# Script generated for node Clientes
Clientes_node1746173707181 = glueContext.create_dynamic_frame.from_catalog(database="vendas", table_name="clientes_csv", transformation_ctx="Clientes_node1746173707181")

# Script generated for node VendasMapping
VendasMapping_node1746173350085 = ApplyMapping.apply(frame=Vendas_node1746173207075, mappings=[("idvenda", "long", "idvenda", "long"), ("idvendedor", "long", "idvendedor_vendas", "long"), ("idcliente", "long", "idcliente_vendas", "long"), ("data", "string", "data", "string"), ("total", "double", "total", "double")], transformation_ctx="VendasMapping_node1746173350085")

# Script generated for node itensvendaMapping
itensvendaMapping_node1746173497415 = ApplyMapping.apply(frame=itensvenda_node1746173452234, mappings=[("idproduto", "long", "idproduto_itensvenda", "long"), ("idvenda", "long", "idvenda_itensvenda", "long"), ("quantidade", "long", "quantidade", "long"), ("valorunitario", "double", "valorunitario", "double"), ("valortotal", "double", "valortotal", "double"), ("desconto", "double", "desconto", "double")], transformation_ctx="itensvendaMapping_node1746173497415")

# Script generated for node Joinvendas_itensvendas
Joinvendas_itensvendas_node1746173599429 = Join.apply(frame1=VendasMapping_node1746173350085, frame2=itensvendaMapping_node1746173497415, keys1=["idvenda"], keys2=["idvenda_itensvenda"], transformation_ctx="Joinvendas_itensvendas_node1746173599429")

# Script generated for node JoinClientes
JoinClientes_node1746173746611 = Join.apply(frame1=Clientes_node1746173707181, frame2=Joinvendas_itensvendas_node1746173599429, keys1=["idcliente"], keys2=["idcliente_vendas"], transformation_ctx="JoinClientes_node1746173746611")

# Script generated for node Joinprodutos
Joinprodutos_node1746173868566 = Join.apply(frame1=produtos_node1746173838554, frame2=JoinClientes_node1746173746611, keys1=["idproduto"], keys2=["idproduto_itensvenda"], transformation_ctx="Joinprodutos_node1746173868566")

# Script generated for node Joinvendedores
Joinvendedores_node1746174022458 = Join.apply(frame1=vendedores_node1746173969450, frame2=Joinprodutos_node1746173868566, keys1=["idvendedor"], keys2=["idvendedor_vendas"], transformation_ctx="Joinvendedores_node1746174022458")

# Script generated for node ColunasFinais
ColunasFinais_node1746175464181 = ApplyMapping.apply(frame=Joinvendedores_node1746174022458, mappings=[("nome", "string", "nome", "string"), ("produto", "string", "produto", "string"), ("preco", "double", "preco", "double"), ("cliente", "string", "cliente", "string"), ("estado", "string", "estado", "string"), ("sexo", "string", "sexo", "string"), ("status", "string", "status", "string"), ("data", "string", "data", "string"), ("total", "double", "total", "double"), ("quantidade", "long", "quantidade", "long"), ("valorunitario", "double", "valorunitario", "double"), ("valortotal", "double", "valortotal", "double"), ("desconto", "double", "desconto", "double")], transformation_ctx="ColunasFinais_node1746175464181")

# Script generated for node Datalake
EvaluateDataQuality().process_rows(frame=ColunasFinais_node1746175464181, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1746172716832", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Datalake_node1746175607653 = glueContext.write_dynamic_frame.from_options(frame=ColunasFinais_node1746175464181, connection_type="s3", format="glueparquet", connection_options={"path": "s3://datalakeengdadosjr/datalake/", "partitionKeys": ["status"]}, format_options={"compression": "snappy"}, transformation_ctx="Datalake_node1746175607653")

job.commit()