public class Autoridade {

    private String nome;
    private String numeroIdentificacao;
    private String email;
    private String contato;
    private String endereco;
    

    public Autoridade(String nome, String numeroIdentificacao, String email, String contato, String endereco) {
        this.nome = nome;
        this.numeroIdentificacao = numeroIdentificacao;
        this.email = email;
        this.contato = contato;
        this.endereco = endereco;
    }
    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getNumIdentificacao() {
        return numeroIdentificacao;
    }
    public void setNumIdentificacao(String numeroIdentificacao) {
        this.numeroIdentificacao = numeroIdentificacao;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getContato() {
        return contato;
    }
    public void setContato(String contato) {
        this.contato = contato;
    }
    public String getEndereco() {
        return endereco;
    }
    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
}
