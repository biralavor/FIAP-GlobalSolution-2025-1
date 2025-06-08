public class ReporteList {

    private Reporte[] listaReportes;
    private int quantidadeReportes = 0;

    public ReporteList(int tamanho) {
        this.listaReportes = new Reporte[tamanho];
    }

    public Reporte[] getReportes() {
        return listaReportes;
    }

    public void setReportes(Reporte[] reportes) {
        this.listaReportes = reportes;
    }

    public int getQuantidadeReportes() {
        return quantidadeReportes;
    }

    public void addToReporteList(Reporte reporte) {
        if (quantidadeReportes < listaReportes.length) {
            listaReportes[quantidadeReportes] = reporte;
            quantidadeReportes++;
        } else {
            System.out.println("Limite de reportes atingido!");
        }
    }

    public void reporteListPrinter() {
        for (int indice = 0; indice < quantidadeReportes; indice++) {
            Reporte reporte = listaReportes[indice];
            System.out.println("ID do Reporte: " + reporte.getIdReporte());
            System.out.println("Descrição: " + reporte.getDescricao());
            System.out.println("Data: " + reporte.getData());
            System.out.println("Hora: " + reporte.getHora());
            System.out.println("Localização: " + reporte.getLocalizacao().getNomeRua());
            System.out.println("Tipo de Reporte: " + reporte.getTipoReporte());
            String grau = (reporte.getConfiabilidade() != null) ? reporte.getConfiabilidade().getGrauConfiabilidade() : "Indefinido";
            System.out.println("Grau de Confiabilidade: " + grau);
            System.out.println("Grau de Prioridade:" + reporte.getPrioridade().getGrauPrioridade());
            System.out.println("-----------------------------");
        }
    }
}
