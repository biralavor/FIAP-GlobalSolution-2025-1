public class Bombeiro extends Autoridade {

    private String especialidade;
    private String unidade;
    private String credencialBombeiro;

    public Bombeiro(String nome, String credencialBombeiro, String email, String contato, String endereco, String especialidade, String unidade) {
        super(nome, credencialBombeiro, email, contato, endereco);
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

}
