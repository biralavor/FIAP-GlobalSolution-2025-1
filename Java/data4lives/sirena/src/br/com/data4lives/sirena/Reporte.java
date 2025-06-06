public class Reporte {

    private final int idReporte;
    private String descricao;
    private String data;
    private String hora;
    private String localizacao;
    private String tipo_reporte;
    private int confiabilidade;
    private String status;

    public Reporte(int idReporte, String descricao, String data, String hora, String localizacao, String tipo_reporte, int confiabilidade, String status) {
        this.idReporte = idReporte;
        this.descricao = descricao;
        this.data = data;
        this.hora = hora;
        this.localizacao = localizacao;
        this.tipo_reporte = tipo_reporte;
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

    public String getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(String localizacao) {
        this.localizacao = localizacao;
    }

    public String getTipo_reporte() {
        return tipo_reporte;
    }

    public void setTipo_reporte(String tipo_reporte) {
        this.tipo_reporte = tipo_reporte;
    }

    public int getConfiabilidade() {
        return confiabilidade;
    }

    public void setConfiabilidade(int confiabilidade) {
        this.confiabilidade = confiabilidade;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
