#!/usr/bin/perl 
#
# IBQUOTA 2.4
# 29/03/04 - Valcir C.
#
# Inserir cabecalho padrao, com a GPL

#Adiciona as funcoes utilizadas
require "/usr/local/ibquota/funcoes.pl";

#Modulos de Politicas de Impressao
#require "modules/grupop.pl";

#use DBI();

#Ler as configuracoes
%configuracoes = LER_CONFIGURACOES("/usr/local/ibquota/ibquota.conf");

$dia = &DIA_DO_MES();
$hoje = $dia;
local $impressoras;
my $impressora;
local $arquivo_job;
local $SPOOL_IMPRESSORA;
#local $job;
  @impressoras = &LISTA_IMPRESSORAS();
  foreach $impressora (@impressoras) {
    @jobs = &LISTA_JOBS_IMPRESSORA($impressora);
    #Verifica se ha jobs
    if ($#jobs == -1) {
     next; # proxima impressora
    }
    $SPOOL_IMPRESSORA=&SPOOL_IMPRESSORA($impressora);
    foreach $job (@jobs) {
      $arquivo_job = &MONTA_ARQUIVO_JOB($job);
     if (&TESTA_JOB($SPOOL_IMPRESSORA . $arquivo_job) == 0) { 
        # Arquivo temporário de impressão inexistente
        &GRAVA_LOG_IMPRESSOES(&DONO_JOB($impressora,$job),$impressora,4);
        &REMOVE_JOB($impressora,$job);
        next; # proximo job
      }
      $dono_job = &DONO_JOB($impressora,$job);
      if ($dono_job eq "NONE") { # Login nao identificado 
        &GRAVA_LOG("Login nao identificado: $impressora-$job ","ERRO");
        &REMOVE_JOB($impressora,$job);
        next; # proximo job
      }
   
#       print &NOME_ESTACAO_JOB($arquivo_job);
       chomp($job);
       print "${job}:${dono_job}:${arquivo_job}:${impressora}\n";
#      &EXECUTA_MODULO_IMPRESSAO_USUARIO($dono_job,$impressora,$arquivo_job);
    }
  }

