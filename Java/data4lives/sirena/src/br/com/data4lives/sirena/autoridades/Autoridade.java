package br.com.data4lives.sirena.autoridades;

import br.com.data4lives.sirena.Localizacao;

public class Autoridade {

    private String nome;
    private String cpf;
    private String email;
    private String contato;
    private Localizacao endereco;
    private String tipoAutoridade;

    public Autoridade(String nome, String cpf, String email, String contato, Localizacao endereco) {
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
    public Localizacao getEndereco() {
        return endereco;
    }
    public void setEndereco(Localizacao endereco) {
        this.endereco = endereco;
    }
    public String getTipoAutoridade() {
        return "Autoridade Pública";
    }
    public void setTipoAutoridade(String tipoAutoridade) {
        this.tipoAutoridade = tipoAutoridade;
    }

    public void autoridadePrinter() {
        System.out.println("Autoridade{" +
                "nome='" + nome + '\'' +
                ", cpf='" + cpf + '\'' +
                ", email='" + email + '\'' +
                ", contato='" + contato + '\'' +
                ", endereco='" + endereco + '\'' +
                ", tipoAutoridade='" + tipoAutoridade + '\'' +
                '}');
    }
}
