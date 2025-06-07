public class Confiabilidade {

    private int idConfiabilidade;
    private String grauConfiabilidade;

    public Confiabilidade() {
        idConfiabilidade = 0; 
        grauConfiabilidade = "Indefinido"; 
    }
    
    public int getIdConfiabilidade() {
        return idConfiabilidade;
    }

    public void setIdConfiabilidade(int idConfiabilidade) {
        this.idConfiabilidade = idConfiabilidade;
    }

    public String getGrauConfiabilidade() {
        return grauConfiabilidade;
    }

    public void setGrauConfiabilidade(String grauConfiabilidade) {
        this.grauConfiabilidade = grauConfiabilidade;
    }

}
