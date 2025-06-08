public class Ocorrencia {

    private Localizacao localOcorrencia;
    private String horaInicioOcorrencia;
    private String horaFimOcorrencia;
    private Confiabilidade confiabilidade;
    private Prioridade prioridade;
    private Autoridade[] autoridade;
    private boolean flagAtendida;
    private String status;

    public Ocorrencia (Localizacao localOcorrencia, String horaInicioOcorrencia, Confiabilidade confiabilidade, Prioridade prioridade, Autoridade[] autoridade, String status){
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
    
    public void atenderOcorrencia(Reporte reporte, String horaInicioOcorrencia) {
        this.localOcorrencia = reporte.getLocalizacao();
        this.confiabilidade = reporte.getConfiabilidade();
        this.prioridade = reporte.getPrioridade();
        if (this.prioridade.equals("Muito Alta") || this.prioridade.equals("Alta")) {
            this.autoridade = new Autoridade[2];
            setHoraInicioOcorrencia(horaInicioOcorrencia);
            this.status = "Em Atendimento";
        } else if (this.prioridade.equals("Média")) {
            this.autoridade = new Autoridade[1];
            this.status = "Em Atendimento";
        } else if (this.prioridade.equals("Baixa") && this.confiabilidade.getGrauConfiabilidade().equals("baixa")) {
            this.status = "Em Análise";
        } else {
            this.status = "Aguardando Atendimento";
        }
    }

    public void finalizarOcorrencia(String horaFimOcorrencia, boolean flagAtendida) {
        this.horaFimOcorrencia = horaFimOcorrencia;
        this.flagAtendida = true;
        this.status = "Finalizada";
    }
}