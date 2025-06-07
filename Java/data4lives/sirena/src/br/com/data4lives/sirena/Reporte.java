public class Reporte {

    private final int idReporte;
    private String descricao;
    private String data;
    private String hora;
    private Localizacao localizacao;
    private String tipoReporte;
    private Confiabilidade confiabilidade;
    private String status;

    public Reporte(int idReporte, String descricao, String data, String hora, Localizacao localizacao2, String tipoReporte, Confiabilidade confiabilidade, String status) {
        this.idReporte = idReporte;
        this.descricao = descricao;
        this.data = data;
        this.hora = hora;
        this.localizacao = localizacao2;
        this.tipoReporte = tipoReporte;
        this.confiabilidade = confiabilidade;
        this.status = status;
    }

    public int getIdReporte() {
        return idReporte;
    }
    // Id não deve ser alterado após a criação do reporte, por isso não há setter.

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public Localizacao getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(Localizacao localizacao) {
        this.localizacao = localizacao;
    }

    public String getTipoReporte() {
        return tipoReporte;
    }

    public void setTipoReporte(String tipoReporte) {
        this.tipoReporte = tipoReporte;
    }

    public Confiabilidade getConfiabilidade() {
        return confiabilidade;
    }

    public void setConfiabilidade(Confiabilidade confiabilidade) {
        this.confiabilidade = confiabilidade;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

}
