public class Bombeiro extends Autoridade {

    private String especialidade;
    private String unidade;
    private String numeroIdentificacao;

    public Bombeiro(String nome, String numeroIdentificacao, String email, String contato, String endereco, String especialidade, String unidade) {
        super(nome, numeroIdentificacao, email, contato, endereco);
        this.especialidade = especialidade;
        this.unidade = unidade;
        this.numeroIdentificacao = numeroIdentificacao;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
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
