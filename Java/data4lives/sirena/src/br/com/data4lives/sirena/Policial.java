public class Policial extends Autoridade{

    private String patente;
    private String unidade;
    private String credencialPolicial;

    public Policial(String nome, String credencialPolicial, String email, String contato, String endereco, String patente, String unidade) {
        super(nome, credencialPolicial, email, contato, endereco);
        this.patente = patente;
        this.unidade = unidade;
        this.credencialPolicial = credencialPolicial;
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

    public String getCredencialPolicial() {
        return credencialPolicial;
    }

    public void setCredencialPolicial(String credencialPolicial) {
        this.credencialPolicial = credencialPolicial;
    }
}