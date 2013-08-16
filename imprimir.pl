#!/usr/bin/perl 
#
# IBQUOTA 2.4
# 29/03/04 - Valcir C.
#
# Inserir cabecalho padrao, com a GPL

#Adiciona as funcoes utilizadas
require "/usr/local/ibquota/funcoes.pl";


$jobs=$ARGV[0];
$dono_job=$ARGV[1];
$arquivo_job=$ARGV[2];
$impressora=$ARGV[3];

%configuracoes = LER_CONFIGURACOES("/usr/local/ibquota/ibquota.conf");

$dia = &DIA_DO_MES();

#print $jobs;
#print $dono_job;
#print $impressora;
#print $arquivo_job;

&EXECUTA_MODULO_IMPRESSAO_USUARIO($dono_job,$impressora,$arquivo_job);
