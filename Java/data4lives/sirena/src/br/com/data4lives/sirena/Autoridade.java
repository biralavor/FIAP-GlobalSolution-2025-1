public class Autoridade {

    private String nome;
    private String cpf;
    private String email;
    private String contato;
    private String endereco;
    

    public Autoridade(String nome, String cpf, String email, String contato, String endereco) {
        this.nome = nome;
        this.cpf = cpf;
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
    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
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
