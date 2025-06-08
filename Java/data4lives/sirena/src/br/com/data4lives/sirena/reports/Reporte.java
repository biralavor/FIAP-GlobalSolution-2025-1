package br.com.data4lives.sirena.reports;

import br.com.data4lives.sirena.Confiabilidade;
import br.com.data4lives.sirena.Localizacao;
import br.com.data4lives.sirena.Prioridade;

public class Reporte {

    private int idReporte;
    private String descricao;
    private String data;
    private String hora;
    private Localizacao localizacao;
    private String tipoReporte;
    private Confiabilidade confiabilidade;
    private boolean pessoaEmPerigo;
    private boolean viaIntransitavel;
    private Prioridade prioridade;

    public Reporte(int idReporte, String descricao, String data, String hora, Localizacao localizacao, String tipoReporte, boolean pessoaEmPerigo, boolean viaIntransitavel) {
        this.idReporte = idReporte;
        this.descricao = descricao;
        this.data = data;
        this.hora = hora;
        this.localizacao = localizacao;
        this.tipoReporte = tipoReporte;
        this.pessoaEmPerigo = pessoaEmPerigo;
        this.viaIntransitavel = viaIntransitavel;
        this.prioridade = new Prioridade();
        this.prioridade.defineGrauPrioridade(pessoaEmPerigo, viaIntransitavel);
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

    public boolean isPessoaEmPerigo() {
        return pessoaEmPerigo;
    }

    public void setPessoaEmPerigo(boolean pessoaEmPerigo) {
        this.pessoaEmPerigo = pessoaEmPerigo;
    }

    public boolean isViaIntransitavel() {
        return viaIntransitavel;
    }

    public void setViaIntransitavel(boolean viaIntransitavel) {
        this.viaIntransitavel = viaIntransitavel;
    }

    public Prioridade getPrioridade() {
        return prioridade;
    }
    public void setPrioridade(Prioridade prioridade) {
        this.prioridade = prioridade;
    }

    public void reportePrinter() {
        System.out.println("===========================================");
        System.out.println("ID do Reporte: " + getIdReporte());
        System.out.println("Descrição: " + getDescricao());
        System.out.println("Data: " + getData());
        System.out.println("Hora: " + getHora());
        System.out.println("Localização: " + getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + getTipoReporte());
        System.out.println("Pessoa em Perigo: " + isPessoaEmPerigo());
        System.out.println("Via Intransitável: " + isViaIntransitavel());
        System.out.println("===========================================");
    }
}

