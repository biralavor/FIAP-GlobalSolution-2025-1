public class Bombeiro extends Autoridade {

    private String especialidade;
    private String unidade;
    private String credencialBombeiro;

    public Bombeiro(String nome, String cpf, String email, String contato, Localizacao endereco, String especialidade, String unidade, String credencialBombeiro) {
        super(nome, cpf, email, contato, endereco);
        this.especialidade = especialidade;
        this.unidade = unidade;
        this.credencialBombeiro = credencialBombeiro;
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

    public String getCredencialBombeiro() {
        return credencialBombeiro;
    }

    public void setCredencialBombeiro(String credencialBombeiro) {
        this.credencialBombeiro = credencialBombeiro;
    }

    @Override
    public String getTipoAutoridade() {
        return "Bombeiro";
    }
    @Override
    public void autoridadePrinter() {
        System.out.println("*********** AUTORIDADE BOMBEIRO ***********");
        System.out.println("Bombeiro{" +
        "nome='" + getNome() + '\'' +
        ", cpf='" + getCpf() + '\'' +
        ", email='" + getEmail() + '\'' +
        ", contato='" + getContato() + '\'' +
        ", endereco='" + getEndereco() + '\'' +
        ", especialidade='" + especialidade + '\'' +
        ", unidade='" + unidade + '\'' +
        ", credencialBombeiro='" + credencialBombeiro + '\'' +
        '}');
        System.out.println("*******************************************\n");
    }
}
