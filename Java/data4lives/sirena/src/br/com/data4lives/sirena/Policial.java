public class Policial extends Autoridade{

    private String patente;
    private String unidade;
    private String credencialPolicial;

    public Policial(String nome, String cpf, String email, String contato, Localizacao endereco, String patente, String unidade, String credencialPolicial) {
        super(nome, cpf, email, contato, endereco);
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

    @Override
    public String getTipoAutoridade() {
        return "Policial";
    }
    @Override
    public void autoridadePrinter() {
        System.out.println("*********** AUTORIDADE POLICIAL ***********");
        System.out.println("Policial{" +
        "nome='" + getNome() + '\'' +
        ", cpf='" + getCpf() + '\'' +
        ", email='" + getEmail() + '\'' +
        ", contato='" + getContato() + '\'' +
        ", endereco='" + getEndereco() + '\'' +
        ", patente='" + patente + '\'' +
        ", unidade='" + unidade + '\'' +
        ", credencialPolicial='" + credencialPolicial + '\'' +
        '}');
        System.out.println("*******************************************\n");
    }
    
}