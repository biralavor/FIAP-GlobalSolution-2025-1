package br.com.data4lives.sirena;

import br.com.data4lives.sirena.autoridades.Autoridade;
import br.com.data4lives.sirena.reports.Reporte;

public class Ocorrencia {

    private Localizacao localOcorrencia;
    private String horaInicioOcorrencia;
    private String horaFimOcorrencia;
    private Confiabilidade confiabilidade;
    private Prioridade prioridade;
    private Autoridade[] autoridade;
    private boolean flagAtendida;
    private String status;

    public Ocorrencia (Localizacao localOcorrencia, String horaInicioOcorrencia, Confiabilidade confiabilidade, Prioridade prioridade, Autoridade[] autoridade){
        this.localOcorrencia = localOcorrencia;
        this.horaInicioOcorrencia = horaInicioOcorrencia;
        this.horaFimOcorrencia = null; 
        this.confiabilidade = confiabilidade;
        this.prioridade = prioridade;
        this.autoridade = autoridade;
        this.flagAtendida = false;
        this.status = "aguardando atendimento";
    }

    public Localizacao getLocalOcorrencia() {
        return localOcorrencia;
    }
    public void setLocalOcorrencia(Localizacao localOcorrencia) {
        this.localOcorrencia = localOcorrencia;
    }
    public String getHoraInicioOcorrencia() {
        return horaInicioOcorrencia;
    }
    public void setHoraInicioOcorrencia(String horaInicioOcorrencia) {
        this.horaInicioOcorrencia = horaInicioOcorrencia;
    }
    public String getHoraFimOcorrencia() {
        return horaFimOcorrencia;
    }
    public void setHoraFimOcorrencia(String horaFimOcorrencia) {
        this.horaFimOcorrencia = horaFimOcorrencia;
    }
    public Confiabilidade getConfiabilidade() {
        return confiabilidade;
    }
    public void setConfiabilidade(Confiabilidade confiabilidade) {
        this.confiabilidade = confiabilidade;
    }
    public Prioridade getPrioridade() {
        return prioridade;
    }
    public void setPrioridade(Prioridade prioridade) {
        this.prioridade = prioridade;
    }
    public Autoridade[] getAutoridade() {
        return autoridade;
    }
    public void setAutoridade(Autoridade[] autoridade) {
        this.autoridade = autoridade;
    }
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
    
    public void atenderOcorrencia(Reporte reporte, String horaAtendimento, Autoridade[] autoridadesResponsaveis) {
        this.localOcorrencia = reporte.getLocalizacao();
        this.confiabilidade = reporte.getConfiabilidade();
        this.prioridade = reporte.getPrioridade();
        this.autoridade = autoridadesResponsaveis;
        setHoraInicioOcorrencia(horaAtendimento);

        String grauPrioridade = this.prioridade.getGrauPrioridade();
        String grauConfiabilidade = this.confiabilidade.getGrauConfiabilidade();

        if (grauPrioridade.equals("Muito Alta") || grauPrioridade.equals("Alta")) {
            status = "Em Atendimento";
        } else if (grauPrioridade.equals("Média")) {
            status = "Em Atendimento";
        } else if (grauPrioridade.equals("Baixa")) {
            status = "Em Análise";
        } else {
            status = "Aguardando Atendimento";
        }
    }

    public void finalizarOcorrencia(String horaFimOcorrencia, boolean flagAtendida) {
        this.horaFimOcorrencia = horaFimOcorrencia;
        this.flagAtendida = true;
        this.status = "Finalizada";
    }

    public void ocorrenciaPrinter() {
        System.out.println("////////////// OCORRENCIA ////////////////////");
        System.out.println("Localização da Ocorrência: " + localOcorrencia.getNomeRua());
        System.out.println("Hora de Início: " + horaInicioOcorrencia);
        System.out.println("Hora de Fim: " + (horaFimOcorrencia != null ? horaFimOcorrencia : "Em andamento"));
        System.out.println("Confiabilidade: " + confiabilidade.getGrauConfiabilidade());
        System.out.println("Prioridade: " + prioridade.getGrauPrioridade());
        System.out.print("Autoridades Envolvidas: ");
        for (Autoridade a : autoridade) {
            if (a != null) {
                System.out.println(a.getNome() + " (" + a.getTipoAutoridade() + ")");
            }
        }
        System.out.println("\nStatus da Ocorrência: " + status);
        System.out.println("//////////////////////////////////////////////\n");
    }
}