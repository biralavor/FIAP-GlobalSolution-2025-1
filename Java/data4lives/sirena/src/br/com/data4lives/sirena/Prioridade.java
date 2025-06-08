public class Prioridade {

    int idPrioridade;
    String grauPrioridade;

    public Prioridade() {
        idPrioridade = 0; 
        grauPrioridade = "Indefinido";
    }

    public int getIdPrioridade() {
        return idPrioridade;
    }
    public void setIdPrioridade(int idPrioridade) {
        this.idPrioridade = idPrioridade;
    }
    public String getGrauPrioridade() {
        return grauPrioridade;
    }
    public void setGrauPrioridade(String grauPrioridade) {
        this.grauPrioridade = grauPrioridade;
    }

    public void defineGrauPrioridade(boolean pessoaEmPerigo, boolean viaIntransitavel) {
        if (pessoaEmPerigo && viaIntransitavel) {
            grauPrioridade = "Muito Alta";
        } else if (pessoaEmPerigo){
            grauPrioridade = "Alta";
        }else if (viaIntransitavel) {
            grauPrioridade = "Média";
        } else {
            grauPrioridade = "Baixa";
        }
    }
}
