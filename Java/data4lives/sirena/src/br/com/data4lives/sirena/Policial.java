public class Policial extends Autoridade{

    private String patente;
    private String unidade;
    private String numeroIdentificacao;

    public Policial(String nome, String numeroIdentificacao, String email, String contato, String endereco, String patente, String unidade) {
        super(nome, numeroIdentificacao, email, contato, endereco);
        this.patente = patente;
        this.unidade = unidade;
        this.numeroIdentificacao = numeroIdentificacao;
    }

    public String getPatente() {
        return patente;
    }

    public void setPatente(String patente) {
        this.patente = patente;
    }

    public String getUnidade() {
        return unidade;
    }

    public void setUnidade(String unidade) {
        this.unidade = unidade;
    }

    public String getNumeroIdentificacao() {
        return numeroIdentificacao;
    }

    public void setNumeroIdentificacao(String numeroIdentificacao) {
        this.numeroIdentificacao = numeroIdentificacao;
    }
}